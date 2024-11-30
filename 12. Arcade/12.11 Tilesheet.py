#              _______________________
#       ______|                       |_____
#       \     |   12.11 TILESHEET     |    /
#        )    |_______________________|   (
#       /________)                (________\     30.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Tilesheets sind ein wesentlicher Bestandteil der Spieleentwicklung. Sie bieten 
# eine effiziente Möglichkeit, viele kleine Grafiken in einer einzigen Bilddatei 
# zu speichern. Durch die Verwendung von XML-Dateien können die Position und 
# Grösse einzelner Subtexturen im Tilesheet präzise definiert werden. Dieses 
# Kapitel zeigt, wie Tilesheets mit Python und der Arcade-Bibliothek geladen 
# und visualisiert werden können.

# In diesem Kapitel lernst du:
# - Wie du ein Tilesheet analysieren und die Texturen in Python extrahieren kansnt.
# 
# - Wie du mit Arcade die geladenen Texturen in einem Raster darstellen.
# 
# - Den Nutzen von Texturpaaren (normal und gespiegelt) für Charakteranimationen.

# Freie Grafiken und Spielelemente findest du zum Beispiel unter:
#
# - https://opengameart.org
#
# - https://kenney.nl


import arcade
import xml.dom.minidom
import os

# Klasse zur Verwaltung eines Tilesheets und zum Laden von Texturen
class Tilesheet():
    # Lädt ein Tilesheet basierend auf einer XML-Datei und speichert die Texturen.
    def __init__(self, xml_file, load_pair=True):
        self.textures = {}  # Dictionary für die geladenen Texturen
        
        try:
            # XML-Dokument parsen
            document = xml.dom.minidom.parse(xml_file)
        except Exception as e:
            raise FileNotFoundError(f"Die Datei {xml_file} konnte nicht geladen werden. Fehler: {e}")
        
        # Hauptknoten des TextureAtlas
        textureAtlas = document.getElementsByTagName("TextureAtlas")[0]
        subTextures = textureAtlas.getElementsByTagName("SubTexture")
        
        image_file = os.path.join(os.path.dirname(xml_file), textureAtlas.getAttribute('imagePath')) 
        
        # Iteriere über alle SubTexturen im Tilesheet
        for subTexture in subTextures:
            name = subTexture.getAttribute('name')  # Name der Textur
            x = int(subTexture.getAttribute('x'))
            y = int(subTexture.getAttribute('y'))
            width = int(subTexture.getAttribute('width'))
            height = int(subTexture.getAttribute('height'))
            
            # Lade entweder nur die normale Textur oder ein Texturpaar
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
            arcade.load_texture(path, x, y, width, height),
            arcade.load_texture(path, x, y, width, height, flipped_horizontally=True)
        ]



# Klasse zur Darstellung eines Charakters mit Texturen aus einem Tilesheet
class Character(arcade.Sprite):
    def __init__(self, xml_file, scale=1):
        super().__init__()
        self.scale = scale  # Skalierung des Sprites
        self.tilesheet = Tilesheet(xml_file).textures  # Lade das Tilesheet



# Demo-Anwendung zur Anzeige aller Texturen eines Tilesheets
class TilesheetDemo(arcade.Window):

    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)  # Setze den Hintergrund
        
        self.player = None  # Platzhalter für die Spielfigur


    # Initialisiert die Spielfigur und lädt die Texturen.
    def setup(self):
        self.player = Character("_assets/12.11/femaleAdventurer.xml", scale=0.3)


    # Zeichnet alle Texturen des Tilesheets in einem Raster.
    def on_draw(self):
        arcade.start_render()
        
        raster_size = 80
        
        self.player.center_x = raster_size  # Startposition X
        self.player.center_y = self.height - raster_size  # Startposition Y
        
        for id, tile in self.player.tilesheet.items():
            self.player.texture = tile[0]  # Lade die normale Textur
            self.player.draw()  # Zeichne die Spielfigur
            
            self.player.center_x += raster_size  # Verschiebe die Position horizontal
            
            # Brich die Zeile um, wenn die Fensterbreite überschritten wird
            if self.player.center_x > self.width - raster_size:
                self.player.center_x = raster_size
                self.player.center_y -= raster_size  # Verschiebe die Position vertikal


# Starte die Anwendung
window = TilesheetDemo(title="Tilesheet Demo")
window.setup()
arcade.run()




