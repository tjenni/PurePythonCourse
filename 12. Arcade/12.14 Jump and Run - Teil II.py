#              ___________________________________
#       ______|                                  |_____
#       \     |   12.12 JUMP AND RUN - TEIL II   |    /
#        )    |__________________________________|   (
#       /________)                           (________\     24.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


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
#   Im Ordner `_assets/12.12` hat es ein Tileset (tiles.png) und 
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
#      * Traps: Fallse
#      * Coins: Münzen
#      * Ladders: Leitern
#      * Walls: Hindernisse oder Wände.
#      * Door: Türen, mit denen der Spieler interagieren kann.
#      * Background: Hintergrundobjekte

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



import arcade
import xml.dom.minidom
import collections
import os


# Klasse zur Verwaltung eines Tilesheets und zum Laden von Texturen
class Tilesheet():
    # Initialisiert das Tilesheet und lädt Texturen basierend auf einer XML-Datei.
    def __init__(self, xml_file, load_pair=True):
        self.textures = {}  # Speichert die geladenen Texturen als Dictionary
        self.n_textures = {}  # Speichert die Anzahl der Texturen pro Zustand
        
        try:
            # XML-Dokument laden und parsen
            document = xml.dom.minidom.parse(xml_file)
        except Exception as e:
            raise FileNotFoundError(f"Die Datei {xml_file} konnte nicht geladen werden. Fehler: {e}")
        
        # Hauptknoten des TextureAtlas aus der XML-Datei
        textureAtlas = document.getElementsByTagName("TextureAtlas")[0]
        subTextures = textureAtlas.getElementsByTagName("SubTexture")
        
        # Pfad zum Bild, das die Texturen enthält
        image_file = os.path.join(os.path.dirname(xml_file), textureAtlas.getAttribute('imagePath')) 
        
        # Iteriere über alle definierten SubTexturen im Tilesheet
        for subTexture in subTextures:
            name = subTexture.getAttribute('name')  # Name der Textur
            
            # Extrahiere die Zahl am Ende des Namens (z. B. "walk1" → "walk", 1)
            nr = ''.join(filter(str.isdigit, name[::-1]))[::-1]
            
            # Zähle die Anzahl der Texturen pro Zustand
            if nr.isdigit():  # Mehrere Texturen pro Zustand
                id = name[:-len(nr)]
                self.n_textures[id] = self.n_textures.get(id, 0) + 1
            else:  # Eine Textur pro Zustand
                self.n_textures[name] = 1
            
            # Lade die Textur-Parameter
            x = int(subTexture.getAttribute('x'))
            y = int(subTexture.getAttribute('y'))
            width = int(subTexture.getAttribute('width'))
            height = int(subTexture.getAttribute('height'))
            
            # Lade entweder nur die normale Textur oder ein Texturpaar (normal + gespiegelt)
            if load_pair:
                texture = self._load_texture_pair(image_file, x, y, width, height)
            else:
                texture = arcade.load_texture(image_file, x, y, width, height)
            
            if name in self.textures:
                raise ValueError(f"Duplikat gefunden: Texturname '{name}' existiert bereits.")
            
            self.textures[name] = texture  # Speichere die Textur im Dictionary


    # Lädt ein Texturpaar: normale und horizontal gespiegelte Version.
    def _load_texture_pair(self, path, x, y, width, height):
        return [
            arcade.load_texture(path, x, y, width, height),  # Normale Textur
            arcade.load_texture(path, x, y, width, height, flipped_horizontally=True)  # Gespiegelte Textur
        ]



