#              ___________________________________
#       ______|                                   |_____
#       \     |     13.8 GRAVITATIONSKRAFT        |    /
#        )    |___________________________________|   (
#       /________)                            (________\      13.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# In diesem Kapitel erweitern wir unsere Simulation, um die Gravitationskräfte zwischen
# Himmelskörpern zu simulieren und die Bahnen von Planeten zu berechnen. Die Gravitationskraft
# zwischen zwei Massen führt zu einer Anziehung, die proportional zum Produkt der Massen und 
# umgekehrt proportional zum Quadrat ihres Abstands ist. Diese Simulation illustriert die 
# Bewegung der Planeten um die Sonne und die Anziehungskraft, die sie aufeinander ausüben.


# _____________________________________
#                                     /
# Grundkonzepte: Gravitationskraft   (
# ____________________________________\

# - Gravitationskraft:
#   Die Gravitationskraft \( F \) zwischen zwei Massen \( m_1 \) und \( m_2 \) im Abstand \( r \) 
#   wird beschrieben durch:
#   
#        F = G * (m1 * m2) / r^2
#   
#   wobei G die Gravitationskonstante ist und in Luft oder Vakuum den Wert
#   6.674 * 10^-11 (Nm}^2/kg^2 hat.
#
# - Himmelskörper:
#   Die Planeten in der Simulation erhalten eine Masse und eine Anfangsgeschwindigkeit,
#   die ihre Bewegung im Gravitationsfeld steuert. Diese Kräfte führen zu elliptischen Bahnen 
#   oder stabilen Orbits je nach Anfangsbedingungen der Bewegung.



import arcade
import arcade.gui 
import numpy as np


class Body:
    def __init__(self, position, velocity, mass=1.0, charge=1.0, radius=1.0, color=arcade.color.BLUE):
        self.mass = mass                                 # Masse in kg
        self.position = np.array(position, dtype=float)  # Position in m
        self.velocity = np.array(velocity, dtype=float)  # Geschwindigkeit in m/s
        self.acceleration = np.array([0.0, 0.0])         # Beschleunigung in m/s^2
        self.force = np.array([0.0, 0.0])                # Resultierende Kraft in N
        self.charge = charge                             # Elektrische Ladung in Coulomb (C)
        self.radius = radius                             # Radius des Körpers in m
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
        self.acceleration = self.force / self.mass
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt
        


# Die Klasse `Interaction` verwaltet die Kollisionserkennung und -berechnung 
# zwischen zwei Körpern.
class Interaction:
    # Die Gravitationskonstante G in Nm²/kg²
    G = 6.67430e-11
    
    def __init__(self, bodyA, bodyB, color=arcade.color.YELLOW):
        self.bodyA = bodyA
        self.bodyB = bodyB

        self.color = color # Farbe für die Darstellung
        
    def check_collision(self):
        # Prüft, ob zwei Körper kollidieren.
        distance = np.linalg.norm(self.bodyA.position - self.bodyB.position)
        return distance <= (self.bodyA.radius + self.bodyB.radius)
        
    
    def resolve_collision(self, restitution=0.9):
        # Berechnet die neuen Geschwindigkeiten der beiden Körper nach einer Kollision.
        normal = (self.bodyB.position - self.bodyA.position) / np.linalg.norm(self.bodyB.position - self.bodyA.position)
        relative_velocity = self.bodyA.velocity - self.bodyB.velocity
        velocity_along_normal = np.dot(relative_velocity, normal)

        # Berechnet nur, wenn die Körper aufeinander zu bewegen
        if velocity_along_normal < 0:
            return

        # Impulsberechnung
        impulse = ((1 + restitution) * velocity_along_normal) / (1 / self.bodyA.mass + 1 / self.bodyB.mass)
        impulse_vector = impulse * normal

        # Aktualisiert die Geschwindigkeit der beiden Körper
        self.bodyA.velocity -= (impulse_vector / self.bodyA.mass)
        self.bodyB.velocity += (impulse_vector / self.bodyB.mass)
        
        
    def calculate_gravitational_force(self):
        # Berechnet die Gravitationskraft zwischen zwei Massen.
        r_vector = self.bodyB.position - self.bodyA.position
        distance = np.linalg.norm(r_vector)
        
        if distance < self.bodyA.radius + self.bodyB.radius:
            return np.array([0.0, 0.0])  # Vermeidet unphysikalisch große Kräfte bei sehr kleinem Abstand

        force_magnitude = Interaction.G * self.bodyA.mass * self.bodyB.mass / distance**2
        force_direction = r_vector / distance  # Einheitsvektor in Richtung des Abstandsvektors
        
        return force_magnitude * force_direction


    # Wendet die Coulomb-Kraft auf beide Körper an
    def update(self):
        force = self.calculate_gravitational_force()
        self.bodyA.add_force(force)
        self.bodyB.add_force(-force)  # Newtons drittes Gesetz (actio = reactio)
        
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
        self.scale = 1e-9                   
        
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

        # Initialisiere zwei Himmelskörper, z.B. Sonne und Planet
        sun = Body([0, 0], [0, 0], mass=1.989e30, radius=1e9, color=arcade.color.RED)
        planet = Body([1.5e11, 0], [0, 2.98e4], mass=5.972e24, radius=1e8, color=arcade.color.BLUE)
        
        self.bodies.extend([sun, planet])
        
        self.interactions.append(Interaction(sun, planet))


    
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
        
        # Zeigt die Simulationszeit an
        time = round(self.time, 1)
        x, y = (-450 + self.center[0], 150 + self.center[1])
        arcade.draw_text(f"t = {time} s", x, y, arcade.color.BLACK)
        
        # Zeigt die FPS an
        fps = round(sum(self.fps_history) / len(self.fps_history), 1)
        x, y = (-450 + self.center[0], 100 + self.center[1])
        arcade.draw_text(f"FPS = {fps}", x, y, arcade.color.BLACK)
        
        # Zeichnet alle Körper in der Szene
        for body in self.bodies:
            x, y = self.meter_to_pixel(body.position[0], body.position[1])
            r = body.radius * self.scale
            r = max(5,r)
            arcade.draw_circle_filled(x, y, r, body.color)



    # Aktualisiert die Simulation um einen Zeitschritt
    def on_update(self, dt):
        # Führe die Funktion nur aus, wenn der Status auf 1 ist.
        if self.state != 1:
            return
        
        # FPS berechnen und als gleitenden Durchschnitt speichern
        self.fps_history.append(1.0/dt)               
        self.fps_history.pop(0)
        
        dt = 5*3600
        
        # Setzt die Kräfte aller Körper auf null
        for body in self.bodies:
            body.clear_force()
        
        
        # Aktualisiert die Kollisionen
        for interacion in self.interactions:
            interacion.update()
            
        # Berechnet die Kräfte und aktualisiert die Bewegungen der Objekte
        for body in self.bodies:
            body.update_ec(dt)  # Aktualisiert Position und Geschwindigkeit
        
            
        # Erhöht die Simulationszeit
        self.time += dt  



if __name__ == "__main__":
    # Initialisiert das Fenster für die Simulation
    window = AnimationWindow(800, 600, "Stern und Planet")

    # starte die Simulation
    arcade.run()






# ____________________________
#                            /
# Zusammenfassung            (
# ____________________________\




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


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


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><




