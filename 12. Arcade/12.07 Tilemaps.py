#              ____________________
#       ______|                    |_____
#       \     |    12.7 TILEMAPS   |    /
#        )    |____________________|   (
#       /________)             (________\     4.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

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
        self.wall_list = arcade.SpriteList()  # Liste für Wände
        self.coin_list = arcade.SpriteList()  # Liste für Münzen
        
        
    # Bereitet die Tilemap-Daten und Sprites vor.
    def setup(self):

        # Zuordnung von Tile-IDs zu Grafiken
        self.tiles = {
            0: None,  # Leer (keine Kachel)
            1: [":resources:images/tiles/grassMid.png", self.wall_list],  # Boden
            2: [":resources:images/items/coinGold.png", self.coin_list],  # Münze
            3: [":resources:images/tiles/spikes.png", self.wall_list]  # Falle
        }
        
        # Tilemap
        self.tilemap = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 2, 1, 1, 3, 0],
            [1, 1, 1, 1, 1, 1]
        ]

        # Tilemap durchlaufen und Sprites erstellen
        for row_index, row in enumerate(self.tilemap):
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
        self.wall_list.draw()
        self.coin_list.draw()


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
# Erweitere die Tilemap und das Dictionary, um zwei neue Kacheln hinzuzufügen:
#
# - Eine Wasser-Kachel (ID 4) mit der Farbe Blau.
#
# - Eine Star-Kachel (ID 5) mit der Farbe Gelb.
#
# Zeige diese Kacheln in der Tilemap an.


# Füge hier deine Lösung ein.





# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Funktion, die die Tilemap während des Spiels ändert.
# Zum Beispiel  wird eine Plattform (ID 1) durch eine Falle (ID 3) ersetzt, wenn 
# eine Taste gedrückt wird.


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


