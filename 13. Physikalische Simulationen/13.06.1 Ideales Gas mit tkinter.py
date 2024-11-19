#              _______________________________________
#       ______|                                       |_____
#       \     |    13.6.1 IDEALES GAS MIT TKINTER     |    /
#        )    |_______________________________________|   (
#       /________)                                (________\      13.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# In diesem Kapitel entwickeln wir eine Simulation eines idealen Gases mithilfe der 
# Tkinter-Bibliothek. Die Simulation visualisiert Partikel, die sich in einem 
# geschlossenen Raum frei bewegen und miteinander kollidieren. Damit können wir 
# einige grundlegende thermodynamische Eigenschaften untersuchen, wie die kinetische 
# Energie, die Temperatur und die Geschwindigkeitsverteilung eines idealen Gases.

# Die Simulation verwendet `matplotlib`, um die Gesamtenergie und die Geschwindigkeits-
# verteilung der Teilchen als Diagramme darzustellen. 

# Da `tkinter` im Vergleich zur Arcade-Bibliothek weniger auf Animationen und grafische 
# Effekte optimiert ist, erfordert es spezielle Anpassungen für eine reibungslose 
# Leistung. Ein wesentlicher Beitrag zur Leistung liefert das `threading`-Moduls. 
# Es ermöglicht die Berechnungen parallel zur grafischen Oberfläche durchzuführen 
# und so die Performance zu verbessern. 

# Die Simulation illustriert Konzepte der kinetischen Gastheorie, indem die Teilchen als 
# elastische Kugeln behandelt werden. Durch Interaktionen zwischen den Partikeln und 
# Kollisionen mit den Wänden entstehen dynamische Geschwindigkeits- und Energieverteilungen, 
# die typisch für ein ideales Gas sind. So können wir durch Anpassungen der Simulation, 
# wie das Erhöhen oder Reduzieren der Geschwindigkeit aller Partikel (Heizen oder Kühlen), 
# nachvollziehen, wie diese Eigenschaften mit der thermischen Energie in Zusammenhang stehen. 

# Diese Simulation bietet eine wertvolle Basis, um die grundlegenden Prinzipien der 
# statistischen Mechanik und Thermodynamik zu veranschaulichen.



import tkinter as tk
import numpy as np
import random
import threading
import time
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk



class Body:
    def __init__(self, mass, position, velocity, radius=5):
        self.mass = mass
        self.position = np.array(position, dtype=float)  # Aktuelle Position
        self.velocity = np.array(velocity, dtype=float)  # Aktuelle Geschwindigkeit
        self.radius = radius  # Radius des Körpers

    def clear_force(self):
        # Setzt die Kräfte zurück (aktuell keine äußeren Kräfte)
        self.force = np.array([0.0, 0.0])

    def apply_force(self, force):
        # Wendet eine gegebene Kraft auf den Körper an
        self.force += np.array(force, dtype=float)

    def update_ec(self, dt):
        # Aktualisiert die Geschwindigkeit und Position des Körpers für den nächsten Zeitschritt
        acceleration = self.force / self.mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt

    def kinetic_energy(self):
        # Berechnet die kinetische Energie des Körpers
        return 0.5 * self.mass * np.linalg.norm(self.velocity)**2




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




class SimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ideales Gas")
        
        # Canvas für die Darstellung der Teilchen
        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.grid(row = 0, column = 0, sticky = tk.N, pady = 2)
        
        # Frame für Buttons
        self.frame = tk.Frame(root, width=300)
        self.frame.grid(row = 0, column = 1, sticky = tk.NW, pady = 2)
        
        # Start-Stop Button
        self.button_1 = tk.Button(self.frame, text ="Start", command = self.start_stop)
        self.button_1.grid(row = 0, column = 0)
        
        # Heizen Button
        self.button_2 = tk.Button(self.frame, text ="heizen", command = self.heat)
        self.button_2.grid(row = 0, column = 1)
        
        # Kühlen Button
        self.button_3 = tk.Button(self.frame, text ="kühlen", command = self.cool)
        self.button_3.grid(row = 0, column = 2)
        
        # Textfeld für Infos
        self.label_1 = tk.Label(self.frame, text= "", font= ('Aerial', 17), justify="left")
        self.label_1.grid(row = 1, columnspan = 3, sticky=tk.NW)
        
        # Variablen für die Simulation
        self.bodies = []  # Liste der Teilchen
        self.interactions = []  # Liste der Wechselwirkungen
        
        # Liste für die Berechnung des gleitenden Durchschnitts der FPS
        self.fps_history = [0] * 60
        self.fps_time = 0
            
        # Energie-Zeit-Diagramm
        self.energies = 60*[0] 
        self.times = 60*[0] 

        self.fig1, self.ax1 = plt.subplots(figsize=(4, 3),constrained_layout=True)
        self.ax1.set_xlabel("Zeit [s]")
        self.ax1.set_ylabel("Gesamtenergie [J]")
        self.ax1.set_ylim(bottom=0, top=20)
        self.line1, = self.ax1.plot([], [], color="blue")
        
        # bette matplotlib in tkinter ein
        self.plot1 = FigureCanvasTkAgg(self.fig1, master=self.root)
        self.plot1.get_tk_widget().grid(row = 1, column = 0, sticky = tk.W, pady = 2)
        
        # matplotlib-Toolbar
        self.toolbar1 = NavigationToolbar2Tk(self.plot1, self.root, pack_toolbar=False)
        self.toolbar1.update()
        self.toolbar1.grid(row = 2, column = 0, sticky = tk.W, pady = 2)
        
        
        # Histogramm der Geschwindigkeiten
        self.fig2, self.ax2 = plt.subplots(figsize=(4, 3),constrained_layout=True)
        self.ax2.set_ylabel("Häufigkeit")
        self.ax2.set_xlabel("Geschwindigkeit [m/s]")
        self.ax2.set_ylim(bottom=0, top=50)
        self.line2, = self.ax2.plot([], [], color="blue")
        
        # Bette matplotlib in tkinter ein
        self.plot2 = FigureCanvasTkAgg(self.fig2, master=root)
        self.plot2.get_tk_widget().grid(row = 1, column = 1, sticky = tk.W, pady = 2)
        
        # matplotlib-Toolbar
        self.toolbar2 = NavigationToolbar2Tk(self.plot2, self.root, pack_toolbar=False)
        self.toolbar2.update()
        self.toolbar2.grid(row = 2, column = 1, sticky = tk.W, pady = 2)
        
        # Status
        self.state = 0
        
        # Zeit
        self.time = 0
        self.dt = 1 
        
        # Erstelle die Teilchen in einem Raster
        for i in range(10):
            for j in range(10):
                vx = 0.5 - random.random()  # Zufällige x-Geschwindigekeit
                vy = 0.5 - random.random()  # Zufällige y-Geschwindigekeit
                body = Body(1.0, [15.0 + i*30.0, 15.0 + j*30.0], [vx, vy], radius=5.0)
                self.bodies.append(body)

        # Erstelle alle Wechselwirkungen zwischen den Teilchen.
        for i in range(len(self.bodies)):
            for j in range(i + 1, len(self.bodies)):
                self.interactions.append(Collision(self.bodies[i], self.bodies[j]))
        
        
        # Erstelle alle canvas Objekte für die Darstellung der Teilchen
        for body in self.bodies:
            x, y = body.position
            body.oval = self.canvas.create_oval(x - body.radius, y - body.radius,
                                    x + body.radius, y + body.radius, fill="red")
        # zeichne alles            
        self.draw()
        

    # starte oder stoppe die Simulation
    def start_stop(self):
        if self.state == 0:
            self.state = 1
            self.button_1.configure(text="Stop") 
        else:
            self.fps_time = time.time()
            self.state = 0
            self.button_1.configure(text="Start")
            
    
    # Die Geschwindigkeit von allen Körper wird erhöht.
    def heat(self):
        for body in self.bodies:
            body.velocity *= 1.2
            
    
    # Die Geschwindigkeit von allen Körper wird reduziert.
    def cool(self):
        for body in self.bodies:
            body.velocity *= 0.8
            
            
    def update(self):
        while True:
            # Pausiere die Simulation
            if self.state != 1:
                time.sleep(0.01)
                continue
            
            # Aktualisiert die FPS-Berechnung (gleitender Durchschnitt)
            time_passed = time.time() - self.fps_time
            self.fps_time = time.time()
            
            self.fps_history.append(1.0 / time_passed)               
            self.fps_history.pop(0)
            
            # Aktualisiere Simulationszeit
            self.time += self.dt
    
            # Setze alle Kräfte auf null
            for body in self.bodies:
                body.clear_force()

            # Berechne die Wechselwirkungen
            for interaction in self.interactions:
                interaction.update()
                
            # Euler-Cromer-Schritt
            for body in self.bodies:
                body.update_ec(self.dt)
            
            # Überprüfe die Kollisionen mit den Wänden
            for body in self.bodies:
                if body.position[0] <= body.radius:
                    body.position[0] = body.radius
                    body.velocity[0] *= -1
                elif body.position[0] >= 300 - body.radius:
                    body.position[0] = 300 - body.radius
                    body.velocity[0] *= -1
                    
                if body.position[1] <= body.radius:
                    body.velocity[1] *= -1
                    body.position[1] = body.radius
                elif body.position[1] >= 300 - body.radius:
                    body.velocity[1] *= -1
                    body.position[1] = 300 - body.radius

            time.sleep(0.01)
    
    
    # Aktualisiere die Kreise auf der canvas
    def draw(self):
        for body in self.bodies:
            x, y = body.position
            self.canvas.coords(body.oval, x-body.radius , y-body.radius, x+body.radius , y+body.radius)
        
        # Aktualisiere die Diagramme und die Information
        self.update_energy_plot()
        self.update_histogram_plot()
        self.update_label()
    
        # Rufe diese Funktion nach 10 ms erneut auf.        
        self.root.after(10, self.draw)
        
    
     # Aktualisiere das Geschwindigkeits-Histogramm
    def update_histogram_plot(self): 
        bins = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
        velocities = []

        for body in self.bodies:
            velocities.append(np.linalg.norm(body.velocity))
        
        v_list = np.histogram(velocities)
        
        self.line2.set_data(bins[:-1], v_list[0] )
        self.ax2.relim()
        self.ax2.autoscale_view()
        self.plot2.draw()
        
    
    # Berechne und speichere die Energie
    def update_energy_plot(self):
        total_energy = sum(body.kinetic_energy() for body in self.bodies)
        self.energies.append(total_energy)
        self.energies.pop(0)
        
        self.times.append(self.time)
        self.times.pop(0)
        
        # berechne y-Skala
        max_energy = max(self.energies)
        self.ax1.set_ylim(bottom=0, top=max(20, 1.1*max_energy))
        
        # Aktualisiere das Energie-Zeit-Diagramm
        self.line1.set_data(self.times, self.energies)
        self.ax1.relim()
        self.ax1.autoscale_view()
        self.plot1.draw()
        
    
    # Aktualisiere die Informationen
    def update_label(self):
        fps = round(sum(self.fps_history) / len(self.fps_history), 1)
        
        text = f"N = {len(self.bodies)}\n"
        text += f"FPS = {fps}"
        self.label_1.configure(text=text) 


