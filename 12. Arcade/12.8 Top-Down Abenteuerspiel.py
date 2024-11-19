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

class TopDownGame(arcade.Window):

    # Initialisiert das Fenster, die Tilemap-Parameter und die Szene.
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        # Tilemap-Konfiguration
        self.tile_map = None            # Die geladene Tilemap
        self.tile_scale = 2.0           # Skalierung der Tiles
        self.tile_offset = (-80, 0)     # Offset für die Tilemap
        self.tile_size = 16 * self.tile_scale  # Grösse eines Tiles
        
        # Spieler-Konfiguration
        self.player_scale = 0.3         # Skalierung des Spielers
        self.player_offset = (16, 22)   # Offset zur Positionierung des Spielers
        
        # Szene und Spieler
        self.scene = None               # Die Szene, die alle Objekte enthält
        self.player_sprite = None       # Das Spieler-Sprite
        
        # Physik-Engine
        self.physics_engine = None      # Physik-Engine für Bewegungen und Kollisionen


    # Lädt die Tilemap, erstellt die Szene und initialisiert den Spieler.
    def setup(self):

        # Lade die Tilemap aus einer .tmx-Datei
        map_name = "_assets/topdown/level_1.tmx"  # Pfad zur .tmx-Datei
        
        # Optionen für die Tilemap-Ebenen
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
            }
        }
        
        # Lade die Tilemap mit den angegebenen Optionen
        self.tile_map = arcade.load_tilemap(map_name, self.tile_scale, layer_options=layer_options)
        
        # Erstelle die Szene basierend auf der geladenen Tilemap
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        
        # Spieler-Sprite hinzufügen
        self.player_sprite = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
            scale=self.player_scale
        )
        
        # Setze die Startposition des Spielers
        self.player_sprite.center_x = self.tile_size * 23 + self.tile_offset[0] + self.player_offset[0]
        self.player_sprite.center_y = self.tile_size * 4 + self.tile_offset[1] + self.player_offset[1]
        
        # Füge das Spieler-Sprite zur Szene hinzu
        self.scene.add_sprite("Player", self.player_sprite)
        
        # Initialisiere die Physik-Engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
            gravity_constant=0.0,  # Keine Schwerkraft, da es ein Top-Down-Spiel ist
            walls=self.scene["Walls"]
        )


    # Aktualisiert die Physik und prüft Kollisionen.
    def on_update(self, delta_time):

        # Aktualisiere die Position des Spielers mithilfe der Physik-Engine
        self.physics_engine.update()
        
        # Prüfe, ob der Spieler mit Türen kollidiert
        door_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene["Door"]
        )

        # Aktionen bei Kollision mit Türen
        for door in door_hit_list:
            print("Tür erreicht!")


    # Zeichnet die Szene und den Spieler.
    def on_draw(self):
        arcade.start_render()  # Starte den Renderprozess
        self.scene.draw()      # Zeichne alle Ebenen der Szene


    # Reagiert auf Tastendrücke und bewegt den Spieler.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = 5  # Bewege nach oben
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -5  # Bewege nach unten
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -5  # Bewege nach links
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5  # Bewege nach rechts


    # Stoppt die Bewegung des Spielers, wenn die Taste losgelassen wird.
    def on_key_release(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.player_sprite.change_y = 0  # Stoppe vertikale Bewegung
        if key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player_sprite.change_x = 0  # Stoppe horizontale Bewegung


# Anwendung starten
window = TopDownGame(title="Dungeon Spiel")
window.setup()  # Initialisiere das Spiel
arcade.run()  # Starte das Spiel




# ____________________________________
#                                    /
# Erstellen von Tilemaps mit Tiled  (
# ___________________________________\

# Tiled ist eine Open-Source-Software, mit der du Karten (Tilemaps) für Spiele 
# erstellen kannst. Diese Karten können anschließend in Arcade verwendet werden, 
# um Spielumgebungen zu gestalten. 

# Was ist eine Tilemap?
# ---------------------
# Eine Tilemap besteht aus einer Sammlung von Kacheln (Tiles), die auf einer Karte 
# angeordnet sind. Jede Kachel repräsentiert ein Element der Spielwelt, z. B. 
# Boden, Wände oder Objekte.

# Was benötigst du?
# -----------------
# - Die Software Tiled (https://www.mapeditor.org/)
#
# - Ein Set von Grafiken, sogenannte Tilesets, um die Karten zu gestalten.
#   Im Ordner _assets/topdown hat es ein Tileset (dungeon_tiles.png) und 
#   die Tilemap (level_1.tmx). Du kannst diese Datei mit der Software
#   Tiled öffnen und verändern. 

# Schritte zum Erstellen einer Tilemap:
# -------------------------------------

# 1. Neues Projekt erstellen
#    - Öffne Tiled und erstelle ein neues Projekt.
# 
#    - Wähle die gewünschte Kartengröße, z. B. 40x30 Kacheln.
# 
#    - Setze die Kachelgröße, z. B. 16x16 Pixel.

# 2. Tilesets hinzufügen
#    - Importiere ein Tileset (eine Sammlung von Kachelbildern), das du für 
#      deine Karte verwenden möchtest.
#
#    - Klicke auf `Map > New Tileset` und wähle die Bilddatei aus.
#
#    - Setze die Größe der Tiles auf die gleiche Größe wie in deiner Karte 
#      (z. B. 16x16 Pixel).

# 3. Ebenen erstellen
#    - In Tiled kannst du mehrere Ebenen (Layers) erstellen. Jede Ebene 
#      repräsentiert eine Kategorie von Objekten.
#
#    - Beispiele:
#      * Floor: Der Boden der Karte.
#      * Walls: Hindernisse oder Wände.
#      * Door: Türen, mit denen der Spieler interagieren kann.

# 4. Karte gestalten
#    - Wähle in der Werkzeugleiste das "Stift"-Werkzeug aus, um Kacheln auf der 
#      Karte zu platzieren.
#
#    - Male deine Karte, indem du die Kacheln aus dem Tileset auf die Ebenen ziehst.

# 5. Kollisions-Ebenen erstellen
#    - Erstelle eine Ebene für Kollisionen (z. B. "Walls").
#
#    - Stelle sicher, dass Hindernisse und Wände auf dieser 
#      Ebene gezeichnet werden.

# 6. Speichern und Exportieren
#    - Speichere die Karte als `.tmx`-Datei. Diese Datei wird später in 
#      Arcade geladen.
#
#    - Stelle sicher, dass alle Grafiken im gleichen Ordner wie die `.tmx`-Datei 
#      gespeichert sind.





# _________________________________
#                                 /
# Zusammenfassung                (
# ________________________________\

# - Tilemaps: Mit Arcade kannst du .tmx-Dateien laden, um eine Spielumgebung zu erstellen.
#
# - Szene: Die `arcade.Scene`-Klasse organisiert alle Sprites und Ebenen.
#
# - Physik-Engine: Die `arcade.PhysicsEnginePlatformer` ermöglicht Bewegung und Kollisionen.
#
# - Kollisionen: Mit `check_for_collision_with_list()` können Interaktionen zwischen 
#   Objekten erkannt werden.




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
        self.player_sprite = None
        
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
        self.player_sprite = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
            scale=self.player_scale
        )
        self.player_sprite.center_x = self.tile_size * 23 + self.tile_offset[0] + self.player_offset[0]
        self.player_sprite.center_y = self.tile_size * 4 + self.tile_offset[1] + self.player_offset[1]
        self.scene.add_sprite("Player", self.player_sprite)
        
        # Physik-Engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
            gravity_constant=0.0,
            walls=self.scene["Walls"]
        )

    def on_update(self, delta_time):
        # Bewegung des Spielers aktualisieren
        self.physics_engine.update()
        
        # Kollision mit Türen prüfen
        door_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.scene["Door"])
        for door in door_hit_list:
            print("Tür erreicht!")
        
        # Kollision mit Schlüsseln prüfen
        keys_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.scene["Keys"])
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
            self.player_sprite.change_y = 5
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -5
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.player_sprite.change_y = 0
        if key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player_sprite.change_x = 0


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
        self.player_sprite = None  # Spieler-Sprite
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
        self.player_sprite = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
            scale=self.player_scale
        )
        
        # Position des Spielers setzen
        self.player_sprite.center_x = self.tile_size * 23 + self.tile_offset[0] + self.player_offset[0]
        self.player_sprite.center_y = self.tile_size * 4 + self.tile_offset[1] + self.player_offset[1]
        self.scene.add_sprite("Player", self.player_sprite)  # Spieler zur Szene hinzufügen
        
        # Physik-Engine für den Spieler
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
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
        traps_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.scene["Trap"])
        for trap in traps_hit_list:
            if self.damage_cooldown == 0:  # Wenn der Spieler nicht unverwundbar ist
                self.health -= 10  # Gesundheit reduzieren
                print(f"Gesundheit: {self.health}")
                self.damage_cooldown = 50  # Setze Unverwundbarkeit (ca. 1 Sekunde bei 60 FPS)
            
            if self.health <= 0:  # Wenn die Gesundheit 0 erreicht
                print("Spieler gestorben. Spiel beendet!")
                arcade.close_window()  # Beende das Spiel
        
        # Kollision mit Türen prüfen
        door_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.scene["Door"])
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
            self.player_sprite.change_y = 5  # Nach oben bewegen
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -5  # Nach unten bewegen
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -5  # Nach links bewegen
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5  # Nach rechts bewegen

    # Spielerbewegung stoppen, wenn die Taste losgelassen wird.
    def on_key_release(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.player_sprite.change_y = 0  # Vertikale Bewegung stoppen
        if key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player_sprite.change_x = 0  # Horizontale Bewegung stoppen


# Spiel starten
window = DungeonGameWithHealth(title="Dungeon-Spiel mit Gesundheit")
window.setup()  # Setup des Spiels
arcade.run()  # Starte das Spiel

'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


