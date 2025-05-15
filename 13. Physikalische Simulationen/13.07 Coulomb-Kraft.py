#              _________________________________
#       ______|                                 |_____
#       \     |       13.7 COULOMB-KRAFT        |    /
#        )    |_________________________________|   (
#       /________)                          (________\      2.3.25 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# In diesem Kapitel erweitern wir unsere Simulation, um die Coulomb-Kraft zwischen
# geladenen Partikeln zu simulieren. Die Coulomb-Kraft beschreibt die elektrostatische 
# Anziehung oder Abstoßung zwischen zwei Ladungen und ist proportional zum Produkt 
# der Ladungen und umgekehrt proportional zum Quadrat ihres Abstands.


# __________________________________
#                                  /
# Grundkonzepte: Coulomb-Kraft    (
# _________________________________\

# - Coulomb-Kraft:
#   Die Coulomb-Kraft F zwischen zwei Ladungen q1 und q2 im Abstand r wird beschrieben durch:
#   
#        F = k * q1 * q2 / r^2
#   
#   wobei k die Coulomb-Konstante ist und in Luft oder Vakuum den Wert k ≈ 8.99e9 Nm²/C² hat.
#
# - Geladene Teilchen:
#   Teilchen in der Simulation erhalten eine Ladung, die entweder positiv oder negativ sein kann.
#   Je nach Vorzeichen der Ladungen werden sie sich anziehen oder abstoßen.


import arcade
import arcade.gui 
import numpy as np


class Body:
    def __init__(self, position, velocity, mass=1.0, charge=1.0, radius=1.0, color=arcade.color.BLUE):
        self.mass = mass                                 # Masse in kg
        self.position = np.array(position, dtype=float)  # Position in m
        self.velocity = np.array(velocity, dtype=float)  # Geschwindigkeit in m/s
        self.acceleration = np.array([0.0, 0.0])         # Beschleunigung in m/s^2
        self.force = np.array([0.0, 0.0])                # Resultierende Kraft in N
        self.charge = charge                             # Elektrische Ladung in Coulomb (C)
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



# Die Klasse `Coulomb` berechnet die Coulomb-Kraft zwischen zwei geladenen Körper.
class Coulomb(Interaction):
    # Die Coulomb-Konstante k in Nm²/C²
    K = 8.99e9
    
    def __init__(self, bodyA, bodyB):
        super().__init__(bodyA, bodyB)
        
    def calculate_coulomb_force(self):
        # Berechnet die Coulomb-Kraft zwischen zwei geladenen Teilchen.
        r_vector = self.bodyA.position - self.bodyB.position
        distance = np.linalg.norm(r_vector)
        
        if distance < self.bodyA.radius + self.bodyB.radius:
            return np.array([0.0, 0.0])  # Vermeidet unphysikalisch große Kräfte bei sehr kleinem Abstand

        force_magnitude = Coulomb.K * self.bodyA.charge * self.bodyB.charge / distance**2
        force_direction = r_vector / distance  # Einheitsvektor in Richtung des Abstandsvektors
        
        # Berechne die Coulomb-Kraft in Richtung des Einheitsvektors
        return force_magnitude * force_direction


    # Wendet die Coulomb-Kraft auf beide Körper an
    def update(self):
        force = self.calculate_coulomb_force()
        self.bodyA.add_force(force)
        self.bodyB.add_force(-force)  # Newtons drittes Gesetz (actio = reactio)

            
            
            
