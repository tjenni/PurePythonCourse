#              _________________________________
#       ______|                                  |_____
#       \     |     13.6 VIELETEILCHENSYSTEM     |    /
#        )    |__________________________________|   (
#       /________)                           (________\      12.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# In diesem Kapitel erweitern wir die Simulation um eine große Anzahl von Körpern, 
# die sich in einem geschlossenen Raum bewegen und miteinander kollidieren. 
# Dieses Szenario kann auf das Verhalten von Molekülen in einem Gas oder Flüssigkeit 
# hinweisen, die häufig miteinander und mit den Begrenzungen ihrer Umgebung 
# kollidieren. Dabei werden alle Kollisionen elastisch behandelt, sodass Impuls 
# und Energie innerhalb der Simulation erhalten bleiben.


# ________________________
#                        /
# Grundlegender Aufbau  (
# _______________________\
#
# Die Simulation besteht aus drei Hauptklassen:
#   1.  Body: 
#       Repräsentiert einen einzelnen Körper mit Masse, Position, Geschwindigkeit 
#       und Radius.
#
#   2.  Interaction: 
#       Stellt die Kollision zwischen zwei Körpern dar und berechnet die neuen 
#       Geschwindigkeiten nach einer Kollision.
#
#   3.  AnimationWindow: 
#       Verwaltet das Fenster und die grafische Darstellung der Simulation. 
#       Hier werden die Körper gezeichnet und die Simulation der Kollisionen und 
#       Bewegung in einem geschlossenen Raum ausgeführt.




# ________________________
#                        /
# Ablauf der Simulation  (
# _______________________\
#
#   1.  Erstellen der Objekte: 
#       In einem Rastermuster werden Körper mit leicht zufälligen Geschwindigkeiten 
#       erzeugt, sodass sie sich im Raum frei bewegen können.
#
#   2.  Kollisionserkennung: 
#       Jede Kombination zweier Körper wird auf eine mögliche Kollision geprüft. 
#       Wenn sich zwei Körper berühren, werden ihre Geschwindigkeiten so angepasst, 
#       dass Impuls und kinetische Energie erhalten bleiben.
#
#   3.  Bewegung und Wände: 
#       Die Körper prallen elastisch an den Begrenzungen des Raumes ab. Der Raum 
#       wird durch Wände eingeschlossen, an denen sich die Körper reflektieren.


import arcade
import numpy as np
import random

# Die Klasse `Body` repräsentiert einen einzelnen Körper in der Simulation.
class Body:
    def __init__(self, mass, position, velocity, radius=1.0, color=arcade.color.BLUE):
        self.mass = mass
        self.position = np.array(position, dtype=float)  # Aktuelle Position
        self.velocity = np.array(velocity, dtype=float)  # Aktuelle Geschwindigkeit
        self.radius = radius  # Radius des Körpers für die Kollisionserkennung
        self.color = color  # Farbe des Körpers

    def clear_force(self):
        # Setzt die Kräfte zurück (aktuell keine äußeren Kräfte)
        self.force = np.array([0.0, 0.0])

    def apply_force(self, force):
        # Wendet eine gegebene Kraft auf den Körper an
        self.force += np.array(force, dtype=float)

    def update_ec(self, dt):
        # Aktualisiert die Geschwindigkeit und Position des Körpers für den nächsten Zeitschritt
        acceleration = self.force / self.mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt

    def kinetic_energy(self):
        # Berechnet die kinetische Energie des Körpers
        return 0.5 * self.mass * np.linalg.norm(self.velocity)**2


# Die Klasse `Interaction` verwaltet die Kollisionserkennung und -berechnung 
# zwischen zwei Körpern.
class Interaction:
    def __init__(self, bodyA, bodyB, color=arcade.color.BLUE):
        self.bodyA = bodyA
        self.bodyB = bodyB

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
        impulse = (2 * velocity_along_normal) / (1 / self.bodyA.mass + 1 / self.bodyB.mass)
        impulse_vector = impulse * normal

        # Aktualisiert die Geschwindigkeit der beiden Körper
        self.bodyA.velocity -= (impulse_vector / self.bodyA.mass)
        self.bodyB.velocity += (impulse_vector / self.bodyB.mass)

    def update(self):
        # Überprüft und berechnet die Kollision, falls nötig
        if self.check_collision():
            self.resolve_collision()


