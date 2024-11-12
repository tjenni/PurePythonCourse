#              _________________________________
#       ______|                                 |_____
#       \     |     13.6 VIELE KOLLISIONEN      |    /
#        )    |_________________________________|   (
#       /________)                          (________\      12.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)




import arcade
import numpy as np
import random



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

    def update_ec(self, dt):
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

        self.time = 0

        # Liste für die Berechnung des gleitendenden Durchschnitt für FPS
        self.fps_history = [0] * 60  
        
        
        for i in range(10):
            for j in range(10):
                vx = 0.5 - random.random()
                vy = 0.5 - random.random()
                ball = Body(1.0, [-2+i/2, -2+j/2], [vx, vy], radius=0.1, color=arcade.color.RED)
                
                for body in self.bodies:
                    interaction = Interaction(body, ball)
                    self.interactions.append(interaction)
                
                self.bodies.append(ball)
        
           


    def meter_to_pixel(self, x, y):
        pixel_x = self.center[0] + x * self.scale
        pixel_y = self.center[1] + y * self.scale
        return pixel_x, pixel_y

    def on_draw(self):
        arcade.start_render()

        # zeichne Box
        x1, y1 = self.meter_to_pixel(-2.1,-2.1)
        x2, y2 = self.meter_to_pixel(2.1,2.1)
        
        w = (x2-x1)
        h = (y2-y1)

        arcade.draw_rectangle_outline(x2-w//2, y2-h//2, w, h, arcade.color.BLACK, 2)


        # zeige die Zeit und die FPS an
        time = round(self.time, 1)
        fps = round( sum(self.fps_history) / len(self.fps_history), 1)
        
        text = f"t = {time} s / FPS = {fps}"
        
        x3, y3 = self.meter_to_pixel(-2.6,2.6)
        arcade.draw_text(text , x3, y3, arcade.color.BLACK)

        # Zeichnen der Objekte
        for body in self.bodies:
            x, y = self.meter_to_pixel(body.position[0], body.position[1])
            radius = body.radius * self.scale

            arcade.draw_circle_filled(x, y, radius, body.color)


    def on_update(self, dt):

        # Berechnung eines gleitenden Durchschnitts der FPS.
        self.fps_history.append(1.0 / dt)               
        self.fps_history.pop(0)

        # Setze die Kräfte zurück
        for body in self.bodies:
            body.clear_force()
        
        # Kollision zwischen den Objekten
        for interacion in self.interactions:
            interacion.update()

        # Aktualisiere die Positionen und Geschwindigkeiten der Objekte
        for body in self.bodies:
            body.update_ec(dt)
        
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
            # Wand links 
            elif body.position[0] < -2:
                body.position[0] = -2
                body.velocity[0] = -body.velocity[0]

        # Zeit erhöhen
        self.time += dt  


if __name__ == "__main__":
    # Erstellen des Fensters mit geeigneter Skalierung
    window = AnimationWindow(800, 600, "Kollision und Impuls", scale=100)
    arcade.run()