# ___________________
#                   /
# Zusammenfassung  (
# __________________\
#
#
# In diesem Kapitel hast du gelernt:
#
# 1.  Tilesheets laden: Mit der Klasse Tilesheet können Sie eine XML-Datei 
#     parsen und die definierten Subtexturen extrahieren.
#  
# 2.  Texturen darstellen: Die Klasse Character verwendet das Tilesheet, um 
#     Texturen für ein Arcade-Sprite zu verwalten.
#
# 3.  Rasterdarstellung: Die Demo-Anwendung zeigt, wie Sie alle geladenen 
#     Texturen in einem Raster anzeigen können.
#
# Die vorgestellte Methode bietet eine strukturierte und flexible Möglichkeit, 
# grosse Mengen von Grafiken effizient in Arcade-Spielen zu verwenden.




# ___________
#            \
# Aufgabe 1  /
# __________/
#
#
# Im Ordner `_assets/12.11` hat es weitere Tilesheets. Lade ein anderes 
# Tileset, indem du den Pfad in der Funktion setup() veränderst.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
#
# Ändere das Programm so, dass nur Texturen mit einem bestimmten Namen 
# angezeigt werden. Zeige nur Texturen an, deren Name mit `walk` beginnt.
#
# Hinweis: Verwende die Methode startswith() für String-Filterung.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#

# Modifiziere das Programm, sodass jede Textur sowohl in normaler als auch in 
# gespiegelter Form dargestellt wird.

# Hinweis: Nutze den Index tile[1] für die gespiegelte Textur.

# Füge hier deine Lösung ein.



#                        ____
#                   ____ \__ \
#                   \__ \__/ / __
#                   __/ ____ \ \ \    ____
#                  / __ \__ \ \/ / __ \__ \
#             ____ \ \ \__/ / __ \/ / __/ / __
#        ____ \__ \ \/ ____ \/ / __/ / __ \ \ \
#        \__ \__/ / __ \__ \__/ / __ \ \ \ \/
#        __/ ____ \ \ \__/ ____ \ \ \ \/ / __
#       / __ \__ \ \/ ____ \__ \ \/ / __ \/ /
#       \ \ \__/ / __ \__ \__/ / __ \ \ \__/          Kachelmuster.
#        \/ ____ \/ / __/ ____ \ \ \ \/ ____
#           \__ \__/ / __ \__ \ \/ / __ \__ \
#           __/ ____ \ \ \__/ / __ \/ / __/ / __
#          / __ \__ \ \/ ____ \/ / __/ / __ \/ /
#          \/ / __/ / __ \__ \__/ / __ \/ / __/
#          __/ / __ \ \ \__/ ____ \ \ \__/ / __
#         / __ \ \ \ \/ ____ \__ \ \/ ____ \/ /
#         \ \ \ \/ / __ \__ \__/ / __ \__ \__/
#          \/ / __ \/ / __/ ____ \ \ \__/
#             \ \ \__/ / __ \__ \ \/
#              \/      \ \ \__/ / __
#                       \/ ____ \/ /
#                          \__ \__/
#                          __/
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
#
# Im Ordner `_assets/12.11` hat es weitere Tilesheets. Lade ein anderes 
# Tileset, indem du den Pfad in der Funktion setup() veränderst.

'''
class TilesheetDemo(arcade.Window):
    ...
    def setup(self):
        # Lade ein anderes Tilesheet, z. B. ein Zombie-Tilesheet
        self.player = Character("_assets/12.11/zombie.xml", scale=0.3)
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
#
# Ändere das Programm so, dass nur Texturen mit einem bestimmten Namen 
# angezeigt werden. Zeige nur Texturen an, deren Name mit `walk` beginnt.
#
# Hinweis: Verwende die Methode startswith() für String-Filterung.

'''
class TilesheetDemo(arcade.Window):
    ...

    # Zeichnet alle Texturen des Tilesheets in einem Raster.
    def on_draw(self):
        
        ...

        for id, tile in self.player.tilesheet.items():
            
            if not id.startswith("walk"):
                continue
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#

# Modifiziere das Programm, sodass jede Textur sowohl in normaler als auch in 
# gespiegelter Form dargestellt wird.

# Hinweis: Nutze den Index tile[1] für die gespiegelte Textur.

'''
class TilesheetDemo(arcade.Window):
    ...

    # Zeichnet alle Texturen des Tilesheets in einem Raster.
    def on_draw(self):
        ...

        for id, tile in self.player.tilesheet.items():
            
            self.player.texture = tile[0]  # Lade die normale Textur
            self.player.draw()  # Zeichne die Spielfigur
            
            self.player.center_x += raster_size  # Verschiebe die Position horizontal
            
            self.player.texture = tile[1]  # Lade die normale Textur
            self.player.draw()  # Zeichne die Spielfigur
            
            self.player.center_x += raster_size  # Verschiebe die Position horizontal

            ...
            
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


