#              ______________________________________
#       ______|                                      |_____
#       \     |     13.5 TOP-DOWN ABENTEUERSPIEL     |    /
#        )    |______________________________________|   (
#       /________)                               (________\     26.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# In einem Top-Down-Abenteuerspiel erkundet der Spieler eine Welt von oben, 
# interagiert mit Objekten und löst Aufgaben. In diesem Kapitel lernst du, wie du 
# mithilfe von Arcade ein solches Spiel erstellst, indem du Tilemaps, Kollisionserkennung 
# und Bewegung implementierst.


# _________________________________
#                                 /
# Einführung                    (
# ________________________________\

# Top-Down-Abenteuerspiele gehören zu den Klassikern der Spielewelt. Sie ermöglichen
# den Spielern, in eine Welt einzutauchen, die aus der Vogelperspektive dargestellt wird.
# Spiele wie *The Legend of Zelda* oder *Stardew Valley* haben dieses Genre berühmt gemacht.

# In einem Top-Down-Spiel bewegt sich der Spieler durch eine Welt, die in Form einer
# Tilemap organisiert ist. Dabei interagiert er mit verschiedenen Objekten, bekämpft
# Gegner und löst Rätsel. In diesem Kapitel lernst du die grundlegenden Techniken, um
# ein solches Spiel mit Arcade zu entwickeln.

# Die wichtigsten Themen dieses Kapitels sind:
# - Tilemaps verwenden: Erstelle eine Welt aus vorgefertigten Kacheln und organisiere
#   sie in einer Szene.
#
# - Spielerbewegung: Implementiere Bewegungen für den Spieler und passe diese an
#   die Kollisionen in der Welt an.
#
# - Gegner-KI: Erstelle einfache Gegner, die den Spieler verfolgen oder angreifen.
#
# - Animationen und Waffen: Füge Animationen für den Spieler und Gegner hinzu und
#   rüste Charaktere mit Waffen aus.
#
# - Kamera und GUI: Halte den Spieler mit der Kamera im Fokus und zeige nützliche
#   Informationen wie Gesundheit oder Punktestand an.

# Dieses Kapitel bildet die Grundlage für komplexere Abenteuerspiele. Du wirst lernen,
# wie du eine modulare Spielstruktur erstellst, die durch weitere Mechaniken und
# Level erweitert werden kann.



import arcade
import math
import random


# Diese Klasse repräsentiert ein Sprite aus einem Tileset, mit der Möglichkeit, 
# Animationen zu laden.
class TilesetSprite(arcade.Sprite):
    
    def __init__(self, width=16, height=16, scale=1.5):
        super().__init__()
        
        self.width = width # Breite des Tiles
        self.height = height # Höhe des Tiles
        self.scale = scale # Skalierungsfaktor für das Sprite
        
        
    # Lädt Texturen aus einem Tileset basierend auf definierten Sprite-Positionen.
    def load_textures(self, tileset, sprite_list):
        textures = {}
        for name, positions in sprite_list.items():
            textures[name] = []
            print(positions)
            
            for position in positions:
                texture = self._load_texture_pair(tileset, position[0], position[1], self.width, self.height)
                textures[name].append(texture)
        
        self.all_textures = textures


    # Lädt ein Texturpaar: normal und horizontal gespiegelt.
    def _load_texture_pair(self, path, x, y, width, height):
        return [
            arcade.load_texture(path, x, y, width, height),
            arcade.load_texture(path, x, y, width, height, flipped_horizontally=True)
        ]
    

# Diese Klasse repräsentiert eine animierte Spielfigur und bietet Funktionen wie 
# Animationen und Angriffe.
class Weapon(TilesetSprite):

    # Definition der Zustände der Spielfigur
    IDLE = 0
    ATTACK = 1
    
    def __init__(self):
        super().__init__()
        
        self.state = Weapon.IDLE
        self.cool_down = 10
        self.frame = 0


    # Aktualisiert die Animation der Spielfigur basierend auf ihrem Zustand und ihrer Bewegung.
    def update_animation(self, delta_time):

        if self.state == Weapon.ATTACK:

            # Cooldown berechnen
            self.frame += 1
            if self.frame > self.cool_down:
                self.frame = 0
                self.state = Weapon.IDLE

            # Waffe drehen
            if self.character.face_direction == Character.LEFT:
                self.angle = 90
            else:
                self.angle = -90

        else:
            self.angle = 0
        
        # Aktualisiere Animation basierend auf dem Zustand
        self.texture = self.all_textures[Weapon.IDLE][0][self.character.face_direction]


    def attack(self):
        self.state = Weapon.ATTACK




