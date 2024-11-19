#              _________________________
#       ______|                         |_____
#       \     |    13.8.3 SEILWELLE     |    /
#        )    |_________________________|   (
#       /________)                  (________\      14.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# In diesem Kapitel modellieren wir die Ausbreitung einer Welle entlang eines Seils.
# Die einzelnen Körper, die das Seil bilden, sind über Federn miteinander verbunden.
# Indem ein Ende des Seils periodisch bewegt wird, entsteht eine Wellenbewegung,
# die sich entlang des Seils ausbreitet. Das System zeigt die Eigenschaften
# einer mechanischen Welle, wie Überlagerung, Dämpfung und Reflexion an den Enden.


import arcade
import arcade.gui 
import numpy as np
import math


# Rechteckige Wellenbewegung
def square_wave(t, frequenz=1):
    return 1 if (int(t * frequenz) % 2 == 0) else -1

# Dreieckige Wellenbewegung
def triangle_wave(t, frequenz=1):
    period = 1 / frequenz
    t = t % period
    return 4 * abs((t / period) - 0.5) - 1

# Sinus Wellenbewegung
def sinus_wave(t, frequenz=1):
    return math.sin(2*math.pi*frequenz*t)



# Die Klasse `Body` modelliert ein physikalisches Objekt in der Simulation, 
# das durch seine Position, Geschwindigkeit und Masse beschrieben wird.

class Body:
    def __init__(self, position, velocity, mass=1.0, radius=1.0, fixed=False, fixed_x=False, color=arcade.color.BLUE):
        self.mass = mass                                 # Masse in kg
        self.position = np.array(position, dtype=float)  # Position in m
        self.velocity = np.array(velocity, dtype=float)  # Geschwindigkeit in m/s
        self.acceleration = np.array([0.0, 0.0])         # Beschleunigung in m/s^2
        self.force = np.array([0.0, 0.0])                # Resultierende Kraft in N
        self.radius = radius    # Radius des Körpers in m
        self.fixed = fixed      # Körper wird festgehalten
        self.fixed_x = fixed_x      # x-Koordinate des Körpers bleibt unverändert
        self.color = color      # Farbe für die Darstellung
        

    # Setzt die resultierende Kraft auf null
    def clear_force(self):
        self.force = np.array([0.0, 0.0])


    # Fügt eine Kraft zum Objekt hinzu, z.B. die Schwerkraft
    def add_force(self, force):
        self.force += np.array(force, dtype=float)


    # Berechnet die neue Geschwindigkeit und Position mithilfe des 
    # Euler-Cromer-Verfahrens, wobei die Beschleunigung auf Basis der Kraft 
    # und Masse aktualisiert wird.
    def update_ec(self, dt):
        if self.fixed:
            self.force = np.array([0.0, 0.0]) 
            self.velocity = np.array([0.0, 0.0]) 
            return
        
        self.acceleration = self.force / self.mass
        self.velocity += self.acceleration * dt
        
        if self.fixed_x:
            self.velocity[0] = 0.0
            
        self.position += self.velocity * dt
        

# Die Klasse `Interaction` ist die Basisklasse für alle Wechselwirkungen. 
class Interaction:
    def __init__(self, bodyA, bodyB):
        self.bodyA = bodyA
        self.bodyB = bodyB

    def update(self):
        pass



# Die Klasse `Spring` simuliert eine Feder zwischen zwei Körpern. 
class Spring(Interaction):

    def __init__(self, bodyA, bodyB, k=1.0, length=None, damping=0.9, color=arcade.color.YELLOW):
        super().__init__(bodyA, bodyB)

        self.k = k # Federkonstante
        
        # Ursprungslänge der Feder
        if length is None:
            self.length = np.linalg.norm(bodyA.position - bodyB.position)
        else:
            self.length = length
        
        self.damping = damping # Dämpfungskonstante
        
        self.color = color 


    def calculate_spring_force(self):
        # Berechnet die Federkraft nach dem Hookeschen Gesetz.
        r_vector = self.bodyB.position - self.bodyA.position
        distance = np.linalg.norm(r_vector)
        extension = distance - self.length  # Auslenkung der Feder

        # Berechnet die Federkraft basierend auf der Auslenkung
        force_magnitude = -self.k * extension
        force_direction = r_vector / distance  # Einheitsvektor in Richtung des Abstandsvektors

        # Dämpfungskraft parallel zur Federkraft
        v_rel = self.bodyB.velocity - self.bodyA.velocity
        force_magnitude += -self.damping * np.dot(v_rel, force_direction)
        
        # Berechne die Federkraft
        return force_magnitude * force_direction


    def update(self):
        force = self.calculate_spring_force()
        self.bodyA.add_force(-force)
        self.bodyB.add_force(force)
    


