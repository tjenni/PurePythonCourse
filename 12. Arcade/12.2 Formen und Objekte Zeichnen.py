#              ____________________________________________
#       ______|                                            |_____
#       \     |     12.2 FORMEN UND OBJEKTE ZEICHNEN       |    /
#        )    |____________________________________________|   (
#       /________)                                     (________\       4.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# In Arcade können verschiedene Formen und Objekte gezeichnet werden, um Spielumgebungen und 
# Charaktere zu gestalten. In diesem Kapitel lernst du, wie du Grundformen zeichnest und 
# sie in deinem Spielfenster anzeigst.

import arcade


# _________________________________
#                                 /
# Formen zeichnen                (
# ________________________________\

# Um Formen in `arcade` zu zeichnen, rufen wir Zeichnen-Funktionen innerhalb der 
# `on_draw()`-Methode auf. Hier sind einige der häufigsten Formen, die du verwenden kannst:

class ShapeDrawer(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Formen und Objekte zeichnen")
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        
        # Kreis zeichnen
        arcade.draw_circle_filled(100, 500, 50, arcade.color.BLUE)
        
        # Rechteck zeichnen
        arcade.draw_rectangle_filled(300, 500, 120, 60, arcade.color.RED)
        
        # Linie zeichnen
        arcade.draw_line(50, 450, 150, 450, arcade.color.BLACK, 5)
        
        # Dreieck zeichnen
        arcade.draw_triangle_filled(500, 500, 450, 400, 550, 400, arcade.color.GREEN)
        
        # Ellipse zeichnen
        arcade.draw_ellipse_filled(700, 500, 80, 50, arcade.color.ORANGE)
        
        # Polygon zeichnen
        arcade.draw_polygon_filled(((350, 250), (450, 300), (500, 250), (450, 200)), arcade.color.PURPLE)
        
        # Text zeichnen
        arcade.draw_text("Formen zeichnen mit Arcade", 200, 100, arcade.color.BLACK, 24)

# Erzeuge das Fenster und starte das Programm
window = ShapeDrawer()
arcade.run()




# _________________________________
#                                 /
# Farben und Transparenz          (
# ________________________________\

# Farben in `arcade` werden über `arcade.color` bereitgestellt. Transparenz kann 
# mit RGBA-Werten erreicht werden, wobei der Alpha-Wert die Transparenz festlegt 
# (0 = transparent, 255 = vollständig sichtbar).

class ColorExample(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Farben und Transparenz")
        arcade.set_background_color(arcade.color.LIGHT_GRAY)

    def on_draw(self):
        arcade.start_render()
        
        # Rechteck mit voller Deckkraft
        arcade.draw_rectangle_filled(200, 300, 100, 50, (255, 0, 0, 255))  # Rotes Rechteck
        
        # Rechteck mit Transparenz
        arcade.draw_rectangle_filled(400, 300, 100, 50, (0, 255, 0, 128))  # Halbtransparentes grünes Rechteck
        
        # Text mit Transparenz
        arcade.draw_text("Transparenz-Beispiel", 200, 100, (0, 0, 255, 128), 24)  # Halbtransparenter blauer Text

# Erzeuge das Fenster und starte das Programm
color_example = ColorExample()
arcade.run()




# _________________________________
#                                 /
# Wiederholte Objekte            (
# ________________________________\

# In vielen Spielen werden wiederholte Objekte wie Bäume oder Münzen verwendet. 
# Schleifen helfen, Objekte effizient zu wiederholen und an verschiedenen Positionen zu zeichnen.

class RepeatedObjects(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Wiederholte Objekte")
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        arcade.start_render()
        
        # Bäume in einer Schleife zeichnen
        for x in range(50, 800, 150):
            arcade.draw_triangle_filled(x, 150, x - 30, 50, x + 30, 50, arcade.color.DARK_GREEN)
            arcade.draw_rectangle_filled(x, 25, 20, 30, arcade.color.BROWN)

# Erzeuge das Fenster und starte das Programm
repeated_objects = RepeatedObjects()
arcade.run()




# _________________________________
#                                 /
# Position und Größe anpassen     (
# ________________________________\

# Arcade verwendet ein Koordinatensystem, bei dem (0, 0) die linke untere Ecke 
# des Fensters ist. Die Position und Größe der Formen können durch Parameter 
# in den Zeichnen-Funktionen angepasst werden.

# Beispiel: Ein beweglicher Kreis

class MovableCircle(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Beweglicher Kreis")
        arcade.set_background_color(arcade.color.LIGHT_CORAL)
        self.circle_x = 100
        self.circle_y = 300
        self.circle_radius = 50

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.circle_x, self.circle_y, self.circle_radius, arcade.color.BLUE)

    def on_update(self, delta_time):
        # Bewege den Kreis um 1 Pixel nach rechts
        self.circle_x += 1
        if self.circle_x > 800:
            self.circle_x = 0

movable_circle = MovableCircle()
arcade.run()




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - `arcade` bietet verschiedene Zeichnen-Funktionen wie `draw_circle_filled()`, 
#   `draw_rectangle_filled()`, usw.
#
# - Transparenz kann über RGBA-Werte eingestellt werden.
#
# - Wiederholte Objekte können effizient mit Schleifen erstellt werden.
#
# - Die Position von Objekten im Fenster lässt sich mit dem Koordinatensystem 
#   von `arcade` anpassen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Fenster, das fünf verschiedene geometrische Formen zeichnet: 
# einen Kreis, ein Rechteck, ein Dreieck, eine Linie und eine Ellipse. 
# Verwende Farben deiner Wahl und platziere die Formen im gesamten Fenster.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Arcade-Anwendung, die zehn Kreise in einer Reihe nebeneinander 
# anzeigt. Verwende eine Schleife, um die Kreise zu zeichnen und die Farbe 
# bei jedem Kreis zu ändern.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Entwickle eine Anwendung, die in einer Schleife ein kleines Quadrat 
# horizontal über das Fenster bewegt. Wenn das Quadrat das Fensterende erreicht, 
# soll es auf der linken Seite wieder erscheinen.


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
# Erstelle ein Fenster, das fünf verschiedene geometrische Formen zeichnet: 
# einen Kreis, ein Rechteck, ein Dreieck, eine Linie und eine Ellipse. 
# Verwende Farben deiner Wahl und platziere die Formen im gesamten Fenster.

'''
class ShapesWindow(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Verschiedene Formen")
        arcade.set_background_color(arcade.color.LIGHT_GRAY)

    def on_draw(self):
        arcade.start_render()
        # Kreis
        arcade.draw_circle_filled(100, 300, 50, arcade.color.RED)
        # Rechteck
        arcade.draw_rectangle_filled(500, 300, 80, 50, arcade.color.BLUE)
        # Dreieck
        arcade.draw_triangle_filled(150, 100, 200, 200, 250, 100, arcade.color.GREEN)
        # Linie
        arcade.draw_line(100, 50, 500, 50, arcade.color.BLACK, 5)
        # Ellipse
        arcade.draw_ellipse_filled(300, 200, 150, 80, arcade.color.PURPLE)

# Fenster starten
window = ShapesWindow()
arcade.run()
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Arcade-Anwendung, die zehn Kreise in einer Reihe nebeneinander 
# anzeigt. Verwende eine Schleife, um die Kreise zu zeichnen und die Farbe 
# bei jedem Kreis zu ändern.

'''
class RowCirclesWindow(arcade.Window):
    def __init__(self):
        super().__init__(600, 200, "Kreise in einer Reihe")
        arcade.set_background_color(arcade.color.WHITE)
        self.colors = [arcade.color.RED, arcade.color.GREEN, arcade.color.BLUE,
                       arcade.color.YELLOW, arcade.color.PURPLE, arcade.color.ORANGE,
                       arcade.color.PINK, arcade.color.BROWN, arcade.color.CYAN, arcade.color.BLACK]

    def on_draw(self):
        arcade.start_render()
        for i in range(10):
            arcade.draw_circle_filled(50 + i * 60, self.height // 2, 20, self.colors[i])

# Fenster starten
window = RowCirclesWindow()
arcade.run()
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Entwickle eine Anwendung, die in einer Schleife ein kleines Quadrat 
# horizontal über das Fenster bewegt. Wenn das Quadrat das Fensterende erreicht, 
# soll es auf der linken Seite wieder erscheinen.

'''
class MovingSquareWindow(arcade.Window):
    def __init__(self):
        super().__init__(600, 200, "Bewegendes Quadrat")
        arcade.set_background_color(arcade.color.WHITE)
        self.square_x = 0

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(self.square_x, self.height // 2, 30, 30, arcade.color.RED)

    def on_update(self, delta_time):
        self.square_x += 5
        if self.square_x > self.width:
            self.square_x = 0

# Fenster starten
window = MovingSquareWindow()
arcade.run()
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


