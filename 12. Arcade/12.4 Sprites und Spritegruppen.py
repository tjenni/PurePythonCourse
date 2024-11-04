#              _______________________________________
#       ______|                                       |_____
#       \     |    12.4 SPRITES UND SPRITE-GRUPPEN    |    /
#        )    |_______________________________________|   (
#       /________)                                (________\     4.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Sprites sind zentrale Elemente in vielen Spielen und stellen Bilder oder Figuren
# dar, die sich auf dem Bildschirm bewegen können. In Arcade sind Sprites besonders
# einfach zu handhaben und zu gruppieren. In diesem Kapitel lernst du, wie du
# Sprites erstellst, bewegst und in Gruppen organisierst.

import arcade

# _________________________________
#                                 /
# Einfache Sprites erstellen      (
# ________________________________\

# Ein Sprite kann einfach mit einem Bild erstellt werden. In Arcade wird dafür die
# Klasse `arcade.Sprite` verwendet. 

class SingleSpriteExample(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Einzelner Sprite")
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)
        
        # Erstelle ein Sprite mit einem Bild und einer Größe
        self.player = arcade.Sprite("character.png", 0.5)  
        self.player.center_x = 400
        self.player.center_y = 300

    def on_draw(self):
        arcade.start_render()
        self.player.draw()  # Sprite zeichnen

    def on_update(self, delta_time):
        self.player.center_x += 2  # Bewegung des Sprites

window = SingleSpriteExample()
arcade.run()




# _________________________________
#                                 /
# Sprite-Gruppen und Listen      (
# ________________________________\

# In Arcade kann man mehrere Sprites in einer `SpriteList` organisieren, was
# besonders nützlich für Gruppen ähnlicher Objekte ist, z.B. Feinde oder Hindernisse.

