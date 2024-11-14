#              ____________________________________
#       ______|                                    |_____
#       \     |     13.6 IDEALES GAS MIT ARCADE    |    /
#        )    |____________________________________|   (
#       /________)                             (________\      13.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# In diesem Kapitel modellieren wir ein ideales Gas, bei dem viele kleine, 
# unabhängige Partikel (Moleküle) in einem geschlossenen Raum (Behälter) zufällig 
# herumschwirren und kollidieren. Die Partikelbewegungen und ihre Kollisionen 
# entsprechen einem idealisierten Modell, in dem Partikel:
#
# - nur durch elastische Kollisionen miteinander und mit den Behälterwänden interagieren,
#
# - keine Anziehungskräfte zwischen sich haben,
#
# - Energie und Impuls während jeder Kollision erhalten bleiben.

# Wir verwenden die Python-Bibliothek Arcade für die grafische Darstellung und 
# Animation der Teilchenbewegungen. Arcade bietet eine benutzerfreundliche Oberfläche 
# für 2D-Grafiken und Animationen und eignet sich gut für physikalische Simulationen.


import arcade
import arcade.gui 
import numpy as np
import random


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
        
    # Berechnet die kinetische Energie des Körpers
    def kinetic_energy(self):
        return 0.5 * self.mass * np.linalg.norm(self.velocity)**2
        


