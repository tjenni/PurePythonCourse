#              ____________________________________________
#       ______|                                            |_____
#       \     |    12.5 SPIEL-LOGIK UND PHYSIK IN ARCADE   |    /
#        )    |____________________________________________|   (
#       /________)                                     (________\     4.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Die Spiel-Logik und Physik sind grundlegende Bestandteile jeder Spielentwicklung.
# In Arcade lassen sich Regeln und Bewegungsabläufe effizient mit eigenen Methoden
# und Funktionen umsetzen. In diesem Kapitel erfährst du, wie du grundlegende
# Spiel-Logik, einfache Physik und Kollisionen für dynamische Spiele implementierst.


import arcade


# _________________________________
#                                 /
# Grundlegende Spiel-Logik        (
# ________________________________\

# Die Spiel-Logik umfasst Regeln und Mechaniken, die bestimmen, wie das Spiel 
# abläuft. Dies können Punkte, Leben, Timer oder Level-Übergänge sein.

class SimpleGameLogicExample(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Grundlegende Spiel-Logik")
        arcade.set_background_color(arcade.color.WHITE)

        # Spiel-Logik
        self.score = 0
        self.lives = 3
        self.player = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.player.center_x = 400
        self.player.center_y = 100

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        
        # Punktzahl und Leben anzeigen
        arcade.draw_text(f"Punkte: {self.score}", 30, 570, arcade.color.BLACK, 18)
        arcade.draw_text(f"Leben: {self.lives}", 670, 570, arcade.color.RED, 18)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.score += 10
        elif key == arcade.key.DOWN:
            self.lives -= 1  # Leben verlieren

window = SimpleGameLogicExample()
arcade.run()




# ______________________________________
#                                      /
# Grundlegende Physik und Schwerkraft (
# _____________________________________\

# Arcade bietet ein Modul für einfache Physik wie Schwerkraft und Kollisionen.
# Dies lässt sich besonders gut mit der `PhysicsEngineSimple` und der `PhysicsEnginePlatformer`
# umsetzen, die Arcade für uns bereitstellt.

class SimplePhysicsExample(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Grundlegende Physik")
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

        # Spieler-Sprite und Boden-Sprite
        self.player = arcade.Sprite("character.png", 0.5)
        self.player.center_x = 400
        self.player.center_y = 300
        self.platform_list = arcade.SpriteList()

        # Einfache Boden-Plattform
        ground = arcade.SpriteSolidColor(800, 50, arcade.color.ASPARAGUS)
        ground.center_x = 400
        ground.center_y = 25
        self.platform_list.append(ground)

        # Physics-Engine mit Schwerkraft
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, self.platform_list, gravity_constant=0.5)

    def on_draw(self):
        arcade.start_render()
        self.platform_list.draw()
        self.player.draw()

    def on_update(self, delta_time):
        # Aktualisierung der Physics-Engine
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        # Springen mit der Leertaste
        if key == arcade.key.SPACE and self.physics_engine.can_jump():
            self.player.change_y = 10

window = SimplePhysicsExample()
arcade.run()




# __________________________________
#                                  /
# Kollisionen und Interaktionen   (
# _________________________________\

# Die Kollisionserkennung und Interaktion sind wichtige Bestandteile der Spiel-Logik,
# um zu bestimmen, wann Objekte aufeinandertreffen und wie sie reagieren sollen.

class CollisionInteractionExample(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Kollision und Interaktion")
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Spieler-Sprite und Plattform-Sprites
        self.player = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.player.center_x = 100
        self.player.center_y = 100
        self.player.speed_x = 0
        self.player.speed_y = 0
        self.coin_list = arcade.SpriteList()

        # Erstelle Münzen für das Sammeln
        for i in range(5):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", 0.5)
            coin.center_x = 150 * (i + 1)
            coin.center_y = 200
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.coin_list.draw()
        
    def on_update(self, delta_time):
        self.player.center_x += self.player.speed_x
        self.player.center_y += self.player.speed_y
        
        # Kollisionserkennung zwischen Spieler und Münzen
        coins_collected = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for coin in coins_collected:
            coin.remove_from_sprite_lists()
            print("Münze eingesammelt!")

    def on_key_press(self, key, modifiers):
        # Bewege den Spieler mit den Pfeiltasten
        if key == arcade.key.UP:
            self.player.speed_y = 5
        elif key == arcade.key.DOWN:
            self.player.speed_y = -5
        elif key == arcade.key.LEFT:
            self.player.speed_x = -5
        elif key == arcade.key.RIGHT:
            self.player.speed_x = 5
            
    def on_key_release(self, key, modifiers):
        # Stoppe die Bewegung, wenn die Taste losgelassen wird
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.player.speed_y = 0
        elif key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player.speed_x = 0

window = CollisionInteractionExample()
arcade.run()







# ____________________________________
#                                    /
# Fortgeschrittene Physik mit pymunk (
# ___________________________________\

# Für komplexere Physik kann die pymunk-Engine in Arcade genutzt werden. Sie
# unterstützt realistische Bewegungen und Kollisionen.
# siehe https://api.arcade.academy/en/2.6.15/tutorials/pymunk_platformer/index.html

class AdvancedPhysicsExample(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Fortgeschrittene Physik")
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Spieler- und Plattform-Sprite
        self.player = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.player.center_x = 400
        self.player.center_y = 300
        self.platform_list = arcade.SpriteList()

        # Plattform mit physikalischen Eigenschaften
        ground = arcade.SpriteSolidColor(800, 50, arcade.color.SAND)
        ground.center_x = 400
        ground.center_y = 25
        self.platform_list.append(ground)
        
        self.right_pressed = False
        self.left_pressed = False

        # pymunk Physics-Engine
        self.physics_engine = arcade.PymunkPhysicsEngine(damping=1.0,
                                                         gravity=(0.0,-1500))
        self.physics_engine.add_sprite(self.player,
                                       mass=1.0,
                                       moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
                                       collision_type="player")
        
        self.physics_engine.add_sprite_list(self.platform_list,
                                            friction=1,
                                            collision_type="wall",
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)
        
    def on_draw(self):
        arcade.start_render()
        self.platform_list.draw()
        self.player.draw()
        
    def on_update(self, delta_time):
            
        # Bewege den Spieler mit den Pfeiltasten
        if self.left_pressed:
            self.physics_engine.apply_force(self.player, (-1000, 0))
            
        elif self.right_pressed:
            self.physics_engine.apply_force(self.player, (1000, 0))
    
        # Aktualisierung der Physics-Engine
        self.physics_engine.step()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
        elif key == arcade.key.UP:
            self.up_pressed = True
            # find out if player is standing on ground, and not on a ladder
            if self.physics_engine.is_on_ground(self.player):
                # She is! Go ahead and jump
                self.physics_engine.apply_impulse(self.player, (0, 800))
            
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
            
window = AdvancedPhysicsExample()
arcade.run()






# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Die Spiel-Logik legt fest, wie das Spiel abläuft und was während des Spiels passiert.
#
# - Grundlegende Physik und Schwerkraft können mit `PhysicsEnginePlatformer` umgesetzt werden.
#
# - Kollisionen und Interaktionen sind essenziell, um Reaktionen und Spielfortschritte
#   im Spiel zu implementieren.
#
# - Für fortgeschrittene Physik kann die `pymunk` in Arcade verwendet werden.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein einfaches Spiel, bei dem ein Ball auf eine Plattform fällt. Füge
# Schwerkraft hinzu und sorge dafür, dass der Ball zurückprallt, wenn er die Plattform berührt.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle eine Anwendung, bei der der Spieler-Sprite Münzen sammeln kann, die zufällig
# auf dem Bildschirm erscheinen. Jede gesammelte Münze sollte die Punktzahl erhöhen,
# und die Punktzahl sollte auf der Konsole angezeigt werden.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe ein Programm, in dem ein Spieler-Sprite Hindernissen ausweichen muss,
# die sich von oben nach unten bewegen. Wenn der Spieler ein Hindernis trifft,
# verliert er ein Leben. Zeige die verbleibenden Leben in der Titelzeile an.


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
# Erstelle ein einfaches Spiel, bei dem ein Ball auf eine Plattform fällt. Füge
# Schwerkraft hinzu und sorge dafür, dass der Ball zurückprallt, wenn er die Plattform berührt.

'''
import arcade
import random

class BallPlatformGame(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Ball und Plattform")
        self.ball = arcade.SpriteCircle(20, arcade.color.BLUE)
        self.ball.center_x = 300
        self.ball.center_y = 300
        self.ball.change_y = 0  # Anfangsgeschwindigkeit
        self.platform = arcade.SpriteSolidColor(100, 20, arcade.color.GREEN)
        self.platform.center_x = 300
        self.platform.center_y = 50
        self.gravity = -0.3

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()
        self.platform.draw()

    def on_update(self, delta_time):
        self.ball.change_y += self.gravity  # Schwerkraft anwenden
        self.ball.center_y += self.ball.change_y
        
        # Prüfe Kollision mit der Plattform
        if self.ball.collides_with_sprite(self.platform) and self.ball.change_y < 0:
            self.ball.change_y *= -0.8  # Rückprall mit Verlust

        # Beschränkung am unteren Rand
        if self.ball.bottom < 0:
            self.ball.center_y = 300
            self.ball.change_y = 0


# Anwendung starten
window = BallPlatformGame()
arcade.run()
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle eine Anwendung, bei der der Spieler-Sprite Münzen sammeln kann, die zufällig
# auf dem Bildschirm erscheinen. Jede gesammelte Münze sollte die Punktzahl erhöhen,
# und die Punktzahl sollte auf der Konsole angezeigt werden.

'''
import arcade
import random

class CoinCollectGame(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Münzen sammeln")
        self.player = arcade.SpriteSolidColor(30, 30, arcade.color.BLUE)
        self.player.center_x = 300
        self.player.center_y = 200
        self.coin_list = arcade.SpriteList()
        self.score = 0
        self.spawn_coins()

    def spawn_coins(self):
        for _ in range(5):
            coin = arcade.SpriteCircle(10, arcade.color.GOLD)
            coin.center_x = random.randint(20, 580)
            coin.center_y = random.randint(20, 380)
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.coin_list.draw()
        arcade.draw_text(f"Punktzahl: {self.score}", 10, 10, arcade.color.BLACK, 14)

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
            print(f"Neue Punktzahl: {self.score}")
            # Nach dem Sammeln wieder neue Münzen hinzufügen, falls alle gesammelt sind
            if len(self.coin_list) == 0:
                self.spawn_coins()


# Anwendung starten
window = CoinCollectGame()
arcade.run()
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe ein Programm, in dem ein Spieler-Sprite Hindernissen ausweichen muss,
# die sich von oben nach unten bewegen. Wenn der Spieler ein Hindernis trifft,
# verliert er ein Leben. Zeige die verbleibenden Leben in der Titelzeile an.

'''
import arcade
import random

class DodgeGame(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Ausweichen")
        self.player = arcade.SpriteSolidColor(30, 30, arcade.color.BLUE)
        self.player.center_x = 300
        self.player.center_y = 50
        self.obstacle_list = arcade.SpriteList()
        self.lives = 3
        self.spawn_obstacles()
        self.update_title()

    def spawn_obstacles(self):
        for _ in range(5):
            obstacle = arcade.SpriteSolidColor(20, 20, arcade.color.RED)
            obstacle.center_x = random.randint(20, 580)
            obstacle.center_y = random.randint(300, 400)
            obstacle.change_y = -2
            self.obstacle_list.append(obstacle)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.obstacle_list.draw()

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
        self.obstacle_list.update()
        
        for obstacle in self.obstacle_list:
            if obstacle.top < 0:
                obstacle.center_y = random.randint(400, 500)
                obstacle.center_x = random.randint(20, 580)
        
        if arcade.check_for_collision_with_list(self.player, self.obstacle_list):
            self.lives -= 1
            print(f"Restliche Leben: {self.lives}")
            self.update_title()
            if self.lives <= 0:
                arcade.close_window()

    def update_title(self):
        self.set_caption(f"Ausweichen - Leben: {self.lives}")


# Anwendung starten
window = DodgeGame()
arcade.run()
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


