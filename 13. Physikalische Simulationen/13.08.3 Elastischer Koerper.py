#              __________________________________
#       ______|                                  |_____
#       \     |    13.8.3 ELASTISCHER KÖRPER     |    /
#        )    |__________________________________|   (
#       /________)                           (________\      14.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Ein elastischer Körper ist ein physikalisches Modell, das durch innere Kräfte 
# und Dämpfungen miteinander verbunden ist. Durch diese elastischen Verbindungen 
# können sich die Objekte verformen und dann zurück in ihre Ausgangsform schwingen, 
# ähnlich wie bei einem Netzwerk aus Federn. In dieser Simulation verwenden wir Federn, 
# um die Wechselwirkungen und Spannungen zwischen den Körpern zu modellieren. 
# Diese Strukturen ermöglichen komplexe dynamische Bewegungen und erlauben die 
# Simulation von Elastizität und Schwingungen in einem flexiblen Körper.

# ___________________________________________________
#                                                   /
# Grundkonzepte: Elastizität und Dämpfung           (
# __________________________________________________\

# - Elastizität:
#   Die elastische Kraft basiert auf dem Hookeschen Gesetz, das eine proportionale 
#   Beziehung zwischen der Auslenkung eines Körpers und der Rückstellkraft beschreibt.
#   Die Federn in diesem Modell simulieren diese elastische Wirkung, um Spannungen 
#   zwischen den verbundenen Körpern zu erzeugen.

# - Dämpfung:
#   Eine Dämpfungskraft ist in das Modell integriert, um die Schwingungen zu kontrollieren
#   und instabile oder unendliche Schwingungen zu vermeiden. Diese Dämpfung wirkt entgegen 
#   der Bewegungsrichtung und reduziert die Amplitude der Schwingungen mit der Zeit.



import arcade
import arcade.gui 
import numpy as np


# Die Klasse `Body` modelliert ein physikalisches Objekt in der Simulation, 
# das durch seine Position, Geschwindigkeit und Masse beschrieben wird.

class Body:
    def __init__(self, position, velocity, mass=1.0, radius=1.0, fixed=False, color=arcade.color.BLUE):
        self.mass = mass                                 # Masse in kg
        self.position = np.array(position, dtype=float)  # Position in m
        self.velocity = np.array(velocity, dtype=float)  # Geschwindigkeit in m/s
        self.acceleration = np.array([0.0, 0.0])         # Beschleunigung in m/s^2
        self.force = np.array([0.0, 0.0])                # Resultierende Kraft in N
        self.radius = radius    # Radius des Körpers in m
        self.fixed = fixed      # Körper wird festgehalten
        self.color = color      # Farbe für die Darstellung
        

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
        if self.fixed:
            self.force = np.array([0.0, 0.0]) 
            self.velocity = np.array([0.0, 0.0]) 
            return
        
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



