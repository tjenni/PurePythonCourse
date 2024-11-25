#              ______________________________________
#       ______|                                      |_____
#       \     |     13.5 TOP-DOWN ABENTEUERSPIEL     |    /
#        )    |______________________________________|   (
#       /________)                               (________\     17.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# In einem Top-Down-Abenteuerspiel erkundet der Spieler eine Welt von oben, 
# interagiert mit Objekten und löst Aufgaben. In diesem Kapitel lernst du, wie du 
# mithilfe von Arcade ein solches Spiel erstellst, indem du Tilemaps, Kollisionserkennung 
# und Bewegung implementierst.


# _________________________________
#                                 /
# Dungeon-Abenteuer-Spiel        (
# ________________________________\

# Dieses Beispiel zeigt, wie du eine Tilemap lädst, ein Spielfeld erstellst und 
# einen Spieler steuerst, der sich durch ein Dungeon bewegt.

# Das Tileset stammt von Robert (https://0x72.itch.io/dungeontileset-ii)

import arcade
import re
import math

# Diese Klasse repräsentiert eine animierte Spielfigur. 
# Sie verwaltet die Animationen für Laufen, Springen, Stehen und Klettern.
class Character(arcade.Sprite):
    
    IDLE = 0
    WALK = 1
    
    RIGHT = 0
    LEFT = 1
    
    def __init__(self, textures_path, x, y, width=16, height=16, scale=1.5):
        super().__init__()

        self.face_direction = Character.RIGHT  # Richtung der Spielfigur (0: rechts, 1: links)
        
        self.scale = scale  # Skalierung der Spielfigur
        
        self.frame = 0  # Animationsrahmenzähler
        self.animation_speed = 3  # Geschwindigkeit der Animation
        
        self.current_texture = 0  # Aktuelle Textur der Animation
        
        self.state = Character.IDLE
        
        # Lade alle Texturen für die Animationen
        self.all_textures = {}

        # Lade die Texturen für Stehen und Springen
        self.all_textures[Character.IDLE] = self._load_textures(textures_path, x, y, width, height, 2)
        
        # Lade die Texturen für die Laufanimation
        self.all_textures[Character.WALK] = self._load_textures(textures_path, x, y, width, height, 4)
        
        # Setze die Anfangstextur
        self.texture = self.all_textures[self.state][0][0]
        
        # Setze die Kollisionsbox basierend auf der Anfangstextur
        self.hit_box = self.texture.hit_box_points
 
    
    def _load_textures(self, textures_path, x, y, width, height, n):
        return [
            self._load_texture_pair(textures_path, x+i*width, y, width, height) for i in range(n)
        ]
        
        
    
    # Lädt ein Texturpaar: eine normale und eine horizontal gespiegelt.
    def _load_texture_pair(self, path, x, y, width, height):
        return [
            arcade.load_texture(path, x, y, width, height),
            arcade.load_texture(path, x, y, width, height, flipped_horizontally=True)
        ]


    # Aktualisiert die Animation der Spielfigur basierend auf ihrem Zustand (Laufen, 
    # Springen, Klettern, Stehen).
    def update_animation(self, delta_time):

        self.frame = (self.frame + 1) % self.animation_speed
        
        # Animation für Laufen
        if self.frame == 0:  # Aktualisiere die Textur nur bei bestimmten Frames
            self.current_texture += 1
            
        # Bestimme die Blickrichtung der Spielfigur
        if self.change_x < 0:
            self.face_direction = 1  # Blick nach links
        elif self.change_x > 0:
            self.face_direction = 0  # Blick nach rechts
        
        
        self.current_texture = self.current_texture % len(self.all_textures[self.state])
        self.texture = self.all_textures[Character.IDLE][self.current_texture][self.face_direction]
        
        
    
    def search_player(self, player):
        dx = player.center_x - self.center_x
        dy = player.center_y - self.center_y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        
        # Bewege den Roboter in Richtung des Spielers
        if distance > 0 and distance < self.max_distance:  # Vermeide Division durch Null
            
            dx = self.speed * (dx / distance)
            dy = self.speed * (dy / distance)
            
            self.center_x += dx
            walls_hit_list = arcade.check_for_collision_with_list(self, self.walls)
            if len(walls_hit_list) > 0:
                self.center_x -= dx
                
            self.center_y += dy
            walls_hit_list = arcade.check_for_collision_with_list(self, self.walls)
            if len(walls_hit_list) > 0:
                self.center_y -= dy
            
        