# Die Klasse `Interaction` verwaltet die Kollisionserkennung und -berechnung 
# zwischen zwei Körpern.
class Interaction:
    def __init__(self, bodyA, bodyB, color=arcade.color.BLUE):
        self.bodyA = bodyA
        self.bodyB = bodyB

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
        impulse = (2 * velocity_along_normal) / (1 / self.bodyA.mass + 1 / self.bodyB.mass)
        impulse_vector = impulse * normal

        # Aktualisiert die Geschwindigkeit der beiden Körper
        self.bodyA.velocity -= (impulse_vector / self.bodyA.mass)
        self.bodyB.velocity += (impulse_vector / self.bodyB.mass)

    def update(self):
        # Überprüft und berechnet die Kollision, falls nötig
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
        
        v_box.add(self.start_button.with_space_around(bottom=10))
        
        
        # heizen Button erstellen
        self.heat_button = arcade.gui.UIFlatButton(text="heizen", height=30, style=default_style)
        self.heat_button.on_click = self.heat
        
        v_box.add(self.heat_button.with_space_around(bottom=10))
        
        # kühlen Button erstellen
        self.cool_button = arcade.gui.UIFlatButton(text="kühlen", height=30, style=default_style)
        self.cool_button.on_click = self.cool
        
        v_box.add(self.cool_button.with_space_around(bottom=10))
        
        
        # UI-Komponenten zur Benutzeroberfläche hinzufügen
        self.uimanager.add( 
            arcade.gui.UIAnchorWidget( 
                anchor_x="center_x", 
                anchor_y="center_y",
                align_x=-310,
                align_y=140,
                child=v_box) 
        )

        # Gesamtenergie aller Teilchen
        self.energy = 0

        # Initialisierung der Körper in einem 10x10-Raster mit zufälligen Geschwindigkeiten
        for i in range(8):
            for j in range(8):
                vx = 0.4 - 0.8*random.random()  # Zufällige Geschwindigkeit in x-Richtung
                vy = 0.4 - 0.8*random.random()  # Zufällige Geschwindigkeit in y-Richtung
                bodyA = Body([-3.5+i, -3.5+j], [vx, vy], radius=0.2, color=arcade.color.RED)
                
                # Erstellen von Interaktionen mit bereits vorhandenen Körpern
                for bodyB in self.bodies:
                    interaction = Interaction(bodyA, bodyB)
                    self.interactions.append(interaction)
                
                self.bodies.append(bodyA)

    
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
    
    
    # Zeichne Histogramm der Geschwindigkeiten
    def draw_v_histogram(self):
        velocities = []
        for body in self.bodies:
            velocities.append(np.linalg.norm(body.velocity))
        
        counts , bins  = np.histogram(velocities,bins=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
        
        w = 10 # Breite der Säulen
        
        x0, y0 = self.meter_to_pixel(-8.8,-3)
        for i, count in enumerate(counts):
            arcade.draw_line(x0+w*i, y0, x0+w*i, y0 + 2*count, arcade.color.RED, w-1)
        
        x, y = self.meter_to_pixel(-9,-1.5)
        arcade.draw_text("Histogramm v", x, y, arcade.color.BLACK)
        
        x, y = self.meter_to_pixel(-9,-3.4)
        arcade.draw_text(str(round(bins[0],2)), x, y, arcade.color.BLACK)
        arcade.draw_text(str(round(bins[-1],2)), x + w*len(counts), y, arcade.color.BLACK)
        


    # Zeichnet die Szene im Fenster
    def on_draw(self):
        arcade.start_render()
        
        # Zeichnet die Benutzeroberfläche
        self.uimanager.draw() 
        
        # Wände und Bodenlinien der Box
        x1, y1 = self.meter_to_pixel(-4,-4)
        x2, y2 = self.meter_to_pixel(4,4)
        w = (x2-x1)
        h = (y2-y1)
        arcade.draw_rectangle_outline(x2-w//2, y2-h//2, w, h, arcade.color.BLACK, 2)

        
        # Zeigt die Simulationszeit an
        time = round(self.time, 1)
        x, y = self.meter_to_pixel(-9, 1)
        arcade.draw_text(f"t = {time} s", x, y, arcade.color.BLACK)
        
        # Zeigt die FPS an
        fps = round(sum(self.fps_history) / len(self.fps_history), 1)
        x, y = self.meter_to_pixel(-9, 0.5)
        arcade.draw_text(f"FPS = {fps}", x, y, arcade.color.BLACK)
        
        # Zeigt die Energie an
        energy = round(self.energy,1)
        x, y = self.meter_to_pixel(-9, 0)
        arcade.draw_text(f"E = {energy} J", x, y, arcade.color.BLACK)
        
        # Zeigt die Anzahl der Körper an
        n = len(self.bodies)
        x, y = self.meter_to_pixel(-9, -0.5)
        arcade.draw_text(f"N = {n}", x, y, arcade.color.BLACK)
        
        # Zeigt das Histogram der Geschwindigkeiten an
        self.draw_v_histogram()
        
        # Zeichnet alle Körper in der Szene
        for body in self.bodies:
            x, y = self.meter_to_pixel(body.position[0], body.position[1])
            r = body.radius * self.scale
            arcade.draw_circle_filled(x, y, r, body.color)

    # Die Geschwindigkeit von allen Körper wird erhöht.
    def heat(self, e):
        for body in self.bodies:
            body.velocity *= 1.2
            
            
    # Die Geschwindigkeit von allen Körper wird reduziert.
    def cool(self, e):
        for body in self.bodies:
            body.velocity *= 0.8
            
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
            body.update_ec(dt)  # Aktualisiert Position und Geschwindigkeit
        
        for body in self.bodies:
            # Überprüft und verarbeitet Kollisionen mit dem Boden
            if body.position[1] < -4 + body.radius:
                body.position[1] = -4 + body.radius
                body.velocity[1] *= -1
            elif body.position[1] > 4 - body.radius:
                body.position[1] = 4 - body.radius
                body.velocity[1] *= -1
                
            # Überprüft die Kollisionen mit den Seitenwänden
            if body.position[0] < -4 + body.radius:
                body.position[0] = -4 + body.radius
                body.velocity[0] *= -1
            elif body.position[0] > 4 - body.radius:
                body.position[0] = 4 - body.radius
                body.velocity[0] *= -1
        
        # Berechne die Gesamtenergie aller Körper und speichere sie
        self.energy = 0.0
        for body in self.bodies:
            self.energy += body.kinetic_energy()
            
        # Erhöht die Simulationszeit
        self.time += dt  



if __name__ == "__main__":
    # Initialisiert das Fenster für die Simulation
    window = AnimationWindow(800, 600, "Ideales Gas")

    # starte die Simulation
    arcade.run()




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# Dieses Kapitel behandelt die Simulation eines idealen Gases mit der Arcade-
# Bibliothek in Python. Die Partikel bewegen sich frei in einem geschlossenen 
# Raum und erfahren elastische Kollisionen untereinander und mit den Begrenzungen 
# des Raumes. Die Simulation veranschaulicht thermodynamische Eigenschaften eines 
# idealen Gases wie die kinetische Energie und Temperatur, und zeigt die Verteilung 
# der Teilchengeschwindigkeiten.


# HAUPTBESTANDTEILE
# -----------------

# 1.  Körper und Interaktionen
#     - Die Klasse `Body` repräsentiert die Teilchen des Gases, modelliert als 
#       Körper mit Masse, Geschwindigkeit und Position.
#
#     - Die Klasse `Interaction` überprüft Kollisionen zwischen den Körpern und 
#       berechnet die neuen Geschwindigkeiten bei elastischen Stößen, wodurch 
#       Energie und Impuls erhalten bleiben.
  
# 2.  Animation und Steuerung
#     - Die Arcade-Bibliothek wird zur Visualisierung der Partikelbewegungen verwendet.
#
#     - Buttons `Heizen` und `Kühlen` ermöglichen es, die Gesamtenergie der Teilchen 
#       zu erhöhen oder zu verringern, was der thermischen Energieänderung entspricht.
  
# 3.  Energie und Temperatur
#     - Die Simulation berechnet die Gesamtenergie basierend auf den kinetischen 
#       Energien der Teilchen.
#
#     - Ein Histogramm zeigt die Verteilung der Teilchengeschwindigkeiten und 
#       ermöglicht es, die Veränderungen der Partikelgeschwindigkeit zu beobachten.


# THERMISCHE EIGENSCHAFTEN
# ------------------------

# - Die Simulation demonstriert die kinetische Gastheorie, indem die Beziehung 
#   zwischen Teilchengeschwindigkeiten, ihrer kinetischen Energie und der Temperatur 
#   illustriert wird.
#
# - Die Partikelverteilung nähert sich der Maxwell-Boltzmann-Verteilung, die die 
#   Geschwindigkeitsverteilung in einem idealen Gas beschreibt.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Verwende den "Heizen"- und "Kühlen"-Button und analysiere, wie sich die 
# Geschwindigkeit der Partikel und die Gesamtenergie verändern. Kannst du 
# einen Zusammenhang mit der thermischen Energie herstellen?


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Experimentiere mit verschiedenen Partikelzahlen und beobachte, wie sich die Gesamtenergie und
# die durchschnittliche Geschwindigkeit im Histogramm verändern. Was passiert, wenn du die 
# Anzahl der Partikel verdoppelst oder halbierst?


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
# Verwende den "Heizen"- und "Kühlen"-Button und analysiere, wie sich die 
# Geschwindigkeit der Partikel und die Gesamtenergie verändern. Kannst du 
# einen Zusammenhang mit der thermischen Energie herstellen?


'''
# Lösung:
# Wenn du den "Heizen"-Button verwendest, erhöht sich die Geschwindigkeit 
# der Partikel. Das bedeutet, dass auch die kinetische Energie der Partikel 
# steigt, da die kinetische Energie proportional zur Geschwindigkeit im Quadrat ist.
# Die Gesamtenergie im System wird daher höher angezeigt. Die erhöhte kinetische 
# Energie steht in direktem Zusammenhang mit der thermischen Energie, denn 
# eine höhere Geschwindigkeit der Teilchen bedeutet eine höhere thermische 
# Energie im Sinne eines wärmeren Systems.

# Der "Kühlen"-Button bewirkt das Gegenteil: Die Geschwindigkeit der Partikel
# nimmt ab, und entsprechend sinkt die kinetische Energie und damit die 
# Gesamtenergie im System. Das Modell zeigt, dass ein langsameres Bewegungsmuster
# der Partikel einer niedrigeren Temperatur entspricht, was auf eine geringere 
# thermische Energie hinweist.
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Experimentiere mit verschiedenen Partikelzahlen und beobachte, wie sich die Gesamtenergie und
# die durchschnittliche Geschwindigkeit im Histogramm verändern. Was passiert, wenn du die 
# Anzahl der Partikel verdoppelst oder halbierst?

'''
# Lösung:
# Wenn die Anzahl der Partikel erhöht wird, bleibt die durchschnittliche Geschwindigkeit
# im Histogramm ähnlich, vorausgesetzt, die Gesamtenergie im System wird nicht verändert.
# Allerdings steigt die Gesamtenergie proportional zur Anzahl der Partikel, weil jedes 
# zusätzliche Teilchen seine eigene kinetische Energie beiträgt. Das Histogramm zeigt 
# tendenziell eine gleichbleibende Verteilung, doch die Summe der Energien aller Teilchen 
# ist höher.

# Bei einer Halbierung der Partikelzahl sinkt die Gesamtenergie entsprechend, da weniger 
# Partikel zur Gesamtkinetik beitragen. Auch hier bleibt die durchschnittliche Geschwindigkeit 
# im Histogramm in etwa konstant, sofern keine externe Energie hinzugefügt oder entzogen 
# wird. Dies zeigt, dass die Gesamtenergie eines idealen Gases von der Anzahl der Teilchen 
# abhängt, während die durchschnittliche kinetische Energie pro Partikel (und damit die 
# Temperatur) stabil bleibt.
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


