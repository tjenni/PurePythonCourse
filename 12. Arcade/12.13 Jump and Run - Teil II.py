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


# Diese Klasse repräsentiert eine animierte Spielfigur. 
# Sie verwaltet die Animationen für Laufen, Springen, Stehen und Klettern.
class Character(arcade.Sprite):
    
    def __init__(self, textures_path, scale=1):
        super().__init__()

        self.n_walking_textures = 8  # Anzahl der Texturen für die Laufanimation
        self.n_climbing_textures = 2  # Anzahl der Texturen für die Kletteranimation
        
        self.face_direction = 0  # Richtung der Spielfigur (0: rechts, 1: links)
        self.can_jump = False  # Gibt an, ob die Spielfigur springen kann
        self.is_on_ladder = False  # Gibt an, ob die Spielfigur auf einer Leiter ist

        self.scale = scale  # Skalierung der Spielfigur
        
        self.frame = 0  # Animationsrahmenzähler
        self.animation_speed = 2  # Geschwindigkeit der Animation
        
        self.current_texture = 0  # Aktuelle Textur der Animation
        
        # Lade alle Texturen für die Animationen
        self.all_textures = {}

        # Lade die Texturen für Stehen und Springen
        self.all_textures["idle"] = self._load_texture_pair(f"{textures_path}_idle.png")
        self.all_textures["jump"] = self._load_texture_pair(f"{textures_path}_jump.png")
        
        # Lade die Texturen für die Laufanimation
        self.all_textures["walk"] = [
            self._load_texture_pair(f"{textures_path}_walk{i}.png") for i in range(self.n_walking_textures)
        ]
        
        # Lade die Texturen für die Kletteranimation
        self.all_textures["climb"] = [
            self._load_texture_pair(f"{textures_path}_climb{i}.png") for i in range(self.n_climbing_textures)
        ]

        # Setze die Anfangstextur
        self.texture = self.all_textures["idle"][0]
        
        # Setze die Kollisionsbox basierend auf der Anfangstextur
        self.hit_box = self.texture.hit_box_points
 

    # Lädt ein Texturpaar: eine normale und eine horizontal gespiegelt.
    def _load_texture_pair(self, path):
        return [
            arcade.load_texture(path),
            arcade.load_texture(path, flipped_horizontally=True)
        ]


    # Aktualisiert die Animation der Spielfigur basierend auf ihrem Zustand (Laufen, 
    # Springen, Klettern, Stehen).
    def update_animation(self, delta_time):

        self.frame = (self.frame + 1) % self.animation_speed

        # Bestimme die Blickrichtung der Spielfigur
        if self.change_x < 0:
            self.face_direction = 1  # Blick nach links
        elif self.change_x > 0:
            self.face_direction = 0  # Blick nach rechts
        
        # Animation für die Leiter
        if self.is_on_ladder:
            if self.change_y == 0:  # Wenn die Figur nicht auf der Leiter bewegt wird
                self.current_texture = 0
            elif self.frame == 0:  # Aktualisiere die Textur nur bei bestimmten Frames
                self.current_texture += 1
            
            self.current_texture = self.current_texture % self.n_climbing_textures
            self.texture = self.all_textures["climb"][self.current_texture][self.face_direction]
            return
        
        # Animation für Springen
        if not self.can_jump:
            self.texture = self.all_textures["jump"][self.face_direction]
            return
        
        # Animation für Stehen
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.all_textures["idle"][self.face_direction]
            return
        
        # Animation fürs Gehen
        if self.frame == 0:  # Aktualisiere die Textur nur bei bestimmten Frames
            self.current_texture += 1
        
        self.current_texture = self.current_texture % self.n_walking_textures
        self.texture = self.all_textures["walk"][self.current_texture][self.face_direction]





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
        self.keys = {"UP": False, "DOWN": False, "LEFT": False, "RIGHT": False}  # Zustände der Tasten
        
        self.tile_offset = (0, 0)     # Offset für die Tilemap
        
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
        self.player = Character("_assets/12.11/femaleAdventurer/character_femaleAdventurer", scale=self.tile_scale/1.5)
        self.player.center_x = 196
        self.player.center_y = 100
        
        # Lade die Tilemap aus einer .tmx-Datei
        map_name = "_assets/12.12/level_1.tmx"  # Pfad zur .tmx-Datei
        
        
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
        

        # Sounds laden
        self.coin_sound = arcade.load_sound(":resources:sounds/coin2.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump3.wav")
        self.gameover_sound = arcade.load_sound(":resources:sounds/gameover2.wav")
        self.success_sound = arcade.load_sound(":resources:sounds/upgrade2.wav")

        self.scene.add_sprite("Player", self.player)

        # Physik-Engine initialisieren
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, gravity_constant=0.5, walls=self.scene["Walls"], ladders=self.scene["Ladders"])


    # Fügt eine neue Kachel an der angegebenen Position hinzu.
    def add_tile(self, column, row, tile_id):

        if self.tiles[tile_id] is None:  # Keine Aktion, wenn die ID leer ist
            return
        
        # Lade die Textur und ermittele den Kacheltyp
        texture = self.tiles[tile_id][0]
        sprite_type = self.tiles[tile_id][1]
                
        # Erstelle ein neues Sprite für die Kachel
        sprite = arcade.Sprite(texture, scale=0.5)
        sprite.center_x = column * self.tile_size + self.tile_size // 2
        sprite.center_y = (len(self.tilemaps[self.level-1]) - 1 - row) * self.tile_size + self.tile_size // 2
        sprite.row = row
        sprite.column = column
        sprite.id = tile_id
        
        # Füge das Sprite zur entsprechenden Sprite-Liste hinzu
        self.sprite_lists[sprite_type].append(sprite)


    # Erstellt die Sprite-Listen basierend auf der Tilemap.
    def create_sprite_lists(self, tilemap):
        
        # Lösche bestehende Sprites in allen Listen
        for sprite_list in self.sprite_lists.values():
            sprite_list.clear()
        
        # Durchlaufe die Tilemap und füge Sprites hinzu
        for i, row in enumerate(tilemap):
            for j, tile_id in enumerate(row):
                self.add_tile(j, i, tile_id)

    
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

        # Bewegung der Spielfigur basierend auf Tasteneingaben
        if self.keys["RIGHT"]:
            self.player.change_x = 5
        elif self.keys["LEFT"]:
            self.player.change_x = -5
        else:
            self.player.change_x = 0

        # Bewegung der Spielfigur auf der Leiter
        if self.player.is_on_ladder:
            if self.keys["UP"]:
                self.player.change_y = 5
            elif self.keys["DOWN"]:
                self.player.change_y = -5
            else:
                self.player.change_y = 0

        # Aktualisiere die Physik-Engine
        self.physics_engine.update()
        
        
        self.update_camera()
    
        
        # Aktualisiere die Zustände der Spielfigur
        self.player.is_on_ladder = self.physics_engine.is_on_ladder()
        self.player.can_jump = self.physics_engine.can_jump() and not self.player.is_on_ladder

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
        
        

    # Verarbeitet Tastendrücke.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.keys["RIGHT"] = True
        elif key == arcade.key.LEFT:
            self.keys["LEFT"] = True
        elif key == arcade.key.UP:
            self.keys["UP"] = True
            
            if self.player.can_jump:
                self.player.change_y = 12

        elif key == arcade.key.DOWN:
            self.keys["DOWN"] = True


    # Verarbeitet das Loslassen von Tasten.
    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.keys["RIGHT"] = False
        elif key == arcade.key.LEFT:
            self.keys["LEFT"] = False
        elif key == arcade.key.UP:
            self.keys["UP"] = False
        elif key == arcade.key.DOWN:
            self.keys["DOWN"] = False


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