class SpriteGroupExample(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Sprite-Gruppen")
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

        # Erstelle eine Sprite-Liste
        self.coins = arcade.SpriteList()

        # Füge der Sprite-Liste mehrere Münzen hinzu
        for i in range(5):
            coin = arcade.Sprite("coin.png", 0.2)
            coin.center_x = i * 100 + 50
            coin.center_y = 300
            self.coins.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.coins.draw()  # Zeichnet alle Sprites in der Liste

window = SpriteGroupExample()
arcade.run()




# _________________________________
#                                 /
# Sprite-Bewegung                (
# ________________________________\

# Die `SpriteList`-Klasse hat nützliche Funktionen für die gleichzeitige Bewegung 
# aller Sprites in der Liste.

class MovingSpriteGroupExample(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Bewegung in Sprite-Gruppen")
        arcade.set_background_color(arcade.color.LIGHT_CORNFLOWER_BLUE)
        
        # Sprite-Liste für fallende Schneeflocken
        self.snowflakes = arcade.SpriteList()

        # Füge Schneeflocken zur Sprite-Liste hinzu
        for i in range(20):
            flake = arcade.Sprite("snowflake.png", 0.1)
            flake.center_x = i * 40 + 20
            flake.center_y = 600
            self.snowflakes.append(flake)

    def on_draw(self):
        arcade.start_render()
        self.snowflakes.draw()

    def on_update(self, delta_time):
        # Bewegt jede Schneeflocke nach unten
        for flake in self.snowflakes:
            flake.center_y -= 2
            if flake.center_y < 0:
                flake.center_y = 600  # Setzt die Schneeflocke zurück

window = MovingSpriteGroupExample()
arcade.run()




# _________________________________
#                                 /
# Kollisionserkennung            (
# ________________________________\

# Arcade ermöglicht eine einfache Kollisionserkennung zwischen Sprites und 
# Sprite-Gruppen, die mit `check_for_collision()` oder `check_for_collision_with_list()` 
# durchgeführt werden kann.

class CollisionExample(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Kollisionserkennung")
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Spieler-Sprite
        self.player = arcade.Sprite("character.png", 0.5)
        self.player.center_x = 400
        self.player.center_y = 100

        # Hindernisse in einer Sprite-Liste
        self.obstacles = arcade.SpriteList()
        for i in range(3):
            obstacle = arcade.Sprite("rock.png", 0.3)
            obstacle.center_x = i * 200 + 200
            obstacle.center_y = 300
            self.obstacles.append(obstacle)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.obstacles.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.center_y += 10
        elif key == arcade.key.DOWN:
            self.player.center_y -= 10
        elif key == arcade.key.LEFT:
            self.player.center_x -= 10
        elif key == arcade.key.RIGHT:
            self.player.center_x += 10

        # Kollisionserkennung
        if arcade.check_for_collision_with_list(self.player, self.obstacles):
            print("Kollision mit Hindernis!")

window = CollisionExample()
arcade.run()




# _________________________________
#                                 /
# Zusammenfassung                (
# ________________________________\

# - Sprites sind zentrale Elemente in Arcade, um Objekte und Figuren darzustellen.
#
# - Mit `SpriteList` können Gruppen von Sprites organisiert und effizient bewegt werden.
#
# - Die Kollisionserkennung zwischen Sprites kann einfach mit 
#   `check_for_collision()` und check_for_collision_with_list()` durchgeführt werden.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine Anwendung, die eine Gruppe von Bällen als Sprites anzeigt.
# Jeder Ball soll sich zufällig nach links oder rechts bewegen und wenn er
# den Rand des Fensters erreicht, soll er die Richtung ändern.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle eine Anwendung, bei der ein Spieler-Sprite durch Pfeiltasten gesteuert wird.
# Wenn der Spieler-Sprite ein Hindernis berührt, soll eine Nachricht „Kollision!“ auf der
# Konsole erscheinen.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Anwendung, bei der eine Gruppe von Münz-Sprites vorhanden ist.
# Wenn der Spieler eine Münze berührt, soll die Münze verschwinden und ein Punkt
# zur Punktzahl hinzugefügt werden. Zeige die aktuelle Punktzahl in der Titelzeile an.


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
# Erstelle eine Anwendung, die eine Gruppe von Bällen als Sprites anzeigt.
# Jeder Ball soll sich zufällig nach links oder rechts bewegen und wenn er
# den Rand des Fensters erreicht, soll er die Richtung ändern.

'''
import arcade
import random

class BallSprite(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(circle_image, 20)
        self.center_x = x
        self.center_y = y
        self.change_x = random.choice([-2, 2])

    def update(self):
        self.center_x += self.change_x
        if self.left < 0 or self.right > arcade.get_window().width:
            self.change_x *= -1  # Richtung ändern


class BallApp(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Ball Bewegung")
        self.ball_list = arcade.SpriteList()

    def setup(self):
        for i in range(10):
            ball = BallSprite(random.randint(50, 550), random.randint(50, 350))
            self.ball_list.append(ball)

    def on_draw(self):
        arcade.start_render()
        self.ball_list.draw()

    def on_update(self, delta_time):
        self.ball_list.update()


# Anwendung starten
window = BallApp()
window.setup()
arcade.run()
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle eine Anwendung, bei der ein Spieler-Sprite durch Pfeiltasten gesteuert wird.
# Wenn der Spieler-Sprite ein Hindernis berührt, soll eine Nachricht „Kollision!“ auf der
# Konsole erscheinen.


'''
import arcade


class PlayerSprite(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


class CollisionApp(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Kollisionsspiel")
        self.player = PlayerSprite("player_image.png", 0.5)
        self.player.center_x = 100
        self.player.center_y = 100
        self.obstacle = arcade.Sprite("obstacle_image.png", 0.5)
        self.obstacle.center_x = 300
        self.obstacle.center_y = 200

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.obstacle.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.change_y = 5
        elif key == arcade.key.DOWN:
            self.player.change_y = -5
        elif key == arcade.key.LEFT:
            self.player.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.UP, arcade.key.DOWN):
            self.player.change_y = 0
        elif key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0

    def on_update(self, delta_time):
        self.player.update()
        if arcade.check_for_collision(self.player, self.obstacle):
            print("Kollision!")


# Anwendung starten
window = CollisionApp()
arcade.run()
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Anwendung, bei der eine Gruppe von Münz-Sprites vorhanden ist.
# Wenn der Spieler eine Münze berührt, soll die Münze verschwinden und ein Punkt
# zur Punktzahl hinzugefügt werden. Zeige die aktuelle Punktzahl in der Titelzeile an.

'''
import arcade
import random


class CoinSprite(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("coin_image.png", 0.5)
        self.center_x = x
        self.center_y = y


class CoinApp(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Münzspiel")
        self.player = PlayerSprite("player_image.png", 0.5)
        self.player.center_x = 100
        self.player.center_y = 100
        self.coin_list = arcade.SpriteList()
        self.score = 0

    def setup(self):
        for _ in range(10):
            coin = CoinSprite(random.randint(50, 550), random.randint(50, 350))
            self.coin_list.append(coin)
        self.update_title()

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.coin_list.draw()

    def update_title(self):
        self.set_caption(f"Münzspiel - Punktzahl: {self.score}")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.change_y = 5
        elif key == arcade.key.DOWN:
            self.player.change_y = -5
        elif key == arcade.key.LEFT:
            self.player.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.UP, arcade.key.DOWN):
            self.player.change_y = 0
        elif key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0

    def on_update(self, delta_time):
        self.player.update()
        coins_hit = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for coin in coins_hit:
            coin.remove_from_sprite_lists()
            self.score += 1
            self.update_title()


# Anwendung starten
window = CoinApp()
window.setup()
arcade.run()
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