# Die Klasse `Spring` simuliert eine Feder zwischen zwei Körpern. 
class Spring(Interaction):

    def __init__(self, bodyA, bodyB, k=1.0, length=None, damping=0.9, color=arcade.color.YELLOW):
        super().__init__(bodyA, bodyB)

        self.k = k # Federkonstante
        
        # Ursprungslänge der Feder
        if length is None:
            self.length = np.linalg.norm(bodyA.position - bodyB.position)
        else:
            self.length = length
        
        self.damping = damping # Dämpfungskonstante
        
        self.color = color 


    def calculate_spring_force(self):
        # Berechnet die Federkraft nach dem Hookeschen Gesetz.
        r_vector = self.bodyB.position - self.bodyA.position
        distance = np.linalg.norm(r_vector)
        extension = distance - self.length  # Auslenkung der Feder

        # Berechnet die Federkraft basierend auf der Auslenkung
        force_magnitude = -self.k * extension
        force_direction = r_vector / distance  # Einheitsvektor in Richtung des Abstandsvektors

        # Dämpfungskraft parallel zur Federkraft
        v_rel = self.bodyB.velocity - self.bodyA.velocity
        force_magnitude += -self.damping * np.dot(v_rel, force_direction)
        
        # Berechne die Federkraft
        return force_magnitude * force_direction


    def update(self):
        force = self.calculate_spring_force()
        self.bodyA.add_force(-force)
        self.bodyB.add_force(force)
    


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
        
        self.frame = 0
        
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

        # Initialisiere die Körper und Wechselwirkungen
        body1 = Body([-1, -1], [0, 5], mass=0.5, radius=0.2, color=arcade.color.RED)
        body2 = Body([0, 1], [0, 5], mass=0.5, radius=0.2, color=arcade.color.GREEN)
        body3 = Body([1, -1], [-5, 0], mass=0.5, radius=0.2, color=arcade.color.BLUE)
        
        self.bodies.extend([body1, body2, body3])
        
        spring12 = Spring(body1, body2, k=40.0, damping=0.98)
        spring13 = Spring(body1, body3, k=40.0, damping=0.98)
        spring23 = Spring(body2, body3, k=40.0, damping=0.98)

        self.interactions.extend([spring12, spring13, spring23])

    
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
        points = []
        points.append(self.meter_to_pixel(-4.5, 4.5))
        points.append(self.meter_to_pixel(-4.5, -4.5))
        points.append(self.meter_to_pixel(4.5, -4.5))
        points.append(self.meter_to_pixel(4.5, 4.5))
        points.append(self.meter_to_pixel(-4.5, 4.5))
        
        arcade.draw_line_strip(points, arcade.color.BLACK, 2)
        
        # Zeigt die Simulationszeit an
        time = round(self.t, 1)
        x, y = self.meter_to_pixel(-9, 3)
        arcade.draw_text(f"t = {time} s", x, y, arcade.color.BLACK)
        
        # Zeigt die FPS an
        fps = round(sum(self.fps_history) / len(self.fps_history), 1)
        x, y = self.meter_to_pixel(-9, 2.5)
        arcade.draw_text(f"FPS = {fps}", x, y, arcade.color.BLACK)

        # Zeichnet die Federn
        for interaction in self.interactions:
            xA, yA = self.meter_to_pixel(interaction.bodyA.position[0], interaction.bodyA.position[1])
            xB, yB = self.meter_to_pixel(interaction.bodyB.position[0], interaction.bodyB.position[1])
            
            arcade.draw_line(xA, yA, xB, yB , interaction.color, 2)
        
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
        
        # Überprüft und verarbeitet Kollisionen mit dem Boden
        for body in self.bodies:
            # Überprüft und verarbeitet Kollisionen mit dem Boden und der Decke
            if body.position[1] > 4.5 - body.radius:
                body.position[1] = 4.5 - body.radius
                body.velocity[1] *= -1
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
        self.t += dt
        
        # erhöhre die Framenummer
        self.frame += 1



if __name__ == "__main__":
    # Initialisiert das Fenster für die Simulation
    window = AnimationWindow(800, 600, "Elastischer Körper")

    # starte die Simulation
    arcade.run()





# ___________________________
#                           /
# Zusammenfassung          (
# __________________________\

# Zusammenfassend modelliert dieses Kapitel elastische Körper und zeigt, wie Federn 
# und Dämpfungskräfte zur Simulation von Spannungen und Deformationen zwischen 
# miteinander verbundenen Körpern eingesetzt werden können. Dies erlaubt die 
# Simulation von elastischen Eigenschaften und die Erforschung dynamischer 
# Schwingungen in Systemen, die unter äußeren Einflüssen stehen.



# ____________________________
#                            /
# Übungsaufgaben            (
# ____________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Experimentiere mit verschiedenen Federkonstanten und Dämpfungseinstellungen für die 
# elastischen Verbindungen. Beobachte, wie sich die Stabilität und Schwingungen der 
# elastischen Körper bei unterschiedlichen Werten für die Federkonstante k und die 
# Dämpfung ändern. Stelle die Werte so ein, dass die Bewegung stabil bleibt.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Rechteck aus vier elastischen Körpern, die über Federn 
# miteinander verbunden sind. Experimentiere mit verschiedenen Anfangs-
# geschwindigkeiten und beobachte, wie sich das Rechteck sich verhält. 
# Analysiere, wie sich das Rechteck deformiert und sich die Schwingungen 
# verhalten.

