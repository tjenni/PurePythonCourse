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




class InfoView(arcade.View):
    
    def __init__(self, text="", color=arcade.color.BLACK):
        super().__init__()
        
        arcade.set_background_color(arcade.color.SKY_BLUE)
        
        self.text = text
        self.color = color

    def on_draw(self):
        self.clear()
        arcade.draw_text(self.text, self.window.width//2, self.window.height//2, self.color, 48, anchor_x="center")
        arcade.draw_text("weiter mit der Leertaste", self.window.width//2, self.window.height//2-50, arcade.color.BLACK, 24, anchor_x="center")
        

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
        

class GameView(arcade.View):
    
    def __init__(self):
        super().__init__()
        
        arcade.set_background_color(arcade.color.SKY_BLUE)
          
        self.player = None
        self.coin_list = None
        self.physics_engine = None
        self.score = 0

    def setup(self, level=1):
        
        self.level = level
        
        self.player = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", scale=0.5)
        self.player.center_x = 50
        self.player.center_y = 100
        self.player.change_x = 0
        self.player.change_y = 0

        
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.object_list = arcade.SpriteList()
        self.trap_list = arcade.SpriteList()
        
        path = ":resources:images/"
        
        self.tiles = {
            1 : [path + "tiles/grassLeft.png", self.wall_list],
            2 : [path + "tiles/grassMid.png", self.wall_list],
            3 : [path + "tiles/grassRight.png", self.wall_list],
            4 : [path + "tiles/grassHalf_left.png", self.wall_list],
            5 : [path + "tiles/grassHalf_mid.png", self.wall_list],
            6 : [path + "tiles/grassHalf_right.png", self.wall_list],
            7 : [path + "tiles/cactus.png", self.object_list],
            8 : [path + "tiles/spikes.png",self.trap_list],
            9 : [path + "items/coinGold.png", self.coin_list],
            10 : [path + "tiles/signExit.png", self.object_list]
            
        }
        
        if level == 1:
            self.tilemap = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 4, 6, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 4, 6, 0, 0, 0, 0],
                [0, 0, 0, 0, 9, 0, 8, 8, 9, 0, 7, 0, 10],
                [2, 3, 0, 1, 2, 2, 2, 2, 2, 2, 3, 0, 1]
            ]
        elif level == 2:
            self.tilemap = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0],
                [0, 9, 0, 0, 0, 4, 4, 6, 0, 0, 0, 0, 0],
                [0, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 4, 5, 6, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 7, 0, 0, 0, 0, 0, 8, 0, 0, 10],
                [2, 2, 2, 3, 0, 0, 0, 0, 0, 2, 3, 0, 1]
            ]
            
            
        
        for i in range(len(self.tilemap)):
            row = self.tilemap[i]
            for j in range(len(row)):
                tile_id = self.tilemap[i][j]
                
                x = j*64
                y = self.window.height - i*64
                
                if tile_id != 0:
                    tile_path = self.tiles[tile_id][0]
                    tile_list = self.tiles[tile_id][1]
                    
                    tile = arcade.Sprite(tile_path, 0.5)
                    tile.center_x = x
                    tile.center_y = y
                    
                    tile_list.append(tile)
                
        
        self.coin_sound = arcade.load_sound(":resources:sounds/coin2.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump3.wav")
        self.gameover_sound = arcade.load_sound(":resources:sounds/gameover2.wav")
        self.succes_sound = arcade.load_sound(":resources:sounds/upgrade2.wav")
        
        self.scene = arcade.Scene()
        
        self.scene.add_sprite_list("Background", sprite_list=self.object_list)
        self.scene.add_sprite_list("Coins", sprite_list=self.coin_list)
        self.scene.add_sprite_list("Walls", sprite_list=self.wall_list)
        self.scene.add_sprite_list("Traps", sprite_list=self.trap_list)
        self.scene.add_sprite("Player", self.player)
        
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, gravity_constant=0.5, walls=self.wall_list)
        

    def on_draw(self):
        arcade.start_render()
        self.scene.draw()
        arcade.draw_text(f"Score: {self.score}", 10, 570, arcade.color.WHITE, 16)
        

    def on_update(self, delta_time):
        self.physics_engine.update()
        
        coin_hit_list = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for coin in coin_hit_list:
            arcade.play_sound(self.coin_sound)
            coin.remove_from_sprite_lists()
            self.score += 1
            
        trap_hit_list = arcade.check_for_collision_with_list(self.player, self.trap_list)
        if len(trap_hit_list) > 0:
            arcade.play_sound(self.gameover_sound)
            view = InfoView("GAME OVER")
            self.window.show_view(view)
        
        if self.player.center_y < 0:
            arcade.play_sound(self.gameover_sound)
            view = InfoView("GAME OVER")
            self.window.show_view(view)
            
        if self.player.center_x > self.window.width:
            arcade.play_sound(self.succes_sound)
            
            if self.level == 1:
                self.setup(level=2)
                
            elif self.level == 2:
                view = InfoView("ENDE", color=arcade.color.AMBER)
                self.window.show_view(view)
            
            
        elif self.player.center_x < 0:
            self.player.center_x = 0
            
            
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP and self.physics_engine.can_jump():
            self.player.change_y = 12
            arcade.play_sound(self.jump_sound)
            
        elif key == arcade.key.LEFT:
            self.player.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0






def main():
    
    window = arcade.Window(800, 600, "Einfaches Plattformspiel")
    view = InfoView(text="Jumpmania", color=arcade.color_from_hex_string("#665d4a"))
    window.show_view(view)
    arcade.run()


if __name__ == "__main__":
    main()
    
    
    





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