if __name__ == "__main__":
    root = tk.Tk()
    app = SimulationApp(root)
    
    # Starte die Simulation in einem eigenen Thread
    thread = threading.Thread(target=app.update, daemon=True)
    thread.start()

    root.mainloop()


# __________________________
#                           /
# Zusammenfassung          (
# __________________________\

# In diesem Kapitel haben wir eine Simulation eines idealen Gases mithilfe von Tkinter entwickelt. 
# Die Simulation zeigt Partikel, die in einem geschlossenen Raum kollidieren und thermodynamische 
# Eigenschaften eines idealen Gases darstellen, wie z. B. die kinetische Energie und 
# die Verteilung der Teilchengeschwindigkeit. Die matplotlib-Bibliothek wird verwendet, um die 
# Gesamtenergie und die Geschwindigkeitsverteilung zu visualisieren. Durch die Anpassung der 
# Partikelgeschwindigkeiten (z. B. durch Heizen und Kühlen) können wir nachvollziehen, wie die 
# thermische Energie mit der Geschwindigkeit der Partikel zusammenhängt. 

# Die Simulation illustriert die kinetische Gastheorie, indem sie die Teilchen als elastische Kugeln 
# behandelt. Die Verteilung der Geschwindigkeiten sowie die Berechnung der Gesamtenergie geben einen 
# guten Überblick über die thermodynamischen Zustandsgrößen eines idealen Gases. Die Umsetzung in Tkinter 
# zeigt zudem, wie komplexe Animationen und Berechnungen auch in einem Framework für einfache GUI-Programmierung 
# umgesetzt werden können.

# Diese Simulation bietet eine ausgezeichnete Möglichkeit, die Grundlagen der statistischen Mechanik und 
# Thermodynamik zu erforschen, indem man mit den Parametern und Bedingungen experimentiert.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Verwende die Buttons „Heizen“ und „Kühlen“ und beobachte, wie sich die 
# durchschnittliche Geschwindigkeit der Teilchen im Geschwindigkeits-Histogramm 
# verändert. Stelle fest, wie sich die thermische Energie und die Gesamtenergie 
# im Diagramm verhält, wenn die Temperatur verändert wird. Wie ist der Zusammenhang 
# zwischen der thermischen Energie und der Geschwindigkeit der Partikel?


