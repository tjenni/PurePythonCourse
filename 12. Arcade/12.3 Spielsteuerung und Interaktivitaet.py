#              ____________________________________________
#       ______|                                            |_____
#       \     |  12.3 SPIELERSTEUERUNG UND INTERAKTIVITÄT  |    /
#        )    |____________________________________________|   (
#       /________)                                     (________\       16.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# Die Spielersteuerung und Interaktivität sind zentrale Elemente für die Dynamik
# und das Spielerlebnis in einem Arcade-Spiel. In diesem Kapitel lernst du, 
# wie du die Steuerung und Benutzerinteraktionen implementieren kannst.


import arcade

# _________________________________
#                                 /
# Bewegung des Spielers          (
# ________________________________\

# In Arcade wird die Bewegung eines Spielers häufig über Tasteneingaben gesteuert.
# Die wichtigsten Methoden hierfür sind:
# - `on_key_press()`: Diese Methode wird aufgerufen, wenn eine Taste gedrückt wird.
#
# - `on_key_release()`: Diese Methode wird aufgerufen, wenn eine Taste losgelassen wird.
#
# - `on_update()`: Diese Methode wird regelmäßig aufgerufen, um die Position oder 
#   andere Zustände zu aktualisieren.

# Die folgende Klasse demonstriert, wie du Tasten zur Spielerbewegung nutzt:

class PlayerControl(arcade.Window):

    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
        
        # Spielerposition
        self.player_x = 400
        self.player_y = 300
        
        # Bewegungsgeschwindigkeit
        self.speed_x = 0
        self.speed_y = 0
    
    # Zeichne den Spieler (als Kreis dargestellt)
    def on_draw(self):
        arcade.start_render()
        
        arcade.draw_circle_filled(self.player_x, self.player_y, 20, arcade.color.RED)
    
    # Aktualisiere die Spielerposition
    def on_update(self, delta_time):
        self.player_x += self.speed_x
        self.player_y += self.speed_y
    
    # Bewege den Spieler mit den Pfeiltasten
    def on_key_press(self, key, modifiers):
        '''
        Diese Methode wird aufgerufen, wenn eine Taste gedrückt wird.

        Parameter:
        - `key`: Die gedrückte Taste (z. B. `arcade.key.UP`).
        - `modifiers`: Zusätzliche Modifier-Tasten wie Shift, Alt oder Ctrl.
        '''
        if key == arcade.key.UP:
            self.speed_y = 5
        elif key == arcade.key.DOWN:
            self.speed_y = -5
        elif key == arcade.key.LEFT:
            self.speed_x = -5
        elif key == arcade.key.RIGHT:
            self.speed_x = 5
    
    # Stoppe die Bewegung, wenn die Taste losgelassen wird
    def on_key_release(self, key, modifiers):
        '''
        Diese Methode wird aufgerufen, wenn eine Taste losgelassen wird.

        Parameter:
        - `key`: Die losgelassene Taste (z. B. `arcade.key.UP`).
        - `modifiers`: Zusätzliche Modifier-Tasten wie Shift, Alt oder Ctrl.
        '''
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.speed_y = 0
        elif key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.speed_x = 0

window = PlayerControl(title="Spielersteuerung und Interaktivität")
arcade.run()


# Wichtige Hinweise 
# _________________

# 1. Tastenbelegung:
#    - Arcade bietet eine breite Palette an Tasten, die du verwenden kannst.
#    - Beispiele:`arcade.key.A`, `arcade.key.SPACE` (Leertaste), 
#      `arcade.key.ENTER` (Eingabetaste).
#
#    - Die vollständige Liste findest du hier:
#      https://api.arcade.academy/en/latest/arcade.key.html

# 2. Modifikatoren:
#    - Zusätzliche Modifikatoren wie `Shift`, `Ctrl` oder `Alt` können mit 
#      `modifiers` überprüft werden.
#
#    - Beispiele:
#        - `modifiers & arcade.key.MOD_SHIFT` prüft, ob Shift gedrückt wird.
#        - `modifiers & arcade.key.MOD_CTRL` prüft, ob Ctrl gedrückt wird.
#        - `modifiers & arcade.key.MOD_ALT` prüft, ob Alt gedrückt wird.




# _________________________________
#                                 /
# Maussteuerung und Klicks       (
# ________________________________\

# In Arcade lassen sich die Mausposition und Klicks einfach abfragen. Die Methoden 
# `on_mouse_motion()`, `on_mouse_press()`, und `on_mouse_release()` erlauben die 
# Interaktion mit der Maus.

class MouseControl(arcade.Window):

    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)

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

mouse_window = MouseControl(title="Maussteuerung")
arcade.run()




# _________________________________
#                                 /
# Grenzen des Spielfelds         (
# ________________________________\

# Um den Spieler innerhalb eines bestimmten Bereichs zu halten, können wir 
# die Position auf die Bildschirmränder begrenzen.

class BoundedMovement(arcade.Window):

    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
    
        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.radius = 20

        self.player_x = 400
        self.player_y = 300

        self.speed_x = 0
        self.speed_y = 0

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.player_x, self.player_y, self.radius, arcade.color.RED)

    def on_update(self, delta_time):
        # Aktualisiere Position und halte den Spieler innerhalb der Grenzen
        self.player_x += self.speed_x
        self.player_y += self.speed_y

        # Links
        if self.player_x < self.radius:
            self.player_x = self.radius
        # Rechts
        elif self.player_x > self.width - self.radius:
            self.player_x = self.width - self.radius
        # Unten
        if self.player_y < self.radius:
            self.player_y = self.radius
        # Oben
        elif self.player_y > self.height - self.radius:
            self.player_y = self.height - self.radius

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

