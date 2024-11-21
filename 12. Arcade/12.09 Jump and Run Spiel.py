#              _______________________________
#       ______|                               |_____
#       \     |   12.7 JUMP AND RUN SPIEL     |    /
#        )    |_______________________________|   (
#       /________)                        (________\     18.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Jump-and-Run-Spiele gehören zu den Klassikern der Videospiele und sind seit den frühen Tagen 
# der Gaming-Welt populär. Typische Vertreter wie "Super Mario" oder "Sonic the Hedgehog" 
# haben ganze Generationen begeistert. Der Reiz dieser Spiele liegt in ihrer Mischung aus 
# Geschicklichkeit, Timing und Entdeckung.

# In einem Jump-and-Run-Spiel steuerst du eine Figur, die durch Level navigiert, Hindernisse 
# überwindet, Münzen sammelt und Fallen ausweicht. Dabei ist Präzision gefragt: Ein falscher 
# Sprung oder eine Berührung mit einer Falle kann das Spiel beenden. Ziel ist es, möglichst 
# viele Punkte zu sammeln und das Ende eines Levels zu erreichen.

# Dieses Kapitel zeigt dir Schritt für Schritt, wie du ein solches Spiel mit Arcade entwickelst. 
# Dabei lernst du grundlegende Konzepte wie Sprite-Management, Kollisionserkennung und die 
# Verwendung von Tilemaps für das Level-Design kennen. Außerdem wirst du Soundeffekte und 
# Level-Übergänge hinzufügen, um das Spielerlebnis abzurunden.

# Hier sind die wichtigsten Themen, die du in diesem Kapitel umsetzen wirst:
#
# - Aufbau eines Spiels mit Start- und Endbildschirmen: 
#   Du lernst, wie du ein Spiel mit einer klaren Struktur startest und abschließt.
#
# - Steuerung der Spielfigur mit der Tastatur: 
#   Die Spielfigur wird mit den Pfeiltasten bewegt und kann springen.
#
# - Hinzufügen von Hindernissen und Fallen: 
#   Du integrierst Wände, Abgründe und andere Elemente, die der Spieler überwinden muss.
#
# - Einsammeln von Münzen: 
#   Punkte werden durch das Sammeln von Münzen erhöht.
#
# - Übergänge zwischen verschiedenen Leveln: 
#   Am Ende eines Levels wird automatisch das nächste Level geladen.
#
# - Soundeffekte und Feedback: 
#   Durch Geräusche für Sprünge, Münzen und Game-Over-Meldungen wird das Spiel lebendig.
#
# Egal, ob du das Spiel minimalistisch oder mit komplexen Features gestalten möchtest, 
# dieses Kapitel liefert dir das Grundgerüst, das du nach deinen Vorstellungen erweitern kannst.


