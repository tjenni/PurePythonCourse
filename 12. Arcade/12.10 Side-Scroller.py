#              _________________________
#       ______|                         |_____
#       \     |   12.10 SIDE-SCROLLER    |    /
#        )    |_________________________|   (
#       /________)                  (________\     21.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# Side-Scrolling-Spiele, bei denen die Kamera dem Spieler folgt, gehören zu den 
# Klassikern in der Spielentwicklung. Mit Arcade kannst du dies mit zwei Kameras 
# umsetzen:
#
# 1. Spielkamera: Verfolgt die Spielfigur und zeigt die Spiellandschaft an.
#
# 2. GUI-Kamera: Zeigt Elemente der Benutzeroberfläche (z. B. Punkte, Leben) 
#    unabhängig von der Spielkamera an.
#
# In diesem Kapitel lernst du, wie du beide Kameras einsetzt, um ein flüssiges 
# Spielerlebnis zu schaffen und gleichzeitig ein übersichtliches GUI zu gestalten.


# _________________________________
#                                 /
# Grundlagen der Kameras         (
# ________________________________\
#
# - Die Spielkamera (`arcade.Camera`) ermöglicht es, den Blick auf eine bewegliche 
#   Spielfigur oder andere Elemente zu richten.
#
# - Die GUI-Kamera wird für das Zeichnen von Benutzeroberflächenelementen genutzt, 
#   die immer an derselben Position auf dem Bildschirm bleiben.
#
# - Kameras können bewegt oder direkt auf eine Position gesetzt werden, um dynamisch 
#   auf Ereignisse zu reagieren.


import arcade


