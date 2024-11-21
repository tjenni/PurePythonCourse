#              ______________________
#       ______|                      |_____
#       \     |     12.7 TILEMAPS    |    /
#        )    |______________________|   (
#       /________)               (________\     21.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# Tilemaps sind eine einfache und leistungsstarke Methode, um Level-Layouts für 
# 2D-Spiele zu erstellen. Anstatt jedes Detail eines Levels manuell zu zeichnen, 
# kannst du kleine Kacheln (“Tiles”) verwenden, um komplexe Welten zu bauen. 
# Jede Kachel repräsentiert dabei ein bestimmtes Spielelement wie Boden, Wand, 
# Hindernis oder Sammelobjekt.

# In Arcade kannst du Tilemaps flexibel einsetzen, um Strukturen und Hindernisse 
# zu definieren. In diesem Kapitel lernst du:
#   - Wie Tilemaps aufgebaut sind.
#
#   - Wie man sie erstellt und im Spiel anzeigt.
#
#   - Wie man verschiedene Elemente wie Wände, Münzen oder Plattformen in einer 
#     Tilemap verwaltet.



# _________________________________
#                                 /
# Grundprinzip von Tilemaps      (
# ________________________________\
#
# Eine Tilemap besteht aus:
#   1.  Tiles: Kleine Grafiken, die verschiedene Elemente wie Gras, Stein oder 
#       Wasser repräsentieren.
# 
#   2.  Tilemap-Grid: Ein Raster, das definiert, wo welche Kachel angezeigt wird. 
#       Jede Position im Raster enthält eine Kachel-ID.
#   
# Beispiel für eine einfache Tilemap:
#   0 0 0 0 0 0
#   0 2 0 0 3 0
#   1 1 1 1 1 1
#
#   1: Repräsentiert z. B. den Boden
#   2: Repräsentiert eine Sammelmünze.
#   3: Repräsentiert eine Plattform.




# _________________________________
#                                 /
# Tilemap in Arcade umsetzen     (
# ________________________________\
#
#
# 1. Aufbau der Datenstruktur
# ---------------------------
#
# In Arcade definieren wir die Tilemap als eine Liste von Listen (2D-Array). 
# Jede Zahl im Array steht für eine Kachel.
#
#   tilemap = [
#       [0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 1, 0, 0],
#       [0, 2, 1, 1, 3, 0],
#       [1, 1, 1, 1, 1, 1]
#   ]
#
#
# 2. Zuordnung der Tile-IDs
# -------------------------
# Mit einer Python-Datenstruktur verknüpfen wir jede Tile-ID mit einem Bild und 
# einer Sprite-Liste.
#
#   tiles = {
#       0: None,  # Leer (keine Kachel)
#       1: ":resources:images/tiles/grassMid.png",  # Boden
#       2: ":resources:images/items/coinGold.png",  # Münze
#       3: ":resources:images/tiles/spikes.png"    # Falle
#   }   
#
# 3. Tilemap anzeigen
# -------------------
# Um die Tilemap anzuzeigen, iterieren wir über das Tilemap-Array. Jede Kachel 
# wird anhand ihrer ID in der entsprechenden Sprite-Liste gespeichert und an der 
# passenden Position gezeichnet.
#

import arcade

class TilemapDemo(arcade.Window):

    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)
        
        self.tile_size = 64  # Größe der Kacheln in Pixel

        self.tilemap = []  # Die Tilemap-Daten
        self.tiles = {}  # Zuordnung der Tile-IDs zu Grafiken

        self.background_list = arcade.SpriteList()  # Liste für den Hintergrund
        self.wall_list = arcade.SpriteList()  # Liste für Wände
        self.item_list = arcade.SpriteList()  # Liste für Objekte
        
        
    # Bereitet die Tilemap-Daten und Sprites vor.
    def setup(self):

        # Zuordnung von Tile-IDs zu Grafiken
        self.tiles = {
            0: None,  # Leer (keine Kachel)
            1: [":resources:images/tiles/grassMid.png", self.wall_list],  # Boden
            2: [":resources:images/items/coinGold.png", self.item_list],  # Münze
            3: [":resources:images/tiles/spikes.png", self.wall_list]  # Falle
        }
        
        # Tilemap
        self.tilemap = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 1, 1, 3, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
        ]

        self.update_SpriteLists(self.tilemap)


    def update_SpriteLists(self, tilemap):
        self.background_list.clear()
        self.wall_list.clear()
        self.item_list.clear()
        
        # Tilemap durchlaufen und Sprites erstellen
        for row_index, row in enumerate(tilemap):
            for col_index, tile_id in enumerate(row):
                if tile_id != 0:  # Nur nicht-leere Kacheln verarbeiten
                    x = col_index * self.tile_size + self.tile_size // 2
                    y = (len(self.tilemap) - 1 - row_index) * self.tile_size + self.tile_size // 2

                    tile = arcade.Sprite(self.tiles[tile_id][0], scale=0.5)
                    tile.center_x = x
                    tile.center_y = y
                    
                    self.tiles[tile_id][1].append(tile)


    # Zeichnet die Tilemap.
    def on_draw(self):
        arcade.start_render()
        self.background_list.draw()
        self.wall_list.draw()
        self.item_list.draw()