# Füge hier deine Lösung ein.



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Stelle dir vor, du möchtest die Auswirkungen von Reibung auf die Partikel simulieren. 
# Erweitere das Programm, sodass die Partikel allmählich langsamer werden und zur Ruhe 
# kommen. Überlege, wie sich diese Änderung auf die Energie- und 
# Geschwindigkeitsdiagramme auswirken könnte.


# Füge hier deine Lösung ein.




#                              /\          /\
#     Tkinter ist manchmal    ( \\        // )
#       wie ein                \ \\      // /
#                               \_\\||||//_/ 
#                                \/ _  _ \ 
#                               \/|(O)(O)|
#                              \/ |      |         
#          ___________________\/  \      /
#         //                //     |____|      
#        //                ||     /      \
#       //|                \|     \ 0  0 /
#      // \       )         V    / \____/ 
#     //   \     /        (     /
#    ""     \   /_________|  |_/
#           /  /\   /     |  ||
#          /  / /  /      \  ||
#          | |  | |        | ||
#          | |  | |        | ||  
#          |_|  |_|        |_||       
#           \_\  \_\        \_\\ Hard'96  
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
# Verwende die Buttons „Heizen“ und „Kühlen“ und beobachte, wie sich die 
# durchschnittliche Geschwindigkeit der Teilchen im Geschwindigkeits-Histogramm 
# verändert. Stelle fest, wie sich die thermische Energie und die Gesamtenergie 
# im Diagramm verhält, wenn die Temperatur verändert wird. Wie ist der Zusammenhang 
# zwischen der thermischen Energie und der Geschwindigkeit der Partikel?

'''
# Lösung:
# Bei Verwendung der „Heizen“- und „Kühlen“-Buttons zeigt das Geschwindigkeits-Histogramm, 
# dass die durchschnittliche Geschwindigkeit der Partikel zunimmt, wenn wir den „Heizen“-Button 
# verwenden, und abnimmt, wenn wir den „Kühlen“-Button verwenden. Dies liegt daran, dass die 
# Geschwindigkeit der Partikel direkt mit der thermischen Energie verbunden ist. Wenn die 
# Temperatur erhöht wird, steigt die kinetische Energie der Teilchen, und somit auch die 
# durchschnittliche Geschwindigkeit. Das Histogramm zeigt, dass die Partikel schneller 
# werden, da sich die Balken nach rechts verschieben. 

# Die Gesamtenergie im Diagramm nimmt ebenfalls zu, wenn „Heizen“ gedrückt wird, 
# da die kinetische Energie der Partikel direkt proportional zur thermischen Energie ist. 
# Analog dazu sinkt die Gesamtenergie beim „Kühlen“, da die Geschwindigkeiten und 
# somit die kinetische Energie der Partikel verringert werden. 
# Dieser Zusammenhang entspricht der kinetischen Gastheorie, bei der die Temperatur 
# proportional zur durchschnittlichen kinetischen Energie der Moleküle ist.
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Stelle dir vor, du möchtest die Auswirkungen von Reibung auf die Partikel simulieren. 
# Erweitere das Programm, sodass die Partikel allmählich langsamer werden und zur Ruhe 
# kommen. Überlege, wie sich diese Änderung auf die Energie- und 
# Geschwindigkeitsdiagramme auswirken könnte.

'''
# Lösung:
# Um die Auswirkungen von Reibung auf die Partikel zu simulieren, können wir eine 
# Reibungskraft hinzufügen, die proportional zur Geschwindigkeit jedes Partikels ist. 
# Diese Kraft wirkt der Bewegungsrichtung der Partikel entgegen und verlangsamt sie allmählich. 
# Beispielsweise können wir die Geschwindigkeit in jedem Zeitschritt um einen kleinen 
# Faktor reduzieren, um eine einfache Reibung zu simulieren:

for body in self.bodies:
    body.velocity *= 0.99  # 1% Geschwindigkeitsverlust pro Zeitschritt

# Diese Änderung hat die folgenden Effekte auf die Diagramme:
# - Im Energie-Zeit-Diagramm wird die Gesamtenergie allmählich abnehmen, da die kinetische Energie 
#   der Partikel verloren geht.
# - Im Geschwindigkeits-Histogramm verschiebt sich die Verteilung allmählich nach links, 
#   da die Teilchen langsamer werden. Die Verteilung wird im Laufe der Zeit enger 
#   werden, bis alle Partikel zur Ruhe gekommen sind und das System im Gleichgewicht steht.

# Durch diese Anpassung können wir untersuchen, wie ein System Energie verliert und 
# zur Ruhe kommt, was den Konzepten von Dämpfung und Energieverlust durch Reibung in realen 
# physikalischen Systemen entspricht.
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><