# Die Klasse `AnimationWindow` steuert die grafische Darstellung und die Simulation 
# der Partikelbewegungen.
class AnimationWindow(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        
        # Hintergrundfarbe des Fensters auf Weiß setzen
        self.background_color = arcade.color.WHITE
        
        # Skalierungsfaktor in Pixel/Meter für die Darstellung
        self.scale_factor = 50                       
        
        # Ursprung des Koordinatensystems in die Mitte des Fensters setzen
        self.center_point = [width // 2 + 100, height // 2]  
        
        # Liste für alle zu simulierenden Körper
        self.bodies = []
        
        # Liste für alle Interaktionen zwischen den Körpern
        self.interactions = []  
    
        # Simulationszeit in Sekunden
        self.t = 0
        
        # Simulationsstatus (0 = Pause, 1 = Ausführen)
        self.state = 0
        
        # FPS-Berechnung mit gleitendem Durchschnitt
        self.fps_history = [0] * 30
        
        # UI-Manager zur Steuerung der Benutzeroberfläche (Buttons)
        self.uimanager = arcade.gui.UIManager() 
        self.uimanager.enable() 
        
        # Erstellen einer vertikalen Box für die Buttons
        anchor = arcade.gui.UIAnchorLayout(x=30)
        box = arcade.gui.UIBoxLayout(vertical=True,space_between=10)
        
        anchor.add(box,anchor_x="left")
        
        # Start/Stop-Button erstellen
        self.start_button = arcade.gui.UIFlatButton(text="Start", height=30)
        self.start_button.on_click = self.on_click_start
        
        box.add(self.start_button)
        
        # UI-Komponenten zur Benutzeroberfläche hinzufügen
        self.uimanager.add(anchor)

        # Initialisiere zwei Körper
        ball1 = Body([-2, 1.1], [0, 2], mass=1.0, charge=1e-4, radius=0.5, color=arcade.color.RED)
        ball2 = Body([2.1, 1], [0, -1], mass=1.0, charge=-1e-4, radius=0.5, color=arcade.color.BLUE)
        self.bodies.extend([ball1, ball2])

        collision12 = Collision(ball1, ball2)
        coulomb12 = Coulomb(ball1, ball2)
        self.interactions.extend([collision12, coulomb12])

    
    # Passt die Ursprungsposition bei Fenstergrößenänderung an
    def on_resize(self, width, height):
        super().on_resize(width, height)
        self.center_point = [width // 2 + 100, height // 2] 
    

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
        pixel_x = self.center_point[0] + x * self.scale_factor
        pixel_y = self.center_point[1] + y * self.scale_factor
        return pixel_x, pixel_y

    # Zeichnet die Szene im Fenster
    def on_draw(self):
        self.clear()
        
        # Zeichnet die Benutzeroberfläche
        self.uimanager.draw() 
        
        # Wände und Bodenlinien der Box
        x1, y1 = self.meter_to_pixel(-4,-4)
        x2, y2 = self.meter_to_pixel(4,4)
        w = (x2-x1)
        h = (y2-y1)
        arcade.draw_rect_outline(arcade.rect.XYWH(x2-w//2, y2-h//2, w, h), arcade.color.BLACK, 2)
        
        # Zeigt die Simulationszeit an
        time = round(self.t, 1)
        x, y = self.meter_to_pixel(-9, 3)
        arcade.draw_text(f"t = {time} s", x, y, arcade.color.BLACK)
        
        # Zeigt die FPS an
        fps = round(sum(self.fps_history) / len(self.fps_history), 1)
        x, y = self.meter_to_pixel(-9, 2.5)
        arcade.draw_text(f"FPS = {fps}", x, y, arcade.color.BLACK)
        
        # Zeichnet alle Körper in der Szene
        for body in self.bodies:
            x, y = self.meter_to_pixel(body.position[0], body.position[1])
            r = body.radius * self.scale_factor
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
            
        # Erhöht die Simulationszeit
        self.t += dt  



if __name__ == "__main__":
    # Initialisiert das Fenster für die Simulation
    window = AnimationWindow(800, 600, "Geladene Kugeln")

    # starte die Simulation
    arcade.run()



# ____________________________
#                            /
# Zusammenfassung            (
# ____________________________\

# Die Coulomb-Kraft zwischen geladenen Teilchen kann dazu führen, dass sie sich 
# entweder abstoßen oder anziehen, je nachdem, ob ihre Ladungen gleich oder 
# entgegengesetzt sind. Diese Simulation ermöglicht es, die Effekte der 
# elektrostatischen Wechselwirkungen zu beobachten und die Bewegung von geladenen 
# Teilchen nachzuvollziehen.





# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Experimentiere mit verschiedenen Ladungswerten und analysiere, wie die 
# unterschiedlichen Polaritäten und Ladungsstärken die Bewegungen und Interaktionen 
# beeinflussen. Passe die Elastizität `restitution` bei der `Interaction`-Klasse
# an um ein gebundenes System (Molekül) zu erhalten. 


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Füge zur Simulation einen dritten geladenen Teil hinzu und beobachte, wie sich die Kräfte 
# zwischen den Teilchen verändern. Wie beeinflusst die zusätzliche Ladung die Dynamik des Systems?


# Füge hier deine Lösung ein.



#      ...     _M_
#     /( )\    ( )            Gewisse Dinge ziehen
#    / / \ \  / : \           sich an. 
#    ~~\%/~~  \|:|/
#     /   \    |||
#    /,,,,,\   |||     R. R. 
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
# Experimentiere mit verschiedenen Ladungswerten und analysiere, wie die 
# unterschiedlichen Polaritäten und Ladungsstärken die Bewegungen und Interaktionen 
# beeinflussen. Passe die Elastizität `restitution` bei der `Interaction`-Klasse
# an um ein gebundenes System (Molekül) zu erhalten. 

'''
# Um mit unterschiedlichen Ladungswerten und der Elastizität zu experimentieren 
# und ein gebundenes System zu schaffen, können wir den restitution-Parameter 
# anpassen und die Ladungen variieren. Die Implementierung erfolgt durch Hinzufügen 
# von Ladungs- und Elastizitätswerten in der Interaction-Klasse.

# Anpassung der Ladungen und Elastizität in der Hauptklasse `AnimationWindow`

# Füge folgenden Code in der __init__-Methode hinzu, um unterschiedliche Ladungen zu testen.
# Beispiel für positive und negative Ladungen für ein mögliches Molekül:

        body1 = Body([-2, 1], [0, 1.5], mass=1.0, charge=1e-4, radius=0.5, color=arcade.color.RED)
        body2 = Body([2, -1], [0, -1.5], mass=1.0, charge=-1e-4, radius=0.5, color=arcade.color.BLUE)
        self.bodies.extend([body1, body2])

        coulomb12 = Coulomb(body1, body2)
        collition12 = Collision(body1, body2, restitution=0.8)
        self.interactions.extend([coulomb12,collition12])

# Hinzufügen der Interaktion mit verringerter Elastizität (restitution) für eine 
# gebundene Bewegung. Dadurch wird die Geschwindigkeit bei jedem Stoß etwas  
# reduziert. Dadurch bleiben die Teilchen näher beieinander und bilden eine Bindung.

# Der Effekt wird durch Verringerung der restitution-Werte verstärkt, was eine Art 
# „Molekülbindung“ erzeugen kann, indem die kinetische Energie im Stoß etwas verloren 
# geht und die Teilchen daher länger in der Nähe bleiben.

'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Füge zur Simulation einen dritten geladenen Teil hinzu und beobachte, wie sich die Kräfte 
# zwischen den Teilchen verändern. Wie beeinflusst die zusätzliche Ladung die Dynamik des Systems?


'''
# Hier fügen wir ein drittes geladenes Teilchen hinzu und beobachten, wie es die Kräfte 
# und Bewegungen beeinflusst.

# In der __init__-Methode einen dritten geladenen Körper hinzufügen:

        # Initialisiere zwei Körper
        body1 = Body([-2, 1.1], [0, 2], mass=1.0, charge=1e-4, radius=0.5, color=arcade.color.RED)
        body2 = Body([2.1, 1], [0, -1], mass=1.0, charge=-1e-4, radius=0.5, color=arcade.color.BLUE)
        body3 = Body([0, -2], [1, 0.5], mass=1.0, charge=1e-4, radius=0.5, color=arcade.color.GREEN)
        self.bodies.extend([body1, body2, body3])

        collision12 = Collision(body1, body2)
        collision13 = Collision(body1, body3)
        collision23 = Collision(body2, body3)
        self.interactions.extend([collision12, collision13, collision23])

        coulomb12 = Coulomb(body1, body2)
        coulomb13 = Coulomb(body1, body3)
        coulomb23 = Coulomb(body2, body3)
        self.interactions.extend([coulomb12, coulomb13, coulomb23])
        

    body3 = Body([0, -2], [1, 0.5], mass=1.0, charge=1e-6, radius=0.5, color=arcade.color.GREEN)
    self.bodies.append(body3)

# Fügen Sie die entsprechenden Interaktionen hinzu, um Coulomb-Kräfte zwischen allen Teilchen zu berücksichtigen:

int13 = Interaction(particle1, particle3)
int23 = Interaction(particle2, particle3)

self.interactions.append(int13)
self.interactions.append(int23)

# Durch Hinzufügen eines dritten Körpers mit positiver Ladung können wir beobachten, 
# wie sich das System dynamisch verändert. Wenn beispielsweise particle1 und 
# particle3 beide positiv geladen sind, wird sich particle3 von particle1 abstoßen, 
# während es gleichzeitig von particle2 angezogen wird, falls particle2 negativ 
# geladen ist. Dadurch entstehen komplexere Bahnkurven, die die Dynamik des Systems 
# weiter veranschaulichen.

# In der Simulation können Sie beobachten, wie das zusätzliche Teilchen die Balance 
# des Systems beeinflusst und das System gegebenenfalls zu stabilen oder instabilen 
# Bahnen führt, abhängig von den Ladungen und Abständen der Teilchen.

'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><






