#              _______________________________________________
#       ______|                                               |_____
#       \     |   12.9 ERSTELLEN EINES EINFACHEN SPIELS       |    /
#        )    |_______________________________________________|   (
#       /________)                                        (________\     4 .11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# In diesem Kapitel entwickeln wir ein einfaches 2D-Spiel mit `arcade`, das die
# bisher erlernten Konzepte kombiniert: Sprites, Kollisionen, Steuerung und Spiel-Logik.
# Das Spiel ist ein klassisches Plattformspiel, bei dem ein Spieler Hindernissen
# ausweichen und Punkte sammeln muss.

import arcade
import random


# _________________________________
#                                 /
# Spiel-Klassen definieren       (
# ________________________________\

# Zunächst erstellen wir eine `Player`-Klasse für den Spieler und eine `Coin`-Klasse
# für die Punkte, die eingesammelt werden müssen.

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", scale=0.5)
        self.center_x = 20
        self.center_y = 100
        self.change_x = 0
        self.change_y = 0


class Coin(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(":resources:images/items/coinGold.png", scale=0.5)
        self.center_x = x
        self.center_y = y




# _________________________________
#                                 /
# Haupt-Spielklasse              (
# ________________________________\

# Die `GameWindow`-Klasse wird das Hauptfenster unseres Spiels sein. Sie verwaltet
# das Spiellayout, die Steuerung und die Interaktion der Objekte.

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Einfaches Plattformspiel")
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.player = None
        self.coin_list = None
        self.physics_engine = None
        self.score = 0

    def setup(self):
        # Spieler- und Coin-Objekte erstellen
        self.player = Player()
        self.coin_list = arcade.SpriteList()
        for i in range(5):
            x = random.randint(100, 700)
            y = random.randint(150, 500)
            coin = Coin(x, y)
            self.coin_list.append(coin)

        # Szene und Physik einrichten
        self.scene = arcade.Scene()
        self.scene.add_sprite("Player", self.player)
        self.scene.add_sprite_list("Coins", sprite_list=self.coin_list)
        
        # Plattformen-Ebene erstellen
        self.wall_list = arcade.SpriteList()
        for x in range(0, 800, 128):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", 0.5)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)
        self.scene.add_sprite_list("Walls", sprite_list=self.wall_list)

        # Physik-Engine aktivieren
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, gravity_constant=0.5, walls=self.wall_list)
        self.score = 0

    def on_draw(self):
        arcade.start_render()
        self.scene.draw()
        arcade.draw_text(f"Score: {self.score}", 10, 570, arcade.color.WHITE, 16)

    def on_update(self, delta_time):
        # Physik aktualisieren und Kollisionen mit Coins prüfen
        self.physics_engine.update()
        coin_hit_list = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP and self.physics_engine.can_jump():
            self.player.change_y = 10
        elif key == arcade.key.LEFT:
            self.player.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0




# _________________________________
#                                 /
# Spiel starten                  (
# ________________________________\

# Erzeuge eine Instanz von `GameWindow` und starte das Spiel.
window = GameWindow()
window.setup()
arcade.run()




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# In diesem Projekt haben wir die Erstellung eines einfachen Spiels behandelt:
#
# - `Player`- und `Coin`-Klassen implementiert und Sprites verwendet.
#
# - Physik-Engine für Kollisionen und Gravitation eingerichtet.
#
# - Benutzersteuerung und Punktezählung implementiert.

# Nutze diese Konzepte als Grundlage für eigene Spiele und erweitere sie mit
# Hindernissen, Level-Designs und neuen Spielmechaniken.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Füge Hindernisse hinzu, die der Spieler vermeiden muss. Verwende dazu
# Sprites und implementiere eine Kollisionserkennung, um Punkte abzuziehen.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Implementiere ein Spielziel, indem du ein Ziel-Sprite platzierst. Wenn der Spieler
# das Ziel erreicht, sollte eine Nachricht angezeigt werden, die das Level als
# abgeschlossen anzeigt.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erweitere das Spiel um mehrere Levels. Erstelle einen Mechanismus, um zum nächsten
# Level zu wechseln, nachdem alle Coins eingesammelt wurden.


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
# Füge Hindernisse hinzu, die der Spieler vermeiden muss. Verwende dazu
# Sprites und implementiere eine Kollisionserkennung, um Punkte abzuziehen.

