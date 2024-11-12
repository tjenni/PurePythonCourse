#              ________________________________________________
#       ______|                                                |_____
#       \     |         13.5 KOLLISIONEN UND IMPULS            |    /
#        )    |________________________________________________|   (
#       /________)                                         (________\      7.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# In diesem Kapitel lernen wir, wie man Kollisionen zwischen Objekten simuliert 
# und den Impuls bewahrt. Kollisionen sind ein zentraler Bestandteil physikalischer 
# Simulationen und Animationen in Spielen. Wir erfahren, wie man eine Kollision 
# erkennt und den Impuls nach dem Prinzip der Impulserhaltung berechnet.


# ___________________________________________________
#                                                   /
# Grundkonzepte: Kollisionen mit Impulserhaltung   (
# __________________________________________________\

# - Impuls:
#   Der Impuls p eines Objekts ist das Produkt seiner Masse und Geschwindigkeit:
#   
#   p = m * v
#   
#   Bei einer Kollision zweier Objekte bleibt der Gesamtimpuls des Systems erhalten.
#
# - Impulserhaltungsgesetz:
#   Das Impulserhaltungsgesetz besagt, dass in einem geschlossenen System, in 
#   dem keine äusseren Kräfte wirken, der Gesamtimpuls vor und nach der Kollision 
#   gleich bleibt.

# - Arten von Kollisionen:
#   Wir betrachten hier elastische Kollisionen, bei denen sowohl Impuls als auch 
#   kinetische Energie erhalten bleiben.


import arcade
import numpy as np


# ____________________________________
#                                    /
# Klassenstruktur für die Kollision (
# ___________________________________\