bounded_movement = BoundedMovement(title="Begrenzte Bewegung")
arcade.run()




# _________________________________
#                                 /
# Zusammenfassung                (
# ________________________________\

# Spielersteuerung und Interaktivität sind zentrale Elemente eines Arcade-Spiels.
# Mit den folgenden Konzepten und Methoden kannst du dynamische und interaktive 
# Spiele entwickeln:

# 1. Tastatureingaben
# - Verwende `on_key_press()` und `on_key_release()`, um die Eingaben der Tastatur 
#   zu verarbeiten.
#
# - Beispiele:
#   - `on_key_press(key, modifiers)`: Wird aufgerufen, wenn eine Taste gedrückt wird.
#
#   - `on_key_release(key, modifiers)`: Wird aufgerufen, wenn eine Taste losgelassen wird.
#
# - Wichtige Tasten:
#   - Pfeiltasten: `arcade.key.UP`, `arcade.key.DOWN`, `arcade.key.LEFT`, `arcade.key.RIGHT`
#
#   - Weitere Tasten wie `arcade.key.W`, `arcade.key.SPACE` (Leertaste) können für 
#     individuelle Steuerungen genutzt werden.

# 2. Modifikatoren
# - Zusätzliche Tasten wie `Shift`, `Ctrl` oder `Alt` können mit Modifikatoren (`modifiers`) kombiniert werden.
# - Beispiel:
#   - `modifiers & arcade.key.MOD_SHIFT` prüft, ob die Shift-Taste gedrückt ist.


# 3. Mausinteraktionen
# - Verwende `on_mouse_motion()`, `on_mouse_press()`, und `on_mouse_release()` für Maussteuerungen.
#
# - Beispiele:
#   - Spielerposition an die Maus koppeln (`on_mouse_motion(x, y, dx, dy)`).
#
#   - Klickereignisse abfangen (`on_mouse_press(x, y, button, modifiers)`).

# 4. Begrenzungen des Spielfelds
# - Begrenze die Bewegung des Spielers durch Abfragen der Spielfeldränder:
#   ```python
#   if self.player_x < 0:
#       self.player_x = 0
#   elif self.player_x > self.width:
#       self.player_x = self.width
#   ```
# - Alternativ kann der Spieler das Fenster verlassen und auf der gegenüberliegenden 
#   Seite wieder erscheinen ("Periodic-Boundary").




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
# Wenn der Spieler das Fenster verlässt, soll er am gegenüberliegenden Rand 
# wieder erscheinen.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Anwendung, in der ein Objekt der Maus folgt. Wenn die linke
# Maustaste gedrückt wird, soll das Objekt verschwinden. Wenn die Maustaste 
# losgelassen wird, soll das Objekt wieder erscheinen.


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



#        _=====_                               _=====_
#       / _____ \                             / _____ \
#     +.-'_____'-.---------------------------.-'_____'-.+
#    /   |     |  '.        S O N Y        .'  |  _  |   \
#   / ___| /|\ |___ \                     / ___| /_\ |___ \
#  / |      |      | ;  __           _   ; | _         _ | ;
#  | | <---   ---> | | |__|         |_:> | ||_|       (_)| |
#  | |___   |   ___| ;SELECT       START ; |___       ___| ;
#  |\    | \|/ |    /  _     ___      _   \    | (X) |    /|
#  | \   |_____|  .','" "', |___|  ,'" "', '.  |_____|  .' |
#  |  '-.______.-' /       \ANALOG/       \  '-._____.-'   |
#  |               |       |------|       |                |
#  |              /\       /      \       /\               |
#  |             /  '.___.'        '.___.'  \              |
#  |            /                            \             |
#   \          /                              \           /
#    \________/                                \_________/
#
#       Jetzt kannst du die Spielfigur kontrollieren. 
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
# Erstelle eine Anwendung, bei der ein Spieler durch Pfeiltasten gesteuert wird.
# Wenn der Spieler das Fenster verlässt, soll er am gegenüberliegenden Rand wieder erscheinen.

'''
import arcade

class PeriodicBoundary(arcade.Window):
    
    def __init__(self, width=600, height=400, title=""):
        super().__init__(width=width, height=height, title=title)
        
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
            
    def on_key_release(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.speed_y = 0
        elif key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.speed_x = 0

window = PeriodicBoundary(title="Periodic Boundary")
arcade.run()
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Anwendung, in der ein Objekt der Maus folgt. Wenn die linke
# Maustaste gedrückt wird, soll das Objekt verschwinden. Wenn die Maustaste 
# losgelassen wird, soll das Objekt wieder erscheinen.

'''
import arcade

class MouseFollower(arcade.Window):
    
    def __init__(self, width=600, height=400, title=""):
        super().__init__(width=width, height=height, title=title)
        
        self.circle_x = 0
        self.circle_y = 0
        self.is_visible = True

    def on_draw(self):
        arcade.start_render()
        if self.is_visible:
            arcade.draw_circle_filled(self.circle_x, self.circle_y, 20, arcade.color.RED)

    def on_mouse_motion(self, x, y, dx, dy):
        self.circle_x = x
        self.circle_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.is_visible = False

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.is_visible = True

# Anwendung starten
window = MouseFollower(title="Mouse Follower")
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
    
    def __init__(self, width=600, height=400, title=""):
        super().__init__(width=width, height=height, title=title)
        
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
            
    def on_key_release(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.speed_y = 0
        elif key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.speed_x = 0

# Anwendung starten
window = BorderAlertPlayer(title="Border Alert Player")
arcade.run()
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