# Diese Klasse repräsentiert eine animierte Spielfigur und bietet Funktionen wie 
# Animationen und Angriffe.
class Character(TilesetSprite):
    
    # Definition der Zustände der Spielfigur
    IDLE = 0
    WALK = 1
    
    # Definition der Blickrichtungen
    RIGHT = 0
    LEFT = 1
    
    def __init__(self):
        super().__init__()
        
        
        self.health = 100 # Lebenspunkte der Figur
        self.luck = 30 # Glücksfaktor für Angriffe
        self.strength = 5 # Stärke des Angriffs
        
        self.state = Character.IDLE # Aktueller Zustand der Spielfigur
        self.is_attacking = False # Gibt an, ob die Figur angreift

        self.face_direction = Character.RIGHT  # Blickrichtung der Spielfigur
        
        self.frame = 0  # Aktueller Animationsrahmen
        self.animation_speed = 4  # Geschwindigkeit der Animation
        self.current_texture = 0  # Aktuelle Textur der Animation

        self.weapon = None # Waffe
        
        
    # Aktualisiert die Animation der Spielfigur basierend auf ihrem Zustand und ihrer Bewegung.
    def update_animation(self, delta_time):

        self.frame = (self.frame + 1) % self.animation_speed
        
        # Animation für Laufen
        if self.frame == 0:  # Aktualisiere die Textur nur bei bestimmten Frames
            self.current_texture += 1
            
        # Aktualisiere Blickrichtung
        if self.change_x < 0:
            self.face_direction = Character.LEFT  # Blick nach links
        elif self.change_x > 0:
            self.face_direction = Character.RIGHT   # Blick nach rechts

        # Aktualisiere Waffe
        if self.weapon is not None:
            self.weapon.update_animation(delta_time)

            if self.face_direction == Character.LEFT:
                self.weapon.center_x = self.center_x - 10
            else:
                self.weapon.center_x = self.center_x + 10

            self.weapon.center_y = self.center_y
        
        # Aktualisiere Animation basierend auf dem Zustand
        self.current_texture = self.current_texture % len(self.all_textures[self.state])
        self.texture = self.all_textures[Character.IDLE][self.current_texture][self.face_direction]
        
        
    # Bewegt die Spielfigur in Richtung eines anderen Charakters und prüft 
    # auf Hindernisse.
    def search_player(self, character):
        dx = character.center_x - self.center_x
        dy = character.center_y - self.center_y
        distance = math.sqrt(dx ** 2 + dy ** 2) # Abstand zwischen den Figuren
        
        # Bewegung in Richtung des Spielers, falls innerhalb der Suchdistanz
        if distance > 20 and distance < self.search_distance:  # Vermeide Division durch Null
            
            dx = self.speed * (dx / distance)
            dy = self.speed * (dy / distance)

            self.change_x = dx
            self.change_y = dy
            
            # Bewegung in x-Richtung prüfen
            self.center_x += dx
            walls_hit_list = arcade.check_for_collision_with_list(self, self.walls)
            if len(walls_hit_list) > 0:
                self.center_x -= dx

            # Bewegung in y-Richtung prüfen
            self.center_y += dy
            walls_hit_list = arcade.check_for_collision_with_list(self, self.walls)
            if len(walls_hit_list) > 0:
                self.center_y -= dy
                
        return distance


    # Rüstet den Charachter mit einer Waffe aus
    def set_weapon(self, weapon):
        self.weapon = weapon
        weapon.character = self


    # Führt einen Angriff auf einen anderen Charakter aus, basierend auf 
    # Glücksfaktor und Stärke.
    def attack(self, character):
        if self.weapon is not None:
            self.weapon.attack()

        if random.randint(0,100) < self.luck:
            character.health -= self.strength
            

# Unterklasse für ein Mädchen-Charakter mit spezifischen Animationen
class Dagger(Weapon):
    def __init__(self):
        super().__init__()
        
        self.load_textures("_assets/12.15/dungeon_tiles.png", {
            Weapon.IDLE : [[18*16, 1*16]],
        })


