#              _______________________
#       ______|                       |_____
#       \     |   12.6 SPIELPHYSIK    |    /
#        )    |_______________________|   (
#       /________)                (________\    20.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# Die Physik eines Spiels bestimmt, wie sich Objekte im Spiel bewegen und 
# miteinander interagieren. In einem Jump-and-Run-Spiel zum Beispiel ist die Physik 
# entscheidend, um realistische Bewegungen zu ermöglichen. 

# Spieler erwarten, dass ihre Figur springt, fällt und Hindernisse überwinden kann, 
# während sie sich an physikalische Regeln hält. In Arcade bietet die `PhysicsEnginePlatformer` 
# eine praktische Möglichkeit, diese Mechaniken umzusetzen.
#
# In diesem Kapitel erfährst du, wie du die Spielphysik für ein Jump-and-Run-Spiel implementierst. 
# Du lernst:
#
# - wie die Schwerkraft die Spielfigur beeinflusst,
#
# - wie Sprünge und Kollisionen realisiert werden,
#
# - wie Hindernisse und Fallen mit der Spielfigur interagieren.
#
# Die hier beschriebenen Grundlagen sind flexibel und lassen sich leicht 
# anpassen oder erweitern, um verschiedene Spiele zu erstellen.




# _____________________________________
#                                     /
# Physik-Engine für Plattformspiele  (
# ____________________________________\

# In Arcade ist die Klasse `PhysicsEnginePlatformer` speziell für Plattformspiele gedacht. 
# Sie ermöglicht es, Schwerkraft und Bewegungsbegrenzungen auf einfache Weise zu integrieren. 
# Die folgenden Kernkonzepte werden in der Engine behandelt:

# 1. Schwerkraft: Die Spielfigur wird kontinuierlich nach unten gezogen, es sei 
#    denn, sie steht auf einer Wand.
#
# 2. Kollisionen: Die Engine verhindert, dass die Spielfigur durch Wände fällt 
#    oder hindurchläuft.
#
# 3. Sprünge: Der Spieler kann springen, wenn er sich auf einer Oberfläche befindet.


import arcade

# Diese Klasse demonstriert die Spielphysik mit Arcade, einschließlich Schwerkraft, 
# Kollisionen und Sprüngen.
class GamePhysicsDemo(arcade.Window):

    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)

        self.player = None  # Die Spielfigur
        self.wall_list = None  # Wände, auf denen die Spielfigur laufen kann
        self.physics_engine = None  # Die Physik-Engine


    # Initialisiert die Spielfigur, die Wände und die Physik-Engine.
    def setup(self):

        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Spielfigur erstellen
        self.player = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", scale=0.5)
        self.player.center_x = 100
        self.player.center_y = 200

        # Wände erstellen
        self.wall_list = arcade.SpriteList()
        for x in range(0, 800, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=0.5)
            wall.center_x = x
            wall.center_y = 64
            self.wall_list.append(wall)

        # Physik-Engine initialisieren
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, gravity_constant=0.5, walls=self.wall_list)

    # Zeichnet die Spielfigur und die Wände.
    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player.draw()

    # Aktualisiert die Physik und Bewegung der Spielfigur.
    def on_update(self, delta_time):
        self.physics_engine.update()

        # Spielfigur aus dem Bildschirm verhindern
        if self.player.center_y < 0:
            self.player.center_y = 200
            self.player.center_x = 100

    # Verarbeitet Tasteneingaben für die Spielfigur.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP and self.physics_engine.can_jump():
            self.player.change_y = 12  # Sprunghöhe
        elif key == arcade.key.LEFT:
            self.player.change_x = -5  # Bewegung nach links
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5  # Bewegung nach rechts

    # Stoppt die Bewegung, wenn die Pfeiltasten losgelassen werden.
    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0


# Hauptprogramm
window = GamePhysicsDemo(title="Spielphysik in Arcade")
window.setup()
arcade.run()




# _______________________________
#                               /
# Erklärung der Physik-Engine  (
# ______________________________\

# 1. Gravitationskonstante:
#    - Die `PhysicsEnginePlatformer` benötigt einen Wert für die Schwerkraft. 
#      In diesem Beispiel wird `gravity_constant=0.5` verwendet.
#
#    - Höhere Werte führen zu schnellerem Fallen, während kleinere Werte 
#      langsameres Fallen bewirken.