# Die Klasse `Collision` verwaltet die Kollisionserkennung und -berechnung 
# zwischen zwei Körpern.
class Collision(Interaction):

    def __init__(self, bodyA, bodyB, restitution=1.0):
        super().__init__(bodyA, bodyB)
        self.restitution = restitution


    def check_collision(self):
        # Prüft, ob zwei Körper kollidieren.
        distance = np.linalg.norm(self.bodyA.position - self.bodyB.position)
        return distance <= (self.bodyA.radius + self.bodyB.radius)


    def resolve_collision(self):
        # Berechnet die neuen Geschwindigkeiten der beiden Körper nach einer Kollision.
        normal = (self.bodyB.position - self.bodyA.position) / np.linalg.norm(self.bodyB.position - self.bodyA.position)
        relative_velocity = self.bodyA.velocity - self.bodyB.velocity
        velocity_along_normal = np.dot(relative_velocity, normal)

        # Berechnet nur, wenn die Körper aufeinander zu bewegen
        if velocity_along_normal < 0:
            return

        # Impulsberechnung
        impulse = ((1 + self.restitution) * velocity_along_normal) / (1 / self.bodyA.mass + 1 / self.bodyB.mass)
        impulse_vector = impulse * normal

        # Aktualisiert die Geschwindigkeit der beiden Körper
        self.bodyA.velocity -= (impulse_vector / self.bodyA.mass)
        self.bodyB.velocity += (impulse_vector / self.bodyB.mass)


    # Überprüft und berechnet die Kollision, falls nötig
    def update(self):
        if self.check_collision():
            self.resolve_collision()


    