# Die Klasse `AnimationWindow` verwaltet die grafische Darstellung und die 
# Animation des Simulationsfensters.
class AnimationWindow(arcade.Window):
    def __init__(self, width, height, title, scale):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

        self.scale = scale  # Skalierungsfaktor für die Darstellung
        self.center = [width // 2, height // 2]  # Zentrum des Fensters
        
        self.bodies = []  # Liste der Körper
        self.interactions = []  # Liste der Interaktionen zwischen Körpern
        
        self.time = 0  # Simulationszeit

        # Liste für die Berechnung des gleitenden Durchschnitts der FPS
        self.fps_history = [0] * 60
        
        # Gesamtenergie aller Teilchen
        self.energy = 0

        # Initialisierung der Körper in einem 10x10-Raster mit zufälligen Geschwindigkeiten
        for i in range(12):
            for j in range(12):
                vx = 0.4 - 0.8*random.random()  # Zufällige Geschwindigkeit in x-Richtung
                vy = 0.4 - 0.8*random.random()  # Zufällige Geschwindigkeit in y-Richtung
                bodyA = Body(1.0, [-1.85+i/3, -1.85+j/3], [vx, vy], radius=0.1, color=arcade.color.RED)
                
                # Erstellen von Interaktionen mit bereits vorhandenen Körpern
                for bodyB in self.bodies:
                    interaction = Interaction(bodyA, bodyB)
                    self.interactions.append(interaction)
                
                self.bodies.append(bodyA)


    def meter_to_pixel(self, x, y):
        # Wandelt Meterkoordinaten in Pixelkoordinaten für die Darstellung um
        pixel_x = self.center[0] + x * self.scale
        pixel_y = self.center[1] + y * self.scale
        return pixel_x, pixel_y


    def draw_v_histogram(self):
        # Zeichne Histogramm der Geschwindigkeiten
        velocities = []
        for body in self.bodies:
            velocities.append(np.linalg.norm(body.velocity))
        
        x4, y4 = self.meter_to_pixel(-3.5,1)
        counts , x  = np.histogram(velocities,bins=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
        
        for i, count in enumerate(counts):
            arcade.draw_line(x4+5*i, y4, x4+5*i, y4 + 2*count, arcade.color.RED, 4)
        
        x5, y5 = self.meter_to_pixel(-3.7,0.6)
        arcade.draw_text("Histogramm v" , x5, y5, arcade.color.BLACK)
        
        x6, y6 = self.meter_to_pixel(-3.7,0.8)
        arcade.draw_text(str(round(x[0],2)) , x6, y6, arcade.color.BLACK)
        
        x7, y7 = self.meter_to_pixel(-2.9,0.8)
        arcade.draw_text(str(round(x[-1],2)) , x7, y7, arcade.color.BLACK) 


    def draw_info(self):
         # Zeigt die Zeit, FPS, Energie und Anzahl Körper an.
        time = round(self.time, 1)
        fps = round(sum(self.fps_history) / len(self.fps_history), 1)
        energy = round(self.energy,1)
        n = len(self.bodies)
        
        text = f"t = {time} s / FPS = {fps} / E = {energy} / N = {n}"
        x3, y3 = self.meter_to_pixel(-2,2.6)
        arcade.draw_text(text , x3, y3, arcade.color.BLACK)


    def on_draw(self):
        # Zeichnet das aktuelle Bild
        arcade.start_render()

        # Zeichnet den umschließenden Rahmen
        x1, y1 = self.meter_to_pixel(-2.1,-2.1)
        x2, y2 = self.meter_to_pixel(2.1,2.1)
        w = (x2-x1)
        h = (y2-y1)
        arcade.draw_rectangle_outline(x2-w//2, y2-h//2, w, h, arcade.color.BLACK, 2)

        # Zeigt die Zeit, FPS, Energie und Anzahl Körper an.
        self.draw_info()
        

        # Zeichnet jeden Körper
        for body in self.bodies:
            x, y = self.meter_to_pixel(body.position[0], body.position[1])
            radius = body.radius * self.scale
            arcade.draw_circle_filled(x, y, radius, body.color)
            
        # Zeichne Histogramm der Geschwindigkeiten
        self.draw_v_histogram()
        


    def on_update(self, dt):
        # Aktualisiert die FPS-Berechnung (gleitender Durchschnitt)
        self.fps_history.append(1.0 / dt)               
        self.fps_history.pop(0)

        # Setzt die Kräfte auf 0 zurück (keine externen Kräfte)
        for body in self.bodies:
            body.clear_force()
        
        # Aktualisiert die Kollisionen
        for interaction in self.interactions:
            interaction.update()

        # Aktualisiert die Positionen und Geschwindigkeiten aller Körper
        for body in self.bodies:
            body.update_ec(dt)
        
        # Überprüft und behandelt Kollisionen mit den Wänden
        for body in self.bodies:
            # Kollision mit Boden und Decke
            if body.position[1]  < -2:
                body.position[1] = -2
                body.velocity[1] = -body.velocity[1]
            elif body.position[1]  > 2:
                body.position[1] = 2
                body.velocity[1] = -body.velocity[1]
                
            # Kollision mit den Seitenwänden
            if body.position[0] > 2:
                body.position[0] = 2
                body.velocity[0] = -body.velocity[0]
            elif body.position[0] < -2:
                body.position[0] = -2
                body.velocity[0] = -body.velocity[0]

        # Berechne die Gesamtenergie aller Körper und speichere sie
        self.energy = 0.0
        for body in self.bodies:
            self.energy += body.kinetic_energy()
           
        

        # Aktualisiert die Simulationszeit
        self.time += dt


if __name__ == "__main__":
    # Erstellen des Fensters mit geeigneter Skalierung
    window = AnimationWindow(800, 600, "Kollision und Impuls", scale=100)
    arcade.run()





# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# todo


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