class Skeleton(Character):
    
    def __init__(self, textures_path, x, y, width=16, height=16, scale=1.5):
        super().__init__(textures_path, x, y, width, height, scale)
        
        self.speed = 3
        self.max_distance = 300
        
        

class OgreMage(Character):
    
    def __init__(self, textures_path, x, y, width=16, height=16, scale=1.5):
        super().__init__(textures_path, x, y, width, height, scale)
        
        self.speed = 1
        self.max_distance = 400
        
        
class RedOgre(Character):
    
    def __init__(self, textures_path, x, y, width=16, height=16, scale=1.5):
        super().__init__(textures_path, x, y, width, height, scale)
        
        self.speed = 2
        self.max_distance = 200
        
        
        
       
    
    




class TopDownGame(arcade.Window):

    # Initialisiert das Fenster, die Tilemap-Parameter und die Szene.
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        # Tilemap-Konfiguration
        self.tile_map = None            # Die geladene Tilemap
        self.tile_scale = 2.0           # Skalierung der Tiles
        self.tile_offset = (0, 0)     # Offset für die Tilemap
        self.tile_size = 16 * self.tile_scale  # Grösse eines Tiles
        
        # Spieler-Konfiguration
        self.player_scale = 1.5         # Skalierung des Spielers
        self.player_offset = (16, -10)   # Offset zur Positionierung des Spielers
        
        # Szene und Spieler
        self.scene = None               # Die Szene, die alle Objekte enthält
        self.player = None       # Das Spieler-Sprite
        self.enemies = None 
        
        # Physik-Engine
        self.physics_engine = None      # Physik-Engine für Bewegungen und Kollisionen

        # Spielkamera: Verfolgt die Spiellandschaft
        self.camera = arcade.Camera(self.width, self.height)

        # GUI-Kamera: Statische Ansicht für Benutzeroberfläche
        self.gui_camera = arcade.Camera(self.width, self.height)
        
        self.score = 0

    # Aktualisiert die Spielkamera, sodass sie der Spielfigur folgt.
    def update_camera(self):
        
        # Kamera zentrieren auf den Spieler, dabei X und Y Achse berücksichtigen
        screen_center_x = max(0, self.player.center_x - self.camera.viewport_width // 2)
        screen_center_y = max(0, self.player.center_y - self.camera.viewport_height // 2)

        # Kamera zur berechneten Position verschieben
        self.camera.move_to((screen_center_x, screen_center_y), speed=0.2)


        
    # Lädt die Tilemap, erstellt die Szene und initialisiert den Spieler.
    def setup(self):
    

        # Lade die Tilemap aus einer .tmx-Datei
        map_name = "_assets/12.15/level_1.tmx"  # Pfad zur .tmx-Datei
        
        # Optionen für die Tilemap-Ebenen
        layer_options = {
            "Walls": {
                "use_spatial_hash": True,
                "offset": self.tile_offset
            },
            "Floor": {
                "offset": self.tile_offset
            },
            "Doors": {
                "offset": self.tile_offset
            }
        }
        
        # Lade die Tilemap mit den angegebenen Optionen
        self.tile_map = arcade.load_tilemap(map_name, self.tile_scale, layer_options=layer_options)
        
        
        # Erstelle die Szene basierend auf der geladenen Tilemap
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        
        
        # Spieler-Sprite hinzufügen
        self.player = Character("_assets/12.15/dungeon_tiles.png", 512, 16)
        self.set_position(self.player, 6,95)
        self.scene.add_sprite("Player", self.player)
        
        # Enemies
        
        enemies = arcade.SpriteList()
        
        for tile in self.scene["Enemies"]:
            
            pattern = r'dungeon_tiles\.png-(\d+)-(\d+)'
            match = re.search(pattern, tile.texture.name)
            
            if match:
                # Extrahiere die Gruppen, die Zahlen enthalten
                tile_position = list(map(int, match.groups()))
                
                if tile_position == [368, 176]:
                    enemy = Skeleton("_assets/12.15/dungeon_tiles.png", tile_position[0], tile_position[1])
                elif tile_position == [368, 80]:
                    enemy = OgreMage("_assets/12.15/dungeon_tiles.png", tile_position[0], tile_position[1])
                elif tile_position == [368, 304]:
                    enemy = RedOgre("_assets/12.15/dungeon_tiles.png", tile_position[0], tile_position[1])
                
                
                enemy.walls = self.scene["Walls"]
                
                enemy.center_x = tile.center_x
                enemy.center_y = tile.center_y
                
                enemies.append(enemy)
            
            
        self.scene["Enemies"].clear()
        self.scene["Enemies"].extend(enemies)
        
        
        # Initialisiere die Physik-Engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player,
            gravity_constant=0.0,  # Keine Schwerkraft, da es ein Top-Down-Spiel ist
            walls=self.scene["Walls"]
        )

    
    def set_position(self, character, x, y):
        x , y = self.tilemap_to_screen(x, y)
        character.center_x = x
        character.center_y = y
        
        
    def tilemap_to_screen(self, x, y):
        return (
            self.tile_size * x + self.tile_offset[0] + self.player_offset[0],
            self.tile_size * (self.tile_map.height - y) + self.tile_offset[1] + self.player_offset[1]
        )
    
    def screen_to_tilemap(self, x, y):
        return (
            round((x - self.player_offset[0] - self.tile_offset[0]) / self.tile_size),
            round(self.tile_map.height - (y - self.player_offset[1] - self.tile_offset[1]) / self.tile_size)
        )
    
        
        
    
    

            
        
            
            
    # Aktualisiert die Physik und prüft Kollisionen.
    def on_update(self, delta_time):

        # Aktualisiere die Position des Spielers mithilfe der Physik-Engine
        self.physics_engine.update()
        
        
        self.player.update_animation(delta_time)
        
        for enemy in self.scene["Enemies"]:
            enemy.update_animation(delta_time)
            enemy.search_player(self.player)
        
        
        self.update_camera()
        
        # Prüfe, ob der Spieler mit Türen kollidiert
        door_hit_list = arcade.check_for_collision_with_list(
            self.player, self.scene["Doors"]
        )
        
        # Aktionen bei Kollision mit Türen
        for door in door_hit_list:
            
            position = self.screen_to_tilemap(door.center_x, door.center_y)
            
            if position == (14,77):
                self.set_position(self.player, 32, 89)
                
            elif position == (32,91):
                self.set_position(self.player,14, 79)
    
            elif position in [(46,74), (46,73)] :
                self.set_position(self.player,26, 66)
                
            elif position == (26,64):
                self.set_position(self.player,45, 74)

                



    # Zeichnet die Szene und den Spieler.
    def on_draw(self):
        arcade.start_render()  # Starte den Renderprozess
        
        # Spielkamera aktivieren
        self.camera.use() 
        self.scene.draw() 

        # GUI-Kamera aktivieren
        self.gui_camera.use()
        arcade.draw_text(f"Punkte: {self.score}", 15, self.height - 30, arcade.color.WHITE, 16)



    # Reagiert auf Tastendrücke und bewegt den Spieler.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.change_y = 5  # Bewege nach oben
        elif key == arcade.key.DOWN:
            self.player.change_y = -5  # Bewege nach unten
        elif key == arcade.key.LEFT:
            self.player.change_x = -5  # Bewege nach links
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5  # Bewege nach rechts


    # Stoppt die Bewegung des Spielers, wenn die Taste losgelassen wird.
    def on_key_release(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.player.change_y = 0  # Stoppe vertikale Bewegung
        if key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player.change_x = 0  # Stoppe horizontale Bewegung


# Anwendung starten
window = TopDownGame(title="Dungeon Spiel")
window.setup()  # Initialisiere das Spiel
arcade.run()  # Starte das Spiel











# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Kopiere die Datei `level_1.tmx`-Datei im Ordner `_assets/topdown` und bennene
# sie in `level_2.tmx` um. Öffne dann die Daei und zeichne das Level 2 des 
# Top-Down Abenteuerspiels.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erweitere das Dungeon-Abenteuerspiel so, dass der Spieler Schlüssel sammeln muss, 
# um Türen zu öffnen. Füge eine neue Tilemap-Ebene namens "Keys" hinzu, auf der die 
# Schlüssel positioniert sind. Wenn der Spieler einen Schlüssel berührt, soll er 
# eingesammelt werden, und die Anzahl der gesammelten Schlüssel in der Konsole 
# angezeigt werden.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Füge dem Dungeon-Spiel eine Gesundheitsanzeige für den Spieler hinzu. Wenn der Spieler 
# mit einem Hindernis (z. B. einer "Trap"-Ebene in der Tilemap) kollidiert, soll seine 
# Gesundheit sinken. Wenn die Gesundheit null erreicht, wird das Spiel beendet.

# Hinweise:
# - Füge eine Variable `self.health` hinzu, um die Gesundheit des Spielers zu speichern.
#
# - Verwende `arcade.Text()` oder `arcade.draw_text()`, um die aktuelle Gesundheit in der 
#   oberen linken Ecke des Fensters anzuzeigen.
#
# - Beende das Spiel mit `arcade.close_window()`, wenn die Gesundheit des Spielers null erreicht.


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
#                             |___/            


# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erweitere das Dungeon-Abenteuerspiel so, dass der Spieler Schlüssel sammeln muss, 
# um Türen zu öffnen. Füge eine neue Tilemap-Ebene namens "Keys" hinzu, auf der die 
# Schlüssel positioniert sind. Wenn der Spieler einen Schlüssel berührt, soll er 
# eingesammelt werden, und die Anzahl der gesammelten Schlüssel in der Konsole 
# angezeigt werden.

# Hinweis:
# - Verwende `arcade.check_for_collision_with_list()` für die Kollisionserkennung.
#
# - Erstelle eine Variable `self.keys_collected`, um die Anzahl der gesammelten Schlüssel 
#   zu speichern.

'''
import arcade

class DungeonGameWithKeys(arcade.Window):
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        # Tilemap-Parameter
        self.tile_map = None
        self.tile_scale = 2.0
        self.tile_offset = (-80, 0)
        self.tile_size = 16 * self.tile_scale
        
        # Spieler-Parameter
        self.player_scale = 0.3
        self.player_offset = (16, 22)
        self.scene = None
        self.player = None
        
        # Physik-Engine
        self.physics_engine = None
        
        # Schlüssel
        self.keys_collected = 0  # Anzahl gesammelter Schlüssel

    def setup(self):
        # Lade die Tilemap
        map_name = "_assets/topdown/level_1_with_keys.tmx"  # Tilemap mit Keys-Ebene
        layer_options = {
            "Walls": {
                "use_spatial_hash": True,
                "offset": self.tile_offset
            },
            "Floor": {
                "offset": self.tile_offset
            },
            "Door": {
                "offset": self.tile_offset
            },
            "Keys": {
                "offset": self.tile_offset
            }
        }
        
        # Erstelle Tilemap und Szene
        self.tile_map = arcade.load_tilemap(map_name, self.tile_scale, layer_options=layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        
        # Spieler-Sprite erstellen
        self.player = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
            scale=self.player_scale
        )
        self.player.center_x = self.tile_size * 23 + self.tile_offset[0] + self.player_offset[0]
        self.player.center_y = self.tile_size * 4 + self.tile_offset[1] + self.player_offset[1]
        self.scene.add_sprite("Player", self.player)
        
        # Physik-Engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player,
            gravity_constant=0.0,
            walls=self.scene["Walls"]
        )

    def on_update(self, delta_time):
        # Bewegung des Spielers aktualisieren
        self.physics_engine.update()
        
        # Kollision mit Türen prüfen
        door_hit_list = arcade.check_for_collision_with_list(self.player, self.scene["Door"])
        for door in door_hit_list:
            print("Tür erreicht!")
        
        # Kollision mit Schlüsseln prüfen
        keys_hit_list = arcade.check_for_collision_with_list(self.player, self.scene["Keys"])
        for key in keys_hit_list:
            # Schlüssel entfernen
            key.remove_from_sprite_lists()
            # Anzahl der gesammelten Schlüssel erhöhen
            self.keys_collected += 1
            print(f"Schlüssel gesammelt: {self.keys_collected}")

    def on_draw(self):
        arcade.start_render()
        self.scene.draw()

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
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.player.change_y = 0
        if key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player.change_x = 0


# Anwendung starten
window = DungeonGameWithKeys(title="Dungeon-Spiel mit Schlüsseln")
window.setup()
arcade.run()

'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Füge dem Dungeon-Spiel eine Gesundheitsanzeige für den Spieler hinzu. Wenn der Spieler 
# mit einem Hindernis (z. B. einer "Trap"-Ebene in der Tilemap) kollidiert, soll seine 
# Gesundheit sinken. Wenn die Gesundheit null erreicht, wird das Spiel beendet.

# Hinweise:
# - Füge eine Variable `self.health` hinzu, um die Gesundheit des Spielers zu speichern.
#
# - Verwende `arcade.Text()` oder `arcade.draw_text()`, um die aktuelle Gesundheit in der 
#   oberen linken Ecke des Fensters anzuzeigen.
#
# - Beende das Spiel mit `arcade.close_window()`, wenn die Gesundheit des Spielers null erreicht.

'''
import arcade


class DungeonGameWithHealth(arcade.Window):
    
    # Initialisiere das Fenster, die Tilemap und alle Spielparameter.
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        # Tilemap-Parameter
        self.tile_map = None  # Tilemap wird später geladen
        self.tile_scale = 2.0  # Skalierung der Tiles
        self.tile_offset = (-80, 0)  # Offset der Tilemap
        self.tile_size = 16 * self.tile_scale  # Größe eines Tiles
        
        # Spieler-Parameter
        self.player_scale = 0.3  # Skalierung des Spieler-Sprites
        self.player_offset = (16, 22)  # Offset für die Positionierung des Spielers
        self.scene = None  # Szene, die alle Ebenen und Objekte enthält
        self.player = None  # Spieler-Sprite
        self.damage_cooldown = 0  # Unverwundbarkeitsdauer (Frames)
        
        # Physik-Engine
        self.physics_engine = None  # Physik-Engine zur Bewegung und Kollisionsprüfung
        
        # Spieler-Gesundheit
        self.health = 100  # Anfangsgesundheit des Spielers


    # Setup-Methode, um die Tilemap zu laden, die Szene zu erstellen und den Spieler zu initialisieren.
    def setup(self):
        # Lade die Tilemap
        map_name = "_assets/topdown/level_1_with_traps.tmx"  # Tilemap-Datei
        layer_options = {
            "Walls": {"use_spatial_hash": True, "offset": self.tile_offset},
            "Floor": {"offset": self.tile_offset},
            "Door": {"offset": self.tile_offset},
            "Trap": {"offset": self.tile_offset},
        }
        
        # Lade die Tilemap mit den angegebenen Ebenen
        self.tile_map = arcade.load_tilemap(map_name, self.tile_scale, layer_options=layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)  # Erstelle die Szene
        
        # Spieler-Sprite initialisieren
        self.player = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
            scale=self.player_scale
        )
        
        # Position des Spielers setzen
        self.player.center_x = self.tile_size * 23 + self.tile_offset[0] + self.player_offset[0]
        self.player.center_y = self.tile_size * 4 + self.tile_offset[1] + self.player_offset[1]
        self.scene.add_sprite("Player", self.player)  # Spieler zur Szene hinzufügen
        
        # Physik-Engine für den Spieler
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player,
            gravity_constant=0.0,  # Keine Schwerkraft in einem Top-Down-Spiel
            walls=self.scene["Walls"]
        )


    # Aktualisiere die Spielmechanik: Bewegung, Kollisionen und Gesundheitslogik.
    def on_update(self, delta_time):
        # Aktualisiere die Bewegung des Spielers mit der Physik-Engine
        self.physics_engine.update()
        
        # Reduziere die Unverwundbarkeitszeit
        if self.damage_cooldown > 0:
            self.damage_cooldown -= 1
        
        # Kollision mit Fallen prüfen
        traps_hit_list = arcade.check_for_collision_with_list(self.player, self.scene["Trap"])
        for trap in traps_hit_list:
            if self.damage_cooldown == 0:  # Wenn der Spieler nicht unverwundbar ist
                self.health -= 10  # Gesundheit reduzieren
                print(f"Gesundheit: {self.health}")
                self.damage_cooldown = 50  # Setze Unverwundbarkeit (ca. 1 Sekunde bei 60 FPS)
            
            if self.health <= 0:  # Wenn die Gesundheit 0 erreicht
                print("Spieler gestorben. Spiel beendet!")
                arcade.close_window()  # Beende das Spiel
        
        # Kollision mit Türen prüfen
        door_hit_list = arcade.check_for_collision_with_list(self.player, self.scene["Door"])
        for door in door_hit_list:
            print("Tür erreicht!")


    # Zeichne die Szene und die Gesundheitsanzeige.
    def on_draw(self):
        arcade.start_render()  # Starte den Renderprozess
        self.scene.draw()  # Zeichne die Szene
        
        # Gesundheitsanzeige in der oberen linken Ecke
        arcade.draw_text(
            f"Gesundheit: {self.health}",
            10, 570,  # Position in Pixeln
            arcade.color.WHITE,  # Farbe des Textes
            20  # Schriftgröße
        )

    # Bewegung des Spielers bei Tastendruck steuern.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.change_y = 5  # Nach oben bewegen
        elif key == arcade.key.DOWN:
            self.player.change_y = -5  # Nach unten bewegen
        elif key == arcade.key.LEFT:
            self.player.change_x = -5  # Nach links bewegen
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5  # Nach rechts bewegen

    # Spielerbewegung stoppen, wenn die Taste losgelassen wird.
    def on_key_release(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.player.change_y = 0  # Vertikale Bewegung stoppen
        if key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player.change_x = 0  # Horizontale Bewegung stoppen


# Spiel starten
window = DungeonGameWithHealth(title="Dungeon-Spiel mit Gesundheit")
window.setup()  # Setup des Spiels
arcade.run()  # Starte das Spiel

'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><



