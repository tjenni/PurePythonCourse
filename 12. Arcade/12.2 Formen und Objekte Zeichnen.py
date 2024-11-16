#              ____________________________________________
#       ______|                                            |_____
#       \     |     12.2 FORMEN UND OBJEKTE ZEICHNEN       |    /
#        )    |____________________________________________|   (
#       /________)                                     (________\       16.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# In Arcade können verschiedene Formen und Objekte gezeichnet werden, um 
# Spielumgebungen und Charaktere zu gestalten. In diesem Kapitel lernst du, 
# wie du Grundformen zeichnest und sie in deinem Spielfenster anzeigst.


import arcade

# _________________________________
#                                 /
# Formen zeichnen                (
# ________________________________\

# Um Formen in `arcade` zu zeichnen, rufen wir Zeichnen-Funktionen innerhalb der 
# `on_draw()`-Methode auf. Hier sind einige der häufigsten Formen, 
# die du verwenden kannst. Unter dem folgenden Link findest du alle 
# Befehle, mit denen du Formen zeichnen kannst.

# https://api.arcade.academy/en/latest/api/drawing_primitives.html

class ShapeDrawer(arcade.Window):

    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)

        arcade.set_background_color(arcade.color.WHITE)


    def on_draw(self):
        arcade.start_render()
        
        # 1. Kreis zeichnen
        # -----------------
        # arcade.draw_circle_filled(x, y, radius, color)
        # - x, y: Die Koordinaten des Mittelpunkts des Kreises
        # - radius: Der Radius des Kreises
        # - color: Die Farbe des Kreises
        arcade.draw_circle_filled(100, 500, 50, arcade.color.BLUE)

        # 2. Rechteck zeichnen
        # ---------------------
        # arcade.draw_rectangle_filled(x, y, width, height, color)
        # - x, y: Die Koordinaten des Mittelpunkts des Rechtecks
        # - width, height: Breite und Höhe des Rechtecks
        # - color: Die Farbe des Rechtecks
        arcade.draw_rectangle_filled(300, 500, 120, 60, arcade.color.RED)

        # 3. Linie zeichnen
        # ------------------
        # arcade.draw_line(x1, y1, x2, y2, color, line_width)
        # - x1, y1: Startpunkt der Linie
        # - x2, y2: Endpunkt der Linie
        # - color: Die Farbe der Linie
        # - line_width: Die Breite der Linie
        arcade.draw_line(100, 300, 200, 400, arcade.color.BLACK, 5)

        # 4. Dreieck zeichnen
        # --------------------
        # arcade.draw_triangle_filled(x1, y1, x2, y2, x3, y3, color)
        # - x1, y1: Erste Ecke des Dreiecks
        # - x2, y2: Zweite Ecke des Dreiecks
        # - x3, y3: Dritte Ecke des Dreiecks
        # - color: Die Farbe des Dreiecks
        arcade.draw_triangle_filled(500, 500, 450, 400, 550, 400, arcade.color.GREEN)

        # 5. Ellipse zeichnen
        # --------------------
        # arcade.draw_ellipse_filled(x, y, width, height, color)
        # - x, y: Die Koordinaten des Mittelpunkts der Ellipse
        # - width, height: Breite und Höhe der Ellipse
        # - color: Die Farbe der Ellipse
        arcade.draw_ellipse_filled(700, 500, 80, 50, arcade.color.ORANGE)

        # 6. Polygon zeichnen
        # --------------------
        # arcade.draw_polygon_filled(point_list, color)
        # - point_list: Eine Liste von Punkten, die die Eckpunkte des Polygons definieren
        # - color: Die Farbe des Polygons
        # Beispiel: Ein Polygon mit 4 Ecken
        arcade.draw_polygon_filled(((350, 250), (450, 300), (500, 250), (450, 200)), arcade.color.PURPLE)

        # 7. Text zeichnen
        # -----------------
        # arcade.draw_text(text, start_x, start_y, color, font_size)
        # - text: Der anzuzeigende Text
        # - start_x, start_y: Die Position der unteren linken Ecke des Textes
        # - color: Die Farbe des Textes
        # - font_size: Die Größe der Schrift
        arcade.draw_text("Formen zeichnen mit Arcade", 200, 100, arcade.color.BLACK, 24)

