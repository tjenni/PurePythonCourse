#              _______________________________
#       ______|                               |_____
#       \     |   12.11 SPIELER ANIMIEREN     |    /
#        )    |_______________________________|   (
#       /________)                        (________\     30.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# Eine animierte Spielfigur ist entscheidend für die Dynamik und das immersive 
# Erlebnis eines Spiels. Anstelle von statischen Bildern verwenden Animationen 
# mehrere Frames, die je nach Spieleraktion angezeigt werden, um realistische 
# Bewegungen zu erzeugen.
#
# In diesem Kapitel lernst du:
# - Wie Animationen für eine Spielfigur erstellt und verwaltet werden.
#
# - Wie die Animationen basierend auf Spieleraktionen wie Laufen, Springen 
#   oder Stehen dynamisch angepasst werden.
#
# - Wie Texturen effizient organisiert und geladen werden, um Animationen 
#   zu optimieren.
#
# Diese Grundlagen bilden die Basis, um komplexere Animationen in Spielen zu integrieren.


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
        self.is_attacking = False

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
        
        # Nur bei bestimmten Frames die Textur wechseln
        if self.frame == 0:
            self.texture_idx += 1

        # Blickrichtung setzen
        if self.change_x < 0:
            self.facing = Character.LEFT
        elif self.change_x > 0:
            self.facing = Character.RIGHT
        
        if self.is_on_ladder:
            self.state = Character.CLIMB
            
            if self.change_y == 0:
                self.texture_idx = 0
           
        elif not self.can_jump:
            self.state = Character.JUMP
        
        elif self.is_attacking:
            self.state = Character.ATTTACK
        
        elif self.change_x == 0:
            self.state = Character.IDLE
        else:
            self.state = Character.WALK
        
        self.update_texture()  # Textur aktualisieren



# Hauptfenster für das Spiel mit der animierten Spielfigur
class AnimatedPlayer(arcade.Window):
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)
        self.player = None  # Spielfigur
        self.walls = None  # Liste der Wände
        self.ladders = None  # Liste der Leitern
        self.physics_engine = None  # Physik-Engine
        self.keys = collections.defaultdict(lambda: False)  # Tastenstatus


    # Initialisiert die Spielumgebung
    def setup(self):
        # Wände (Boden) erstellen
        self.walls = arcade.SpriteList()
        for x in range(0, 1600, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=0.5)
            wall.center_x, wall.center_y = x, 32
            self.walls.append(wall)
        
        # Schräge erstellen
        for x in range(0, 512, 128):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=0.5)
            wall.center_x, wall.center_y = 256 + x, 32 + x
            self.walls.append(wall)
        
        # Leitern erstellen
        self.ladders = arcade.SpriteList()
        for y in range(0, 384, 64):
            ladder = arcade.Sprite(":resources:images/tiles/ladderMid.png", scale=0.5)
            ladder.center_x, ladder.center_y = 704, 96 + y
            self.ladders.append(ladder)
        
        # Spielfigur initialisieren
        self.player = Character("_assets/12.11/femaleAdventurer.xml", scale=0.3)
        self.player.center_x, self.player.center_y = 100, 100
        
        # Physik-Engine konfigurieren
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player, gravity_constant=0.5, walls=self.walls, ladders=self.ladders
        )
        self.player.register_physics_engine(self.physics_engine)  # Physik-Engine der Spielfigur hinzufügen


    # Zeichnet die Spielumgebung und die Spielfigur
    def on_draw(self):
        arcade.start_render()  # Zeichenbereich leeren
        self.walls.draw()  # Wände zeichnen
        self.ladders.draw()  # Leitern zeichnen
        self.player.draw()  # Spielfigur zeichnen


    # Aktualisiert den Spielzustand und die Animation der Spielfigur
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

        # Aktualisiere die Animation der Spielfigur
        self.player.update_animation(delta_time)


    # Verarbeitet Tastendrücke
    def on_key_press(self, key, modifiers):
        self.keys[key] = True  # Markiere die Taste als gedrückt
        if key == arcade.key.UP:  # Sprungaktion
            self.player.jump()


    # Verarbeitet das Loslassen von Tasten
    def on_key_release(self, key, modifiers):
        self.keys[key] = False  # Markiere die Taste als losgelassen


# Hauptprogramm
if __name__ == "__main__":
    window = AnimatedPlayer(title="Player Animation")  # Fenster erstellen
    window.setup()  # Spielumgebung initialisieren
    arcade.run()  # Spiel starten



# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# In diesem Kapitel hast du gelernt, wie man eine Spielfigur animiert und die 
# Animationen auf Spieleraktionen abstimmt. Hier die wichtigsten Punkte:
#
# 1. Animationen basieren auf verschiedenen Texturen:
#    - Jede Aktion (z. B. Laufen, Springen, Klettern) hat eine eigene Gruppe 
#      von Texturen.
#    - Texturen werden sequentiell durchlaufen, um die Animation zu erzeugen.
#
# 2. Dynamische Animation:
#    - Animationen passen sich automatisch an den Zustand der Spielfigur an 
#      (z. B. Stehen, Springen, auf einer Leiter sein).
#
# 3. Physik und Bewegung:
#    - Die Physik-Engine wurde integriert, um realistische Bewegungen und 
#      Interaktionen mit Wänden, Leitern und der Schwerkraft zu ermöglichen.
#
# 4. Texturverwaltung:
#    - Texturen wurden mit einem flexiblen Schema organisiert und geladen, 
#      einschließlich horizontal gespiegelter Varianten.
#
# Mit diesen Grundlagen kannst du Animationen in deinem Spiel erweitern und 
# anpassen, z. B. durch Hinzufügen neuer Bewegungen oder Effekte.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Füge der Spielfigur eine neue Animation hinzu: eine "Schlag"-Animation. 
# Erstelle einen neuen Zustand, in dem der Spieler einen Schlag ausführt, wenn 
# die Leertaste gedrückt wird. Passe die Animationen an.
#

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine neue Spielfigur mit einer anderen Animation. Lade dafür 
# Texturen eines anderen Charakters und teste die Animationen für Laufen, 
# Springen und Stehen.
#
# Hinweis: Verwende die `Character`-Klasse, aber initialisiere sie mit 
# einem anderen `textures_path`.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Füge eine Animationssequenz hinzu, die abläuft, wenn der Spieler hinunterfällt. 
# Lade eine spezielle Animation für den "Fall"-Zustand und wechsle in diesen Zustand, 
# wenn die Spielfigur nach unten fällt.

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
# Aufgabe 1  /
# __________/
#
# Füge der Spielfigur eine neue Animation hinzu: eine "Schlag"-Animation. 
# Erstelle einen neuen Zustand, in dem der Spieler einen Schlag ausführt, wenn 
# die Leertaste gedrückt wird. Lade die entsprechenden Texturen und passe 
# die Animationen an.
#
# Hinweis: Erweitere die `Character`-Klasse und die Methode `update_animation()`.

'''

class Character(arcade.Sprite):
    
    ...
    
    ATTACK = 'attack'
    ...
    
    def __init__(self, textures_path, scale=1):
        ...

        self.is_attacking = False  # Gibt an, ob die Spielfigur zuschlägt
 

    ...


    # Aktualisiert die Animation der Spielfigur basierend auf ihrem Zustand (Laufen, Springen, Klettern, Stehen).
    def update_animation(self, delta_time):
        ...

        # Animation für die Leiter
        ...
        
        # Animation für Schlagen
        if self.is_attacking:
            self.state = Character.ATTTACK
        
        ...



class AnimatedPlayerDemo(arcade.Window):

    ...


    # Verarbeitet Tastendrücke.
    def on_key_press(self, key, modifiers):
        ...

        elif key == arcade.key.SPACE:
            self.player.is_attacking = True


    # Verarbeitet das Loslassen von Tasten.
    def on_key_release(self, key, modifiers):
        ...

        elif key == arcade.key.SPACE:
            self.player.is_attacking = False

'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine neue Spielfigur mit einer anderen Animation. Lade dafür 
# Texturen eines anderen Charakters und teste die Animationen für Laufen, 
# Springen und Stehen.
#
# Hinweis: Verwende die `Character`-Klasse, aber initialisiere sie mit 
# einem anderen `textures_path`.

'''
        self.player = Character("_assets/12.11/robot.xml", scale=0.3)
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Füge eine Animationssequenz hinzu, die abläuft, wenn der Spieler hinunterfällt. 
# Lade eine spezielle Animation für den "Fall"-Zustand und wechsle in diesen Zustand, 
# wenn die Spielfigur nach unten fällt.


'''

import arcade


class Character(arcade.Sprite):

    ...
    
    FALL = "fall"
    ...
    
    def __init__(self, textures_path, scale=1):
        ...
 
        self.n_textures = {
            Character.IDLE : 1,
            Character.JUMP : 1,
            Character.FALL : 1,
            Character.WALK : 8,
            Character.CLIMB : 2
        }

    def update_animation(self, delta_time):
        ...
        
        # Animation für Schlagen
        ...
        
        # Animation fürs Fallen
        if self.change_y < 0:
            self.state = Character.FALL
        
        ...



'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><



