#              ____________________________________
#       ______|                                    |_____
#       \     |   13.8.2 DAS DREIKÖRPERPROBLEM     |    /
#        )    |____________________________________|   (
#       /________)                             (________\      11.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Das Dreikörperproblem beschreibt die komplexe Bewegung dreier Körper unter der 
# gegenseitigen Anziehungskraft. Beispiele dafür sind die Sonne, die Erde und der 
# Mond in unserem Sonnensystem. Im Gegensatz zu einfachen Zwei-Körper-Problemen 
# führt die Einführung eines dritten Körpers zu chaotischem Verhalten, das analytisch 
# nicht mehr gelöst werden kann. Daher verwenden wir numerische Methoden wie 
# das Runge-Kutta-Verfahren zur Simulation.

# Dieses Kapitel führt ein Python-Programm ein, das die Bewegung von drei Körpern 
# unter dem Einfluss der Gravitation simuliert. Dabei wird das 
# `Runge-Kutta-Verfahren zweiter Ordnung` zur Berechnung der Positionen und 
# Geschwindigkeiten der Körper verwendet.


import numpy as np
import matplotlib.pyplot as plt


# _______________________
#                        /
# Klasse Body           (
# _______________________\
#
# Die Klasse `Body` repräsentiert einen Körper mit Position, Geschwindigkeit, Masse 
# und Radius. Die Methode `update` aktualisiert die Position und Geschwindigkeit 
# des Körpers.

class Body:
    def __init__(self, position=[0.0, 0.0], velocity=[0.0, 0.0], mass=1.0):
        self.position = position.copy()
        self.velocity = velocity.copy()
        self.mass = mass
        
    def update(self, position, velocity):
        self.position = position
        self.velocity = velocity


# _______________________
#                        /
# Klasse World          (
# _______________________\
#
# Die Klasse `World` verwaltet die Berechnung der Gravitationskräfte zwischen 
# allen Körpern und führt die Berechnungen für das Runge-Kutta-Verfahren 2. Ordnung 
# durch. Die Methode `simulate` führt die Zeitschritte der Simulation aus und speichert 
# die Positionen der Körper für die Visualisierung.

class World:
    
    # Gravitationskonstante
    G = 6.67430e-11  # m^3 kg^-1 s^-2
    
    def __init__(self):
        self.positions = []
        self.velocities = []
        self.masses = []
        
        self.bodies = []
        
    
    # Hinzufügen eines Körpers zur Welt
    def add_body(self, body):
        self.bodies.append(body)
        
        # Kopiere die Daten des Körpers in die Weltarrays
        self.positions.append(body.position.copy())
        self.velocities.append(body.velocity.copy())
        self.masses.append(body.mass)
        

    # Berechne die Gravitationskraft zwischen zwei Massen.
    def gravity(self, pos1, pos2, m1, m2):
        r_vec = pos2 - pos1
        distance = np.linalg.norm(r_vec)
        
        if distance == 0:
            return np.array([0.0, 0.0])  # Keine Kraft bei null Abstand
        
        force_magnitude = World.G * m1 * m2 / distance**2
        force_direction = r_vec / distance  # Einheitsvektor
        
        return force_magnitude * force_direction

    
    # Berechne die Kräfte zwischen den Körpern
    def calculate_forces(self, positions, masses):
        forces = np.zeros_like(positions)
    
        for i in range(len(masses)):
            for j in range(i + 1, len(masses)):
                force = self.gravity(positions[i], positions[j], masses[i], masses[j])
                forces[i] += force
                forces[j] -= force
        
        return forces
    
    
    # Runge-Kutta-2-Update zur Berechnung des nächsten Zeitschritts
    def update_rk2(self, dt):
        
        # Kräfte beim Start des Zeitschritts berechnen
        forces = self.calculate_forces(self.positions, self.masses)
    
        # k1 für Positionen und Geschwindigkeiten berechnen
        k1_v = dt * forces / self.masses[:, None]
        k1_y = dt * self.velocities

        # Zwischenschritt für k2
        mid_positions = self.positions + 0.5 * k1_y
        mid_velocities = self.velocities + 0.5 * k1_v
        
        # Kräfte im Zwischenschritt berechnen
        mid_forces = self.calculate_forces(mid_positions, self.masses)
        
        # k2 für Positionen und Geschwindigkeiten berechnen
        k2_v = dt * mid_forces / self.masses[:, None]
        k2_y = dt * mid_velocities

        # Positionen und Geschwindigkeiten aktualisieren
        self.positions += k2_y
        self.velocities += k2_v
        
        
    # Simulation ausführen
    def simulate(self, dt, time_end):
        
        # Kopiere die Körperdaten in numpy-Arrays für die Berechnung
        self.positions = np.array(self.positions)
        self.velocities = np.array(self.velocities)
        self.masses = np.array(self.masses)
        
        # Erstelle ein Array für die Visualisierung der Positionen
        positions = [[] for _ in self.bodies]
        
        time_elapsed = 0

        while time_elapsed < time_end:
            
            self.update_rk2(dt)
            
            # Füge die berechneten Positionen zum array positions hinzu.
            for i, body in enumerate(self.bodies):
                body.update(self.positions[i], self.velocities[i])
                positions[i].append(body.position.copy())
            
            time_elapsed += dt
            
        return [np.array(pos) for pos in positions]