# Erzeuge das Fenster und starte das Programm
window = ShapeDrawer(title="Formen und Objekte zeichnen")
arcade.run()




# _________________________________
#                                 /
# Farben und Transparenz         (
# ________________________________\

# Farben in `arcade` werden über `arcade.color` bereitgestellt. Transparenz kann 
# mit RGBA-Werten erreicht werden, wobei der Alpha-Wert die Transparenz festlegt 
# (0 = transparent, 255 = vollständig sichtbar).

class ColorExample(arcade.Window):

    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        
        # Rotes Rechteck mit voller Deckkraft
        arcade.draw_rectangle_filled(300, 300, 200, 100, (255, 0, 0, 255))
        
        # Halbtransparentes grünes Rechteck
        arcade.draw_rectangle_filled(400, 300, 100, 200, (0, 255, 0, 128))
        
        # Blauer Text mit Transparenz
        arcade.draw_text("Transparenz-Beispiel", 200, 300, (0, 0, 255, 128), 24)

# Erzeuge das Fenster und starte das Programm
color_example = ColorExample(title="Farben und Transparenz")
arcade.run()




# _________________________________
#                                 /
# Wiederholte Objekte            (
# ________________________________\

# In vielen Spielen werden wiederholte Objekte wie Bäume oder Münzen verwendet. 
# Schleifen helfen, Objekte effizient zu wiederholen und an verschiedenen 
# Positionen zu zeichnen.

class RepeatedObjects(arcade.Window):

    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)

        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        arcade.start_render()
        
        # Bäume in einer Schleife zeichnen
        for x in range(100, 800, 150):
            arcade.draw_triangle_filled(x, 350, x - 30, 250, x + 30, 250, arcade.color.DARK_GREEN)
            arcade.draw_rectangle_filled(x, 225, 20, 30, arcade.color.BROWN)

# Erzeuge das Fenster und starte das Programm
repeated_objects = RepeatedObjects(title="Wiederholte Objekte")
arcade.run()




# _________________________________
#                                 /
# Position und Größe anpassen    (
# ________________________________\

# Arcade verwendet ein Koordinatensystem, bei dem (0, 0) die linke untere Ecke 
# des Fensters ist. Die Position und Größe der Formen können durch Parameter 
# in den Zeichnen-Funktionen angepasst werden.

class MovableCircle(arcade.Window):

    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)

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

movable_circle = MovableCircle(title="Beweglicher Kreis")
arcade.run()




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# In diesem Kapitel hast du gelernt, wie du grundlegende Formen und Objekte mit der
# `arcade`-Bibliothek zeichnen kannst. Hier sind die wichtigsten Punkte zusammengefasst:

# 1. Grundformen zeichnen:
#    - Mit Funktionen wie `draw_circle_filled()`, `draw_rectangle_filled()` oder 
#      `draw_line()` kannst du Kreise, Rechtecke, Linien und viele weitere 
#      Formen erstellen.
#
#    - Jede Funktion bietet Parameter, um Position, Größe und Farbe der 
#      Form anzupassen.
# 
#    - Die Koordinaten (x, y) beziehen sich auf das Koordinatensystem von Arcade, 
#      bei dem (0, 0) die linke untere Ecke des Fensters ist.

# 2. Text zeichnen:
#    - Der Text wird mit der Funktion `arcade.draw_text()` gezeichnet.
#
#    - Du kannst Schriftgröße, Position, Farbe und den anzuzeigenden Text definieren.

