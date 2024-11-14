#              ____________________________________________
#       ______|                                            |_____
#       \     |  12.3 SPIELERSTEUERUNG UND INTERAKTIVITÄT  |    /
#        )    |____________________________________________|   (
#       /________)                                     (________\       4.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# Die Spielersteuerung und Interaktivität sind zentrale Elemente für die Dynamik
# und das Spielerlebnis in einem Arcade-Spiel. In diesem Kapitel lernst du, 
# wie du die Steuerung und Benutzerinteraktionen implementieren kannst.

import arcade


# _________________________________
#                                 /
# Bewegung des Spielers          (
# ________________________________\

# Um einen Spieler zu bewegen, wird in `arcade` häufig das Tasteneingabesystem genutzt. 
# Hierzu verwenden wir `on_key_press()` und `on_key_release()`, um die Tastendrücke 
# zu erfassen, und `on_update()`, um die Position zu aktualisieren.

class PlayerControl(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Spielersteuerung und Interaktivität")
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
        
        # Spielerposition
        self.player_x = 400
        self.player_y = 300
        
        # Bewegungsgeschwindigkeit
        self.speed_x = 0
        self.speed_y = 0

    def on_draw(self):
        arcade.start_render()
        
        # Zeichne den Spieler (als Kreis dargestellt)
        arcade.draw_circle_filled(self.player_x, self.player_y, 20, arcade.color.RED)

    def on_update(self, delta_time):
        # Aktualisiere die Spielerposition
        self.player_x += self.speed_x
        self.player_y += self.speed_y

    def on_key_press(self, key, modifiers):
        # Bewege den Spieler mit den Pfeiltasten
        if key == arcade.key.UP:
            self.speed_y = 5
        elif key == arcade.key.DOWN:
            self.speed_y = -5
        elif key == arcade.key.LEFT:
            self.speed_x = -5
        elif key == arcade.key.RIGHT:
            self.speed_x = 5

    def on_key_release(self, key, modifiers):
        # Stoppe die Bewegung, wenn die Taste losgelassen wird
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.speed_y = 0
        elif key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.speed_x = 0

window = PlayerControl()
arcade.run()




# _________________________________
#                                 /
# Maussteuerung und Klicks       (
# ________________________________\

# In Arcade lassen sich die Mausposition und Klicks einfach abfragen. Die Methoden 
# `on_mouse_motion()`, `on_mouse_press()`, und `on_mouse_release()` erlauben die 
# Interaktion mit der Maus.

class MouseControl(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Maussteuerung")
        arcade.set_background_color(arcade.color.LIGHT_GREEN)
        
        # Spielerposition
        self.player_x = 400
        self.player_y = 300

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.player_x, self.player_y, 20, arcade.color.RED)

    def on_mouse_motion(self, x, y, dx, dy):
        # Spielerposition folgt der Mausbewegung
        self.player_x = x
        self.player_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        # Klickeffekt bei Mausklick
        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Klick!")

mouse_window = MouseControl()
arcade.run()




# _________________________________
#                                 /
# Grenzen des Spielfelds         (
# ________________________________\

# Um den Spieler innerhalb eines bestimmten Bereichs zu halten, können wir 
# die Position auf die Bildschirmränder begrenzen.

class BoundedMovement(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Begrenzte Bewegung")
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.player_x = 400
        self.player_y = 300
        self.speed_x = 0
        self.speed_y = 0

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.player_x, self.player_y, 20, arcade.color.RED)

    def on_update(self, delta_time):
        # Aktualisiere Position und halte den Spieler innerhalb der Grenzen
        self.player_x = max(20, min(self.player_x + self.speed_x, 780))
        self.player_y = max(20, min(self.player_y + self.speed_y, 580))

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.speed_y = 5
        elif key == arcade.key.DOWN:
            self.speed_y = -5
        elif key == arcade.key.LEFT:
            self.speed_x = -5
        elif key == arcade.key.RIGHT:
            self.speed_x = 5

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.speed_y = 0
        elif key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.speed_x = 0

bounded_movement = BoundedMovement()
arcade.run()




# _________________________________
#                                 /
# Zusammenfassung                (
# ________________________________\

# - Verwende `on_key_press()` und `on_key_release()`, um den Spieler über 
#   Tastatureingaben zu steuern.
#
# - Mausinteraktionen können mit `on_mouse_motion()`, `on_mouse_press()` und 
#  `on_mouse_release()` behandelt werden.
# 
# - Begrenze die Bewegung des Spielers mit max- und min-Funktionen, um ihn 
#   innerhalb der Spielfeldgrenzen zu halten.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine Anwendung, bei der ein Spieler durch Pfeiltasten gesteuert wird.
# Wenn der Spieler das Fenster verlässt, soll er am gegenüberliegenden Rand wieder erscheinen.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Anwendung, in der ein Objekt der Maus folgt, aber nur dann sichtbar ist,
# wenn die linke Maustaste gedrückt wird. Wenn die Maustaste losgelassen wird, soll
# das Objekt verschwinden.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Entwickle eine Anwendung, bei der ein Spieler über die Pfeiltasten gesteuert wird.
# Wenn der Spieler die Ränder des Fensters erreicht, soll eine Nachricht „Grenze erreicht!“ 
# auf der Konsole ausgegeben werden.


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
# Erstelle eine Anwendung, bei der ein Spieler durch Pfeiltasten gesteuert wird.
# Wenn der Spieler das Fenster verlässt, soll er am gegenüberliegenden Rand wieder erscheinen.

'''
import arcade

class WrapAroundPlayer(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Wrap Around Player")
        self.player_x = self.width // 2
        self.player_y = self.height // 2
        self.speed_x = 0
        self.speed_y = 0

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.player_x, self.player_y, 20, arcade.color.BLUE)
        
    def on_update(self, delta_time):
        # Aktualisiere die Spielerposition
        self.player_x += self.speed_x
        self.player_y += self.speed_y
        
        # Wenn der Spieler das Fenster verlässt, erscheint er auf der gegenüberliegenden Seite
        if self.player_x > self.width:
            self.player_x = 0
        elif self.player_x < 0:
            self.player_x = self.width
        if self.player_y > self.height:
            self.player_y = 0
        elif self.player_y < 0:
            self.player_y = self.height

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.speed_y = 5
        elif key == arcade.key.DOWN:
            self.speed_y = -5
        elif key == arcade.key.LEFT:
            self.speed_x = -5
        elif key == arcade.key.RIGHT:
            self.speed_x = 5

# Anwendung starten
window = WrapAroundPlayer()
arcade.run()
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Anwendung, in der ein Objekt der Maus folgt, aber nur dann sichtbar ist,
# wenn die linke Maustaste gedrückt wird. Wenn die Maustaste losgelassen wird, soll
# das Objekt verschwinden.

'''
import arcade

class MouseFollower(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Mouse Follower")
        self.circle_x = 0
        self.circle_y = 0
        self.is_visible = False

    def on_draw(self):
        arcade.start_render()
        if self.is_visible:
            arcade.draw_circle_filled(self.circle_x, self.circle_y, 20, arcade.color.RED)

    def on_mouse_motion(self, x, y, dx, dy):
        self.circle_x = x
        self.circle_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.is_visible = True

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.is_visible = False

# Anwendung starten
window = MouseFollower()
arcade.run()

'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Entwickle eine Anwendung, bei der ein Spieler über die Pfeiltasten gesteuert wird.
# Wenn der Spieler die Ränder des Fensters erreicht, soll eine Nachricht „Grenze erreicht!“ 
# auf der Konsole ausgegeben werden.

'''
import arcade

class BorderAlertPlayer(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Border Alert Player")
        self.player_x = self.width // 2
        self.player_y = self.height // 2
        self.speed_x = 0
        self.speed_y = 0

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.player_x, self.player_y, 20, arcade.color.GREEN)
        
    def on_update(self, delta_time):
        # Aktualisiere die Spielerposition
        self.player_x += self.speed_x
        self.player_y += self.speed_y
        
        # Prüfen, ob der Spieler den Rand des Fensters erreicht hat
        if self.player_x <= 0 or self.player_x >= self.width:
            print("Grenze erreicht!")
        if self.player_y <= 0 or self.player_y >= self.height:
            print("Grenze erreicht!")
    
    # Bewege den Spieler mit den Pfeiltasten    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.speed_y = 5
        elif key == arcade.key.DOWN:
            self.speed_y = -5
        elif key == arcade.key.LEFT:
            self.speed_x = -5
        elif key == arcade.key.RIGHT:
            self.speed_x = 5

# Anwendung starten
window = BorderAlertPlayer()
arcade.run()
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

