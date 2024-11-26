#              ____________________________
#       ______|                            |_____
#       \     |     12.4.1 SNAKE-SPIEL     |    /
#        )    |____________________________|   (
#       /________)                     (________\     26.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Das Snake-Spiel ist ein Klassiker der Videospielgeschichte. Ursprünglich für 
# einfache Geräte wie Mobiltelefone oder Taschenrechner entwickelt, erfreut sich 
# das Spiel aufgrund seiner Einfachheit und hohen Wiederspielbarkeit bis heute 
# großer Beliebtheit.

# In diesem Kapitel lernst du, wie du ein Snake-Spiel mit `arcade` programmierst. 
# Du wirst die grundlegende Spiellogik, das Bewegungssystem der Schlange, das 
# Einsammeln von Nahrung und die Endbedingungen (Game Over) implementieren.

# Die zentralen Themen in diesem Kapitel sind:
# - Bewegung der Schlange und Richtungswechsel durch Tasteneingaben.
# - Hinzufügen neuer Segmente, wenn die Schlange Nahrung frisst.
# - Überprüfung auf Kollisionen mit den Wänden und dem eigenen Körper.
# - Punktesystem und Neustart des Spiels.


# _____________________________
#                             /
# Aufbau des Spiels          (
# ____________________________\

# Das Spielfeld besteht aus einem Raster, auf dem die Schlange sich bewegt. 
# Die Schlange besteht aus mehreren Segmenten, die jeweils einen Bereich des 
# Rasters belegen. Das Spielziel ist es, so viel Nahrung wie möglich zu fressen, 
# ohne mit den Wänden oder dem eigenen Körper zu kollidieren.

import arcade
import random


