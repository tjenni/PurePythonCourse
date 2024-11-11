#              ________________________________________________
#       ______|                                                |_____
#       \     |        13.3 KRÄFTE UND NEWTONS GESETZE         |    /
#        )    |________________________________________________|   (
#       /________)                                       (________\      7.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# In diesem Kapitel untersuchen wir, wie man Kräfte und Newtons Bewegungsgesetze
# in einer Simulation umsetzt. Dazu implementieren wir eine Klasse `Body`, die
# die grundlegenden Eigenschaften und Bewegungsgleichungen für ein Objekt beschreibt.


# _____________________________
#                              /
# Kräfte und Newtons Gesetze  (
# _____________________________\

# Nach Newtons zweitem Gesetz ist die resultierende Kraft auf ein Objekt
# proportional zu seiner Beschleunigung:
#
#     F = m * a
#
# Mit der Klasse `Body` können wir Objekte simulieren, die unter dem Einfluss
# verschiedener Kräfte beschleunigt werden. Beispiele sind Schwerkraft,
# Reibung und Federkraft (z.B. für harmonische Oszillatoren).


import numpy as np
import matplotlib.pyplot as plt


# _____________________________
#                              /
# Klasse Body                  (
# _____________________________\

# Die Klasse `Body` repräsentiert ein Objekt mit Masse, Position, Geschwindigkeit,
# und ermöglicht es, Kräfte zu berechnen und anzuwenden.

class Body:
    def __init__(self, position, velocity, mass):                                
        self.position = np.array(position, dtype=float)  # in m
        self.velocity = np.array(velocity, dtype=float)  # in m/s
        self.force = np.array([0.0, 0.0])                # in N
        self.mass = mass                                 # in kg

    # Setze die Kraft auf null
    def clear_force(self):
        self.force = np.array([0.0, 0.0])

    # Addiere eine Kraft
    def add_force(self, force):
        self.force += np.array(force, dtype=float)

    # Berechnen einen Zeitschritt mit dem Euler-Cromer-Verfahren    
    def update(self, dt):
        acceleration = self.force / self.mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt


    

# ________________________________
#                                /
# Freier Fall unter Schwerkraft (
# _______________________________\

# Ein einfaches Beispiel für die `Body`-Klasse ist ein fallendes Objekt
# unter der Wirkung der Schwerkraft ohne Luftwiderstand.

g = 9.81                     # Erdbeschleunigung in m/s^2

mass = 1.0                   # in kg
initial_position = [0, 100]  # in m
initial_velocity = [0, 0]    # in m/s


dt = 0.01       # Zeitschritt in s
t_end = 5.0     # Endzeit der Simulation in s

# Liste mit allen Zeiten in s
times = np.arange(0, t_end, dt)

# Liste zur Aufzeichnung der Bewegung
positions_1 = []       

# erstelle ein `Body`-Objekt
body = Body(initial_position, initial_velocity, mass)


# Simulation des freien Falls
for time in times:
    body.clear_force()
    
    F_G = [0.0, -body.mass * g]  # Schwerkraft
    body.add_force(F_G)
    
    body.update(dt)

    positions_1.append(body.position[1])  # Höhe speichern


# Visualisierung der Höhe über die Zeit
plt.plot(times, positions_1)
plt.xlabel("Zeit in s")
plt.ylabel("Höhe in m")
plt.title("Freier Fall")
plt.show()




# _____________________
#                     /
# Fall mit Reibung   (
# ____________________\

# Hier erweitern wir das Beispiel, indem wir eine einfache Luftreibung
# proportional zur Geschwindigkeit hinzufügen. Die Reibungskraft ist:
#     F_reibung = -k * v
# wobei k eine Reibungskonstante ist.

drag = 0.8  # Reibungskonstante

# Zurücksetzen der Anfangswerte
body.position = np.array([0.0, 100.0])
body.velocity = np.array([0.0, 0.0])

# Liste zur Aufzeichnung der Bewegung
positions_2 = []

# Simulation des Falls mit Reibung
for time in times:
    body.clear_force()
    
    F_G = [0.0, -body.mass * g] # Schwerkraft
    F_R = -drag * body.velocity   # Reibung

    body.add_force(F_G + F_R)
    
    body.update(dt)
    
    positions_2.append(body.position[1])  # Höhe speichern

# Visualisierung
plt.plot(times, positions_1, label="ohne Reibung")
plt.plot(times, positions_2, label="mit Reibung")
plt.xlabel("Zeit in s")
plt.ylabel("Höhe in m")
plt.title("Freier Fall")
plt.legend()
plt.show()