# Diese Klasse repräsentiert eine animierte Spielfigur.
# Sie verwaltet die Animationen und Zustände wie Laufen, Springen, Stehen und Klettern.
class Character(arcade.Sprite):
    # Richtungs- und Zustandskonstanten für die Spielfigur
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3
    
    IDLE = 'idle'
    WALK = 'walk'
    JUMP = 'jump'
    CLIMB = 'climb'
    
    def __init__(self, xml_file, scale=0.25):
        super().__init__()
        
        self.speed = 5  # Bewegungsgeschwindigkeit
        self.jump_impulse = 12  # Sprungkraft
        
        self.facing = Character.RIGHT  # Blickrichtung der Spielfigur
        self.can_jump = False  # Gibt an, ob die Spielfigur springen kann
        self.is_on_ladder = False  # Gibt an, ob die Spielfigur auf einer Leiter ist
        
        self.scale = scale  # Skalierung der Spielfigur
        
        self.frame = 0  # Aktueller Animationsframe
        self.texture_idx = 0  # Index der aktuellen Textur in der Animation
        self.frames_per_texture = 2  # Anzahl der Frames pro Textur
        
        # Lade das Tilesheet für die Animationen
        self.tilesheet = Tilesheet(xml_file)
        self.state = Character.IDLE  # Initialzustand der Spielfigur
        
        # Setze die Anfangstextur
        self.update_texture()
    

    # Aktualisiert die aktuelle Textur der Spielfigur basierend auf Zustand und Blickrichtung
    def update_texture(self):
        # Bestimme die Richtung (normal oder gespiegelt)
        facing_idx = 1 if self.facing == Character.LEFT else 0
        
        # Bestimme die richtige Textur basierend auf Zustand und Texturindex
        n = self.tilesheet.n_textures[self.state]
        self.texture_idx %= n
        texture_key = f"{self.state}{self.texture_idx}" if n > 1 else self.state
        
        self.texture = self.tilesheet.textures[texture_key][facing_idx]
        self.hit_box = self.texture.hit_box_points  # Aktualisiere die Kollisionsbox
    

    # Bewegt die Spielfigur in eine bestimmte Richtung mit optionaler Geschwindigkeit
    def move(self, direction=None, speed=None):
        speed = self.speed if speed is None else speed
        if direction == Character.RIGHT:
            self.change_x = speed
        elif direction == Character.LEFT:
            self.change_x = -speed
        elif direction == Character.UP:
            self.change_y = speed
        elif direction == Character.DOWN:
            self.change_y = -speed
    

    # Führt einen Sprung aus, wenn erlaubt
    def jump(self):
        if self.can_jump:
            self.change_y = self.jump_impulse


    # Aktualisiert die Animation der Spielfigur basierend auf ihrem Zustand
    def update_animation(self, delta_time):
        self.frame = (self.frame + 1) % self.frames_per_texture  # Animationsframe erhöhen
        
        # Zustände aktualisieren
        if len(self.physics_engines) > 0:
            engine = self.physics_engines[0]
            self.is_on_ladder = engine.is_on_ladder()
            self.can_jump = engine.can_jump() and not self.is_on_ladder
        
        # Nur beim Frame null die Textur wechseln
        if self.frame == 0:
            self.texture_idx += 1

        # Blickrichtung setzen
        if self.change_x < 0:
            self.facing = Character.LEFT

        elif self.change_x > 0:
            self.facing = Character.RIGHT
        
        # Zustand setzen
        if self.is_on_ladder:
            self.state = Character.CLIMB
            
            if self.change_y == 0:
                self.texture_idx = 0
                
        elif not self.can_jump:
            self.state = Character.JUMP
            
        elif self.change_x == 0:
            self.state = Character.IDLE

        else:
            self.state = Character.WALK
        
        self.update_texture()  # Textur aktualisieren



