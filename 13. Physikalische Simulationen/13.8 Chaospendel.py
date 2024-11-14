#              _____________________________________________
#       ______|                                             |_____
#       \     |             13.7 DAS FADENPENDEL            |    /
#        )    |_____________________________________________|   (
#       /________)                                     (________\      13.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# In diesem Kapitel erweitern wir unsere Simulation, um die Bewegung eines 
# Fadenpendels zu simulieren. Das Fadenpendel besteht aus einem Punktkörper, 
# der an einem festen Punkt mit einem masselosen Seil aufgehängt ist.
# Die Rückstellkraft ist proportional zur Auslenkung und zeigt in Richtung 
# der Ruhelage. Diese Kraft ergibt sich durch die Schwerkraft.

# ___________________________________________________
#                                                   /
# Grundkonzepte: Das Fadenpendel                    (
# __________________________________________________\

# - Seilkraft und Schwerkraft:
#   Das Fadenpendel schwingt unter dem Einfluss der Schwerkraft. Die Seilkraft hält den
#   Pendelkörper auf einem festen Radius von der Aufhängung.
#   
#   Es gilt: 
#   
#        F_g = m * g
#        F_seil = - F_g * cos(θ) * r
#   
#   wobei g die Erdbeschleunigung ist und θ der Winkel zwischen dem Seil und der
#   Senkrechten ist. 




import arcade
import arcade.gui 
import numpy as np



# Die Klasse `Body` modelliert ein physikalisches Objekt in der Simulation, 
# das durch seine Position, Geschwindigkeit und Masse beschrieben wird.

class Body:
    def __init__(self, position, velocity, mass=1.0, radius=1.0, fixed=False, color=arcade.color.BLUE):
        self.mass = mass                                 # Masse in kg
        self.position = np.array(position, dtype=float)  # Position in m
        self.velocity = np.array(velocity, dtype=float)  # Geschwindigkeit in m/s
        self.acceleration = np.array([0.0, 0.0])         # Beschleunigung in m/s^2
        self.force = np.array([0.0, 0.0])                # Resultierende Kraft in N
        self.radius = radius                             # Radius des Körpers in m
        self.fixed = fixed                               # Körper wird festgehalten
        self.color = color                               # Farbe für die Darstellung


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
        self.position += self.velocity * dt
        


# Die Klasse `Interaction` verwaltet die Kollisionserkennung und -berechnung 
# zwischen zwei Körpern.
class Interaction:
    def __init__(self, bodyA, bodyB, k=1.0, rest_length=None, restitution=1.0, color=arcade.color.YELLOW):
        self.bodyA = bodyA
        self.bodyB = bodyB

        self.k = k # Federkonstante
        
        # Ursprungslänge der Feder
        if rest_length is None:
            self.rest_length = np.linalg.norm(bodyA.position - bodyB.position)
        else:
            self.rest_length = rest_length
        
        self.restitution = restitution # Energieerhaltung
        
        self.color = color # Farbe für die Darstellung

            

            
    def calculate_spring_force(self):
        # Berechnet die Federkraft nach dem Hookeschen Gesetz.
        r_vector = self.bodyB.position - self.bodyA.position
        distance = np.linalg.norm(r_vector)
        extension = distance - self.rest_length  # Auslenkung der Feder

        # Berechnet die Federkraft basierend auf der Auslenkung
        force_magnitude = -self.k * extension 
        force_direction = r_vector / distance  # Einheitsvektor in Richtung des Abstandsvektors
        
        # Dämpfungskraft proportional zur Geschwindigkeit, entgegengesetzt zur Bewegungsrichtung
        v_rel = self.bodyB.velocity - self.bodyA.velocity
        force_magnitude += -self.restitution * np.dot(v_rel, force_direction)
            
        # Berechne die Federkraft
        return force_magnitude * force_direction


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

    def update(self):
        force = self.calculate_spring_force()
        self.bodyA.add_force(-force)
        self.bodyB.add_force(force)  # Newtons drittes Gesetz (actio = reactio)
        
        # Überprüft und berechnet die Kollision, falls nötig
        #if self.check_collision():
        #    self.resolve_collision()
            
            
            
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

        # Initialisiere zwei Körper
        ball1 = Body([0, 1], [0, 0], mass=0.1, radius=0.1, fixed=True, color=arcade.color.BLACK)
        self.bodies.append(ball1)
        
        ball2 = Body([0, 2.5], [0, 0], mass=0.2, radius=0.2, color=arcade.color.BLUE)
        self.bodies.append(ball2)

        ball3 = Body([0, 4], [-2, 0], mass=0.1, radius=0.2, color=arcade.color.RED)
        self.bodies.append(ball3)

        int12 = Interaction(ball1, ball2, k=300.0, restitution=0.98)
        self.interactions.append(int12)

        int23 = Interaction(ball2, ball3, k=300.0, restitution=0.98)
        self.interactions.append(int23)

    
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
        points.append(self.meter_to_pixel(-4.5, 5))
        points.append(self.meter_to_pixel(-4.5, -4.5))
        points.append(self.meter_to_pixel(4.5, -4.5))
        points.append(self.meter_to_pixel(4.5, 5))
        
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
            #arcade.draw_line(x, y, x + 2*body.velocity[0], y + 2*body.velocity[1] , arcade.color.GREEN, 2)
            
            # zeichne die resultierende Kraft
            #arcade.draw_line(x, y, x + 2*body.force[0], y + 2*body.force[1] , arcade.color.BARN_RED, 2)
        

        
     



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
        for interacion in self.interactions:
            interacion.update()
            
        # Berechnet die Kräfte und aktualisiert die Bewegungen der Objekte
        for body in self.bodies:
            F_G = np.array([0.0, -body.mass * 9.81])  # Schwerkraft
            body.add_force(F_G)

            body.update_ec(dt)  # Aktualisiert Position und Geschwindigkeit
        
        # Überprüft und verarbeitet Kollisionen mit dem Boden
        for body in self.bodies:
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
    window = AnimationWindow(800, 600, "Fadenpendel")

    # starte die Simulation
    arcade.run()





# ____________________________
#                            /
# Wichtige Konzepte          (
# ____________________________\




# ____________________________
#                            /
# Übungsaufgaben            (
# ____________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#


# Füge hier deine Lösung ein.



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
#   


# ___________
#            \
# Aufgabe 1  /
# __________/
#




# ___________
#            \
# Aufgabe 2  /
# __________/
#



# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><