# ________________________________
#                                /
# Schwingungen mit Federkraft   (
# _______________________________\

# Jetzt fügen wir eine Federkraft hinzu, um eine harmonische Schwingung zu simulieren:
#
#     F_feder = -D * x
#
# wobei `D` die Federkonstante ist und x die Auslenkung.

D = 5.0  # Federkonstante in N/m

# Zurücksetzen der Anfangswerte für die harmonische Bewegung
body.position = np.array([1.0, 0.0])  # Auslenkung von 1 m in x-Richtung
body.velocity = np.array([0.0, 0.0])

# Liste zur Aufzeichnung der Bewegung
positions_3 = []

# Simulation der harmonischen Schwingung
for time in times:
    body.clear_force()
    
    # Federkraft in x-Richtung
    F_F = -D * body.position[0]
    body.add_force([F_F, 0])
    
    body.update(dt)

    positions_3.append(body.position[0])  # x-Position speichern

# Visualisierung der Schwingung
plt.plot(times, positions_3)
plt.xlabel("Zeit in s")
plt.ylabel("Auslenkung in m")
plt.title("Harmonische Schwingung")
plt.show()




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Die Klasse `Body` ermöglicht es, Kräfte und Bewegung nach Newtons
#   Gesetzen zu simulieren.
#
# - Schwerkraft: Einfache Kraft nach Newton, die auf das Objekt wirkt.
#
# - Reibung: Modelliert durch eine Kraft proportional zur Geschwindigkeit.
#
# - Federkraft: Erzeugt eine harmonische Schwingung als einfache Modellierung
#   eines Oszillators.
#
# Diese Simulationen helfen, Kräfte und Bewegung physikalisch zu verstehen und
# sind die Grundlage für komplexere physikalische Simulationen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\

# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Simuliere eine gedämpfte harmonische Schwingung. Füge zur Federkraft eine
# Dämpfungskraft hinzu, die proportional zur Geschwindigkeit ist, mit einer 
# Dämpfungskonstanten `d`. Experimentiere mit verschiedenen Werten für `d`
# (z. B. 0.1, 0.5 und 1.0) und zeichne die Position über die Zeit.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Simuliere die Bewegung eines Fallschirmspringers mit der Masse 60 kg, der in 
# einer Höhe von 1000 m aus einem Flugzeug springt. Das Flugzeug hat eine 
# Geschwindigkeit in x-Richtung von 360 km/h. Berechne die Reibungskraft mit 
# der Formel
#
#     friction = -drag * np.linalg.norm(body.v) * body.v
#
# wodurch die Luftreibungskraft quadratisch mit der Geschwindigkeit zunimmt. 
#
# Zeichne die Flugbahn des Springers und die Geschwindigkeit in x- und y-Richtung 
# über die Zeit. Sorge dafür, dass der Fallschirmspringer nicht zu schnell 
# auf dem Boden auftrifft. 


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
# Simuliere eine gedämpfte harmonische Schwingung. Füge zur Federkraft eine
# Dämpfungskraft hinzu, die proportional zur Geschwindigkeit ist, mit einer 
# Dämpfungskonstanten `d`. Experimentiere mit verschiedenen Werten für `d`
# (z. B. 0.1, 0.5 und 1.0) und zeichne die Position über die Zeit.