# Hauptprogramm
window = TilemapDemo(title="Tilemap Demo")
window.setup()
arcade.run()




# _________________________________
#                                 /
# Zusammenfassung                (
# ________________________________\

# Tilemaps sind eine zentrale Technik für das Level-Design in 2D-Spielen.
# Mit Arcade kannst du:
#
# - Komplexe Spielwelten durch ein einfaches Raster definieren.
#
# - Jedes Element einer Kachel (Tile) zuordnen, z. B. Boden, Münzen oder Hindernisse.
#
# - Sprite-Listen verwenden, um die Objekte der Tilemap effizient zu verwalten und anzuzeigen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erweitere die Tilemap und das zugehörige Dictionary, um zwei neue Kacheln zu 
# implementieren. Eine der neuen Kacheln repräsentiert Wasser und soll die ID 4 haben. 
# Die zweite Kachel repräsentiert einen Stein, der mit der ID 5 verknüpft ist. 
# Nachdem du diese Kacheln hinzugefügt hast, integriere sie in die bestehende Tilemap, 
# sodass sie korrekt in der Spielwelt angezeigt werden können. 


# Füge hier deine Lösung ein.





# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Verändere das Programm so, dass die Tilemap während des Spiels geändert wird.
# Zum Beispiel  wird eine Plattform (ID 1) durch eine Falle (ID 3) ersetzt, wenn 
# eine Taste gedrückt wird.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Füge ein System hinzu, bei dem Münzen verschwinden, wenn sie mit der 
# Spielfigur kollidieren. Verwende dazu die Methode `arcade.check_for_collision_with_list()`.


# Füge hier deine Lösung ein.




#       Jetzt kannst du ganze Landschaften erstellen. 
#
#                                           |
#                                         \ _ /
#                                       -= (_) =-
#      .\/.                               /   \
#   .\\//o\\                      ,\/.      |              ,~
#   //o\\|,\/.   ,.,.,   ,\/.  ,\//o\\                     |\
#     |  |//o\  /###/#\  //o\  /o\\|                      /| \
#   ^^|^^|^~|^^^|' '|:|^^^|^^^^^|^^|^^^""""""""("~~~~~~~~/_|__\~~~~~~~~~~
#    .|'' . |  '''""'"''. |`===`|''  '"" "" " (" ~~~~ ~ ~======~~  ~~ ~
#    jgs^^   ^^^ ^ ^^^ ^^^^ ^^^ ^^ ^^ "" """( " ~~~~~~ ~~~~~  ~~~ ~
#
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
# Aufgabe 1  /
# __________/
#
# Erweitere die Tilemap und das zugehörige Dictionary, um zwei neue Kacheln zu 
# implementieren. Eine der neuen Kacheln repräsentiert Wasser und soll die ID 4 haben. 
# Die zweite Kachel repräsentiert einen Stein, der mit der ID 5 verknüpft ist. 
# Nachdem du diese Kacheln hinzugefügt hast, integriere sie in die bestehende Tilemap, 
# sodass sie korrekt in der Spielwelt angezeigt werden können. 