# Die Klasse `Body` repräsentiert einen einzelnen Körper in der Simulation.
class Body:
    def __init__(self, position, velocity, mass=1.0, radius=1.0, color=arcade.color.BLUE):
        self.mass = mass
        self.position = np.array(position, dtype=float) # Aktuelle Position
        self.velocity = np.array(velocity, dtype=float) # Aktuelle Geschwindigkeit
        self.radius = radius # Radius des Körpers für die Kollisionserkennung
        self.color = color # Farbe des Körpers

    def clear_force(self):
        # Setzt die Kräfte zurück (aktuell keine äußeren Kräfte)
        self.force = np.array([0.0, 0.0])

    def add_force(self, force):
        # Wendet eine gegebene Kraft auf den Körper an
        self.force += np.array(force, dtype=float)

    def update_ec(self, dt):
        # Aktualisiert die Geschwindigkeit und Position des Körpers für den nächsten Zeitschritt
        acceleration = self.force / self.mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt



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

        # Liste für die Berechnung des gleitendenden Durchschnitt für FPS
        self.fps_history = [0] * 60  

        # Erstellen von zwei sich bewegenden Kugeln für die Kollision
        ball1 = Body([-2, 0.1], [2, 0], mass=1.0, radius=0.5, color=arcade.color.RED)
        self.bodies.append(ball1)
        
        ball2 = Body([2, 0], [-2, 0], mass=1.0, radius=0.5, color=arcade.color.BLUE)
        self.bodies.append(ball2)

        int12 = Interaction(ball1, ball2)
        self.interactions.append(int12)


    def meter_to_pixel(self, x, y):
        # Wandelt Meterkoordinaten in Pixelkoordinaten für die Darstellung um
        pixel_x = self.center[0] + x * self.scale
        pixel_y = self.center[1] + y * self.scale
        return pixel_x, pixel_y


    def on_draw(self):
        # Zeichnet das aktuelle Bild
        arcade.start_render()

        # Zeichnet den umschliessenden Rahmen
        x1, y1 = self.meter_to_pixel(-2.5,-2.5)
        x2, y2 = self.meter_to_pixel(2.5,2.5)
        
        w = (x2-x1)
        h = (y2-y1)

        arcade.draw_rectangle_outline(x2-w//2, y2-h//2, w, h, arcade.color.BLACK, 2)


        # Zeigt die Zeit und die FPS an
        time = round(self.time, 1)
        fps = round( sum(self.fps_history) / len(self.fps_history), 1)
        
        text = f"t = {time} s / FPS = {fps}"
        
        x3, y3 = self.meter_to_pixel(-2.6,2.6)
        arcade.draw_text(text , x3, y3, arcade.color.BLACK)

        # Zeichnet jeden Körper
        for body in self.bodies:
            x, y = self.meter_to_pixel(body.position[0], body.position[1])
            radius = body.radius * self.scale

            arcade.draw_circle_filled(x, y, radius, body.color)


    def on_update(self, dt):
        # Aktualisiert die FPS-Berechnung (gleitender Durchschnitt)
        self.fps_history.append(1.0 / dt)               
        self.fps_history.pop(0)

        # Setzt die Kräfte auf 0 zurück (keine externen Kräfte)
        for body in self.bodies:
            body.clear_force()
        
        # Aktualisiert die Kollisionen
        for interacion in self.interactions:
            interacion.update()

        # Aktualisiert die Positionen und Geschwindigkeiten aller Körper
        for body in self.bodies:
            body.update_ec(dt)
        
        # Überprüft und behandelt Kollisionen mit den Wänden
        for body in self.bodies:
            # Kollision mit Boden und Decke
            if body.position[1]  < -2:
                body.position[1] = -2
                body.velocity[1] *= -1
            elif body.position[1]  > 2:
                body.position[1] = 2
                body.velocity[1] *= -1
                
            # Kollision mit den Seitenwänden
            if body.position[0] > 2:
                body.position[0] = 2
                body.velocity[0] *= -1
            elif body.position[0] < -2:
                body.position[0] = -2
                body.velocity[0] *= -1
            
        # Aktualisiert die Simulationszeit
        self.time += dt  


if __name__ == "__main__":
    # Erstellen des Fensters mit geeigneter Skalierung
    window = AnimationWindow(800, 600, "Kollision und Impuls", scale=100)
    arcade.run()



# ____________________________
#                            /
# Wichtige Konzepte          (
# ____________________________\

# Kollisionserkennung:
# Die Methode `check_collision` überprüft den Abstand zwischen zwei Objekten und 
# bestimmt, ob sie kollidieren. Die Kollision wird erkannt, wenn die Entfernung 
# zwischen ihren Mittelpunkten kleiner oder gleich der Summe ihrer Radien ist.

# Impulserhaltung:
# Die Methode `resolve_collision` berechnet die neue Geschwindigkeit beider Objekte 
# unter Berücksichtigung des Impulserhaltungsgesetzes. Dies stellt sicher, dass 
# die Objekte nach einer Kollision in korrekter Richtung abprallen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ____________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine Simulation mit drei Bällen, die zufällig im Raum positioniert 
# sind und aufeinander zufliegen. Erhöhe die Schwierigkeit, indem du die 
# Geschwindigkeit und Richtung jedes Balls variierst.


# Füge hier deine Lösung ein.



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Modifiziere die Kollisionen der Objekte, sodass eine Energieverlustregel 
# simuliert wird. Das bedeutet, dass bei jeder Kollision 10 % der Energie 
# verloren gehen und die Geschwindigkeit entsprechend angepasst wird.


# Füge hier deine Lösung ein.



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Simulation mit Wänden. Lasse die Objekte abprallen, wenn 
# sie die Fenstergrenzen erreichen, und überprüfe die Impulserhaltung 
# bei jeder Kollision mit der Wand.


# Füge hier deine Lösung ein.



#  ___ _  _ ___  ___ 
# | __| \| |   \| __|
# | _|| .` | |) | _| 
# |___|_|\_|___/|___|
#                
# -=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=-=x=-=x=-=x=-=-=



