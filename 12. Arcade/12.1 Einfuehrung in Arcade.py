#              _______________________________________
#       ______|                                       |_____
#       \     |       12.1 EINFÜHRUNG IN ARCADE       |    /
#        )    |_______________________________________|   (
#       /________)                                (________\       4.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# Das Arcade-Modul ist ein beliebtes Python-Framework für die einfache Entwicklung 
# von 2D-Spielen und grafischen Anwendungen. Es bietet viele Funktionen, um Grafiken 
# und Animationen darzustellen, Benutzereingaben zu verarbeiten und eine interaktive 
# Umgebung für Spiele zu schaffen.

# _________________________________
#                                 /
# Installation und Import        (
# ________________________________\

# Um Arcade zu verwenden, musst du es zuerst installieren. In Thonny musst du dazu
# unter Werkzeuge > Verwalte Packete ... das arcade-Modul installieren. 

# Nachdem das Modul installiert ist, kannst du es in deinem Code importieren:

import arcade


# _________________________________
#                                 /
# Ein Fenster erstellen           (
# ________________________________\

# In Arcade wird ein Spielfenster mit der `arcade.Window`-Klasse erstellt. 
# Damit definieren wir die Grundstruktur des Spiels, legen Fenstergröße, Titel und Hintergrund fest.

# Hier ein Beispiel, um ein Fenster zu erstellen und anzuzeigen:

class MyGame(arcade.Window):
    def __init__(self):
        # Erstelle ein Fenster mit Titel und Hintergrund
        super().__init__(width=800, height=600, title="Mein erstes Arcade-Spiel")
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        # Zeichnet den Bildschirm jedes Mal, wenn die Fensterfläche aktualisiert wird
        arcade.start_render()
        arcade.draw_text("Willkommen in meinem ersten Arcade-Spiel!", 100, 300,
                         arcade.color.BLACK, 24)

# Ein Spiel-Objekt erstellen und die Schleife starten
window = MyGame()
arcade.run()




# _________________________________
#                                 /
# Grundlegende Methoden           (
# ________________________________\

# Die Hauptmethoden in einem Arcade-Spiel sind:
#
# - `setup()`: Wird verwendet, um das Spiel zu initialisieren.
#
# - `on_draw()`: Definiert, was auf dem Bildschirm gezeichnet wird.
#
# - `on_update(delta_time)`: Aktualisiert den Zustand des Spiels in bestimmten Intervallen.
# 
# Beispiel:

import arcade

import arcade

class SimpleGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Ein einfaches Arcade-Spiel")
        arcade.set_background_color(arcade.color.LIGHT_GREEN)
        
        self.center = (width // 2, height // 2)
        self.frame = 0

    def setup(self):
        print("Spiel ist bereit!")

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text(self.frame, self.center[0], self.center[1], arcade.color.BLACK, 24, anchor_x="center")
        arcade.draw_text("Arcade ist cool!", self.center[0], self.center[1]+40, arcade.color.BLACK, 24, anchor_x="center")

    def on_update(self, delta_time):
        self.frame += 1


game = SimpleGame(600, 400)
game.setup()
arcade.run()






# _________________________________
#                                 /
# Benutzer-Eingaben               (
# ________________________________\

# Arcade unterstützt Tastatur- und Maus-Eingaben für interaktive Spiele. Dies geschieht
# durch das Überschreiben von Methoden wie `on_key_press`, `on_key_release`,
# `on_mouse_motion` und `on_mouse_press`.

# Beispiel für Tastatursteuerung:

class ControlGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Tastatursteuerung")
        arcade.set_background_color(arcade.color.LIGHT_CORAL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Drücke eine Taste und betrachte die Konsole!", 150, 300,
                         arcade.color.BLACK, 20)

    def on_key_press(self, key, modifiers):
        print(f"Taste {key} wurde gedrückt.")

    def on_key_release(self, key, modifiers):
        print(f"Taste {key} wurde losgelassen.")

control_game = ControlGame()
arcade.run()




# _________________________________
#                                 /
# Zeichnen von Formen            (
# ________________________________\

# Arcade bietet verschiedene Zeichenfunktionen, z. B.:
# - `arcade.draw_circle_filled(x, y, radius, color)`: Zeichnet einen gefüllten Kreis.
# - `arcade.draw_rectangle_filled(x, y, width, height, color)`: Zeichnet ein gefülltes Rechteck.
# - `arcade.draw_line(x1, y1, x2, y2, color, line_width)`: Zeichnet eine Linie.

# Beispiel für das Zeichnen mehrerer Formen:

class ShapesGame(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Formen zeichnen")
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(300, 200, 50, arcade.color.BLUE)
        arcade.draw_rectangle_filled(300, 100, 60, 40, arcade.color.RED)
        arcade.draw_line(0, 0, 600, 400, arcade.color.GREEN, 3)

shapes_game = ShapesGame()
arcade.run()




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Installiere Arcade, um einfache 2D-Spiele zu entwickeln.
#
# - Verwende die `arcade.Window`-Klasse, um ein Spielfenster zu erstellen.
#
# - Hauptmethoden:
#   - `setup()`, `on_draw()`, `on_update()` zur Spielinitialisierung, 
#     Bildschirmzeichnung und Aktualisierung.
#
# - Arcade bietet viele Zeichenfunktionen, um Formen und Texte zu visualisieren.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein einfaches Arcade-Fenster mit einem hellgelben Hintergrund und
# zeige „Hallo, Arcade!“ in der Mitte des Bildschirms an.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Fenster mit einer Zeichenfläche. Zeichne in der Mitte des Fensters
# einen roten Kreis mit einem Radius von 40 und ein grünes Rechteck darunter.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Implementiere eine Anwendung, die auf Tastendrücke reagiert. Bei jedem
# Drücken der Leertaste soll der Text „Sprung!“ auf der Konsole ausgegeben werden.


# Füge hier deine Lösung ein.



#        ___------__
#   |\__-- /\       _-
#   |/    __      -
#   //\  /  \    /__                Arcade klingt nach Action.
#   |  o|  0|__     --_
#   \\____-- __ \   ___-
#   (@@    __/  / /_
#      -_____---   --_
#       //  \ \\   ___-
#     //|\__/  \\  \
#     \_-\_____/  \-\
#          // \\--\|   -Han J. Lee-
#     ____//  ||_
#    /_____\ /___\
#  ______________________
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
# Erstelle ein einfaches Arcade-Fenster mit einem hellgelben Hintergrund und
# zeige „Hallo, Arcade!“ in der Mitte des Bildschirms an.

'''
class HelloWorldWindow(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Hallo, Arcade!")
        arcade.set_background_color(arcade.color.LIGHT_YELLOW)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Hallo, Arcade!", self.width / 2, self.height / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

# Fenster starten
window = HelloWorldWindow()
arcade.run()
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Fenster mit einer Zeichenfläche. Zeichne in der Mitte des Fensters
# einen roten Kreis mit einem Radius von 40 und ein grünes Rechteck darunter.

'''
class ShapesWindow(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Zeichenfläche")
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.width / 2, self.height / 2,
                                  40, arcade.color.RED)
        arcade.draw_rectangle_filled(self.width / 2, (self.height / 2) - 60,
                                     80, 40, arcade.color.GREEN)

# Fenster starten
window = ShapesWindow()
arcade.run()
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Implementiere eine Anwendung, die auf Tastendrücke reagiert. Bei jedem
# Drücken der Leertaste soll der Text „Sprung!“ auf der Konsole ausgegeben werden.

'''
class KeyPressWindow(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Tastendruck")
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Drücke die Leertaste", self.width / 2, self.height / 2,
                         arcade.color.BLACK, font_size=24, anchor_x="center")

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            print("Sprung!")

# Fenster starten
window = KeyPressWindow()
arcade.run()
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

