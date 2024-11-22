#              _______________________________
#       ______|                               |_____
#       \     |   12.11 SPIELER ANIMIEREN     |    /
#        )    |_______________________________|   (
#       /________)                        (________\     21.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


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



# Diese Klasse repräsentiert eine animierte Spielfigur. 
# Sie verwaltet die Animationen für Laufen, Springen, Stehen und Klettern.
class Character(arcade.Sprite):
    
    def __init__(self, textures_path):
        super().__init__()

        self.n_walking_textures = 8  # Anzahl der Texturen für die Laufanimation
        self.n_climbing_textures = 2  # Anzahl der Texturen für die Kletteranimation
        
        self.face_direction = 0  # Richtung der Spielfigur (0: rechts, 1: links)
        self.can_jump = False  # Gibt an, ob die Spielfigur springen kann
        self.is_on_ladder = False  # Gibt an, ob die Spielfigur auf einer Leiter ist

        self.scale = 0.5  # Skalierung der Spielfigur
        
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


    # Aktualisiert die Animation der Spielfigur basierend auf ihrem Zustand (Laufen, Springen, Klettern, Stehen).
    def update_animation(self, delta_time):

        self.frame = (self.frame + 1) % self.animation_speed

        # Bestimme die Blickrichtung der Spielfigur
        if self.change_x < 0:
            self.face_direction = 1  # Blick nach links
        else:
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
        
        # Animation für Laufen
        if self.frame == 0:  # Aktualisiere die Textur nur bei bestimmten Frames
            self.current_texture += 1
        
        self.current_texture = self.current_texture % self.n_walking_textures
        self.texture = self.all_textures["walk"][self.current_texture][self.face_direction]



class AnimatedPlayerDemo(arcade.Window):

    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
    
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)

        self.player = None  # Spielfigur
        self.wall_list = None  # Liste der Wände (Boden)
        self.ladder_list = None  # Liste der Leitern
        self.physics_engine = None  # Physik-Engine
        self.keys = {"UP": False, "DOWN": False, "LEFT": False, "RIGHT": False}  # Zustände der Tasten


    # Initialisiert die Spielumgebung, die Leitern und die Spielfigur.
    def setup(self):

        # Erstelle die Wände (Boden)
        self.wall_list = arcade.SpriteList()
        for x in range(0, 1600, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=0.5)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        # Erstelle eine Schräge
        for x in range(0, 512, 128):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=0.5)
            wall.center_x = 256 + x
            wall.center_y = 32 + x
            self.wall_list.append(wall)

        # Erstelle Leitern
        self.ladder_list = arcade.SpriteList()
        for y in range(0, 384, 64):
            ladder = arcade.Sprite(":resources:images/tiles/ladderMid.png", scale=0.5)
            ladder.center_x = 704
            ladder.center_y = 96 + y
            self.ladder_list.append(ladder)

        # Initialisiere die Spielfigur
        self.player = Character(":resources:images/animated_characters/female_adventurer/femaleAdventurer")
        self.player.center_x = 100
        self.player.center_y = 100

        # Initialisiere die Physik-Engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player,
            gravity_constant=0.5,
            walls=self.wall_list,
            ladders=self.ladder_list
        )


    # Zeichnet die Spielumgebung und die Spielfigur.
    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.ladder_list.draw()
        self.player.draw()


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

        # Aktualisiere die Zustände der Spielfigur
        self.player.is_on_ladder = self.physics_engine.is_on_ladder()
        self.player.can_jump = self.physics_engine.can_jump() and not self.player.is_on_ladder

        # Aktualisiere die Animation der Spielfigur
        self.player.update_animation(delta_time)


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
window = AnimatedPlayerDemo(title="Player Animation Demo")
window.setup()
arcade.run()


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
# die Leertaste gedrückt wird. Lade die entsprechenden Texturen und passe 
# die Animationen an.
#
# Hinweis: Erweitere die `Character`-Klasse und die Methode `update_animation()`.

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






# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><