import arcade
import random

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

        self.score = 0


    # Initialisiert das Spiel für ein spezifisches Level.
    def setup(self, level=1):
        self.level = level
        
        self.tile_path = ":resources:images/"
        self.tile_scale = 0.5

        # Spieler-Sprite erstellen
        self.player = arcade.Sprite(self.tile_path + "animated_characters/female_adventurer/femaleAdventurer_idle.png", scale=self.tile_scale)
        self.player.center_x = 50
        self.player.center_y = 100

        # Sprite-Listen initialisieren
        self.wall_list = arcade.SpriteList()
        self.object_list = arcade.SpriteList()

        # Zuordnung der Tile-IDs zu Grafiken und Listen
        path = ":resources:images/"
        self.tiles = {
            1: ["tiles/grassLeft.png", self.wall_list],
            2: ["tiles/grassMid.png", self.wall_list],
            3: ["tiles/grassRight.png", self.wall_list],
            4: ["tiles/grassHalf_left.png", self.wall_list],
            5: ["tiles/grassHalf_mid.png", self.wall_list],
            6: ["tiles/grassHalf_right.png", self.wall_list],
            7: ["tiles/cactus.png", self.object_list],
            8: ["tiles/spikes.png", self.object_list],
            9: ["items/coinGold.png", self.object_list],
            10: ["tiles/signExit.png", self.object_list],
        }

        # Tilemap-Daten für mehrere Level
        self.level_tilemaps = [
            # Level 1
            [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 4, 6, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 4, 6, 0, 0, 0, 0],
            [0, 0, 0, 0, 9, 0, 8, 8, 9, 0, 7, 0, 10],
            [2, 3, 0, 1, 2, 2, 2, 2, 2, 2, 3, 0, 1]
            ],

            # Level 2
            [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0],
            [0, 9, 0, 0, 0, 4, 5, 6, 0, 0, 0, 0, 0],
            [0, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 4, 5, 6, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 7, 0, 0, 0, 0, 0, 8, 0, 0, 10],
            [2, 2, 2, 3, 0, 0, 0, 0, 0, 2, 3, 0, 1]
            ]
        ]


        # Objekte basierend auf der Tilemap erstellen
        for i, row in enumerate(self.level_tilemaps[self.level-1]):
            for j, tile_id in enumerate(row):
                if tile_id != 0:
                    tile_file, tile_list = self.tiles[tile_id]
                    tile = arcade.Sprite(self.tile_path + tile_file, self.tile_scale)

                    tile.center_x = j * 64
                    tile.center_y = self.window.height - i * 64

                    tile.id = tile_id

                    tile_list.append(tile)

        # Sounds laden
        self.coin_sound = arcade.load_sound(":resources:sounds/coin2.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump3.wav")
        self.gameover_sound = arcade.load_sound(":resources:sounds/gameover2.wav")
        self.success_sound = arcade.load_sound(":resources:sounds/upgrade2.wav")

        # Szene initialisieren
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Objects", sprite_list=self.object_list)
        self.scene.add_sprite_list("Walls", sprite_list=self.wall_list)
        self.scene.add_sprite("Player", self.player)

        # Physik-Engine initialisieren
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, gravity_constant=0.5, walls=self.wall_list)


    # Zeichnet die Szene und die Punktzahl.
    def on_draw(self):
        arcade.start_render()
        self.scene.draw()
        arcade.draw_text(f"Score: {self.score}", 10, 570, arcade.color.WHITE, 16)


    # Aktualisiert die Spiellogik, wie Kollisionen und Levelübergänge.
    def on_update(self, delta_time):
        self.physics_engine.update()

        # Kollisionserkennung mit Objekten
        object_hit_list = arcade.check_for_collision_with_list(self.player, self.object_list)
        for obj in object_hit_list:
            # Münzen
            if obj.id == 9:
                arcade.play_sound(self.coin_sound)
                obj.remove_from_sprite_lists()
                self.score += 1
                
            # Falle
            elif obj.id == 8:
                arcade.play_sound(self.gameover_sound)
                self.window.show_view(InfoView("GAME OVER"))

        # Übergang zum nächsten Level
        if self.player.center_x > self.window.width:
            arcade.play_sound(self.success_sound)

            if self.level < len(self.level_tilemaps):
                self.setup(level=self.level + 1)
            else:
                self.window.show_view(InfoView("ENDE", color=arcade.color.AMBER))

        # Spieler innerhalb des Fensters halten
        elif self.player.center_x < 0:
            self.player.center_x = 0

        # Spieler fällt aus dem Fenster
        if self.player.center_y < 0:
            arcade.play_sound(self.gameover_sound)
            self.window.show_view(InfoView("GAME OVER"))
            

    # Verarbeitet Tasteneingaben für Spielerbewegungen.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP and self.physics_engine.can_jump():
            self.player.change_y = 12
            arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT:
            self.player.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5

    # Stoppt die Bewegung des Spielers bei Loslassen der Tasten.
    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0


# Startet das Spiel und zeigt die Startansicht.
def main():
    window = arcade.Window(800, 600, "Jumpmania")

    window.show_view(InfoView(text="Jumpmania", color=arcade.color_from_hex_string("#665d4a")))

    arcade.run()


if __name__ == "__main__":
    main()




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# In diesem Kapitel hast du ein vollständiges Jump-and-Run-Spiel entwickelt. 
# Hier sind die wichtigsten Konzepte und Funktionen, die du dabei kennengelernt hast:

# 1. Spielansichten (Views):
#    - Du hast verschiedene Ansichten wie den Startbildschirm, das Hauptspiel und 
#      die Endbildschirme erstellt. 
#
#    - Mit der Klasse `arcade.View` kannst du unterschiedliche Zustände des Spiels 
#      verwalten, z. B. die Anzeige einer Start- oder Game-Over-Nachricht.
#
#    - Die Methode `self.window.show_view(view)` ermöglicht den Wechsel zwischen 
#      den Ansichten.

# 2. Sprite-Management:
#    - Du hast gelernt, wie Sprites erstellt, positioniert und in verschiedenen 
#      Sprite-Listen organisiert werden.
# 
#    - Die `arcade.SpriteList`-Klasse bietet eine effiziente Möglichkeit, 
#      Gruppen von Sprites wie Münzen, Fallen oder Wände zu verwalten.