# Diese Klasse repräsentiert das Snake-Spiel.
class SnakeGame(arcade.Window):
    
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        # Hintergrundfarbe setzen
        arcade.set_background_color(arcade.color.BLACK)
        
        # Schlange und andere Spielobjekte initialisieren
        self.snake = None  # Liste der Segmente, die die Schlange darstellen
        self.food = None  # Position der Nahrung
        self.direction = None  # Richtung, in die sich die Schlange bewegt
        self.score = 0  # Aktueller Punktestand
        self.game_over = False  # Spielstatus
        
        # Timer zur Steuerung der Bewegungsgeschwindigkeit
        self.move_timer = 0

        self.tile_size = 20 
        self.snake_speed = 5  # Geschwindigkeit der Schlange in Updates pro Sekunde
        

    # Setzt das Spiel zurück und startet eine neue Runde.
    def setup(self):
        # Schlange initialisieren
        self.snake = [
            [self.width // 2, self.height // 2],  # Kopf der Schlange
        ]
        
        self.direction = "UP"  # Anfangsrichtung der Schlange
        self.spawn_food()  # Nahrung auf dem Spielfeld platzieren
        self.score = 0  # Punktestand zurücksetzen
        self.game_over = False  # Spielstatus zurücksetzen

    # Platziert die Nahrung an einer zufälligen Position auf dem Spielfeld.
    def spawn_food(self):
        while True:
            # Zufällige Position innerhalb des Spielfelds
            x = random.randint(0, (self.width // self.tile_size) - 1) * self.tile_size
            y = random.randint(0, (self.height // self.tile_size) - 1) * self.tile_size
            
            # Stelle sicher, dass die Nahrung nicht auf der Schlange erscheint
            if [x, y] not in self.snake:
                self.food = [x, y]
                break

    # Zeichnet alle Elemente des Spiels.
    def on_draw(self):
        arcade.start_render()
        
        # Schlange zeichnen
        for segment in self.snake:
            arcade.draw_rectangle_filled(
                segment[0] + self.tile_size // 2,
                segment[1] + self.tile_size // 2,
                self.tile_size,
                self.tile_size,
                arcade.color.GREEN
            )
        
        # Nahrung zeichnen
        arcade.draw_rectangle_filled(
            self.food[0] + self.tile_size // 2,
            self.food[1] + self.tile_size // 2,
            self.tile_size,
            self.tile_size,
            arcade.color.RED
        )
        
        # Punktestand anzeigen
        arcade.draw_text(
            f"Punkte: {self.score}",
            10,
            self.height - 30,
            arcade.color.WHITE,
            16
        )
        
        # Game-Over-Bildschirm anzeigen, falls das Spiel vorbei ist
        if self.game_over:
            arcade.draw_text(
                "GAME OVER",
                self.width // 2,
                self.height // 2,
                arcade.color.WHITE,
                30,
                anchor_x="center"
            )
            arcade.draw_text(
                "Drücke R für Neustart",
                self.width // 2,
                self.height // 2 - 50,
                arcade.color.GRAY,
                20,
                anchor_x="center"
            )

    # Bewegt die Schlange und überprüft Kollisionen.
    def on_update(self, delta_time):
        if self.game_over:
            return

        # Aktualisiere den Timer und bewege die Schlange entsprechend der Geschwindigkeit
        self.move_timer += delta_time
        if self.move_timer < 1 / self.snake_speed:
            return
        self.move_timer = 0
        
        # Aktuellen Kopf der Schlange bestimmen
        head_x, head_y = self.snake[0]

        # Bewegung basierend auf der aktuellen Richtung
        if self.direction == "UP":
            head_y += self.tile_size
        elif self.direction == "DOWN":
            head_y -= self.tile_size
        elif self.direction == "LEFT":
            head_x -= self.tile_size
        elif self.direction == "RIGHT":
            head_x += self.tile_size
        
        # Neue Position des Kopfes hinzufügen
        new_head = [head_x, head_y]
        self.snake.insert(0, new_head)
        
        # Überprüfung: Nahrung eingesammelt?
        if new_head == self.food:
            self.score += 1
            self.spawn_food()  # Neue Nahrung generieren
        else:
            self.snake.pop()  # Letztes Segment der Schlange entfernen
        
        # Überprüfung: Kollisionen
        if (
            head_x < 0 or head_x >= self.width or
            head_y < 0 or head_y >= self.height or
            new_head in self.snake[1:]
        ):
            self.game_over = True  # Spiel ist vorbei

    # Verarbeitet die Tasteneingaben für die Steuerung der Schlange.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP and self.direction != "DOWN":
            self.direction = "UP"
        elif key == arcade.key.DOWN and self.direction != "UP":
            self.direction = "DOWN"
        elif key == arcade.key.LEFT and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif key == arcade.key.RIGHT and self.direction != "LEFT":
            self.direction = "RIGHT"
        
        # Neustart bei Game Over
        if self.game_over and key == arcade.key.R:
            self.setup()


# Hauptprogramm starten
game = SnakeGame(title="Snake Spiel")
game.setup()
arcade.run()




# ____________________________
#                            /
# Zusammenfassung            (
# ____________________________\

# In diesem Kapitel hast du ein vollständiges Snake-Spiel erstellt. 
# Du hast gelernt:
# - Wie man eine Schlange auf einem Spielfeld bewegt und steuert.
# - Wie man Kollisionen überprüft, um Spielregeln umzusetzen.
# - Wie man einfache Objekte wie Nahrung zufällig generiert.
# - Wie man einen Punktestand und einen Neustart-Mechanismus implementiert.

# Dieses Grundgerüst kann leicht erweitert werden, z. B. durch:
# - Hinzufügen von Hindernissen auf dem Spielfeld.
# - Verschiedene Schwierigkeitsstufen mit steigender Geschwindigkeit.
# - Power-Ups, die die Schlange schneller oder länger machen.


# ____________________________
#                            /
# Übungsaufgaben            (
# ____________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erweitere das Spiel, indem du Hindernisse auf dem Spielfeld hinzufügst.
# Wenn die Schlange mit einem Hindernis kollidiert, endet das Spiel.


# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Implementiere einen Mechanismus, bei dem die Geschwindigkeit der Schlange
# mit jedem eingesammelten Punkt zunimmt.


# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Füge verschiedene Power-Ups hinzu, z. B. eines, das die Schlange schneller 
# macht, und eines, das sie für kurze Zeit unbesiegbar macht.