# 2. Kollisionserkennung:
#    - Die Engine überprüft automatisch, ob die Spielfigur mit Wänden kollidiert.
#
#    - Wenn die Spielfigur auf einer Wand steht, wird verhindert, dass sie 
#      nach unten fällt.

# 3. Sprünge:
#    - Die Methode `can_jump()` prüft, ob die Spielfigur sich auf einer 
#      Oberfläche befindet, bevor ein Sprung ausgeführt wird.

# 4. Spielgrenzen:
#    - Um zu verhindern, dass die Spielfigur aus dem Spielfeld fällt, wird die 
#      Y-Koordinate in der Methode `on_update()` überprüft und zurückgesetzt.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# In diesem Kapitel hast du die Grundlagen der Spielphysik in Arcade kennengelernt:
#
# - Die `PhysicsEnginePlatformer` bietet eine einfache Möglichkeit, Schwerkraft 
#   und Kollisionen zu implementieren.
#
# - Sprünge und Bewegungen können durch Tasteneingaben gesteuert werden.
#
# - Die Engine kümmert sich um die physikalische Korrektheit der Spielfigur.
#
# Mit diesen Werkzeugen kannst du realistische Bewegungen für deine Spielfigur 
# implementieren. Nutze die Funktionen der Physik-Engine, um kreative und 
# herausfordernde Levels zu gestalten!




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Experimentiere mit verschiedenen Werten für die gravity_constant in der 
# PhysicsEnginePlatformer.
#
# Erstelle drei Varianten des Spiels:
#
# a) Mit sehr geringer Schwerkraft (z. B. 0.1), um ein “Mondlandung”-Gefühl
#    zu erzeugen.
# 
# b) Mit normaler Schwerkraft (0.5), wie im Beispielcode.
#
# c) Mit starker Schwerkraft (2.0), bei der die Spielfigur sehr schnell fällt.
#
# Ziel:
# Beobachte, wie sich die Schwerkraft auf das Spielerlebnis auswirkt, 
# und beschreibe die Unterschiede zwischen den Varianten.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Füge zusätzliche Hindernisse zur wall_list hinzu, z. B. Plattformen in 
# der Luft, auf die der Spieler springen kann. Erstelle ein einfaches Level-Design 
# mit mindestens zwei Plattformen auf verschiedenen Höhen. Gestalte eine 
# Herausforderung, bei der die Spielfigur über mehrere Plattformen springen muss, 
# um ans Ziel zu gelangen.
#
#
# Hinweis:
# Verwende den Codeabschnitt zur Erstellung der Wände und passe die center_x- 
# und center_y-Werte an, um die Plattformen zu positionieren.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Füge eine bewegliche Plattform  hinzu, die sich horizontal zwischen zwei Punkten 
# hin- und herbewegt. Implementiere die Bewegung der Plattform mit einer einfachen 
# Änderung von center_x innerhalb von on_update(). Sorge dafür, dass die Richtung 
# der Bewegung umkehrt, wenn die Plattform einen der beiden Punkte erreicht. 
# Zeichne die Plattform in der on_draw()-Methode.

# Füge hier deine Lösung ein.




#         -''--.
#         _`>   `\.-'<
#      _.'     _     '._
#    .'   _.='   '=._   '.         Spielphysik ist genial!
#    >_   / /_\ /_\ \   _<
#      / (  \o/\\o/  ) \
#      >._\ .-,_)-. /_.<
#  jgs     /__/ \__\ 
#            '---'     E=mc^2
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
# Experimentiere mit verschiedenen Werten für die gravity_constant in der 
# PhysicsEnginePlatformer.
#
# Erstelle drei Varianten des Spiels:
#
# a) Mit sehr geringer Schwerkraft (z. B. 0.1), um ein “Mondlandung”-Gefühl
#    zu erzeugen.
# 
# b) Mit normaler Schwerkraft (0.5), wie im Beispielcode.
#
# c) Mit starker Schwerkraft (2.0), bei der die Spielfigur sehr schnell fällt.
#
# Ziel:
# Beobachte, wie sich die Schwerkraft auf das Spielerlebnis auswirkt, 
# und beschreibe die Unterschiede zwischen den Varianten.