# 3. Tilemaps für Level-Design:
#    - Mit Hilfe einer Tilemap hast du das Spielfeld für verschiedene Level erstellt.
#    
#    - Tilemaps ermöglichen es, das Level-Layout systematisch zu definieren, 
#      indem Kacheln (Tiles) für bestimmte Elemente wie Wände, Münzen oder 
#      Fallen verwendet werden.
#
#    - Die Tilemap wird in Python als verschachtelte Liste dargestellt, wobei 
#      jeder Eintrag eine bestimmte Tile-ID repräsentiert.

# 4. Physik-Engine:
#    - Mit der Klasse `arcade.PhysicsEnginePlatformer` wurde die Bewegung des 
#      Spielers realistisch simuliert.
#
#    - Die Engine sorgt dafür, dass der Spieler korrekt mit Wänden kollidiert 
#      und Sprünge ausführen kann, während die Schwerkraft berücksichtigt wird.

# 5. Kollisionserkennung:
#    - Kollisionen zwischen dem Spieler und anderen Objekten (Münzen, Fallen) 
#      wurden mit der Methode `arcade.check_for_collision_with_list()` überprüft.
#
#    - Diese Methode erlaubt es, Kollisionen effizient zu erkennen und entsprechende 
#      Aktionen auszulösen, z. B. das Einsammeln von Münzen oder das Verlieren 
#      des Spiels.

# 6. Soundeffekte:
#    - Das Spiel wurde durch Soundeffekte wie das Einsammeln von Münzen oder das 
#      Verlieren des Spiels verbessert.
#
#    - Sounds wurden mit `arcade.play_sound()` abgespielt, um dem Spiel ein 
#      immersiveres Erlebnis zu verleihen.

# 7. Level-Übergänge:
#    - Wenn der Spieler das Ende eines Levels erreicht, wird automatisch das 
#      nächste Level gestartet.
#
#    - Mit einer neuen Tilemap kannst du leicht weitere Level hinzufügen, 
#      um das Spiel zu erweitern.

# 8. Spielgrenzen und Logik:
#    - Der Spieler wurde darauf beschränkt, sich nur innerhalb des Spielfelds 
#      zu bewegen.
#
#    - Das Spiel erkennt, wenn der Spieler aus dem Spielfeld fällt, und zeigt 
#      dann eine Game-Over-Nachricht an.

# Diese grundlegenden Konzepte sind die Bausteine für jedes 2D-Jump-and-Run-Spiel. 
# Mit diesem Wissen kannst du das Spiel weiterentwickeln, z. B. durch Hinzufügen 
# neuer Objekte, Power-Ups oder benutzerdefinierter Level. Nutze die Aufgaben 
# als Gelegenheit, deine Kenntnisse zu vertiefen!




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Füge eine Gesundheitsanzeige hinzu, die jedes Mal reduziert wird, wenn der 
# Spieler mit einer Falle kollidiert. Wenn die Gesundheit 0 erreicht, wird 
# das Spiel beendet.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein drittes Level mit einer neuen Tilemap, die komplexer ist als die 
# ersten beiden.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Füge ein Power-Up hinzu, das der Spieler einsammeln kann. Das Power-Up sollte 
# die Sprunghöhe des Spielers temporär erhöhen.


# Füge hier deine Lösung ein.