# Unterklasse für ein Mädchen-Charakter mit spezifischen Animationen
class Girl(Character):
    def __init__(self):
        super().__init__()
        
        self.load_textures("_assets/12.15/dungeon_tiles.png", {
            Character.IDLE : [[32*16, 1*16], [33*16, 1*16]],
            Character.WALK : [[32*16, 1*16], [33*16, 1*16], [34*16, 1*16], [35*16, 1*16]]
        })

        self.set_weapon(Dagger())
        
        
        
# Unterklasse für ein Skelett-Charakter mit spezifischen Attributen und Animationen
class Skeleton(Character):
    
    def __init__(self):
        super().__init__()
        
        self.load_textures("_assets/12.15/dungeon_tiles.png", {
            Character.IDLE : [[23*16, 5*16],[24*16, 5*16]],
            Character.WALK : [[23*16, 5*16],[24*16, 5*16],[25*16, 5*16],[26*16, 5*16]]
        })

        self.set_weapon(Dagger())
        
        self.health = 20
        self.luck = 2
        self.strength = 1
        self.speed = 3
        
        self.search_distance = 70
        
        
# Weitere Unterklassen (z. B. OgreMage, RedOgre) folgen einem ähnlichen Muster.
class OgreMage(Character):
    
    def __init__(self):
        super().__init__()
        
        self.load_textures("_assets/12.15/dungeon_tiles.png", {
            Character.IDLE : [[23*16, 11*16],[24*16, 11*16]],
            Character.WALK : [[23*16, 11*16],[24*16, 11*16],[25*16, 11*16],[26*16, 11*16]]
        })
        
        self.health = 30
        self.luck = 5
        self.strength = 2
        self.speed = 1
        
        self.search_distance = 400
        
        
class RedOgre(Character):
    
    def __init__(self):
        super().__init__()
        
        self.load_textures("_assets/12.15/dungeon_tiles.png", {
            Character.IDLE : [[23*16, 19*16],[24*16, 19*16]],
            Character.WALK : [[23*16, 19*16],[24*16, 19*16],[25*16, 19*16],[26*16, 19*16]]
        })

        self.set_weapon(Dagger())
        
        self.health = 20
        self.luck = 3
        self.strength = 5
        self.speed = 2
        
        self.search_distance = 200
        
        