# ____________________________________
#                                    /
# Hauptprogramm und Visualisierung  (
# ___________________________________\

# Instanziiere das `World`-Objekt und füge Körper hinzu (Sonne, Erde und Mond)
world = World()

# Sonne
sun = Body([0.0, 0.0], [0.0, 0.0], mass=1.989e30)  
world.add_body(sun)

# Erde
earth = Body([1.496e11, 0], [0, 29.78e3], mass=5.972e24)
world.add_body(earth)

# Mond
moon = Body([1.496e11 + 3.844e8, 0], [0, 29.78e3 + 1.022e3], mass=7.348e22)  
world.add_body(moon)


# Parameter für die Simulation
dt = 1000           # Zeitschritt in Sekunden   
time_end = 3.154e7  # Sekunden eines Jahres

# Simulation ausführen und Positionen zurückgeben
positions = world.simulate(dt, time_end)


# Visualisiere die Resultate
plt.figure(figsize=(10, 10))
plt.plot(positions[0][:,0], positions[0][:,1], label="Körper 1 (z.B. Sonne)")
plt.plot(positions[1][:,0], positions[1][:,1], label="Körper 2 (z.B. Erde)")
plt.plot(positions[2][:,0], positions[2][:,1], label="Körper 3 (z.B. Mond)")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.legend()
plt.title("Dreikörperproblem")
plt.grid()
plt.axis("equal")
plt.show()




# _____________________________
#                             /
# Übungsaufgaben             (
# ____________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Untersuchung der Umlaufbahn des Mondes
# --------------------------------------
# Ändere die Anfangsposition oder -geschwindigkeit des Mondes und beobachte,
# wie sich die Bahnkurven der Erde und des Mondes um die Sonne ändern.
#
# Ziel: Finde eine Kombination, bei der der Mond eine stabile Umlaufbahn
#       um die Erde beibehält, während beide die Sonne umkreisen.
#
# Zusatz: Beobachte, wie leichte Veränderungen der Anfangsgeschwindigkeit
#         des Mondes zu chaotischen Bahnen führen können.
#
# Hinweis: Ändere die Anfangswerte des Mondes und starte die Simulation neu.