'''
import numpy as np
import matplotlib.pyplot as plt

# Definition der Body-Klasse
class Body:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = np.array(position, dtype=float)  # Position [x, y]
        self.velocity = np.array(velocity, dtype=float)  # Geschwindigkeit [vx, vy]
        self.force = np.array([0.0, 0.0])  # Resultierende Kraft [Fx, Fy]

    def clear_force(self):
        self.force = np.array([0.0, 0.0])

    def add_force(self, force):
        self.force += np.array(force, dtype=float)

    def update(self, dt):
        acceleration = self.force / self.mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt


# Parameter für die gedämpfte Schwingung
mass = 1.0  # Masse in kg
k_spring = 5.0  # Federkonstante in N/m
d_values = [0.1, 0.5, 1.0]  # Dämpfungskonstanten

dt = 0.01  # Zeitschritt in Sekunden
t_end = 10.0  # Endzeit der Simulation in Sekunden

times = np.arange(0, t_end, dt)

plt.figure(figsize=(10, 6))

# Simulation für jede Dämpfungskonstante
for d in d_values:
    body = Body(mass, [1.0, 0.0], [0.0, 0.0])  # Startauslenkung von 1 m und null Geschwindigkeit
    positions = []

    for t in times:
        body.clear_force()
        
        # Federkraft
        spring_force = -k_spring * body.position[0]

        # Dämpfungskraft
        damping_force = -d * body.velocity[0]
        
        body.add_force([spring_force + damping_force, 0.0])  # Kraft in x-Richtung anwenden
        body.update(dt)
        
        positions.append(body.position[0])  # x-Position speichern

    plt.plot(times, positions, label=f"Dämpfung d = {d}")

plt.xlabel("Zeit in s")
plt.ylabel("Auslenkung in m")
plt.title("Gedämpfte harmonische Schwingung")
plt.legend()
plt.show()
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Simuliere die Bewegung eines Fallschirmspringers mit der Masse 60 kg, der in 
# einer Höhe von 1000 m aus einem Flugzeug springt. Das Flugzeug hat eine 
# Geschwindigkeit in x-Richtung von 360 km/h. Berechne die Reibungskraft mit 
# der Formel
#
#     friction = -drag * np.linalg.norm(body.v) * body.v
#
# wodurch die Luftreibungskraft quadratisch mit der Geschwindigkeit zunimmt. 
#
# Zeichne die Flugbahn des Springers und die Geschwindigkeit in x- und y-Richtung 
# über die Zeit. Sorge dafür, dass der Fallschirmspringer nicht zu schnell 
# auf dem Boden auftrifft. 


'''
import numpy as np
import matplotlib.pyplot as plt

# Parameter für den Fallschirmspringer

mass = 60.0  # Masse des Fallschirmspringers in kg
g = 9.81  # Erdbeschleunigung in m/s^2

drag_1 = 0.1  # Reibungskoeffizient ungeöffneter Fallschirm
drag_2 = 30 # Reibungskoeffizient offener Fallschirm

y_0 = 1000  # Starthöhe in Metern
vx_0 = 360 * 1000 / 3600  # Geschwindigkeit in x-Richtung, umgerechnet von km/h in m/s

dt = 0.01  # Zeitschritt in Sekunden
t_end = 60.0  # Endzeit der Simulation in Sekunden


# Initialisiere den Body für den Fallschirmspringer
class Body:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = np.array(position, dtype=float)  # Position [x, y]
        self.velocity = np.array(velocity, dtype=float)  # Geschwindigkeit [vx, vy]
        self.force = np.array([0.0, 0.0])  # Resultierende Kraft [Fx, Fy]

    def clear_force(self):
        self.force = np.array([0.0, 0.0])

    def add_force(self, force):
        self.force += np.array(force, dtype=float)

    def update(self, dt):
        acceleration = self.force / self.mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt


# Erstellen des Body-Objekts
body = Body(mass, [0.0, y_0], [vx_0, 0.0])

# Listen zur Aufzeichnung der Position und Geschwindigkeit
x = []
y = []
vx = []
vy = []
times = np.arange(0, t_end, dt)

# Simulation der Bewegung
for t in times:
    body.clear_force()
    
    if t < 10:
        drag = drag_1
    else:
        drag = drag_2
    
    # Schwerkraft in y-Richtung
    gravity = np.array([0.0, -body.mass * g])
    
    # Luftreibung proportional zur Geschwindigkeit in x- und y-Richtung
    friction = -drag * np.linalg.norm(body.velocity) * body.velocity  # Reibungskraft
    
    # Gesamtkräfte anwenden
    body.add_force(gravity + friction)
    
    # Update der Position und Geschwindigkeit
    body.update(dt)
    
    # Position und Geschwindigkeit speichern
    x.append(body.position[0])
    y.append(body.position[1])
    vx.append(body.velocity[0])
    vy.append(body.velocity[1])

    # Simulation abbrechen, wenn der Fallschirmspringer den Boden erreicht
    if body.position[1] <= 0:
        break

# Visualisierung der Trajektorie eines Fallschirmspringers
plt.figure(figsize=(6, 7))
plt.subplot(2, 1, 1)
plt.plot(x, y, color="blue")
plt.xlabel("x in m")
plt.ylabel("y in m")
plt.title("Trajektorie des Fallschirmspringers")

# Visualisierung der Geschwindigkeit in x- und y-Richtung über die Zeit
plt.subplot(2, 1, 2)
plt.plot(times[:len(vx)], vx, label="vx in m/s", color="red")
plt.plot(times[:len(vy)], vy, label="vy in m/s", color="green")
plt.xlabel("Zeit in s")
plt.ylabel("Geschwindigkeit in m/s")
plt.title("Geschwindigkeit des Fallschirmspringers")
plt.legend()

plt.tight_layout()
plt.show()
'''



# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><