#   ⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠒⠛⠛⠓⢦⡀⠀⢀⣀⡀⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⣤⢦⢡⣷⣴⣛⠩⡙⠓⢦⡀⠀
#   ⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⢀⠤⠑⠈⠉⣀⣤⣤⣭⢷⣀⠀⡇⠀
#   ⠀⠀⠀⠀⣀⡟⠀⠀⡠⠊⠁⣀⠤⠂⠁⣬⣟⣉⠀⠀⢀⡼⠃⠀
#   ⠀⠀⠀⡞⠉⠃⠀⣼⣇⠈⠁⠀⢿⠀⠀⠉⠉⠉⠙⣦⠾⠁⠀⠀    Go Mario !
#   ⠀⠀⠀⢧⡔⠈⡉⠻⣿⡷⠀⣤⣄⣀⡀⠀⠀⠀⢀⡾⠀⠀⠀⠀
#   ⠀⠀⠀⠸⡄⠀⠈⠀⠈⠁⠀⠙⢿⣿⣿⣷⣶⣶⠟⠁⠀⠀⠀⠀
#   ⠀⠀⠀⠀⠙⠲⣶⣶⣦⣀⠀⠀⢈⠉⡹⡻⣩⠏⠀⠀⠀⠀⠀⠀
#   ⠀⠀⣠⡤⠶⡋⠁⢀⡠⠜⢹⠒⠲⡓⢫⠻⣅⣀⡴⠶⠶⣤⡀⠀
#   ⠀⡴⠋⠀⠀⠀⢑⡏⠀⠀⡰⢠⠂⠈⠄⠀⠏⢻⠁⠀⠀⢸⢻⡆
#   ⢸⡃⠊⠰⠀⠀⠀⣏⠐⠈⠀⠈⠢⠤⠂⠀⠈⡟⠀⠀⢀⢢⡟⠀
#   ⠀⠳⣄⡀⠀⣲⠞⠉⠹⢦⡀⠀⠀⠀⠀⢀⣼⣇⡀⢀⢨⡟⠀⠀
#   ⠀⠀⠀⢹⠏⠇⠀⠀⠀⢸⠧⠤⠤⠶⠚⠋⠀⠈⠉⠙⠛⠁⠀⠀
#   ⠀⠀⠀⢼⢰⠀⠀⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#   ⠀⠀⠀⠈⠛⠦⣤⡤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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
# Füge eine Gesundheitsanzeige hinzu, die jedes Mal reduziert wird, wenn der 
# Spieler mit einer Falle kollidiert. Wenn die Gesundheit 0 erreicht, wird 
# das Spiel beendet.

'''
class GameView(GameView):

    def setup(self, level=1):
        ...
        # Spieler-Sprite erstellen
        ...

        self.player.health = 100  
        self.player.damage_cooldown = 0


    def on_update(self, delta_time):
        ...

        self.hurt_sound = arcade.load_sound(":resources:sounds/hurt1.wav")
        ...

        # Kollisionen mit Fallen
        object_hit_list = arcade.check_for_collision_with_list(self.player, self.object_list)
        for obj in object_hit_list:

            ...

            # Spikes
            elif obj.id == 8:
                if self.player.damage_cooldown > 0:
                    self.player.damage_cooldown -= 1
                else:
                    self.player.health -= 10  # Gesundheit reduzieren
                    self.player.damage_cooldown = 50
                    
                    arcade.play_sound(self.hurt_sound)
                    
                    if self.player.health <= 0:
                        arcade.play_sound(self.gameover_sound)
                        self.window.show_view(InfoView("GAME OVER"))
        
        # Fall in die Tiefe
        if self.player.center_y < 0:
            arcade.play_sound(self.gameover_sound)
            self.window.show_view(InfoView("GAME OVER"))


    def on_draw(self):
        ...

        arcade.draw_text(f"Health: {self.player.health}", 10, 540, arcade.color.RED, 16)
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein drittes Level mit einer neuen Tilemap, die komplexer ist als die 
# ersten beiden.

'''
class GameView(GameView):
    ...

    def setup(self, level=1):
            ...

            # Level 3
            [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 4, 6, 0, 0, 0, 0, 0],
            [0, 0, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 9, 8, 0, 9, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 4, 6, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 8, 9, 8, 0, 0, 8, 9, 7, 0, 10],
            [2, 3, 0, 1, 2, 3, 0, 0, 1, 2, 3, 0, 1]
            ]

'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Füge ein Power-Up hinzu, das der Spieler einsammeln kann. Das Power-Up sollte 
# die Sprunghöhe des Spielers temporär erhöhen.

'''
...

class GameView(arcade.View):
    ...

    def setup(self, level=1):
        ...
        
        # Tilemap-Daten für mehrere Level
        self.tiles = {
            ...

            11: ["items/star.png", self.object_list],
        }

        ...

        # Sounds laden
        ...

        self.upgrade_sound = arcade.load_sound(":resources:sounds/upgrade1.wav")


    def on_update(self, delta_time):

        # Spieler-Sprite erstellen
        self.player.upgrade_timer = 0
        
        ...

        for obj in object_hit_list:
            ...

            # Sternen
            elif obj.id == 11:
                arcade.play_sound(self.upgrade_sound)
                obj.remove_from_sprite_lists()
                self.player.upgrade_timer = 50
        
        # Aktualisiere den Upgrade Timer
        if self.player.upgrade_timer > 0:
            self.player.upgrade_timer -= 1
    
    ...

    # Verarbeitet Tasteneingaben für Spielerbewegungen.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP and self.physics_engine.can_jump():
            if self.player.upgrade_timer > 0:
                self.player.change_y = 15
            else:
                self.player.change_y = 12
        ...

'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


