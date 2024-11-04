#              _________________________________
#       ______|                                 |_____
#       \     |     12.8 TILEMAPS IN ARCADE     |    /
#        )    |_________________________________|   (
#       /________)                          (________\     4.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# Tilemaps sind Karten, die aus kleinen, sich wiederholenden Grafiken (Tiles) 
# erstellt werden, und ermöglichen die einfache Erstellung von Levels und 
# Spielwelten. Mit `arcade` können Entwickler Tilemaps verwenden, um komplexe 
# Umgebungen zu gestalten.


import arcade


# _________________________________
#                                 /
# Was ist eine Tilemap?          (
# ________________________________\

# Eine `Tilemap` ist eine 2D-Struktur, die in einem Raster organisiert ist und aus
# wiederholten Grafiken (Tiles) besteht. Die Tiles werden über eine externe Software
# wie Tiled erstellt und dann in Arcade geladen. Tiled ist eine beliebte, kostenlose Software,
# die Kartenerstellung und Ebenen (Layers) unterstützt.




# _________________________________
#                                 /
# Vorbereitungen                  (
# ________________________________\

# - Lade Tiled von `https://www.mapeditor.org/` herunter und erstelle ein Tilemap-Layout.
# - Exportiere das Projekt als `.tmx`-Datei und speichere es im Projektordner.

# Um Tilemaps in `arcade` zu verwenden, ist es wichtig, sicherzustellen, dass `pymunk`
# installiert ist, da `arcade` dies für die Kollisionserkennung in Tilemaps verwendet.

# Installiere in Thonny die Erweiterung `pymunk`.




# _________________________________
#                                 /
# Einfache Tilemap laden         (
# ________________________________\

# Arcade ermöglicht das Laden von Tilemaps mit der Funktion `arcade.load_tilemap()`.
# Hierbei wird die `.tmx`-Datei verwendet, die in Tiled erstellt wurde.

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Tilemap Beispiel")
        self.tile_map = None
        self.scene = None
        self.player_sprite = None

    def setup(self):
        # Lädt die Tilemap und die zugehörigen Ebenen
        map_name = "level_1.tmx"  # Pfad zur .tmx-Datei
        layer_options = {
            "Platforms": {"use_spatial_hash": True},  # Konfiguriert die Plattform-Ebene für Kollisionen
            "Background": {},  # Hintergrundebene ohne Kollisionen
        }
        self.tile_map = arcade.load_tilemap(map_name, layer_options=layer_options)
        
        # Erstellt die Szene basierend auf der Tilemap
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Spieler-Sprite hinzufügen
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", scale=0.5)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 200
        self.scene.add_sprite("Player", self.player_sprite)

    def on_draw(self):
        arcade.start_render()
        self.scene.draw()


window = MyGame()
window.setup()
arcade.run()




# _________________________________
#                                 /
# Kollisionserkennung einbauen    (
# ________________________________\

# In der Tilemap können Ebenen definiert werden, die für die Kollisionserkennung genutzt
# werden. Dies ermöglicht, dass bestimmte Elemente im Level als Hindernisse oder Plattformen
# fungieren.

class CollisionGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Tilemap mit Kollisionen")
        self.scene = None
        self.physics_engine = None
        self.player_sprite = None

    def setup(self):
        map_name = "level_with_collisions.tmx"
        layer_options = {
            "Platforms": {"use_spatial_hash": True},
        }
        tile_map = arcade.load_tilemap(map_name, layer_options=layer_options)
        self.scene = arcade.Scene.from_tilemap(tile_map)

        # Spieler-Sprite erstellen
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", scale=0.5)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 200
        self.scene.add_sprite("Player", self.player_sprite)

        # Physik-Engine einrichten
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, gravity_constant=0.5, walls=self.scene["Platforms"])

    def on_draw(self):
        arcade.start_render()
        self.scene.draw()

    def on_update(self, delta_time):
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = 10
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


window = CollisionGame()
window.setup()
arcade.run()




# _________________________________
#                                 /
# Arbeiten mit mehreren Ebenen   (
# ________________________________\

# Eine Tilemap kann verschiedene Ebenen enthalten, z.B. für Hintergrund, Plattformen,
# Hindernisse oder interaktive Elemente. Diese Ebenen können in `arcade` individuell
# aktiviert und angepasst werden.




# _________________________________
#                                 /
# Tilemap-Grössenanpassung        (
# ________________________________\

# Beim Laden einer Tilemap kann man einen Skalierungsfaktor verwenden, um die Karte
# anzupassen. Dies ist nützlich, wenn man eine Karte vergrössern oder verkleinern möchte.

