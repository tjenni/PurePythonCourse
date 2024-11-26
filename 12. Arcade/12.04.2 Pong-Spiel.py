#              ____________________________
#       ______|                            |_____
#       \     |  12.4.2 PONG SPIEL         |    /
#        )    |____________________________|   (
#       /________)                     (________\     22.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Pong ist eines der ersten Videospiele überhaupt und ein Klassiker der Spielgeschichte. 
# Es simuliert ein Tischtennis-Spiel, bei dem zwei Spieler mit Schlägern versuchen, 
# den Ball am Gegner vorbei zu spielen.

# In diesem Kapitel lernst du, wie du ein Pong-Spiel mit Arcade entwickelst. 
# Du wirst die grundlegende Spiellogik, die Bewegung der Schläger und des Balls 
# sowie die Punkteverwaltung implementieren.

# Die zentralen Themen in diesem Kapitel sind:
# - Steuerung der Schläger durch Tasteneingaben.
# - Bewegung und Kollisionsverhalten des Balls.
# - Punkteverwaltung und Neustart des Spiels.


# ____________________________
#                            /
# Aufbau des Spiels          (
# ____________________________\

# Das Spielfeld ist ein Rechteck mit zwei Schlägern und einem Ball. Die Schläger 
# bewegen sich vertikal entlang der Spielfeldränder, während der Ball sich 
# diagonal bewegt. Ziel des Spiels ist es, den Ball am gegnerischen Schläger 
# vorbei zu spielen.


import arcade
import random
import math


class Paddle():
    def __init__(self, x, y, width=20, height=100, color=arcade.color.WHITE):
        self.x = x
        self.y = y

        self.vy = 0

        self.width = width
        self.height = height

        self.speed = 5

        self.color = color


    def check_collision(self, ball):
        
        result_x = (ball.x - ball.radius < self.x - self.width // 2) and (ball.x + ball.radius > self.x + self.width // 2)
        result_y =  (ball.y - ball.radius < self.y + self.height // 2) and (ball.y + ball.radius > self.y - self.height // 2)

        return result_x and result_y


    def update(self):
        self.y += self.vy


    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)



class Ball():
    def __init__(self, x, y, radius=20, color=arcade.color.WHITE):
        self.x = x
        self.y = y

        self.speed = 5

        angle = math.pi * random.random()

        if angle > math.pi // 2:
            angle += math.pi // 2
        else:
            angle -= math.pi // 2

        self.vx = self.speed * math.cos(angle)
        self.vy = self.speed * math.sin(angle)

        self.radius = radius

        self.color = color


    def update(self):
        self.x += self.vx
        self.y += self.vy


    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius // 2, self.color)

        

        
# Diese Klasse repräsentiert das Pong-Spiel.
class PongGame(arcade.Window):
    
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        arcade.set_background_color(arcade.color.BLACK)

        self.paddle_left = None  # Linker Schläger
        self.paddle_right = None  # Rechter Schläger
        self.ball = None  # Ball

        self.score_left = 0  # Punktestand des linken Spielers
        self.score_right = 0  # Punktestand des rechten Spielers



    # Setzt das Spiel zurück und startet eine neue Runde.
    def setup(self):

        # Schlägerpositionen initialisieren
        self.paddle_left = Paddle(20, self.height // 2, 20, 100)
        self.paddle_right = Paddle(self.width - 20, self.height // 2, 20, 100)
        
        # Ballposition initialisieren
        self.ball = Ball(self.width // 2, self.height // 2)


    # Zeichnet alle Elemente des Spiels.
    def on_draw(self):
        arcade.start_render()
        
        self.paddle_left.draw()
        self.paddle_right.draw()

        self.ball.draw()
        
        # Punktestände anzeigen
        arcade.draw_text(
            f"{self.score_left}", self.width // 4, self.height - 40, arcade.color.WHITE, 20, anchor_x="center"
        )
        arcade.draw_text(
            f"{self.score_right}", 3 * self.width // 4, self.height - 40, arcade.color.WHITE, 20, anchor_x="center"
        )

        #print(self.paddle_left.x, self.ball.x)

    # Aktualisiert den Spielzustand.
    def on_update(self, delta_time):

        self.paddle_left.update()
        self.paddle_right.update()
        self.ball.update()

        # Pralle an der Decke und dem Boden ab
        if self.ball.y <= self.ball.radius  or self.ball.y >= self.height - self.ball.radius:
            self.ball.vy *= -1

        # Pralle von Schläger ab
        if self.paddle_left.check_collision(self.ball) or self.paddle_right.check_collision(self.ball):
            self.ball.vx *= -1
            self.ball.vy += 0.1*(0.5 - random.random())


        # Punkt für den rechten Spieler
        if self.ball.x <= 0:
            self.score_right += 1
            self.setup()
        
        # Punkt für den linken Spieler
        if self.ball.x >= self.width:
            self.score_left += 1
            self.setup()


    # Verarbeitet Tastendrücke für die Bewegung der Schläger.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.paddle_left.vy = self.paddle_left.speed
        elif key == arcade.key.S:
            self.paddle_left.vy = -self.paddle_left.speed
        elif key == arcade.key.UP:
            self.paddle_right.vy = self.paddle_right.speed
        elif key == arcade.key.DOWN:
            self.paddle_right.vy = -self.paddle_right.speed



    def on_key_release(self, key, modifiers):
        if key in [arcade.key.W, arcade.key.S]:
            self.paddle_left.vy = 0
        elif key in [arcade.key.UP, arcade.key.DOWN]:
            self.paddle_right.vy = 0



        


# Hauptprogramm starten
game = PongGame(title="Pong Spiel")
game.setup()
arcade.run()



# ____________________________
#                            /
# Zusammenfassung            (
# ____________________________\

# In diesem Kapitel hast du ein Pong-Spiel programmiert, bei dem zwei Spieler 
# gegeneinander antreten. Du hast gelernt:
# - Wie man die Schläger bewegt und den Ball mit den Schlägern kollidieren lässt.
# - Wie man Punkte vergibt und das Spiel bei einem Punktestand zurücksetzt.
# - Wie man grundlegende Spiellogik implementiert und Arcade-Methoden verwendet.

# Dieses Grundgerüst kann leicht erweitert werden, z. B. durch:
# - Hinzufügen eines Schwierigkeitsgrades für den rechten Spieler (KI-Steuerung).
# - Implementieren eines Punktelimits, bei dem ein Spieler gewinnt.
# - Hinzufügen von Power-Ups, die den Ball schneller oder unvorhersehbarer machen.


# ____________________________
#                            /
# Übungsaufgaben            (
# ____________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erweitere das Spiel, indem du eine KI für den rechten Spieler implementierst.
# Die KI sollte den Schläger automatisch bewegen, um den Ball zu treffen.


# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Füge ein Punktelimit hinzu, bei dem das Spiel endet und der Gewinner angezeigt wird.


# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Füge Power-Ups hinzu, die den Ball schneller machen oder seine Richtung zufällig ändern.


