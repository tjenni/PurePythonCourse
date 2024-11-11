#              ________________________________________
#       ______|                                        |_____
#       \     |      13.4 ANIMATIONEN MIT ARCADE       |    /
#        )    |________________________________________|   (
#       /________)                                 (________\      11.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# In diesem Kapitel erweitern wir die physikalischen Simulationen aus dem
# vorherigen Abschnitt und erstellen Animationen mit der Arcade-Bibliothek.
# Der Einfachheit halber, gehen wir wieder zurück zum Euler-Cromer-Verfahren. 
# Arcade eignet sich ideal zur grafischen Darstellung von Objekten und 
# zur Implementierung interaktiver Animationen.


# __________________________________________
#                                          /
# Grundkonzepte der Animation mit Arcade  (
# _________________________________________\

# Die grundlegenden Schritte zur Erstellung einer Animation mit Arcade sind:
#
# 1. Initialisiere das Fenster (`arcade.Window`).
#
# 2. Zeichne die Objekte (`on_draw`-Methode).
#
# 3. Aktualisiere die Position und Bewegung der Objekte in jedem Frame (`on_update`-Methode).


# ___________________________
#                           /
# Installation von Arcade  (
# __________________________\

# Installiere die Arcade-Bibliothek in Thonny, dalls du sie noch nicht 
# installiert hast.


import arcade
import numpy as np

# _________________________________
#                                 /
# Klassenstruktur für Animation  (
# ________________________________\


# Die Klasse `Body` bleibt weitgehend gleich. Sie ist das Modell für den 
# physikalischen Körper. 

class Body:
    def __init__(self, position=[0.0, 0.0], velocity=[0.0, 0.0], mass=1.0, radius = 1.0, color=arcade.color.BLUE):
        self.position = position.copy()
        self.velocity = velocity.copy()
        self.mass = mass

        self.color = color
        self.radius = radius  
        
    def update(self, position, velocity):
        self.position = position
        self.velocity = velocity





class World:
    
    # Erdbeschleunigung
    g = 9.81  # m/s^2
    
    def __init__(self):
        self.positions = []
        self.velocities = []
        self.masses = []
        
        self.bodies = []
        
        self.time = 0
        
    
    # Hinzufügen eines Körpers zur Welt
    def add_body(self, body):
        self.bodies.append(body)
        
        # Kopiere die Daten des Körpers in die Weltarrays
        self.positions.append(body.position.copy())
        self.velocities.append(body.velocity.copy())
        self.masses.append(body.mass)
        

    # Berechne die Gravitationskraft zwischen zwei Massen.
    def gravity(self):
        return np.array([0.0, -World.g])

    
    # Berechne die Kräfte, welche auf die Körper wirken.
    def calculate_forces(self, positions, velocities, masses):
        forces = np.zeros_like(positions)

        for i in range(len(masses)):
            # Erdanziehungskraft
            forces[i] = masses[i] * self.gravity()

            # füge hier weitere Kräfte hinzu
            # ...

        return forces
    
    
    # Euler-Cromer-Update zur Berechnung des nächsten Zeitschritts
    def update_ec(self, dt):
        
        # Kräfte beim Start des Zeitschritts berechnen
        forces = self.calculate_forces(self.positions, self.velocities, self.masses)
        
        self.velocities += dt * forces / self.masses
        self.positions += dt * self.velocities
        
        for i, body in enumerate(self.bodies):
            body.update(self.positions[i], self.velocities[i])
        
        self.time += dt
        

    def init_simulation(self):
        # Kopiere die Körperdaten in numpy-Arrays für die Berechnung
        self.positions = np.array(self.positions)
        self.velocities = np.array(self.velocities)
        self.masses = np.array(self.masses)
        
        self.time = 0




