#              ________________________________________________
#       ______|                                                |_____
#       \     |         13.4 ANIMATIONEN MIT ARCADE            |    /
#        )    |________________________________________________|   (
#       /________)                                         (________\      13.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# In diesem Kapitel erweitern wir die physikalischen Simulationen aus dem
# vorherigen Abschnitt und erstellen Animationen mit der Arcade-Bibliothek.
# Der Vorteil von Arcade ist, dass die grafische Darstellung sehr schnell 
# abläuft. Daher ist Arcade ideal für die Darstellung von Objekten und 
# zur Implementierung interaktiver Animationen.


# __________________________________________
#                                          /
# Grundkonzepte der Animation mit Arcade  (
# _________________________________________\

# Die grundlegenden Schritte zur Erstellung einer Animation mit Arcade sind:
#
# 1. Initialisiere das Fenster `arcade.Window`.
#
# 2. Zeichne die Objekte in der `on_draw`-Methode.
#
# 3. Aktualisiere die Position und Bewegung der Körper in jedem Frame 
#    mithilfe der `on_update`-Methode.


# ___________________________
#                           /
# Installation von Arcade  (
# __________________________\

# Installiere die Arcade-Bibliothek in Thonny, falls du sie noch nicht 
# installiert hast.

import arcade
import arcade.gui 
import numpy as np

# _________________________________
#                                 /
# Klassenstruktur für Animation  (
# ________________________________\

# Die Klasse `Body` modelliert ein physikalisches Objekt in der Simulation, 
# das durch seine Position, Geschwindigkeit und Masse beschrieben wird.

class Body:
    def __init__(self, position, velocity, mass=1.0, radius=1.0, color=arcade.color.BLUE):
        self.mass = mass                                 # Masse in kg
        self.position = np.array(position, dtype=float)  # Position in m
        self.velocity = np.array(velocity, dtype=float)  # Geschwindigkeit in m/s
        self.acceleration = np.array([0.0, 0.0])         # Beschleunigung in m/s^2
        self.force = np.array([0.0, 0.0])                # Resultierende Kraft in N
        self.radius = radius                             # Radius des Körpers in m
        self.color = color                               # Farbe für die Darstellung


    # Setzt die resultierende Kraft auf null
    def clear_force(self):
        self.force = np.array([0.0, 0.0])


    # Fügt eine Kraft zum Objekt hinzu, z.B. die Schwerkraft
    def add_force(self, force):
        self.force += np.array(force, dtype=float)


    # Berechnet die neue Geschwindigkeit und Position mithilfe des 
    # Euler-Cromer-Verfahrens, wobei die Beschleunigung auf Basis der Kraft 
    # und Masse aktualisiert wird.
    def update_ec(self, dt):
        self.acceleration = self.force / self.mass
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt
        


