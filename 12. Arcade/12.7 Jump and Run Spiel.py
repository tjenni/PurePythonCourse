#              _______________________________
#       ______|                               |_____
#       \     |   12.7 JUMP AND RUN SPIEL     |    /
#        )    |_______________________________|   (
#       /________)                        (________\     18 .11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

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

# Ansicht für Start-, Game-Over- oder Endbildschirme
class InfoView(arcade.View):

    # Initialisiert die Info-Ansicht mit einem Text und einer Hintergrundfarbe.
    def __init__(self, text="", color=arcade.color.BLACK):
        super().__init__()

        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.text = text  # Der anzuzeigende Text
        self.color = color  # Die Textfarbe

    # Zeichnet den Text und eine Anleitung zur Interaktion.
    def on_draw(self):
        self.clear()
        arcade.draw_text(self.text, self.window.width // 2, self.window.height // 2, self.color, 48, anchor_x="center")
        arcade.draw_text(
            "weiter mit der Leertaste",
            self.window.width // 2,
            self.window.height // 2 - 50,
            arcade.color.BLACK,
            24,
            anchor_x="center",
        )

    # Wechselt zur Spielansicht, wenn die Leertaste gedrückt wird.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)


# Die Hauptspiel-Ansicht
class GameView(arcade.View):

    # Initialisiert das Spiel mit Spieler, Objekten und weiteren Listen.
    def __init__(self):
        super().__init__()

        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.player = None
        self.coin_list = None
        self.physics_engine = None
        self.score = 0


    # Initialisiert das Spiel für das gegebene Level.
    def setup(self, level=1):
        self.level = level

        # Spieler-Sprite erstellen
        self.player = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", scale=0.5)
        self.player.center_x = 50
        self.player.center_y = 100

        # Sprite-Listen initialisieren
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.object_list = arcade.SpriteList()
        self.trap_list = arcade.SpriteList()

        # Zuordnung der Tile-IDs zu Grafiken und Listen
        path = ":resources:images/"
        self.tiles = {
            1: [path + "tiles/grassLeft.png", self.wall_list],
            2: [path + "tiles/grassMid.png", self.wall_list],
            3: [path + "tiles/grassRight.png", self.wall_list],
            4: [path + "tiles/grassHalf_left.png", self.wall_list],
            5: [path + "tiles/grassHalf_mid.png", self.wall_list],
            6: [path + "tiles/grassHalf_right.png", self.wall_list],
            7: [path + "tiles/cactus.png", self.object_list],
            8: [path + "tiles/spikes.png", self.trap_list],
            9: [path + "items/coinGold.png", self.coin_list],
            10: [path + "tiles/signExit.png", self.object_list],
        }

        # Tilemap für Level 1 oder 2 laden
        if level == 1:
            self.tilemap = [
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
            ]
        elif level == 2:
            self.tilemap = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0],
                [0, 9, 0, 0, 0, 4, 4, 6, 0, 0, 0, 0, 0],
                [0, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 4, 5, 6, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 7, 0, 0, 0, 0, 0, 8, 0, 0, 10],
                [2, 2, 2, 3, 0, 0, 0, 0, 0, 2, 3, 0, 1]
            ]

        # Erstellen der Objekte basierend auf der Tilemap
        for i, row in enumerate(self.tilemap):
            for j, tile_id in enumerate(row):
                if tile_id != 0:
                    tile_path, tile_list = self.tiles[tile_id]
                    tile = arcade.Sprite(tile_path, 0.5)
                    tile.center_x = j * 64
                    tile.center_y = self.window.height - i * 64
                    tile_list.append(tile)

        # Sounds laden
        self.coin_sound = arcade.load_sound(":resources:sounds/coin2.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump3.wav")
        self.gameover_sound = arcade.load_sound(":resources:sounds/gameover2.wav")
        self.success_sound = arcade.load_sound(":resources:sounds/upgrade2.wav")

        # Szene erstellen und Sprite-Listen hinzufügen
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Background", sprite_list=self.object_list)
        self.scene.add_sprite_list("Coins", sprite_list=self.coin_list)
        self.scene.add_sprite_list("Walls", sprite_list=self.wall_list)
        self.scene.add_sprite_list("Traps", sprite_list=self.trap_list)
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

        # Kollisionen mit Münzen
        coin_hit_list = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for coin in coin_hit_list:
            arcade.play_sound(self.coin_sound)
            coin.remove_from_sprite_lists()
            self.score += 1

        # Kollisionen mit Fallen
        trap_hit_list = arcade.check_for_collision_with_list(self.player, self.trap_list)
        if trap_hit_list or self.player.center_y < 0:
            arcade.play_sound(self.gameover_sound)
            self.window.show_view(InfoView("GAME OVER"))

        # Übergang zum nächsten Level
        if self.player.center_x > self.window.width:
            arcade.play_sound(self.success_sound)
            if self.level == 1:
                self.setup(level=2)
            else:
                self.window.show_view(InfoView("ENDE", color=arcade.color.AMBER))

        # Spieler bleibt im Fensterbereich
        elif self.player.center_x < 0:
            self.player.center_x = 0

    # Reagiert auf Tastendrücke, um den Spieler zu bewegen.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP and self.physics_engine.can_jump():
            self.player.change_y = 12
            arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT:
            self.player.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5

    # Stoppt die Bewegung des Spielers, wenn die Taste losgelassen wird.
    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0


# Startet die Anwendung und zeigt die Startansicht an.
def main():
    window = arcade.Window(800, 600, "Einfaches Plattformspiel")

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
# Füge eine Gesundheitsanzeige hinzu, die jedes Mal reduziert wird, wenn der 
# Spieler mit einer Falle kollidiert. Wenn die Gesundheit 0 erreicht, wird 
# das Spiel beendet.

'''
class GameView(GameView):

    def setup(self, level=1):
        ...

        self.player.health = 100  
        self.player.damage_cooldown = 0


    def on_update(self, delta_time):
        ...

        self.hurt_sound = arcade.load_sound(":resources:sounds/hurt1.wav")
        ...

        # Kollisionen mit Fallen
        trap_hit_list = arcade.check_for_collision_with_list(self.player, self.trap_list)
        if trap_hit_list:

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

        arcade.draw_text(f"Health: {self.health}", 10, 540, arcade.color.RED, 16)
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

        if level == 3:
            self.tilemap = [
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

    def on_update(self, delta_time):
        ...

        if self.player.center_x > self.window.width:
            arcade.play_sound(self.success_sound)
            if self.level == 1:
                self.setup(level=2)
            if self.level == 2:
                self.setup(level=3)
            elif self.level == 3:
                self.window.show_view(InfoView("ENDE", color=arcade.color.AMBER))

'''

            




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Füge ein Power-Up hinzu, das der Spieler einsammeln kann. Das Power-Up sollte 
# die Sprunghöhe des Spielers temporär erhöhen.


# Füge hier deine Lösung ein.






# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><