# Beispiel für das Laden mit einer Skalierung von 0.5:
# ```
# tile_map = arcade.load_tilemap("level_1.tmx", scaling=0.5)
# ```



# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Tilemaps bieten eine einfache Möglichkeit, Levels in `arcade` zu erstellen.
#
# - `arcade.load_tilemap()` lädt eine Tilemap und die zugehörigen Ebenen für die
#   Verwendung in einem Spiel.
#
# - Die Kollisionserkennung wird mithilfe spezifizierter Ebenen in der Tilemap eingerichtet.
#
# - Der Wechsel zwischen Ebenen und das Arbeiten mit mehreren Ebenen ist in `arcade`
#   unkompliziert und leistungsstark.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Lade eine Tilemap mit einer Hintergrund- und einer Plattform-Ebene. Zeige sie
# auf dem Bildschirm an und füge ein Spieler-Sprite hinzu.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Tilemap mit einer Hindernis-Ebene. Lasse das Spieler-Sprite sich
# bewegen, aber verhindere, dass es durch Hindernisse hindurchgeht.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Entwickle ein Level mit Plattformen und Hindernissen, das der Spieler durchqueren
# muss. Füge eine Schwerkraft- und Sprungmechanik hinzu, um das Level spielbar zu machen.


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
# Lade eine Tilemap mit einer Hintergrund- und einer Plattform-Ebene. Zeige sie
# auf dem Bildschirm an und füge ein Spieler-Sprite hinzu.


'''
import arcade

class TilemapGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Tilemap mit Plattformen")
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 150

        # Tilemap laden
        map_name = "example_map.json"  # Bitte durch den Pfad zur Tilemap-Datei ersetzen
        self.tile_map = arcade.load_tilemap(map_name, scaling=1)
        self.background_layer = self.tile_map.sprite_lists["Hintergrund"]
        self.platform_layer = self.tile_map.sprite_lists["Plattformen"]

    def on_draw(self):
        arcade.start_render()
        self.background_layer.draw()
        self.platform_layer.draw()
        self.player_sprite.draw()

window = TilemapGame()
arcade.run()
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Tilemap mit einer Hindernis-Ebene. Lasse das Spieler-Sprite sich
# bewegen, aber verhindere, dass es durch Hindernisse hindurchgeht.

'''
import arcade

class ObstacleGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Tilemap mit Hindernissen")
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 150

        # Tilemap laden
        map_name = "example_map_with_obstacles.json"  # Pfad zur Tilemap mit Hindernissen
        self.tile_map = arcade.load_tilemap(map_name, scaling=1)
        self.obstacle_layer = self.tile_map.sprite_lists["Hindernisse"]

    def on_draw(self):
        arcade.start_render()
        self.obstacle_layer.draw()
        self.player_sprite.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -5

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.RIGHT, arcade.key.LEFT):
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        # Bewegung aktualisieren
        self.player_sprite.update()

        # Kollision mit Hindernissen verhindern
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.obstacle_layer)
        if hit_list:
            self.player_sprite.change_x = 0

window = ObstacleGame()
arcade.run()
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Entwickle ein Level mit Plattformen und Hindernissen, das der Spieler durchqueren
# muss. Füge eine Schwerkraft- und Sprungmechanik hinzu, um das Level spielbar zu machen.

'''
import arcade

class PlatformerGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Platformer Level")
        self.gravity = -0.5
        self.player_jump_speed = 10
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 150
        self.player_sprite.change_y = 0
        self.player_on_ground = False

        # Tilemap laden
        map_name = "platformer_level.json"  # Bitte durch den Pfad zur Level-Tilemap ersetzen
        self.tile_map = arcade.load_tilemap(map_name, scaling=1)
        self.platform_layer = self.tile_map.sprite_lists["Plattformen"]

    def on_draw(self):
        arcade.start_render()
        self.platform_layer.draw()
        self.player_sprite.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
        elif key == arcade.key.UP and self.player_on_ground:
            self.player_sprite.change_y = self.player_jump_speed
            self.player_on_ground = False

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.RIGHT, arcade.key.LEFT):
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        # Schwerkraft anwenden
        self.player_sprite.change_y += self.gravity
        self.player_sprite.update()

        # Plattform-Kollision prüfen
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.platform_layer)
        if hit_list:
            self.player_sprite.change_y = 0
            self.player_on_ground = True
        else:
            self.player_on_ground = False

window = PlatformerGame()
arcade.run()
'''



# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