'''
class TilemapDemo(arcade.Window):
    
    ...

    def setup(self):

        # Zuordnung von Tile-IDs zu Grafiken
        self.tiles = {
            0: None,  # Leer (keine Kachel)
            1: [":resources:images/tiles/grassMid.png", self.wall_list],  # Boden
            2: [":resources:images/items/coinGold.png", self.item_list],  # Münze
            3: [":resources:images/tiles/spikes.png", self.wall_list],  # Falle
            4: [":resources:images/tiles/waterTop_low.png", self.background_list],  # Falle
            5: [":resources:images/tiles/rock.png", self.background_list]  # Falle
                
        }
        
        # Tilemap
        self.tilemap = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 1, 1, 3, 0, 0, 0, 0, 0, 5, 0],
            [1, 1, 1, 1, 1, 1, 4, 4, 4, 1, 1, 1]
        ]

'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Verändere das Programm so, dass die Tilemap während des Spiels geändert wird.
# Zum Beispiel  wird eine Plattform (ID 1) durch eine Falle (ID 3) ersetzt, wenn 
# eine Taste gedrückt wird.

'''
import arcade

class TilemapDemo(arcade.Window):

    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)
        
        self.tile_size = 64  # Größe der Kacheln in Pixel
        
        self.tilemap = []  # Die Tilemap-Daten
        self.tiles = {}  # Zuordnung der Tile-IDs zu Grafiken

        self.background_list = arcade.SpriteList()  # Liste für den Hintergrund
        self.wall_list = arcade.SpriteList()  # Liste für Wände
        self.item_list = arcade.SpriteList()  # Liste für Objekte
        
        
    # Bereitet die Tilemap-Daten und Sprites vor.
    def setup(self):

        # Zuordnung von Tile-IDs zu Grafiken
        self.tiles = {
            0: None,  # Leer (keine Kachel)
            1: [":resources:images/tiles/grassMid.png", self.wall_list],  # Boden
            2: [":resources:images/items/coinGold.png", self.item_list],  # Münze
            3: [":resources:images/tiles/spikes.png", self.wall_list]  # Falle
        }
        
        # Tilemap
        self.tilemap = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 1, 1, 3, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
        ]

        self.update_SpriteLists(self.tilemap)
    
        
        
    def update_SpriteLists(self, tilemap):
        self.background_list.clear()
        self.wall_list.clear()
        self.item_list.clear()
        
        # Tilemap durchlaufen und Sprites erstellen
        for row_index, row in enumerate(tilemap):
            for col_index, tile_id in enumerate(row):
                if tile_id != 0:  # Nur nicht-leere Kacheln verarbeiten
                    x = col_index * self.tile_size + self.tile_size // 2
                    y = (len(self.tilemap) - 1 - row_index) * self.tile_size + self.tile_size // 2

                    tile = arcade.Sprite(self.tiles[tile_id][0], scale=0.5)
                    tile.center_x = x
                    tile.center_y = y
                    
                    self.tiles[tile_id][1].append(tile)



    # Zeichnet die Tilemap.
    def on_draw(self):
        arcade.start_render()
        
        self.background_list.draw()
        self.wall_list.draw()
        self.item_list.draw()
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            
            self.tilemap[3][3] = 3
            
            print()
            self.update_SpriteLists(self.tilemap)


# Hauptprogramm
window = TilemapDemo(title="Tilemap Demo")
window.setup()
arcade.run()
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Füge ein System hinzu, bei dem Münzen verschwinden, wenn sie mit der 
# Spielfigur kollidieren. Verwende dazu die Methode `arcade.check_for_collision_with_list()`.