# Die Klasse `AnimationWindow` steuert die grafische Darstellung und die Simulation 
# der Partikelbewegungen.
class AnimationWindow(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        
        # Hintergrundfarbe des Fensters auf Weiß setzen
        arcade.set_background_color(arcade.color.WHITE)
        
        # Minimale Fenstergröße festlegen
        self.set_min_size(width, height)
        
        # Skalierungsfaktor in Pixel/Meter für die Darstellung
        self.scale = 50                       
        
        # Ursprung des Koordinatensystems in die Mitte des Fensters setzen
        self.center = [width // 2 + 100, height // 2]  
        
        # Liste für alle zu simulierenden Körper
        self.bodies = []
        
        # Liste für alle Interaktionen zwischen den Körpern
        self.interactions = []  

        # Simulationszeit in Sekunden
        self.time = 0
        
        # Simulationsstatus (0 = Pause, 1 = Ausführen)
        self.state = 0
        
        # FPS-Berechnung mit gleitendem Durchschnitt
        self.fps_history = [0] * 30
        
        # UI-Manager zur Steuerung der Benutzeroberfläche (Buttons)
        self.uimanager = arcade.gui.UIManager() 
        self.uimanager.enable() 
  
        # Standardstil für Buttons
        default_style = {
            "font_name": ("calibri", "arial"),
            "font_size": 10,
            "font_color": arcade.color.BLACK,
            "border_width": 2,
            "border_color": arcade.color.BLACK,
            "bg_color": arcade.color.WHITE,
            "bg_color_pressed": arcade.color.BLACK,
            "border_color_pressed": arcade.color.BLACK,
            "font_color_pressed": arcade.color.WHITE,
        }
        
        # Erstellen einer vertikalen Box für die Buttons
        v_box = arcade.gui.UIBoxLayout()
        
        # Start/Stop-Button erstellen
        self.start_button = arcade.gui.UIFlatButton(text="Start", height=30, style=default_style)
        self.start_button.on_click = self.on_click_start
        
        v_box.add(self.start_button.with_space_around(bottom=20))
        
        # UI-Komponenten zur Benutzeroberfläche hinzufügen
        self.uimanager.add( 
            arcade.gui.UIAnchorWidget( 
                anchor_x="center_x", 
                anchor_y="center_y",
                align_x=-310,
                align_y=210,
                child=v_box) 
        )

        # Initialisiere die Körper und Wechselwirkungen
        last_body = None
        for i in range(-14,15,1):
            body = Body([i/4, 0], [0, 0], mass=0.1, radius=0.1, fixed_x=True, color=arcade.color.RED)
            
            if last_body is not None:
                spring = Spring(last_body, body, k=30.0, damping=1)
                self.interactions.append(spring)
                
            self.bodies.append(body)
            last_body = body
            
        last_body.fixed = True
    
    # Passt die Ursprungsposition bei Fenstergrößenänderung an
    def on_resize(self, width, height):
        super().on_resize(width, height)
        self.center = [width // 2 + 100, height // 2] 
    

    # Startet und stoppt die Simulation, wenn der Button geklickt wird
    def on_click_start(self, e):
        if self.state == 0:
            self.state = 1
            self.start_button.text = "Stop"
        else:
            self.state = 0
            self.start_button.text = "Start"
    

    # Konvertiert Meterkoordinaten in Pixelkoordinaten für die Darstellung
    def meter_to_pixel(self, x, y):
        pixel_x = self.center[0] + x * self.scale
        pixel_y = self.center[1] + y * self.scale
        return pixel_x, pixel_y


    # Zeichnet die Szene im Fenster
    def on_draw(self):
        arcade.start_render()
        
        # Zeichnet die Benutzeroberfläche
        self.uimanager.draw() 
        
        # Wände und Bodenlinien der Box
        points = []
        points.append(self.meter_to_pixel(-4.5, 4.5))
        points.append(self.meter_to_pixel(-4.5, -4.5))
        points.append(self.meter_to_pixel(4.5, -4.5))
        points.append(self.meter_to_pixel(4.5, 4.5))
        points.append(self.meter_to_pixel(-4.5, 4.5))
        
        arcade.draw_line_strip(points, arcade.color.BLACK, 2)
        
        # Zeigt die Simulationszeit an
        time = round(self.time, 1)
        x, y = self.meter_to_pixel(-9, 3)
        arcade.draw_text(f"t = {time} s", x, y, arcade.color.BLACK)
        
        # Zeigt die FPS an
        fps = round(sum(self.fps_history) / len(self.fps_history), 1)
        x, y = self.meter_to_pixel(-9, 2.5)
        arcade.draw_text(f"FPS = {fps}", x, y, arcade.color.BLACK)

        # Zeichnet die Federn
        for interaction in self.interactions:
            xA, yA = self.meter_to_pixel(interaction.bodyA.position[0], interaction.bodyA.position[1])
            xB, yB = self.meter_to_pixel(interaction.bodyB.position[0], interaction.bodyB.position[1])
            
            arcade.draw_line(xA, yA, xB, yB , interaction.color, 2)
        
        # Zeichnet alle Körper in der Szene
        for body in self.bodies:
            x, y = self.meter_to_pixel(body.position[0], body.position[1])
            r = body.radius * self.scale
            arcade.draw_circle_filled(x, y, r, body.color)

            # zeichne die Geschwindigkeit
            arcade.draw_line(x, y, x + 2*body.velocity[0], y + 2*body.velocity[1] , arcade.color.GREEN, 2)
            
            # zeichne die resultierende Kraft
            arcade.draw_line(x, y, x + 2*body.force[0], y + 2*body.force[1] , arcade.color.BARN_RED, 2)
                


    # Aktualisiert die Simulation um einen Zeitschritt
    def on_update(self, dt):
        # Führe die Funktion nur aus, wenn der Status auf 1 ist.
        if self.state != 1:
            return
        
        # FPS berechnen und als gleitenden Durchschnitt speichern
        self.fps_history.append(1.0/dt)               
        self.fps_history.pop(0)
        
        # Setzt die Kräfte aller Körper auf null
        for body in self.bodies:
            body.clear_force()
        
        # Aktualisiert die Kollisionen
        for interaction in self.interactions:
            interaction.update()
            
        # Berechnet die Kräfte und aktualisiert die Bewegungen der Objekte
        for body in self.bodies:
            body.update_ec(dt)  # Aktualisiert Position und Geschwindigkeit
            
        # move last body in periodic order
        self.bodies[-1].position[1] = sinus_wave(self.time, frequenz=0.5)
        
        # Überprüft und verarbeitet Kollisionen mit dem Boden
        for body in self.bodies:
            # Überprüft und verarbeitet Kollisionen mit dem Boden und der Decke
            if body.position[1] > 4.5 - body.radius:
                body.position[1] = 4.5 - body.radius
                body.velocity[1] *= -1
            if body.position[1] < -4.5 + body.radius:
                body.position[1] = -4.5 + body.radius
                body.velocity[1] *= -1
                
            # Überprüft die Kollisionen mit den Seitenwänden
            if body.position[0] > 4.5 - body.radius:
                body.position[0] = 4.5 - body.radius
                body.velocity[0] *= -1
            elif body.position[0] < -4.5 + body.radius:
                body.position[0] = -4.5 + body.radius
                body.velocity[0] *= -1
            
        # Erhöht die Simulationszeit
        self.time += dt



if __name__ == "__main__":
    # Initialisiert das Fenster für die Simulation
    window = AnimationWindow(800, 600, "Elastischer Körper")

    # starte die Simulation
    arcade.run()




# ___________________________
#                           /
# Zusammenfassung          (
# __________________________\
#
# Die Simulation der Seilwelle zeigt, wie sich Wellen entlang eines elastischen Seils 
# fortpflanzen, indem Kräfte zwischen benachbarten Körpern wirken. Die Welle breitet sich 
# von einem fixierten Ende bis zum anderen aus und spiegelt dabei die Eigenschaften von 
# Wellen in der realen Welt wider, wie Reflexion, Ausbreitungsgeschwindigkeit und Amplitudendämpfung.



# ____________________________
#                            /
# Übungsaufgaben            (
# ____________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Verändere die Federkonstante `k` und die Dämpfung für die Verbindungen zwischen 
# den Körpern im Seil. Beobachte, wie sich die Ausbreitungsgeschwindigkeit und die 
# Amplitude der Welle durch Änderungen dieser Parameter beeinflussen lassen.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Experimentiere mit verschiedenen Bewegungsmustern am fixierten Ende des Seils.
# Erstelle zum Beispiel eine rechteckige oder dreieckige Wellenform und analysiere,
# wie sich diese Wellenform entlang des Seils ausbreitet und an den Enden reflektiert wird.

# Füge hier deine Lösung ein.




#
#   Wellen erzeugen macht Spass.
#       
#      ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(
#   `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `
#  ___ _  _ ___  ___ 
# | __| \| |   \| __|
# | _|| .` | |) | _| 
# |___|_|\_|___/|___|
#                
# -=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=-=x=-=x=-=x=-=-=




# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><
#  _    _   _                                  
# | |  (_)_(_)___ _   _ _ __   __ _  ___ _ __  
# | |   / _ \/ __| | | | '_ \ / _` |/ _ \ '_ \ 
# | |__| (_) \__ \ |_| | | | | (_| |  __/ | | |
# |_____\___/|___/\__,_|_| |_|\__, |\___|_| |_|
#                             |___/            


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Verändere die Federkonstante `k` und die Dämpfung für die Verbindungen zwischen 
# den Körpern im Seil. Beobachte, wie sich die Ausbreitungsgeschwindigkeit und die 
# Amplitude der Welle durch Änderungen dieser Parameter beeinflussen lassen.

'''
# Um die Federkonstante `k` und die Dämpfung anzupassen, ändere die Werte 
# direkt in den Initialisierungen der `Spring`-Objekte in der Klasse `AnimationWindow`.
        
        # Zeile 246
        
        # Initialisiere die Körper und Wechselwirkungen
        last_body = None
        for i in range(-14,15,1):
            body = Body([i/4, 0], [0, 0], mass=0.1, radius=0.1, fixed_x=True, color=arcade.color.RED)
            
            if last_body is not None:
                spring = Spring(last_body, body, k=60.0, damping=0.5)
                self.interactions.append(spring)
                
            self.bodies.append(body)
            last_body = body
            
# Beobachte die Effekte:
# - Ein höherer Wert für `k` erhöht die Wellenfortpflanzungsgeschwindigkeit.
#
# - Eine geringere Dämpfung führt zu größeren Amplituden und weniger Energieverlust
#   pro Schwingungszyklus, was dazu führt, dass die Welle sich weiter ausbreitet.
#
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Experimentiere mit verschiedenen Bewegungsmustern am fixierten Ende des Seils.
# Erstelle zum Beispiel eine rechteckige oder dreieckige Wellenform und analysiere,
# wie sich diese Wellenform entlang des Seils ausbreitet und an den Enden reflektiert wird.

'''
# Ersetze die Bewegung in Zeile 354 mit 

    self.bodies[-1].position[1] = square_wave(self.time, frequenz=0.5)
    
# oder

    self.bodies[-1].position[1] = triangle_wave(self.time, frequenz=0.5)

# Beobachtungen:
# - Die rechteckige Welle erzeugt schnelle Wechsel in der Auslenkung,
#   was schärfere Wellenfronten entlang des Seils zur Folge hat.
#
# - Die dreieckige Welle verläuft langsamer, was zu einer glatteren 
#   Wellenbewegung entlang des Seils führt.
#
# - Analysiere, wie die Wellen an den Rändern reflektiert werden und
#   wie sich die Form der Wellenfront nach der Reflexion verändert.
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

