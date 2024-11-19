#              ________________________________________________
#       ______|                                                |_____
#       \     |      13.5 KOLLISIONEN MIT IMPULSERHALTUNG      |    /
#        )    |________________________________________________|   (
#       /________)                                         (________\      13.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# In diesem Kapitel lernen wir, wie man Kollisionen zwischen Objekten simuliert 
# und den Impuls bewahrt. Kollisionen sind ein zentraler Bestandteil physikalischer 
# Simulationen und Animationen in Spielen. Wir erfahren, wie man eine Kollision 
# erkennt und den Impuls nach dem Prinzip der Impulserhaltung berechnet.


# ___________________________________________________
#                                                   /
# Grundkonzepte: Kollisionen mit Impulserhaltung   (
# __________________________________________________\

# - Impuls:
#   Der Impuls p eines Objekts ist das Produkt seiner Masse und Geschwindigkeit:
#   
#        p = m * v
#   
#   Bei einer Kollision zweier Objekte bleibt der Gesamtimpuls des Systems erhalten.
#
# - Impulserhaltungsgesetz:
#   Das Impulserhaltungsgesetz besagt, dass in einem geschlossenen System, in 
#   dem keine äusseren Kräfte wirken, der Gesamtimpuls vor und nach der Kollision 
#   gleich bleibt.

# - Arten von Kollisionen:
#   Wir betrachten hier elastische Kollisionen, bei denen sowohl Impuls als auch 
#   kinetische Energie erhalten bleiben.




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
        


# Die Klasse `Interaction` ist die Basisklasse für alle Wechselwirkungen. 
class Interaction:
    def __init__(self, bodyA, bodyB):
        self.bodyA = bodyA
        self.bodyB = bodyB

    def update(self):
        pass



# Die Klasse `Collision` verwaltet die Kollisionserkennung und -berechnung 
# zwischen zwei Körpern.
class Collision(Interaction):

    def __init__(self, bodyA, bodyB, restitution=1.0):
        super().__init__(bodyA, bodyB)
        self.restitution = restitution


    def check_collision(self):
        # Prüft, ob zwei Körper kollidieren.
        distance = np.linalg.norm(self.bodyA.position - self.bodyB.position)
        return distance <= (self.bodyA.radius + self.bodyB.radius)


    def resolve_collision(self):
        # Berechnet die neuen Geschwindigkeiten der beiden Körper nach einer Kollision.
        normal = (self.bodyB.position - self.bodyA.position) / np.linalg.norm(self.bodyB.position - self.bodyA.position)
        relative_velocity = self.bodyA.velocity - self.bodyB.velocity
        velocity_along_normal = np.dot(relative_velocity, normal)

        # Berechnet nur, wenn die Körper aufeinander zu bewegen
        if velocity_along_normal < 0:
            return

        # Impulsberechnung
        impulse = ((1 + self.restitution) * velocity_along_normal) / (1 / self.bodyA.mass + 1 / self.bodyB.mass)
        impulse_vector = impulse * normal

        # Aktualisiert die Geschwindigkeit der beiden Körper
        self.bodyA.velocity -= (impulse_vector / self.bodyA.mass)
        self.bodyB.velocity += (impulse_vector / self.bodyB.mass)


    # Überprüft und berechnet die Kollision, falls nötig
    def update(self):
        if self.check_collision():
            self.resolve_collision()
            
            
            
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
        
        # Liste für alle Interaktionen zwischen den Körpern
        self.interactions = []  

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

        # Initialisiere zwei Körper
        ball1 = Body([-2, 1.1], [2, 0], mass=1.0, radius=0.5, color=arcade.color.RED)
        ball2 = Body([2, 1], [-2, 0], mass=1.0, radius=0.5, color=arcade.color.BLUE)
        self.bodies.extend([ball1, ball2])

        int12 = Collision(ball1, ball2)
        self.interactions.extend([int12])

    
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
            
            # zeichne die resultierende Kraft
            arcade.draw_line(x, y, x + 2*body.force[0], y + 2*body.force[1] , arcade.color.BARN_RED, 2)
        


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
        
        
        # Aktualisiert die Kollisionen
        for interacion in self.interactions:
            interacion.update()
            
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
    window = AnimationWindow(800, 600, "Zwei Flummis")

    # starte die Simulation
    arcade.run()





# ____________________________
#                            /
# Wichtige Konzepte          (
# ____________________________\

# Kollisionserkennung:
# Die Methode `check_collision` überprüft den Abstand zwischen zwei Objekten und 
# bestimmt, ob sie kollidieren. Die Kollision wird erkannt, wenn die Entfernung 
# zwischen ihren Mittelpunkten kleiner oder gleich der Summe ihrer Radien ist.

# Impulserhaltung:
# Die Methode `resolve_collision` berechnet die neue Geschwindigkeit beider Objekte 
# unter Berücksichtigung des Impulserhaltungsgesetzes. Dies stellt sicher, dass 
# die Objekte nach einer Kollision in korrekter Richtung abprallen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ____________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Füge zur Simulation einen dritten Ball hinzu. Denke daran, auch die Wechsel-
# wirkungen hinzuzufügen. Teste die Simulation.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Modifiziere die Kollisionen der Objekte, sodass eine Energieverlustregel 
# simuliert wird. Das bedeutet, dass bei jeder Kollision 10 % der Energie 
# verloren gehen und die Geschwindigkeit entsprechend angepasst wird.


# Füge hier deine Lösung ein.



#            _...----.._
#         ,:':::::.     `>.
#       ,' |:::::;'     |:::.
#      /    `'::'       :::::\
#     /         _____     `::;\
#    :         /:::::\      `  :      Das sieht nun so aus wie
#    | ,.     /::SSt::\        |      beim Fussball. :-)
#    |;:::.   `::::::;'        |
#    ::::::     `::;'      ,.  ;
#     \:::'              ,::::/
#      \                 \:::/
#       `.     ,:.        :;'
#         `-.::::::..  _.''
#            ```----'''
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
# Füge zur Simulation einen dritten Ball hinzu. Denke daran, auch die Wechsel-
# wirkungen hinzuzufügen. Teste die Simulation.


'''
        # Initialisiere zwei Körper
        ball1 = Body([-2, 1.1], [2, 0], mass=1.0, radius=0.5, color=arcade.color.RED)
        ball2 = Body([2, 1], [-2, 0], mass=1.0, radius=0.5, color=arcade.color.BLUE)
        ball3 = Body([0, 1], [-1, 0], mass=1.0, radius=0.5, color=arcade.color.GREEN)
        self.bodies.extend([ball1, ball2, ball3])
        
        int12 = Collision(ball1, ball2)
        int13 = Collision(ball1, ball3)
        int23 = Collision(ball2, ball3)
        self.interactions.extend([int12,int13,int23])
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Modifiziere die Kollisionen der Objekte, sodass eine Energieverlustregel 
# simuliert wird. Das bedeutet, dass bei jeder Kollision 10 % der Energie 
# verloren gehen und die Geschwindigkeit entsprechend angepasst wird.


'''
        # Initialisiere zwei Körper
        ball1 = Body([-2, 1.1], [2, 0], mass=1.0, radius=0.5, color=arcade.color.RED)
        ball2 = Body([2, 1], [-2, 0], mass=1.0, radius=0.5, color=arcade.color.BLUE)
        self.bodies.extend([ball1, ball2])

        int12 = Collision(ball1, ball2, restitution=0.9)
        self.interactions.extend([int12])

'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><