# Hauptklasse des Spiels
class TopDownGame(arcade.Window):

    # Initialisiert die Fensterparameter, Tilemap-Optionen und Kameras.
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
        self.scene = None        # Die Szene, die alle Objekte enthält
        self.player = None       # Das Spieler-Sprite
        
        # Physik-Engine
        self.physics_engine = None      # Physik-Engine für Bewegungen und Kollisionen

        # Spielkamera: Verfolgt den Spieler
        self.camera = arcade.Camera(self.width, self.height)

        # GUI-Kamera: Statische Ansicht für Benutzeroberfläche
        self.gui_camera = arcade.Camera(self.width, self.height)
        
        # Punktzahl
        self.score = 0

    # Aktualisiert die Kamera, um dem Spieler zu folgen.
    def update_camera(self):
        
        # Kamera zentrieren auf den Spieler, dabei X und Y Achse berücksichtigen
        screen_center_x = max(0, self.player.center_x - self.camera.viewport_width // 2)
        screen_center_y = max(0, self.player.center_y - self.camera.viewport_height // 2)

        # Kamera zur berechneten Position verschieben
        self.camera.move_to((screen_center_x, screen_center_y), speed=0.2)


        
    # Lädt die Tilemap und erstellt die Szene sowie den Spieler.
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

        # Erstelle eine Liste für die Waffen
        self.scene.add_sprite_list("Weapons", arcade.SpriteList())
        
        # Spieler initialisieren
        self.player = Girl()
        self.set_position(self.player, 6,95)
        
        self.scene.add_sprite("Player", self.player)
        self.scene["Weapons"].append(self.player.weapon)

        

        # Gegner initialisieren
        enemies = arcade.SpriteList()
        
        for tile in self.scene["Enemies"]:
            
            tile_id = tile.properties["tile_id"]
            
            if tile_id == 727:
                enemy = OgreMage()
            elif tile_id == 343:
                enemy = Skeleton()
            elif tile_id == 1239:
                enemy = RedOgre()
            
            enemy.walls = self.scene["Walls"]
            enemy.center_x = tile.center_x
            enemy.center_y = tile.center_y

            if enemy.weapon is not None:
                self.scene["Weapons"].append(enemy.weapon)

            enemies.append(enemy)
            
        self.scene["Enemies"].clear()
        self.scene["Enemies"].extend(enemies)
        
        
        # Initialisiere die Physik-Engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player,
            gravity_constant=0.0,  # Keine Schwerkraft, da es ein Top-Down-Spiel ist
            walls=self.scene["Walls"]
        )

    
    # Helferfunktion: Setzt die Position eines Charakters in der Tilemap.
    def set_position(self, character, x, y):
        x , y = self.tilemap_to_screen(x, y)
        character.center_x = x
        character.center_y = y


    # Wandelt Tilemap-Koordinaten in Bildschirmkoordinaten um.
    def tilemap_to_screen(self, x, y):
        return (
            self.tile_size * x + self.tile_offset[0] + self.player_offset[0],
            self.tile_size * (self.tile_map.height - y) + self.tile_offset[1] + self.player_offset[1]
        )


    # Hauptspiel: Aktualisiert Animationen, prüft Kollisionen und Kamerabewegungen.
    def screen_to_tilemap(self, x, y):
        return (
            round((x - self.player_offset[0] - self.tile_offset[0]) / self.tile_size),
            round(self.tile_map.height - (y - self.player_offset[1] - self.tile_offset[1]) / self.tile_size)
        )
    
              
    # Aktualisiert die Physik und prüft Kollisionen.
    def on_update(self, delta_time):

        # Aktualisiere die Position des Spielers mithilfe der Physik-Engine
        self.physics_engine.update()
        self.update_camera()
        
        self.player.update_animation(delta_time)
        
        if self.player.is_attacking:
            self.player.weapon.attack()

        for enemy in self.scene["Enemies"]:
            enemy.update_animation(delta_time)
            distance = enemy.search_player(self.player)
            
            if distance < 22:
                enemy.attack(self.player)
                
                if self.player.is_attacking:
                    self.player.attack(enemy)
                    self.player.is_attacking = False
                    
                    if enemy.health <= 0:
                        if enemy.weapon is not None:
                            enemy.weapon.remove_from_sprite_lists()

                        enemy.remove_from_sprite_lists()
                        break

        
        # Prüfe, ob der Spieler durch eine Tür geht
        door_hit_list = arcade.check_for_collision_with_list(self.player, self.scene["Doors"])
        
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
        arcade.draw_text(f"Leben: {self.player.health}", 15, self.height - 60, arcade.color.WHITE, 16)


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
        elif key == arcade.key.SPACE:
            self.player.is_attacking = True  # Führe eine Attacke aus


    # Stoppt die Bewegung des Spielers, wenn die Taste losgelassen wird.
    def on_key_release(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.player.change_y = 0  # Stoppe vertikale Bewegung
        if key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player.change_x = 0  # Stoppe horizontale Bewegung
        elif key == arcade.key.SPACE:
            self.player.is_attacking = False

# Anwendung starten
window = TopDownGame(title="Dungeon Spiel")
window.setup()  # Initialisiere das Spiel
arcade.run()  # Starte das Spiel



# ____________________________
#                            /
# Zusammenfassung           (
# ___________________________\

# In diesem Kapitel hast du gelernt, wie ein Top-Down-Abenteuerspiel mit Arcade erstellt wird.
# Dieses Spielkonzept bietet viele Möglichkeiten, Mechaniken wie Bewegung, Kollisionen,
# Animationen und Interaktionen zu implementieren. Hier sind die wichtigsten Punkte, die
# in diesem Kapitel behandelt wurden:

# 1. Tilemaps und Szenen:
#    - Du hast gelernt, wie Tilemaps geladen werden und wie man sie verwendet, um Levels
#      mit Wänden, Böden, Türen und interaktiven Objekten zu erstellen.
#    - Die Verwendung von `arcade.Scene` bietet eine saubere Möglichkeit, Objekte wie
#      Wände, Gegner und den Spieler zu organisieren.

# 2. Spieler und Gegner:
#    - Spielfiguren wie der Spieler und Gegner wurden durch animierte Sprites mit
#      spezifischen Eigenschaften und Animationen dargestellt.
#    - Gegner konnten Spieler erkennen und sich auf Basis von Suchradien bewegen,
#      was ihnen eine einfache KI verlieh.

# 3. Waffen und Angriffe:
#    - Waffen wurden den Charakteren zugeordnet und konnten durch Animationen und
#      Logik für Angriffe erweitert werden.
#    - Das Spiel berücksichtigt sowohl die Angriffe des Spielers als auch die der
#      Gegner, wodurch Interaktionen spannender wurden.

# 4. Kollisionserkennung:
#    - Kollisionen wurden genutzt, um Interaktionen wie das Einsammeln von Objekten
#      (z. B. Schlüssel) oder die Bewegung durch Türen zu ermöglichen.
#    - Arcade bietet effiziente Methoden wie `arcade.check_for_collision_with_list()`,
#      um solche Logiken umzusetzen.

# 5. Kamera und GUI:
#    - Mit der Kamera wurde der Spieler immer im Fokus gehalten, während die Spielwelt
#      durch die Szene navigiert wurde.
#    - Eine GUI-Kamera ermöglichte die Anzeige von Punkteständen und Lebenspunkten
#      unabhängig von der Kameraposition.

# 6. Spielmechanik erweitern:
#    - Du hast die Grundlage gelegt, um das Spiel durch neue Ebenen, Interaktionen
#      und Mechaniken wie Fallen oder Schlüssel weiterzuentwickeln.

# Dieses Kapitel bietet die Grundlage für viele weitere Erweiterungen, sei es durch
# komplexere Gegner, zusätzliche Level oder neue Herausforderungen wie Rätsel oder
# dynamische Ereignisse. Nutze die Übungsaufgaben, um das Gelernte zu festigen und
# dein Spiel weiter auszubauen.



# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Kopiere die Datei `level_1.tmx`-Datei im Ordner `_assets/12.15` und bennene
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
#
# Hinweis:
# - Verwende `arcade.check_for_collision_with_list()` für die Kollisionserkennung.
#
# - Erstelle eine Variable `self.keys_collected`, um die Anzahl der gesammelten Schlüssel 
#   zu speichern.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Füge dem Dungeon-Spiel eine "Trap"-Ebene in der Tilemap hinzu. Wenn der Spieler
# mit den Fallen kollidiert, soll seine Gesundheit sinken. Wenn die Gesundheit null 
# erreicht, wird das Spiel beendet.

# Hinweise:
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
        
        ...

        # Schlüssel
        self.keys_collected = 0  # Anzahl gesammelter Schlüssel

    def setup(self):
        
        ...

        layer_options = {
            ...

            "Keys": {
                "offset": self.tile_offset
            }
        }
  

    def on_update(self, delta_time):
        ...

        # Kollision mit Schlüsseln prüfen
        keys_hit_list = arcade.check_for_collision_with_list(self.player, self.scene["Keys"])

        for key in keys_hit_list:
            # Schlüssel entfernen
            key.remove_from_sprite_lists()

            # Anzahl der gesammelten Schlüssel erhöhen
            self.keys_collected += 1
            print(f"Schlüssel gesammelt: {self.keys_collected}")


'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Füge dem Dungeon-Spiel eine "Trap"-Ebene in der Tilemap hinzu. Wenn der Spieler
# mit den Fallen kollidiert, soll seine Gesundheit sinken. Wenn die Gesundheit null 
# erreicht, wird das Spiel beendet.

# Hinweise:
# - Beende das Spiel mit `arcade.close_window()`, wenn die Gesundheit des Spielers null erreicht.

'''
import arcade



class Character(TilesetSprite):
    
    ...

    def __init__(self):
        super().__init__()

        self.damage_cooldown = 0


    def update_animation(self, delta_time):

        ...

        if self.damage_cooldown > 0:
            self.damage_cooldown -= 1




class DungeonGameWithHealth(arcade.Window):
    
   ...


    # Setup-Methode, um die Tilemap zu laden, die Szene zu erstellen und den Spieler zu initialisieren.
    def setup(self):
        ...

        layer_options = {
            ...

            "Trap": {"offset": self.tile_offset},
        }
        


    # Aktualisiere die Spielmechanik: Bewegung, Kollisionen und Gesundheitslogik.
    def on_update(self, delta_time):
        ...

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
        

'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><