'''
a) Geringe Schwerkraft (0.1)
----------------------------

Die Spielfigur fällt langsam zu Boden. Sprünge sind sehr hoch und dauern länger.
Das Spielerlebnis erinnert an das Springen auf dem Mond: Träge Bewegungen und 
längere Zeit in der Luft. Der Schwierigkeitsgrad des Spiels ist einfach, da 
Hindernisse leicht übersprungen werden können.

b) Normale Schwerkraft (0.5)
----------------------------
Die Spielfigur bewegt sich flüssig und realistisch. Sprünge sind kontrollierbar, 
und die Landung erfolgt in moderatem Tempo. Diese Einstellung eignet sich für 
ein klassisches Jump-and-Run-Spiel. Der Schwierigkeitsgrad ist Ausgewogen, 
da die Bewegung präzise bleibt.

c) Starke Schwerkraft (2.0)
---------------------------
Die Spielfigur fällt sehr schnell zu Boden. Sprünge sind flach und erfordern 
präzises Timing, um Hindernisse zu überwinden. Das Spielerlebnis ist hektischer 
und für den Spieler herausfordernder. Der Schwierigkeitsgrad ist schwer, da 
Timing entscheidend ist und Fehler weniger verzeihend sind.

'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Füge zusätzliche Hindernisse zur wall_list hinzu, z. B. Plattformen in 
# der Luft, auf die der Spieler springen kann. Erstelle ein einfaches Level-Design 
# mit mindestens zwei Plattformen auf verschiedenen Höhen. Gestalte eine 
# Herausforderung, bei der die Spielfigur über mehrere Plattformen springen muss, 
# um ans Ziel zu gelangen.
#
#
# Hinweis:
# Verwende den Codeabschnitt zur Erstellung der Wände und passe die center_x- 
# und center_y-Werte an, um die Plattformen zu positionieren.


'''
class GamePhysicsDemo(arcade.Window):

    def setup(self):
        ...
        # Wände erstellen
        ...
        walls = [
            (3*64,2*64),
            (5*64,4*64),
            (8*64,5*64),
            (10*64,6*64),
            ]
        for position in walls:
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=0.5)
            wall.center_x = position[0]
            wall.center_y = position[1]
            self.wall_list.append(wall)
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Füge eine bewegliche Plattform  hinzu, die sich horizontal zwischen zwei Punkten 
# hin- und herbewegt. Implementiere die Bewegung der Plattform mit einer einfachen 
# Änderung von center_x innerhalb von on_update(). Sorge dafür, dass die Richtung 
# der Bewegung umkehrt, wenn die Plattform einen der beiden Punkte erreicht. 
# Zeichne die Plattform in der on_draw()-Methode.

'''

class GamePhysicsDemo(arcade.Window):

    def setup(self):
        ...

        # Bewegliche Plattformen erstellen
        self.moving_platforms = arcade.SpriteList()
        
        platform_positions = [
            (3 * 64, 3 * 64),
            (5 * 64, 4 * 64),
            (8 * 64, 5 * 64),
            (10 * 64, 6 * 64),
        ]
        
        for position in platform_positions:
            platform = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=0.5)
            platform.center_x = position[0]
            platform.center_y = position[1]
            platform.start_x = position[0] - 64  # Bewegungsbereich Start
            platform.end_x = position[0] + 64  # Bewegungsbereich Ende
            platform.change_x = 1  # Geschwindigkeit der Plattform
            self.moving_platforms.append(platform)
            self.wall_list.append(platform)  # Bewegliche Plattformen auch zur Kollisionsliste hinzufügen

    ...

    def on_update(self, delta_time):
       ...
        # Bewegliche Plattformen aktualisieren
        for platform in self.moving_platforms:
            platform.center_x += platform.change_x  # Plattform bewegen
            
            # Plattform umkehren, wenn sie das Ende ihres Bewegungsbereichs erreicht
            if platform.change_x > 0 and platform.center_x > platform.end_x:
                platform.change_x *= -1
            elif platform.change_x < 0 and platform.center_x < platform.start_x:
                platform.change_x *= -1

'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