# Die Klasse `AnimationWindow` steuert die grafische Darstellung und die Simulation 
# der Partikelbewegungen.
class AnimationWindow(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        
        # Hintergrundfarbe des Fensters auf Weiß setzen
        arcade.set_background_color(arcade.color.WHITE)
        
        # Minimale Fenstergröße festlegen
        self.set_min_size(width, height)
        
        # Skalierungsfaktor in Pixel/Meter für die Darstellung
        self.scale = 50                       
        
        # Ursprung des Koordinatensystems in die Mitte des Fensters setzen
        self.center = [width // 2 + 100, height // 2]  
        
        # Liste für alle zu simulierenden Körper
        self.bodies = []

        # Simulationszeit in Sekunden
        self.time = 0
        
        # Simulationsstatus (0 = Pause, 1 = Ausführen)
        self.state = 0
        
        # FPS-Berechnung mit gleitendem Durchschnitt
        self.fps_history = [0] * 30
        
        # UI-Manager zur Steuerung der Benutzeroberfläche (Buttons)
        self.uimanager = arcade.gui.UIManager() 
        self.uimanager.enable() 
  
        # Standardstil für Buttons
        default_style = {
            "font_name": ("calibri", "arial"),
            "font_size": 10,
            "font_color": arcade.color.BLACK,
            "border_width": 2,
            "border_color": arcade.color.BLACK,
            "bg_color": arcade.color.WHITE,
            "bg_color_pressed": arcade.color.BLACK,
            "border_color_pressed": arcade.color.BLACK,
            "font_color_pressed": arcade.color.WHITE,
        }
        
        # Erstellen einer vertikalen Box für die Buttons
        v_box = arcade.gui.UIBoxLayout()
        
        # Start/Stop-Button erstellen
        self.start_button = arcade.gui.UIFlatButton(text="Start", height=30, style=default_style)
        self.start_button.on_click = self.on_click_start
        
        v_box.add(self.start_button.with_space_around(bottom=20))
        
        # UI-Komponenten zur Benutzeroberfläche hinzufügen
        self.uimanager.add( 
            arcade.gui.UIAnchorWidget( 
                anchor_x="center_x", 
                anchor_y="center_y",
                align_x=-310,
                align_y=210,
                child=v_box) 
        )

        # Initialisiere einen Körper zur Simulation
        body = Body([0.0, 4.0], [4.0, 0.0], mass=1.0, radius=0.5)
        self.bodies.extend([body])

    
    # Passt die Ursprungsposition bei Fenstergrößenänderung an
    def on_resize(self, width, height):
        super().on_resize(width, height)
        self.center = [width // 2 + 100, height // 2] 
    

    # Startet und stoppt die Simulation, wenn der Button geklickt wird
    def on_click_start(self, e):
        if self.state == 0:
            self.state = 1
            self.start_button.text = "Stop"
        else:
            self.state = 0
            self.start_button.text = "Start"
    

    # Konvertiert Meterkoordinaten in Pixelkoordinaten für die Darstellung
    def meter_to_pixel(self, x, y):
        pixel_x = self.center[0] + x * self.scale
        pixel_y = self.center[1] + y * self.scale
        return pixel_x, pixel_y

    # Zeichnet die Szene im Fenster
    def on_draw(self):
        arcade.start_render()
        
        # Zeichnet die Benutzeroberfläche
        self.uimanager.draw() 
        
        # Wände und Bodenlinien der Box
        points = []
        points.append(self.meter_to_pixel(-4.5, 5))
        points.append(self.meter_to_pixel(-4.5, -4.5))
        points.append(self.meter_to_pixel(4.5, -4.5))
        points.append(self.meter_to_pixel(4.5, 5))
        
        arcade.draw_line_strip(points, arcade.color.BLACK, 2)
        
        # Zeigt die Simulationszeit an
        time = round(self.time, 1)
        x, y = self.meter_to_pixel(-9, 3)
        arcade.draw_text(f"t = {time} s", x, y, arcade.color.BLACK)
        
        # Zeigt die FPS an
        fps = round(sum(self.fps_history) / len(self.fps_history), 1)
        x, y = self.meter_to_pixel(-9, 2.5)
        arcade.draw_text(f"FPS = {fps}", x, y, arcade.color.BLACK)
        
        # Zeichnet alle Körper in der Szene
        for body in self.bodies:
            x, y = self.meter_to_pixel(body.position[0], body.position[1])
            r = body.radius * self.scale
            arcade.draw_circle_filled(x, y, r, body.color)
            
            # zeichne die Geschwindigkeit
            arcade.draw_line(x, y, x + 2*body.velocity[0], y + 2*body.velocity[1] , arcade.color.GREEN, 2)
            
            
    # Aktualisiert die Simulation um einen Zeitschritt
    def on_update(self, dt):
        # Führe die Funktion nur aus, wenn der Status auf 1 ist.
        if self.state != 1:
            return
        
        # FPS berechnen und als gleitenden Durchschnitt speichern
        self.fps_history.append(1.0/dt)               
        self.fps_history.pop(0)
        
        # Setzt die Kräfte aller Körper auf null
        for body in self.bodies:
            body.clear_force()

        # Berechnet die Kräfte und aktualisiert die Bewegungen der Objekte
        for body in self.bodies:
            F_G = np.array([0.0, -body.mass * 9.81])  # Schwerkraft
            body.add_force(F_G)

            body.update_ec(dt)  # Aktualisiert Position und Geschwindigkeit
        
        # Überprüft und verarbeitet Kollisionen mit dem Boden
        for body in self.bodies:
            if body.position[1] < -4.5 + body.radius:
                body.position[1] = -4.5 + body.radius
                body.velocity[1] *= -1
                
            # Überprüft die Kollisionen mit den Seitenwänden
            if body.position[0] > 4.5 - body.radius:
                body.position[0] = 4.5 - body.radius
                body.velocity[0] *= -1
            elif body.position[0] < -4.5 + body.radius:
                body.position[0] = -4.5 + body.radius
                body.velocity[0] *= -1
            
        # Erhöht die Simulationszeit
        self.time += dt  



if __name__ == "__main__":
    # Initialisiert das Fenster für die Simulation
    window = AnimationWindow(800, 600, "Flummi")

    # starte die Simulation
    arcade.run()



# _____________________
#                     /
# Wichtige Konzepte  (
# ____________________\

# Skalierungsfaktor
# Der Skalierungsfaktor `scale` ist entscheidend, um physikalische Grössen (in Metern) 
# in Pixel umzuwandeln. Ein scale von 50 bedeutet, dass 1 Meter physikalische Distanz 
# 50 Pixel im Fenster entspricht. Diese Umrechnung sorgt dafür, dass die Simulation 
# unabhängig von der Fenstergrösse sinnvoll dargestellt wird.

# Koordinatensystem
# Das Koordinatensystem wird so gewählt, dass das Zentrum des Fensters der Ursprung 
# (0,0) der Simulation ist. Dadurch können wir die physikalische Position der Objekte 
# in Bezug auf den Ursprung des Fensters flexibel steuern.

# Zeit und Zeitschritt
# Arcade läuft standardmässig mit einem Zeitschritt (delta_time) von 1/60 Sekunden 
# pro Frame. Dies simuliert die Zeit für jeden Frame und sorgt für eine flüssige 
# Animation. Der Parameter self.dt im Code definiert diesen Zeitschritt und beeinflusst 
# die Aktualisierung der Objektposition.

# Wände und Kollisionen
# Kollisionen mit den Wänden und dem Boden werden in der on_update()-Methode 
# durch eine Anpassung der Position und eine Umkehrung der Geschwindigkeit des 
# Objekts modelliert. Dies sorgt dafür, dass das Objekt bei einer Kollision „abprallt“.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# Vorteile dieser Animation mit Arcade:
# 
# Flexible Skalierung
# Die Möglichkeit, physikalische Einheiten in eine visuelle Darstellung zu übersetzen.
# 
# Zentrumsverschiebung
# Ermöglicht, das Koordinatensystem flexibel im Fenster zu positionieren.
# 
# Realistische Zeitsteuerung:
# Durch den konstanten Zeitschritt von delta_time bleibt die Bewegung konsistent 
# und kontrollierbar.

# Mit diesen Erweiterungen wird die Simulation intuitiver und ermöglicht es, 
# physikalische Prozesse mit Arcade einfach und effektiv zu visualisieren.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Verändere das Programm so, dass der Ball sich unter dem Einfluss
# der Schwerkraft und einer Reibungskraft bewegt. Verwende eine geeignete 
# Reibungskonstante, damit der Ball zur Ruhe kommt.


# Füge hier deine Lösung ein.



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Verändere das Programm so, dass eine Schwingungsanimation entsteht. 
# Lass dazu eine Federkraft in Abhängigkeit von der Auslenkung auf den Ball
# wirken. Stelle sicher, dass der Ball in der Ruhelage stoppt, wenn keine Kraft 
# mehr auf ihn wirkt.


# Füge hier deine Lösung ein.




#                                        |
#                             ___________I____________
#                            ( _____________________ ()
#                          _.-'|                    ||
#                      _.-'   ||    Nun kannst      ||
#     ______       _.-'       ||                    ||
#    |      |_ _.-'           ||        du          ||
#    |      |_|_              ||                    ||
#    |______|   `-._          ||    Animationen     ||
#       /\          `-._      ||                    ||
#      /  \             `-._  ||     erstellen!     ||
#     /    \                `-.I____________________||
#    /      \                 ------------------------
#   /________\___________________/________________\______
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
#   


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Verändere das Programm so, dass der Ball sich unter dem Einfluss
# der Schwerkraft und einer Reibungskraft bewegt. Verwende eine geeignete 
# Reibungskonstante, damit der Ball zur Ruhe kommt.


'''
            # füge den folgenden Code auf Zeile 225 hinzu. 
            k = 0.1
            F_R = -k*body.velocity
            body.add_force(F_R)
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Verändere das Programm so, dass eine Schwingungsanimation entsteht. 
# Lass dazu eine Federkraft in Abhängigkeit von der Auslenkung auf den Ball
# wirken. Stelle sicher, dass der Ball in der Ruhelage stoppt, wenn keine Kraft 
# mehr auf ihn wirkt.


'''
            # Ändere die Anfangsbedingungen für den Körper in Zeile 148 auf
            body = Body([0.0, 2.0], [0.0, 0.0], mass=1.0, radius=0.5)


            # Ersetzte die Schwerkraft auf den Zeilen 223,224 durch die 
            # folgende Federkraft.
            D = 1
            F_F = -D*body.position  
            body.add_force(F_F)

'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><