# Diese Klasse repräsentiert eine Ansicht für Informationsbildschirme wie Start-, 
# Game-Over- oder Endbildschirme.
class InfoView(arcade.View):

    # Initialisiert die Info-Ansicht mit einem Text und einer Hintergrundfarbe.
    def __init__(self, text="", color=arcade.color.BLACK):
        super().__init__()

        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.text = text  # Der anzuzeigende Text
        self.color = color  # Die Textfarbe

    # Zeichnet die Ansicht mit dem Text und einer Anweisung zur Interaktion.
    def on_draw(self):
        self.clear()
        arcade.draw_text(self.text, self.window.width // 2, self.window.height // 2, self.color, 48, anchor_x="center")
        arcade.draw_text(
            "weiter mit der Leertaste",
            self.window.width // 2,
            self.window.height // 2 - 50,
            arcade.color.BLACK,
            14,
            anchor_x="center",
        )

    # Wechselt zur Spielansicht, wenn die Leertaste gedrückt wird.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)



# Diese Klasse repräsentiert die Hauptspiel-Logik, einschließlich der Spielerbewegung, 
# Levelstruktur und Kollisionserkennung.
class GameView(arcade.View):

    # Initialisiert das Spiel mit einem Spieler, Sprite-Listen und der Punktzahl.
    def __init__(self):
        super().__init__()

        arcade.set_background_color(arcade.color.SKY_BLUE)
        
        # Spielkamera: Verfolgt die Spiellandschaft
        self.camera = arcade.Camera(self.window.width, self.window.height)

        # GUI-Kamera: Statische Ansicht für Benutzeroberfläche
        self.gui_camera = arcade.Camera(self.window.width, self.window.height)

        self.score = 0
        
        self.n_level = 1

        # Größe jeder Kachel in Pixel
        self.tile_size = 64
        
        self.tile_offset = (0, 0)     # Offset für die Tilemap
        
        self.keys = collections.defaultdict(lambda: False)  # Tastenstatus
        
    # Aktualisiert die Spielkamera, sodass sie der Spielfigur folgt.
    def update_camera(self):
        
        # Kamera zentrieren auf den Spieler, dabei X und Y Achse berücksichtigen
        screen_center_x = max(0, self.player.center_x - self.camera.viewport_width // 2)
        screen_center_y = max(0, self.player.center_y - self.camera.viewport_height // 2)

        # Kamera zur berechneten Position verschieben
        self.camera.move_to((screen_center_x, screen_center_y), speed=0.2)


    # Initialisiert das Spiel für ein spezifisches Level.
    def setup(self, level=1):
        self.level = level
        
        self.tile_scale = 0.5

        # Spieler-Sprite erstellen
        self.player = Character("_assets/12.11/femaleAdventurer.xml", scale=self.tile_scale/1.5)
        self.player.center_x = 196
        self.player.center_y = 100
        
        # Lade die Tilemap aus einer .tmx-Datei
        map_name = "_assets/12.14/level_1.tmx"  # Pfad zur .tmx-Datei
        
        
        # Optionen für die Tilemap-Ebenen
        layer_options = {
            "Walls": {
                "use_spatial_hash": True,
                "offset": self.tile_offset
            },
            "Ladders": {
                "offset": self.tile_offset
            },
            "Traps": {
                "offset": self.tile_offset
            },
            "Coins": {
                "offset": self.tile_offset
            },
            "Doors": {
                "offset": self.tile_offset
            },
            "Background": {
                "offset": self.tile_offset
            }
        }
        
        # Lade die Tilemap mit den angegebenen Optionen
        self.tile_map = arcade.load_tilemap(map_name, self.tile_scale, layer_options=layer_options)
        
        # Erstelle die Szene basierend auf der geladenen Tilemap
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        
        # Sounds laden
        self.coin_sound = arcade.load_sound(":resources:sounds/coin2.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump3.wav")
        self.gameover_sound = arcade.load_sound(":resources:sounds/gameover2.wav")
        self.success_sound = arcade.load_sound(":resources:sounds/upgrade2.wav")

        self.scene.add_sprite("Player", self.player)

        # Physik-Engine initialisieren
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player,
            gravity_constant=0.5,
            walls=self.scene["Walls"],
            ladders=self.scene["Ladders"]
        )
        
        self.player.register_physics_engine(self.physics_engine)  # Physik-Engine der Spielfigur hinzufügen

    
    # Zeichnet die Szene und die Punktzahl.
    def on_draw(self):
        arcade.start_render()
        
        # Spielkamera aktivieren
        self.camera.use() 
        self.scene.draw() 

        # GUI-Kamera aktivieren
        self.gui_camera.use()
        arcade.draw_text(f"Punkte: {self.score}", 15, self.window.height - 30, arcade.color.WHITE, 16)


    # Aktualisiert den Spielzustand und die Animation der Spielfigur.
    def on_update(self, delta_time):

        # Bewege die Spielfigur basierend auf Tasteneingaben
        if self.keys[arcade.key.RIGHT]:
            self.player.move(Character.RIGHT)  # Bewegung nach rechts
        elif self.keys[arcade.key.LEFT]:
            self.player.move(Character.LEFT)  # Bewegung nach links
        else:
            self.player.move(Character.RIGHT, 0)  # Keine horizontale Bewegung
        
        # Bewegung auf der Leiter
        if self.player.is_on_ladder:
            if self.keys[arcade.key.UP]:
                self.player.move(Character.UP)  # Bewegung nach oben
            elif self.keys[arcade.key.DOWN]:
                self.player.move(Character.DOWN)  # Bewegung nach unten
            else:
                self.player.move(Character.UP, 0)  # Keine vertikale Bewegung


        # Aktualisiere die Physik-Engine
        self.physics_engine.update()
        
        # Aktualisiere die Kamera
        self.update_camera()
    
        
        # Aktualisiere die Animation der Spielfigur
        self.player.update_animation(delta_time)
        
        # Kollisionserkennung mit Coins
        coin_hit_list = arcade.check_for_collision_with_list(self.player, self.scene["Coins"])
        for coin in coin_hit_list:
            arcade.play_sound(self.coin_sound)
            coin.remove_from_sprite_lists()
            self.score += 1
        
        # Kollision mit Fallen
        trap_hit_list = arcade.check_for_collision_with_list(self.player, self.scene["Traps"])
        for trap in trap_hit_list:
            arcade.play_sound(self.gameover_sound)
            self.window.show_view(InfoView("GAME OVER"))
        
        # Kollision mit Türen
        door_hit_list = arcade.check_for_collision_with_list(self.player, self.scene["Doors"])
        for door in door_hit_list:
            arcade.play_sound(self.success_sound)
            
            if self.level < self.n_level:
                self.setup(level=self.level + 1)
            else:
                self.window.show_view(InfoView("ENDE", color=arcade.color.AMBER))
             
        # Spieler innerhalb des Fensters halten
        if self.player.center_x < 0:
            self.player.center_x = 0
        
        # Spieler fällt aus dem Fenster
        if self.player.center_y < 0:
            arcade.play_sound(self.gameover_sound)
            self.window.show_view(InfoView("GAME OVER"))
        
        
    # Verarbeitet Tastendrücke
    def on_key_press(self, key, modifiers):
        self.keys[key] = True  # Markiere die Taste als gedrückt
        if key == arcade.key.UP:  # Sprungaktion
            self.player.jump()


    # Verarbeitet das Loslassen von Tasten
    def on_key_release(self, key, modifiers):
        self.keys[key] = False  # Markiere die Taste als losgelassen


# Hauptprogramm

window = arcade.Window(800, 600, "Jumpmania")
window.show_view(InfoView(text="Jumpmania", color=arcade.color_from_hex_string("#665d4a")))
arcade.run()






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


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#



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


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><




