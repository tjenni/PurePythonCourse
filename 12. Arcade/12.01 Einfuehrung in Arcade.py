#              _______________________________________
#       ______|                                       |_____
#       \     |       12.1 EINFÜHRUNG IN ARCADE       |    /
#        )    |_______________________________________|   (
#       /________)                                (________\       2.3.25 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


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

# Nachdem das Modul installiert ist, kannst du es in deinem Code importieren.


import arcade


# _________________________________
#                                 /
# Ein Fenster erstellen          (
# ________________________________\

# In Arcade wird ein Spielfenster mit der `arcade.Window`-Klasse erstellt. 
# Damit definieren wir die Grundstruktur des Spiels, legen Fenstergröße, Titel 
# und Hintergrund fest.

# Hier ein Beispiel, um ein Fenster zu erstellen und anzuzeigen:

class MyFirstGame(arcade.Window):

    # Erstelle ein Fenster mit Titel und Hintergrund
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)

        self.background_color = arcade.csscolor.SKY_BLUE

    # Zeichnet den Bildschirm jedes Mal, wenn die Fensterfläche aktualisiert wird
    def on_draw(self):
        
        # löscht den Bildschirm
        self.clear()
        
        arcade.draw_text("Willkommen bei Arcade!", 400, 300, 
                            arcade.color.BLACK, 24, 
                            anchor_x="center")

# Ein Spiel-Objekt erstellen und die Schleife starten
window = MyFirstGame(800,600, "Mein erstes Arcade-Spiel")
arcade.run()




# _________________________________
#                                 /
# Grundlegende Methoden          (
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

class SimpleGame(arcade.Window):
    
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        self.background_color = arcade.csscolor.LIGHT_GREEN
        
        self.frame = 0

    def setup(self):
        print("Spiel ist bereit!")

    def on_draw(self):
        self.clear()

        arcade.draw_text(self.frame, 400, 300, 
                            arcade.color.BLACK, 24, 
                            anchor_x="center")

        arcade.draw_text("Arcade ist cool!", 400, 260,
                            arcade.color.BLACK, 24, 
                            anchor_x="center")

    def on_update(self, delta_time):
        self.frame += 1


game = SimpleGame(title="Ein einfaches Arcade-Spiel")
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
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        self.background_color = arcade.csscolor.LIGHT_CORAL
        

    def on_draw(self):
        self.clear()
        arcade.draw_text("Drücke eine Taste und betrachte die Konsole!", 400, 300,
                         arcade.color.BLACK, 20,
                         anchor_x="center")

    def on_key_press(self, key, modifiers):
        print(f"Taste {key} wurde gedrückt.")

    def on_key_release(self, key, modifiers):
        print(f"Taste {key} wurde losgelassen.")

control_game = ControlGame(title="Tasten drücken")
arcade.run()




# _________________________________
#                                 /
# Zeichnen von Formen            (
# ________________________________\

# Arcade bietet verschiedene Zeichenfunktionen, z. B.:
# - `arcade.draw_circle_filled(x, y, radius, color)`: Zeichnet einen gefüllten Kreis.
# - `arcade.draw_rect_filled(x, y, width, height, color)`: Zeichnet ein gefülltes Rechteck.
# - `arcade.draw_line(x1, y1, x2, y2, color, line_width)`: Zeichnet eine Linie.

# Beispiel für das Zeichnen mehrerer Formen:

class ShapesGame(arcade.Window):
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        self.background_color = arcade.csscolor.WHITE
        

    def on_draw(self):
        self.clear()
        
        arcade.draw_circle_filled(200, 300, 50, arcade.color.BLUE)
        arcade.draw_rect_filled(arcade.rect.XYWH(500, 300, 100, 50), arcade.color.RED)
        arcade.draw_line(0, 0, 800, 600, arcade.color.GREEN, 3)

shapes_game = ShapesGame(title="Formen zeichnen")
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
# einen roten Kreis mit einem Radius von 100 und ein grünes Rechteck darunter.


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
#                             |___/            


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein einfaches Arcade-Fenster mit einem hellgelben Hintergrund und
# zeige „Hallo, Arcade!“ in der Mitte des Bildschirms an.

'''
class HelloWorldWindow(arcade.Window):
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        self.background_color = arcade.csscolor.LIGHT_YELLOW
        

    def on_draw(self):
        self.clear()
        arcade.draw_text("Hallo, Arcade!", self.width / 2, self.height / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

# Fenster starten
window = HelloWorldWindow(title="Aufgabe 1")
arcade.run()
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Fenster mit einer Zeichenfläche. Zeichne in der Mitte des Fensters
# einen roten Kreis mit einem Radius von 100 und ein grünes Rechteck darunter.

'''
class ShapesWindow(arcade.Window):
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        self.background_color = arcade.color.WHITE
        

    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(self.width / 2, self.height / 2,
                                  100, arcade.color.RED)
        
        arcade.draw_rect_filled(arcade.rect.XYWH(self.width // 2, (self.height // 2) - 120, 80, 40), arcade.color.GREEN)

# Fenster starten
window = ShapesWindow(title="Aufgabe 2")
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
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        self.background_color = arcade.csscolor.SKY_BLUE
        

    def on_draw(self):
        self.clear()
        arcade.draw_text("Drücke die Leertaste", self.width / 2, self.height / 2,
                         arcade.color.BLACK, font_size=24, anchor_x="center")

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            print("Sprung!")

# Fenster starten
window = KeyPressWindow(title="Aufgabe 3")
arcade.run()
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