# Füge hier deinen Code zur Anpassung der Startbedingungen und Auswertung ein.



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Trifft der Komet die Erde?
# --------------------------
# Ergänze die Simulation um einen Kometen und untersuche, ob dieser die Erde trifft
# oder ob er das Sonnensystem nur durchquert. Der Komet beginnt seine Bahn außerhalb
# der Erdbahn und bewegt sich mit hoher Geschwindigkeit Richtung Sonne.
#
# - Komet:
#     - Position (x): 2.5e11 m (entspricht etwa 1.67-facher Erdentfernung zur Sonne)
#     - Geschwindigkeit (y): -3.0e4 m/s (auf die Sonne zugehend)
#     - Masse: 1.0e14 kg (fiktive Masse)
#
# - Simulation:
#     - Führe die Simulation über einen Zeitraum von etwa 1 Jahr durch 
#       (3.154e7 Sekunden).
#
#     - Zeichne die Bahn des Kometen sowie der Erde und der Sonne auf, 
#       um zu beobachten, ob der Komet die Erde kreuzt oder sich eine Kollision 
#       ereignet.
#       
# - Zusatzaufgaben:
#     - Annäherung: Wenn keine Kollision stattfindet, bestimme den minimalen
#       Abstand zwischen dem Kometen und der Erde während der Simulation.
#
#     - Geschwindigkeitsvariation: Experimentiere mit leicht veränderten
#       Startgeschwindigkeiten (z. B. -2.5e4 m/s oder -3.5e4 m/s), um zu sehen, ob
#       sich die Bahn des Kometen dadurch beeinflussen lässt.
#
# Hinweise:
# - Um eine Kollision zu detektieren, prüfe während der Simulation den Abstand zwischen
#   Erde und Komet. Falls dieser Abstand kleiner als der Radius der Erde ist (6.371e6 m),
#   könnte eine Kollision vorliegen.
#
# - Achte auf die Einheiten der Positionen und Geschwindigkeiten, um eine präzise
#   Simulation sicherzustellen.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Füge weitere Planeten hinzu
# ---------------------------
# Ergänze die Simulation des Sonnensystems um weitere Planeten, sodass das Modell
# realistischer wird und die Bahnbewegungen der Planeten um die Sonne besser 
# erkennbar sind.
#
# Verwende die folgenden Anfangsbedingungen für Positionen und Geschwindigkeiten 
# der Planeten in SI-Einheiten (Meter für die Entfernung, Meter pro Sekunde für 
# die Geschwindigkeit). Alle Planeten starten in der x-Achse, und ihre 
# Geschwindigkeiten verlaufen in die y-Richtung:
#
# - Merkur: 
#     - Position (x): 5.79e10 m
#     - Geschwindigkeit (y): 4.79e4 m/s
#     - Masse: 3.30e23 kg
#
# - Venus:
#     - Position (x): 1.082e11 m
#     - Geschwindigkeit (y): 3.50e4 m/s
#     - Masse: 4.87e24 kg
#
# - Erde (ist bereits vorhanden, aber zur Orientierung):
#     - Position (x): 1.496e11 m
#     - Geschwindigkeit (y): 2.978e4 m/s
#     - Masse: 5.97e24 kg
#
# - Mars:
#     - Position (x): 2.279e11 m
#     - Geschwindigkeit (y): 2.41e4 m/s
#     - Masse: 6.42e23 kg
#
# - Jupiter:
#     - Position (x): 7.785e11 m
#     - Geschwindigkeit (y): 1.31e4 m/s
#     - Masse: 1.90e27 kg
#
# - Saturn:
#     - Position (x): 1.433e12 m
#     - Geschwindigkeit (y): 9.68e3 m/s
#     - Masse: 5.68e26 kg
#
# - Uranus:
#     - Position (x): 2.877e12 m
#     - Geschwindigkeit (y): 6.80e3 m/s
#     - Masse: 8.68e25 kg
#
# - Neptun:
#     - Position (x): 4.503e12 m
#     - Geschwindigkeit (y): 5.43e3 m/s
#     - Masse: 1.02e26 kg
#
# - Zusatz: Versuche, die Simulation so anzupassen, dass die Planeten in 
#   unterschiedlichen Farben dargestellt werden, um die Bahnen visuell besser 
#   unterscheiden zu können.
#
# - Optional: Teste die Simulation über einen Zeitraum von mehreren Jahren 
#   und beobachte, wie stabil die Bahnen der einzelnen Planeten sind.



#           ~+
#   
#                    *       +
#              '                  |          Erde, Sonne, Mond und alle Planeten. 
#          ()    .-.,="``"=.    - o -        Runge-Kutta machts möglich.
#                '=/_       \     |         
#             *   |  '=._    |
#                  \     `=./`,        '
#               .   '=.__.=' `='      *
#      +                         +
#           O      *        '       .
#   jgs
#   
#  ___ _  _ ___  ___ 
# | __| \| |   \| __|
# | _|| .` | |) | _| 
# |___|_|\_|___/|___|
#                
# -=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=-=x=-=x=-=x=-=-=