# 3. Farben und Transparenz:
#    - Farben in Arcade sind einfach zu handhaben. Du kannst sie aus der 
#      `arcade.color`-Bibliothek auswählen.
#
#    - Für Transparenz verwendest du RGBA-Werte, wobei der Alpha-Wert (A) die 
#      Transparenz regelt (0 = vollständig transparent, 255 = vollständig deckend).

# 4. Wiederholte Objekte:
#    - Wenn du ähnliche Objekte wie Bäume, Münzen oder Kreise an verschiedenen 
#      Positionen erstellen möchtest, kannst du Schleifen verwenden.
#
#    - Dies spart Code und ermöglicht eine schnelle Platzierung von 
#      mehreren Objekten.

# 5. Position und Bewegung:
#    - Du kannst die Position und Größe von Formen dynamisch ändern, um 
#      bewegliche Objekte wie ein sich bewegendes Quadrat zu erstellen.
#
#    - Die Methode `on_update()` hilft dir, die Position eines Objekts bei 
#      jedem Frame zu aktualisieren.

# Arcade bietet viele weitere Zeichnen-Funktionen und Tools, die es dir ermöglichen, 
# komplexe Grafiken für Spiele und Simulationen zu erstellen.
#
# Mit einer Kombination aus Formen, Farben und Animationen kannst du 
# kreative und ansprechende Designs gestalten!




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
# Erstelle eine Arcade-Anwendung, die zehn konzentrische Kreise 
# anzeigt. Verwende eine Schleife, um die Kreise zu zeichnen und die Farbe 
# bei jedem Kreis zu ändern.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Entwickle eine Anwendung, die in einer Schleife ein kleines Quadrat 
# vertikal von oben nach unten über das Fenster bewegt. Wenn das Quadrat das 
# Fensterende erreicht, soll es oben wieder erscheinen.


# Füge hier deine Lösung ein.




#          _-_.
#       _-',^. `-_.
#   ._-' ,'   `.   `-_ 
#  !`-_._________`-':::           Formen zeichnen macht Spass. :-)
#  !   /\        /\::::
#  ;  /  \      /..\:::
#  ! /    \    /....\::
#  !/      \  /......\:
#  ;--.___. \/_.__.--;; 
#   '-_    `:!;;;;;;;'
#      `-_, :!;;;''
#          `-!'         mn
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
# Erstelle eine Arcade-Anwendung, die zehn konzentrische Kreise 
# anzeigt. Verwende eine Schleife, um die Kreise zu zeichnen und die Farbe 
# bei jedem Kreis zu ändern.

'''
class RowCirclesWindow(arcade.Window):
    
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        arcade.set_background_color(arcade.color.WHITE)
        
        self.colors = [arcade.color.RED, arcade.color.GREEN, arcade.color.BLUE,
                       arcade.color.YELLOW, arcade.color.PURPLE, arcade.color.ORANGE,
                       arcade.color.PINK, arcade.color.BROWN, arcade.color.CYAN, arcade.color.BLACK]

    def on_draw(self):
        arcade.start_render()
        
        for i in range(9):
            arcade.draw_circle_filled(400, 300, 200-10*i, self.colors[i])

# Fenster starten
window = RowCirclesWindow(title="Kreise in einer Reihe")
arcade.run()
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Entwickle eine Anwendung, die in einer Schleife ein kleines Quadrat 
# vertikal von oben nach unten über das Fenster bewegt. Wenn das Quadrat das 
# Fensterende erreicht, soll es oben wieder erscheinen.

'''
class MovingSquareWindow(arcade.Window):
    
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        arcade.set_background_color(arcade.color.WHITE)
        self.square_y = 600

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(self.width // 2, self.square_y, 30, 30, arcade.color.RED)

    def on_update(self, delta_time):
        self.square_y -= 5
        if self.square_y < 0:
            self.square_y = self.height

window = MovingSquareWindow(title="Bewegendes Quadrat")
arcade.run()
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