# Füge hier deine Lösung ein.



#               ..ee$$$$$ee..
#           .e$*""    $    ""*$e.            Das ist auch ein 
#         z$"*.       $         $$c          elastischer Körper.
#       z$"   *.      $       .P  ^$c
#      d"      *      $      z"     "b
#     $"        b     $     4%       ^$
#    d%         *     $     P         '$
#   .$          'F    $    J"          $r
#   4L...........b....$....$...........J$
#   $F           F    $    $           4$
#   4F          4F    $    4r          4P
#   ^$          $     $     b          $%
#    3L        .F     $     'r        JP
#     *c       $      $      3.      z$
#      *b     J"      $       3r    dP
#       ^$c  z%       $        "c z$"
#         "*$L        $        .d$"
#            "*$ee..  $  ..ze$P"  Gilo94'
#                ""*******""
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
# Experimentiere mit verschiedenen Federkonstanten und Dämpfungseinstellungen für die 
# elastischen Verbindungen. Beobachte, wie sich die Stabilität und Schwingungen der 
# elastischen Körper bei unterschiedlichen Werten für die Federkonstante k und die 
# Dämpfung ändern. Stelle die Werte so ein, dass die Bewegung stabil bleibt.

'''
        # Initialisiere die Körper und Wechselwirkungen
        body1 = Body([-1, -1], [0, 5], mass=1.0, radius=0.2, color=arcade.color.RED)
        body2 = Body([0, 1], [0, 5], mass=1.0, radius=0.2, color=arcade.color.GREEN)
        body3 = Body([1, -1], [-5, 0], mass=1.0, radius=0.2, color=arcade.color.BLUE)
        
        self.bodies.extend([body1, body2, body3])
        
        spring12 = Spring(body1, body2, k=4.0, damping=0.98)
        spring13 = Spring(body1, body3, k=4.0, damping=0.98)
        spring23 = Spring(body2, body3, k=4.0, damping=0.98)

        self.interactions.extend([spring12, spring13, spring23])
'''

# ___________
#            \
# Aufgabe 2  /
# __________/
#
#
# Erstelle ein Rechteck aus vier elastischen Körpern, die über Federn 
# miteinander verbunden sind. Experimentiere mit verschiedenen Anfangs-
# geschwindigkeiten und beobachte, wie sich das Rechteck sich verhält. 
# Analysiere, wie sich das Rechteck deformiert und sich die Schwingungen 
# verhalten.

'''
        # Initialisiere die Körper und Wechselwirkungen
        body1 = Body([-1, 1], [-2, -1], mass=1.0, radius=0.2, color=arcade.color.RED)
        body2 = Body([1, 1], [-2, -1], mass=1.0, radius=0.2, color=arcade.color.BLUE)
        body3 = Body([-1, -1], [1, 1], mass=1.0, radius=0.2, color=arcade.color.GREEN)
        body4 = Body([1, -1], [-1, -1], mass=1.0, radius=0.2, color=arcade.color.ORANGE)
        
        self.bodies.extend([body1, body2, body3, body4])
        
        # Füge die elastischen Verbindungen zwischen den Körpern hinzu, um das Rechteck zu bilden
        spring12 = Spring(body1, body2, k=50.0, damping=0.9)
        spring13 = Spring(body1, body3, k=50.0, damping=0.9)
        spring24 = Spring(body2, body4, k=50.0, damping=0.9)
        spring34 = Spring(body3, body4, k=50.0, damping=0.9)

        # Verbindungen entlang der Diagonalen für zusätzliche Stabilität
        spring14 = Spring(body1, body4, k=50.0, damping=0.9)
        spring23 = Spring(body2, body3, k=50.0, damping=0.9)
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