'''
import arcade

class TilemapDemo(arcade.Window):
    """
    Eine Demo-Anwendung zur Verwendung von Tilemaps und Sprites mit Arcade.
    Die Tilemap definiert die Spielumgebung, und die Spielfigur kann mit Objekten interagieren.
    """
    

    def __init__(self, width=800, height=600, title=""):
        """
        Initialisiert das Fenster und die grundlegenden Variablen.
        """
        super().__init__(width=width, height=height, title=title)
        
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)  # Hintergrundfarbe setzen
        
        self.tile_size = 64  # Größe jeder Kachel in Pixel

        self.tilemap = []  # Die Tilemap-Daten (als 2D-Array)
        self.tiles = {}  # Zuordnung der Tile-IDs zu Grafiken und Sprite-Listen
        
        self.player = None  # Die Spielfigur

        # Sprite-Listen für verschiedene Elemente
        self.background_list = arcade.SpriteList()  # Hintergrund-Sprites
        self.wall_list = arcade.SpriteList()  # Wände
        self.item_list = arcade.SpriteList()  # Sammelbare Objekte (z. B. Münzen)
    

    def setup(self):
        """
        Initialisiert die Spielfigur, die Tilemap und die Physik-Engine.
        """
        # Spielfigur erstellen und ihre Startposition setzen
        self.player = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", scale=0.5)
        self.player.center_x = 100
        self.player.center_y = 200

        # Zuordnung von Tile-IDs zu Grafiken und Sprite-Listen
        self.tiles = {
            0: None,  # Leer (keine Kachel)
            1: [":resources:images/tiles/grassMid.png", self.wall_list],  # Boden
            2: [":resources:images/items/coinGold.png", self.item_list],  # Münze
            3: [":resources:images/tiles/spikes.png", self.wall_list]  # Falle
        }
        
        # Definiert die Tilemap als 2D-Array
        self.tilemap = [
            [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 2],
            [0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 3, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
        ]

        # Generiert die Sprite-Listen basierend auf der Tilemap
        self.update_SpriteLists(self.tilemap)
        
        # Initialisiert die Physik-Engine mit Schwerkraft und Kollisionswänden
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, gravity_constant=0.5, walls=self.wall_list)


    def update_SpriteLists(self, tilemap):
        """
        Durchläuft die Tilemap-Daten und erstellt die zugehörigen Sprites.
        """
        # Löscht bestehende Sprite-Listen, um sie neu zu erstellen
        self.background_list.clear()
        self.wall_list.clear()
        self.item_list.clear()
        
        for row_index, row in enumerate(tilemap):  # Iteriert über die Zeilen der Tilemap
            for col_index, tile_id in enumerate(row):  # Iteriert über die Spalten
                if tile_id != 0:  # Nur nicht-leere Kacheln verarbeiten
                    # Berechnet die Position der Kachel im Fenster
                    x = col_index * self.tile_size + self.tile_size // 2
                    y = (len(self.tilemap) - 1 - row_index) * self.tile_size + self.tile_size // 2

                    # Erstellt das entsprechende Sprite basierend auf der Tile-ID
                    tile = arcade.Sprite(self.tiles[tile_id][0], scale=0.5)
                    tile.center_x = x
                    tile.center_y = y
                    tile.id = tile_id
                    
                    # Fügt das Sprite der zugehörigen Liste hinzu
                    self.tiles[tile_id][1].append(tile)


    def on_draw(self):
        """
        Zeichnet alle Sprites (Hintergrund, Wände, Objekte und Spieler).
        """
        arcade.start_render()  # Startet den Renderprozess
        self.background_list.draw()  # Zeichnet Hintergrund-Sprites
        self.wall_list.draw()  # Zeichnet Wände
        self.item_list.draw()  # Zeichnet sammelbare Objekte
        self.player.draw()  # Zeichnet die Spielfigur

        
    def on_update(self, delta_time):
        """
        Aktualisiert die Spielfigur und überprüft Kollisionen mit Objekten.
        """
        self.physics_engine.update()  # Aktualisiert die Physik der Spielfigur

        # Überprüft Kollisionen zwischen der Spielfigur und den Objekten
        for item in arcade.check_for_collision_with_list(self.player, self.item_list):
            if item.id == 2:  # Wenn das Objekt eine Münze ist
                item.remove_from_sprite_lists()  # Entfernt die Münze aus den Sprite-Listen


    def on_key_press(self, key, modifiers):
        """
        Reagiert auf Tastendrücke, um die Spielfigur zu bewegen.
        """
        if key == arcade.key.UP and self.physics_engine.can_jump():
            self.player.change_y = 12  # Springt nach oben
        elif key == arcade.key.LEFT:
            self.player.change_x = -5  # Bewegt sich nach links
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5  # Bewegt sich nach rechts


    def on_key_release(self, key, modifiers):
        """
        Stoppt die Bewegung der Spielfigur, wenn eine Bewegungstaste losgelassen wird.
        """
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0  # Stoppt die horizontale Bewegung


# Hauptprogramm
window = TilemapDemo(title="Tilemap Demo")  # Erstellt das Fenster
window.setup()  # Initialisiert die Spielfigur und die Tilemap
arcade.run()  # Startet die Arcade-Game-Loop

'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><