'''
import arcade
import random

class AvoidObstacleGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Hindernisse vermeiden")
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 150
        self.obstacle_list = arcade.SpriteList()
        self.score = 100

        # Hindernisse erstellen
        for i in range(5):
            obstacle = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", 0.5)
            obstacle.center_x = random.randint(200, 700)
            obstacle.center_y = random.randint(100, 500)
            self.obstacle_list.append(obstacle)

    def on_draw(self):
        arcade.start_render()
        self.player_sprite.draw()
        self.obstacle_list.draw()
        arcade.draw_text(f"Punkte: {self.score}", 10, 570, arcade.color.BLACK, 20)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
        elif key == arcade.key.UP:
            self.player_sprite.change_y = 5
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -5

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.RIGHT, arcade.key.LEFT):
            self.player_sprite.change_x = 0
        elif key in (arcade.key.UP, arcade.key.DOWN):
            self.player_sprite.change_y = 0

    def on_update(self, delta_time):
        self.player_sprite.update()
        # Kollisionserkennung
        if arcade.check_for_collision_with_list(self.player_sprite, self.obstacle_list):
            self.score -= 1  # Punktabzug

window = AvoidObstacleGame()
arcade.run()
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Implementiere ein Spielziel, indem du ein Ziel-Sprite platzierst. Wenn der Spieler
# das Ziel erreicht, sollte eine Nachricht angezeigt werden, die das Level als
# abgeschlossen anzeigt.

'''
import arcade
import random

class ReachGoalGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Ziel erreichen")
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 150
        self.goal_sprite = arcade.Sprite(":resources:images/items/flagGreen1.png", 0.5)
        self.goal_sprite.center_x = 750
        self.goal_sprite.center_y = 150
        self.level_complete = False

    def on_draw(self):
        arcade.start_render()
        self.player_sprite.draw()
        self.goal_sprite.draw()
        if self.level_complete:
            arcade.draw_text("Level abgeschlossen!", 300, 300, arcade.color.GREEN, 24)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
        elif key == arcade.key.UP:
            self.player_sprite.change_y = 5
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -5

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.RIGHT, arcade.key.LEFT):
            self.player_sprite.change_x = 0
        elif key in (arcade.key.UP, arcade.key.DOWN):
            self.player_sprite.change_y = 0

    def on_update(self, delta_time):
        self.player_sprite.update()
        # Überprüfen, ob das Ziel erreicht wurde
        if arcade.check_for_collision(self.player_sprite, self.goal_sprite):
            self.level_complete = True

window = ReachGoalGame()
arcade.run()
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erweitere das Spiel um mehrere Levels. Erstelle einen Mechanismus, um zum nächsten
# Level zu wechseln, nachdem alle Coins eingesammelt wurden.

'''
import arcade
import random

class MultiLevelGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Mehrere Levels")
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 150
        self.coin_list = arcade.SpriteList()
        self.level = 1
        self.score = 0
        self.setup_level()

    def setup_level(self):
        # Coins für das Level erstellen
        self.coin_list = arcade.SpriteList()
        for i in range(self.level * 5):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", 0.5)
            coin.center_x = random.randint(100, 700)
            coin.center_y = random.randint(100, 500)
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.player_sprite.draw()
        self.coin_list.draw()
        arcade.draw_text(f"Level: {self.level}", 10, 570, arcade.color.BLACK, 20)
        arcade.draw_text(f"Punkte: {self.score}", 10, 550, arcade.color.BLACK, 20)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
        elif key == arcade.key.UP:
            self.player_sprite.change_y = 5
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -5

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.RIGHT, arcade.key.LEFT):
            self.player_sprite.change_x = 0
        elif key in (arcade.key.UP, arcade.key.DOWN):
            self.player_sprite.change_y = 0

    def on_update(self, delta_time):
        self.player_sprite.update()
        # Überprüfen, ob ein Coin gesammelt wurde
        coins_collected = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coins_collected:
            coin.remove_from_sprite_lists()
            self.score += 10
        
        # Zum nächsten Level wechseln, wenn alle Coins eingesammelt sind
        if len(self.coin_list) == 0:
            self.level += 1
            self.setup_level()

window = MultiLevelGame()
arcade.run()
'''



# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


