#              ________________________________________________
#       ______|                                                |_____
#       \     |         13.5 KOLLISIONEN UND IMPULS            |    /
#        )    |________________________________________________|   (
#       /________)                                         (________\      7.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# In diesem Kapitel lernen wir, wie man Kollisionen zwischen Objekten simuliert 
# und den Impuls bewahrt. Kollisionen sind ein zentraler Bestandteil physikalischer 
# Simulationen und Animationen in Spielen. Wir erfahren, wie man eine Kollision 
# erkennt und den Impuls nach dem Prinzip der Impulserhaltung berechnet.


# __________________________________________
#                                          /
# Grundkonzepte: Impuls und Kollisionen   (
# _________________________________________\

# - **Impuls**:
#   Der Impuls \( p \) eines Objekts ist das Produkt seiner Masse und Geschwindigkeit:
#   \[
#   p = m \times v
#   \]
#   Bei einer Kollision zweier Objekte bleibt der Gesamtimpuls des Systems erhalten.
#
# - **Impulserhaltungsgesetz**:
#   Das Impulserhaltungsgesetz besagt, dass in einem geschlossenen System, in dem keine äußeren Kräfte wirken, der Gesamtimpuls vor und nach der Kollision gleich bleibt.

# - **Arten von Kollisionen**:
#   Wir betrachten hier elastische Kollisionen, bei denen sowohl Impuls als auch kinetische Energie erhalten bleiben.


import arcade
import numpy as np


# _________________________________
#                                 /
# Klassenstruktur für die Kollision(
# _________________________________\

# Die `Body`-Klasse enthält Methoden zur Kollisionserkennung und 
# Impulsberechnung. Eine zusätzliche `AnimationWindow`-Klasse 
# sorgt für das Fenster und die Simulation der Kollisionen.

class Body:
    def __init__(self, mass, position, velocity, radius=1.0, color=arcade.color.BLUE):
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.radius = radius
        self.color = color

    def clear_force(self):
        self.force = np.array([0.0, 0.0])

    def apply_force(self, force):
        self.force += np.array(force, dtype=float)

    def update(self, dt):
        acceleration = self.force / self.mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt



class Interaction:
    def __init__(self, bodyA, bodyB, color=arcade.color.BLUE):
        self.bodyA = bodyA
        self.bodyB = bodyB

    def check_collision(self):
        """Prüfe, ob zwei Objekte kollidieren."""
        distance = np.linalg.norm(self.bodyA.position - self.bodyB.position)
        return distance <= (self.bodyA.radius + self.bodyB.radius)
    
    def resolve_collision(self):
        """Berechne die Geschwindigkeit nach der Kollision mit einem anderen Objekt."""
        normal = (self.bodyB.position - self.bodyA.position) / np.linalg.norm(self.bodyB.position - self.bodyA.position)
        relative_velocity = self.bodyA.velocity - self.bodyB.velocity
        velocity_along_normal = np.dot(relative_velocity, normal)

        # Nur berechnen, wenn die Objekte aufeinander zu bewegen
        if velocity_along_normal < 0:
            return

        # Berechnung des Impulses
        impulse = (2 * velocity_along_normal) / (1 / self.bodyA.mass + 1 / self.bodyB.mass)
        impulse_vector = impulse * normal

        # Geschwindigkeit nach der Kollision
        self.bodyA.velocity -= (impulse_vector / self.bodyA.mass)
        self.bodyB.velocity += (impulse_vector / self.bodyB.mass)


    def update(self):

        if self.check_collision():
            self.resolve_collision()









class AnimationWindow(arcade.Window):
    def __init__(self, width, height, title, scale):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

        self.scale = scale
        self.center = [width // 2, height // 2]
        
        self.bodies = []
        self.interactions = []

        # Erstellen von zwei sich bewegenden Kugeln für die Kollision
        ball1 = Body(1.0, [-2, 0.1], [2, 0], radius=0.5, color=arcade.color.RED)
        self.bodies.append(ball1)
        
        ball2 = Body(1.0, [2, 0], [-2, 0], radius=0.5, color=arcade.color.BLUE)
        self.bodies.append(ball2)


        int12 = Interaction(ball1, ball2)
        self.interactions.append(int12)


    def meter_to_pixel(self, x, y):
        pixel_x = self.center[0] + x * self.scale
        pixel_y = self.center[1] + y * self.scale
        return pixel_x, pixel_y

    def on_draw(self):
        arcade.start_render()

        # Zeichnen der Objekte
        for body in self.bodies:
            x, y = self.meter_to_pixel(body.position[0], body.position[1])
            radius = body.radius * self.scale

            arcade.draw_circle_filled(x, y, radius, body.color)


    def on_update(self, delta_time):
        # Bewegung der Objekte
        for body in self.bodies:
            body.clear_force()
        
        # Kollisionserkennung und -lösung
        for interacion in self.interactions:
            interacion.update()
        
        # Überprüfe Kollisionen mit den Wänden
        for body in self.bodies:
            # Boden
            if body.position[1]  < -2:
                body.position[1] = -2
                body.velocity[1] = -body.velocity[1]
            # Decke
            elif body.position[1]  > 2:
                body.position[1] = 2
                body.velocity[1] = -body.velocity[1]
                
            # Wand rechts 
            if body.position[0] > 2:
                body.position[0] = 2
                body.velocity[0] = -body.velocity[0]
            # Wand rechts 
            elif body.position[0] < -2:
                body.position[0] = -2
                body.velocity[0] = -body.velocity[0]
            

        # Aktualisiere die Position der Kugeln
        for body in self.bodies:
            body.update(delta_time)


if __name__ == "__main__":
    # Erstellen des Fensters mit geeigneter Skalierung
    window = AnimationWindow(800, 600, "Kollision und Impuls", scale=100)
    arcade.run()



# ____________________________
#                            /
# Wichtige Konzepte          (
# ____________________________\

# **Kollisionserkennung**:
# Die Methode `check_collision` überprüft den Abstand zwischen zwei Objekten und 
# bestimmt, ob sie kollidieren. Die Kollision wird erkannt, wenn die Entfernung 
# zwischen ihren Mittelpunkten kleiner oder gleich der Summe ihrer Radien ist.

# **Impulserhaltung**:
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

