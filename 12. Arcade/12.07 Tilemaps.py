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
#       1: [":resources:images/tiles/grassMid.png", "Walls"]  # Boden
#       2: [":resources:images/items/coinGold.png", "Items"]  # Münze
#       3: [":resources:images/tiles/spikes.png", "Trap"]    # Falle
#   }   
#
# 3. Tilemap anzeigen
# -------------------
# Um die Tilemap anzuzeigen, iterieren wir über das Tilemap-Array. Jede Kachel 
# wird anhand ihrer ID in der entsprechenden Sprite-Liste gespeichert und an der 
# passenden Position gezeichnet.


# _________________________________
#                                 /
# Beispiel                       (
# ________________________________\

import arcade

# Eine Demo-Klasse für die Verwendung von Tilemaps in einem Arcade-Spiel.
# Dieses Programm zeigt, wie Kacheln hinzugefügt, entfernt und gezeichnet werden.
class TilemapDemo(arcade.Window):
    
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        # Hintergrundfarbe des Fensters setzen
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)
        
        # Größe jeder Kachel in Pixel
        self.tile_size = 64
        self.sprite_lists = None  # Sammlung von Sprite-Listen für unterschiedliche Kacheltypen
        self.tiles = None  # Zuordnung von Tile-IDs zu Grafiken und Typen
        self.tilemap = None  # 2D-Liste, die die Tile-IDs speichert
        

    # Bereitet die Tilemap-Daten, Zuordnungen und Sprite-Listen vor. 
    def setup(self):
        
        # Initialisiere die Sprite-Listen für verschiedene Kacheltypen
        self.sprite_lists = {
            "Walls": arcade.SpriteList(),  # Wände
            "Items": arcade.SpriteList(),  # Sammelbare Objekte
            "Traps": arcade.SpriteList()   # Fallen
        }

        # Zuordnung von Tile-IDs zu Grafiken und Sprite-Listen
        self.tiles = {
            0: None,  # Leere Kachel
            1: [":resources:images/tiles/grassMid.png", "Walls"],  # Boden
            2: [":resources:images/items/coinGold.png", "Items"],  # Münze
            3: [":resources:images/tiles/spikes.png", "Traps"]     # Falle
        }
        
        # Definition der Tilemap als 2D-Liste
        self.tilemap = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 1, 1, 3, 0, 0, 0, 3, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0]
        ]

        # Sprites aus der Tilemap erstellen
        self.create_sprite_lists(self.tilemap)
        
        # Beispiel: Eine Kachel entfernen und eine neue hinzufügen
        self.remove_tile(4, 4, 3)  # Entferne die Falle an Position (4, 4)
        self.add_tile(4, 4, 2)     # Füge eine Münze an derselben Position hinzu


    # Entfernt eine Kachel basierend auf ihrer Position und ID.
    def remove_tile(self, column, row, tile_id):

        if self.tiles[tile_id] is None:  # Keine Aktion, wenn die ID leer ist
            return
        
        # Ermittele den Typ der Kachel (z. B. "Walls")
        tile_type = self.tiles[tile_id][1]
        
        # Entferne das Sprite an der angegebenen Position
        for sprite in self.sprite_lists[tile_type]:
            if sprite.id == tile_id and sprite.column == column and sprite.row == row:
                sprite.remove_from_sprite_lists()
                break


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
        sprite.center_y = (len(self.tilemap) - 1 - row) * self.tile_size + self.tile_size // 2
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


    # Zeichnet alle Sprite-Listen auf den Bildschirm.
    def on_draw(self):
        
        arcade.start_render()  # Bildschirminhalt vorbereiten
        
        # Zeichne alle Sprite-Listen
        for sprite_list in self.sprite_lists.values():
            sprite_list.draw()


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

        # Initialisiere die Sprite-Listen für verschiedene Kacheltypen
        self.sprite_lists = {
            "Walls": arcade.SpriteList(),  # Wände
            "Items": arcade.SpriteList(),  # Sammelbare Objekte
            "Traps": arcade.SpriteList(),  # Fallen
            "Water": arcade.SpriteList()   # Wasser
        }

        # Zuordnung von Tile-IDs zu Grafiken
        self.tiles = {
            0: None,  # Leer (keine Kachel)
            1: [":resources:images/tiles/grassMid.png", "Walls"],  # Boden
            2: [":resources:images/items/coinGold.png", "Items"],  # Münze
            3: [":resources:images/tiles/spikes.png", "Traps"],  # Falle
            4: [":resources:images/tiles/waterTop_low.png", "Water"],  # Falle
            5: [":resources:images/tiles/rock.png", "Items"]  # Falle
                
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

    ...

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.remove_tile(3, 3, 1) 
            self.add_tile(3, 3, 3) 
    
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
    
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)  # Hintergrundfarbe setzen
        
        self.tilemap = []  # Die Tilemap-Daten (als 2D-Array)
        self.tiles = {}  # Zuordnung der Tile-IDs zu Grafiken und Sprite-Listen
        
        self.player = None  # Die Spielfigur

        self.tile_size = 64  # Größe jeder Kachel in Pixel
        self.tilemap = None  # 2D-Liste, die die Tile-IDs speichert
        self.tiles = None  # Zuordnung von Tile-IDs zu Grafiken und Typen
        self.sprite_lists = None  # Sammlung von Sprite-Listen für unterschiedliche Kacheltypen
    

    def setup(self):
        """
        Initialisiert die Spielfigur, die Tilemap und die Physik-Engine.
        """
        # Spielfigur erstellen und ihre Startposition setzen
        self.player = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", scale=0.5)
        self.player.center_x = 100
        self.player.center_y = 200
        
        # Initialisiere die Sprite-Listen für verschiedene Kacheltypen
        self.sprite_lists = {
            "Walls": arcade.SpriteList(),  # Wände
            "Coins": arcade.SpriteList(),  # Münzen
        }

        # Zuordnung von Tile-IDs zu Grafiken und Sprite-Listen
        self.tiles = {
            0: None,  # Leer (keine Kachel)
            1: [":resources:images/tiles/grassMid.png", "Walls"],  # Boden
            2: [":resources:images/items/coinGold.png", "Coins"],  # Münze
            3: [":resources:images/tiles/spikes.png", "Walls"]  # Falle
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
        self.create_sprite_lists(self.tilemap)
        
        # Initialisiert die Physik-Engine mit Schwerkraft und Kollisionswänden
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, gravity_constant=0.5, walls=self.sprite_lists["Walls"])


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
        sprite.center_y = (len(self.tilemap) - 1 - row) * self.tile_size + self.tile_size // 2
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

               
    def on_draw(self):
        arcade.start_render()
        
        # Zeichne alle Sprite-Listen
        for sprite_list in self.sprite_lists.values():
            sprite_list.draw()
        
        self.player.draw()  # Zeichnet die Spielfigur


    # Aktualisiert die Spielfigur und überprüft Kollisionen mit Objekten.
    def on_update(self, delta_time):
        self.physics_engine.update()  # Aktualisiert die Physik der Spielfigur

        # Überprüft Kollisionen zwischen der Spielfigur und den Objekten
        for item in arcade.check_for_collision_with_list(self.player, self.sprite_lists["Coins"]):
            item.remove_from_sprite_lists()  # Entfernt die Münze aus den Sprite-Listen


    # Reagiert auf Tastendrücke, um die Spielfigur zu bewegen.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP and self.physics_engine.can_jump():
            self.player.change_y = 12  # Springt nach oben
        elif key == arcade.key.LEFT:
            self.player.change_x = -5  # Bewegt sich nach links
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5  # Bewegt sich nach rechts


    # Stoppt die Bewegung der Spielfigur, wenn eine Bewegungstaste losgelassen wird.
    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0  # Stoppt die horizontale Bewegung


# Hauptprogramm
window = TilemapDemo(title="Tilemap Demo")  # Erstellt das Fenster
window.setup()  # Initialisiert die Spielfigur und die Tilemap
arcade.run()  # Startet die Arcade-Game-Loop
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><