# Diese Klasse wird die Animation steuern und das Fenster 
# der Applikation verwalten. Speziell an dieser Klasse ist, 
# dass man die Grösse der Simulation über den Skalierungsfaktor 
# `scale` steuern kann. 
class AnimationWindow(arcade.Window):

    def __init__(self, width, height, title, scale):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        
        # Skalierungsfaktor in Pixel/Meter
        self.scale = scale                       
        
        # Der Ursprung des Koordinatensystems ist in der Mitte des Fensters
        self.center = [width // 2, height // 2]      
        
        # Liste für die Berechnung des gleitendenden Durchschnitt für FPS
        self.fps_history = [0] * 60    
        
        # initialisiere das World-Objekt
        self.world = World()
        
        # erstelle ein Body-Objekt
        body = Body([0.0, 5.0], [1.0, 0.0], mass=1.0, radius=0.5)
        self.world.add_body(body)

        self.world.init_simulation()
        
    
    # Umrechnung von Meter zu Pixel
    def meter_to_pixel(self,x,y):
        pixel_x = self.center[0] + x * self.scale
        pixel_y = self.center[1] + y * self.scale
        
        return pixel_x, pixel_y


    # Zeichne die Objekte auf den Bildschirm
    def on_draw(self):
        arcade.start_render()
        
        # zeichne Wände und Boden
        x1, y1 = self.meter_to_pixel(-4.5,5)
        x2, y2 = self.meter_to_pixel(-4.5,-4.5)
        x3, y3 = self.meter_to_pixel(4.5,-4.5)
        x4, y4 = self.meter_to_pixel(4.5,5)
        
        arcade.draw_line(x1, y1, x2, y2, arcade.color.BLACK, 2)
        arcade.draw_line(x2, y2, x3, y3, arcade.color.BLACK, 2)
        arcade.draw_line(x3, y3, x4, y4, arcade.color.BLACK, 2)
        

        # zeige die Zeit und die FPS an
        time = round(self.world.time, 1)
        fps = round( sum(self.fps_history) / len(self.fps_history), 1)
        
        text = f"t = {time} s / FPS = {fps}"
        
        x5, y5 = self.meter_to_pixel(-7,5.5)
        arcade.draw_text(text , x5, y5, arcade.color.BLACK)
        

        # zeichne die Bälle
        for body in self.world.bodies:
            x_pixel, y_pixel = self.meter_to_pixel(body.position[0], body.position[1])
            r_pixel = body.radius * self.scale
        
            arcade.draw_circle_filled(x_pixel, y_pixel, r_pixel, body.color)
    

    # Berechnung des nächsten Zeitschritts
    def on_update(self, dt):
        
        # FPS am Ende der Liste hinzufügen und am Anfang entfernen.
        # Das erlaubt die Berechnung eines gleitenden Durchschnitts.
        self.fps_history.append(1.0 / dt)               
        self.fps_history.pop(0)
        
        # Berechne einen Euler-Cromer-Schritt
        self.world.update_ec(dt)
        
        # check boundary-conditions for all bodies
        for i, body in enumerate(self.world.bodies):
            
            # Boden
            if self.world.positions[i][1]  < -4:
                self.world.positions[i][1] = -4
                self.world.velocities[i][1] *= -1
                
            # Wand rechts 
            if self.world.positions[i][0] > 4:
                self.world.positions[i][0] = 4
                self.world.velocities[i][0] *= -1

            # Wand links 
            elif self.world.positions[i][0] < -4:
                self.world.positions[i][0] = -4
                self.world.velocities[i][0] *= -1
                
        
if __name__ == "__main__":
    # Fenstergröße und Skalierung anpassen
    window = AnimationWindow(800, 600, "Physikalische Animation", scale=50)
    arcade.run()




# _____________________
#                     /
# Wichtige Konzepte  (
# ____________________\

# Skalierungsfaktor
# Der Skalierungsfaktor `scale` ist entscheidend, um physikalische Größen (in Metern) 
# in Pixel umzuwandeln. Ein scale von 50 bedeutet, dass 1 Meter physikalische Distanz 
# 50 Pixel im Fenster entspricht. Diese Umrechnung sorgt dafür, dass die Simulation 
# unabhängig von der Fenstergröße sinnvoll dargestellt wird.

# Koordinatensystem
# Das Koordinatensystem wird so gewählt, dass das Zentrum des Fensters der Ursprung 
# (0,0) der Simulation ist. Dadurch können wir die physikalische Position der Objekte 
# in Bezug auf den Ursprung des Fensters flexibel steuern.

# Zeit und Zeitschritt
# Arcade läuft standardmäßig mit einem Zeitschritt (delta_time) von 1/60 Sekunden 
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
# Erstelle eine Arcade-Animation, die einen Ball zeigt, der sich unter dem Einfluss
# der Schwerkraft und einer Reibungskraft bewegt. Verwende eine geeignete 
# Reibungskonstante, damit der Ball zur Ruhe kommt.


# Füge hier deine Lösung ein.



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle eine Schwingungsanimation, bei der die Federkraft in Abhängigkeit
# von der Auslenkung wirkt. Stelle sicher, dass der Ball in der Ruhelage stoppt,
# wenn keine Kraft mehr auf ihn wirkt.


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







# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><