class SideScrollingDemo(arcade.Window):
    
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)

        # Spielkamera: Verfolgt die Spiellandschaft
        self.camera = arcade.Camera(self.width, self.height)

        # GUI-Kamera: Statische Ansicht für Benutzeroberfläche
        self.gui_camera = arcade.Camera(self.width, self.height)

        # Spielfigur (Spieler)
        self.player = None

        # Sprite-Listen
        self.wall_list = None

        # Punkteanzeige
        self.score = 0
    
    
    # Initialisiert das Spiel: Erstellt Spielfigur, Wände und setzt die Kameras.
    def setup(self):
        
        # Hintergrundfarbe setzen
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Spielfigur erstellen
        self.player = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", scale=0.5)
        self.player.center_x = 100
        self.player.center_y = 100

        # Wände erstellen
        self.wall_list = arcade.SpriteList()
        for x in range(0, 1600, 64):  # Langer Boden für Scrolling
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=0.5)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)
            
        # Physik-Engine initialisieren
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, gravity_constant=0.5, walls=self.wall_list)

    
    # Aktualisiert die Spielkamera, sodass sie der Spielfigur folgt.
    def update_camera(self):
        
        # Kamera zentrieren auf den Spieler, dabei X und Y Achse berücksichtigen
        screen_center_x = max(0, self.player.center_x - self.camera.viewport_width // 2)
        screen_center_y = max(0, self.player.center_y - self.camera.viewport_height // 2)

        # Kamera zur berechneten Position verschieben
        self.camera.move_to((screen_center_x, screen_center_y), speed=0.2)


    def on_draw(self):
        arcade.start_render()
        
        # Spielkamera aktivieren
        self.camera.use() 
        self.wall_list.draw()  # Wände zeichnen
        self.player.draw()  # Spielfigur zeichnen

        # GUI-Kamera aktivieren
        self.gui_camera.use()
        arcade.draw_text(f"Punkte: {self.score}", 15, self.height - 30, arcade.color.WHITE, 16)


    def on_update(self, delta_time):
        self.physics_engine.update()
        self.update_camera()


    # Verarbeitet Tasteneingaben für Spielerbewegungen.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5


    # Stoppt die Bewegung des Spielers bei Loslassen der Tasten.
    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0


window = SideScrollingDemo(title="Side-Scrolling mit Kameras")
window.setup()
arcade.run()




# ___________________
#                   /
# Zusammenfassung  (
# __________________\
#
#
# In diesem Kapitel hast du gelernt, wie man eine Spielkamera und eine GUI-Kamera
# in einem Side-Scrolling-Spiel verwendet. Diese Kameras helfen, dynamisch den
# Fokus auf Spielfiguren zu setzen, während das GUI an Ort und Stelle bleibt.
#
# Die wichtigsten Konzepte waren:
#
# 1. arcade.Camera: Dynamische Bewegung und Verfolgung von Spielfiguren.
#
# 2. GUI-Kamera: Statische Benutzeroberfläche, unabhängig von der Spiellandschaft.
#
# 3. Bewegung der Kamera: move_to() sorgt für sanfte Übergänge.
#
# Mit diesen Werkzeugen kannst du sowohl die Spielszene als auch die
# Benutzeroberfläche effizient gestalten und steuern.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
#
# Füge ein Sammelobjekt (z. B. Münze) hinzu, das der Spieler einsammeln kann.
# Zeige die Punktzahl im GUI an und erhöhe sie bei jeder eingesammelten Münze.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle einen Spielbereich, der nach oben und unten erweitert ist. Lass
# die Kamera sowohl horizontal als auch vertikal dem Spieler folgen.

# Füge hier deine Lösung ein.




#                         __
#                         (=[)
#              pb       /`\ -.
#   `` ,,``           /`| ,_,_`-._           Jetzt kannst du zum Beispiel ein
#        ,,'         /  `---,)`--.)          Ski-Sidescroller machen.
#     ``,,  ''      (  '._-/_   /
#    ,,    `` ``,,   \   /') )/'
#     , ``,''`;; ,,   `>' / / 
#    `` '',`;;,`;;, -/' /|  \
#       ``,; --..._/|  \ ```---...___
#                /'  ```---...___   _```--'
#                                ```
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
# Füge ein Sammelobjekt (z. B. Münze) hinzu, das der Spieler einsammeln kann.
# Zeige die Punktzahl im GUI an und erhöhe sie bei jeder eingesammelten Münze.

'''
import arcade

class SideScrollingDemo(arcade.Window):
    
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)

        # Spielkamera: Verfolgt die Spiellandschaft
        self.camera = arcade.Camera(self.width, self.height)

        # GUI-Kamera: Statische Ansicht für Benutzeroberfläche
        self.gui_camera = arcade.Camera(self.width, self.height)

        # Spielfigur (Spieler)
        self.player = None

        # Sprite-Listen
        self.wall_list = None
        
        self.coin_list = None

        # Punkteanzeige
        self.score = 0
    
    
    # Initialisiert das Spiel: Erstellt Spielfigur, Wände und setzt die Kameras.
    def setup(self):
        
        # Hintergrundfarbe setzen
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Spielfigur erstellen
        self.player = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", scale=0.5)
        self.player.center_x = 100
        self.player.center_y = 100

        # Wände erstellen
        self.wall_list = arcade.SpriteList()
        for x in range(0, 1600, 64):  # Langer Boden für Scrolling
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=0.5)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)
            
        # Coins erstellen
        self.coin_list = arcade.SpriteList()
        for x in range(256, 1600, 256):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", 0.5)
            coin.center_x = x
            coin.center_y = 96
            self.coin_list.append(coin)
        
        # Physik-Engine initialisieren
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, gravity_constant=0.5, walls=self.wall_list)

    
    # Aktualisiert die Spielkamera, sodass sie der Spielfigur folgt.
    def update_camera(self):
        
        # Kamera zentrieren auf den Spieler, dabei X und Y Achse berücksichtigen
        screen_center_x = max(0, self.player.center_x - self.camera.viewport_width // 2)
        screen_center_y = max(0, self.player.center_y - self.camera.viewport_height // 2)

        # Kamera zur berechneten Position verschieben
        self.camera.move_to((screen_center_x, screen_center_y), speed=0.2)


    def on_draw(self):
        arcade.start_render()
        
        # Spielkamera aktivieren
        self.camera.use() 
        self.wall_list.draw()  # Wände zeichnen
        self.coin_list.draw()
        self.player.draw()  # Spielfigur zeichnen

        # GUI-Kamera aktivieren
        self.gui_camera.use()
        arcade.draw_text(f"Punkte: {self.score}", 15, self.height - 30, arcade.color.WHITE, 16)


    def on_update(self, delta_time):
        self.physics_engine.update()
        self.update_camera()
        
        # Prüfe, ob der Spieler eine oder mehrere Münzen berührt
        coins_hit = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for coin in coins_hit:
            coin.remove_from_sprite_lists()  # Entferne die Münze aus der Sprite-Liste
            self.score += 1  # Erhöhe den Punktestand


    # Verarbeitet Tasteneingaben für Spielerbewegungen.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP and self.physics_engine.can_jump():
            self.player.change_y = 12
        elif key == arcade.key.LEFT:
            self.player.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5


    # Stoppt die Bewegung des Spielers bei Loslassen der Tasten.
    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0


window = SideScrollingDemo(title="Side-Scrolling mit Kameras")
window.setup()
arcade.run()
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle einen Spielbereich, der nach oben und unten erweitert ist. Lass
# die Kamera sowohl horizontal als auch vertikal dem Spieler folgen.

'''
# Initialisiert das Spiel: Erstellt Spielfigur, Wände und setzt die Kameras.
    def setup(self):
        
        ...

        # Spielfigur erstellen
        self.player = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", scale=0.5)
        self.player.center_x = 100
        self.player.center_y = 200

        # Wände erstellen
        self.wall_list = arcade.SpriteList()
        for x in range(0, 1600, 64):  # Langer Boden für Scrolling
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=0.5)
            wall.center_x = x
            wall.center_y = 32 + x
            self.wall_list.append(wall)

    ...

    # Verarbeitet Tasteneingaben für Spielerbewegungen.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP and self.physics_engine.can_jump():
            self.player.change_y = 12
        elif key == arcade.key.LEFT:
            self.player.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5

'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


