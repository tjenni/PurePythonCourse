#              ____________________________________
#       ______|                                    |_____
#       \     |     13.8 DAS ZWEIKÖRPERPROBLEM     |    /
#        )    |____________________________________|   (
#       /________)                             (________\      11.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Das Zweikörperproblem beschreibt die Bewegung zweier Körper, die unter ihrem 
# gegenseitigen Gravitationsfeld stehen. Durch die Gravitation wird eine kreis- 
# oder ellipsenförmige Bewegung erzeugt.
#
# Ein anschauliches Beispiel dafür ist die Erde, die sich unter dem Einfluss der 
# Schwerkraft um die Sonne bewegt. In diesem Kapitel lernen wir, wie man die Bahnen 
# zweier Körper simuliert und visualisiert.



import numpy as np
import matplotlib.pyplot as plt


# _______________________
#                        /
# Klasse Body           (
# _______________________\
#
# Die Klasse `Body` repräsentiert einen Körper mit Position, Geschwindigkeit und
# Masse. Die Methode `update` aktualisiert die Position und Geschwindigkeit 
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


# Parameter für die Simulation
dt = 1000           # Zeitschritt in Sekunden   
time_end = 3.154e7  # Sekunden eines Jahres

# Simulation ausführen und Positionen zurückgeben
positions = world.simulate(dt, time_end)


# Visualisiere die Resultate
plt.figure(figsize=(10, 10))
plt.plot(positions[0][:,0], positions[0][:,1], label="Körper 1 (z.B. Sonne)")
plt.plot(positions[1][:,0], positions[1][:,1], label="Körper 2 (z.B. Erde)")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.legend()
plt.title("Zweikörperproblem")
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
# Erzeuge eine elliptische Umlaufbahn der Erde um die Sonne.
#
# - Ändere die Anfangsposition oder -geschwindigkeit der Erde. Versuche, 
#   eine elliptische Umlaufbahn zu erzeugen.
#
# - Experimentiere mit leichten Anpassungen der Startgeschwindigkeit 
#   und der Position, um eine stabile elliptische Bahn zu finden.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
# 
# Zeitschrittoptimierung für das Zweikörperproblem.
# 
# - Führe die Simulation mit verschiedenen Zeitschritten dt durch, z. B. 500, 
#   1000, 2000 und 5000 Sekunden.
#
# - Beobachte die Genauigkeit der Bahnkurven und die Rechengeschwindigkeit
#   für jeden Zeitschritt.
#
# - Finde einen optimalen Wert für dt, bei dem die Bahnkurve präzise bleibt,
#   ohne die Simulation zu stark zu verlangsamen.
#
# - Zusatz: Erkläre, warum ein kleiner Zeitschritt zwar genauere Ergebnisse 
#   liefert, aber auch die Berechnungszeit verlängert.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
# 
# Langzeitverhalten des Erde-Sonne-Systems.
#
# - Simuliere das Erde-Sonne-System über einen Zeitraum von 1 Million Jahren.
# 
# - Beobachte, ob die Erde ihre Bahn beibehält oder ob sich die Umlaufbahn
#   durch Akkumulation numerischer Fehler verändert.
#
# - Zeichne die resultierende Bahn und kommentiere, ob die Simulation den
#   Energie- und Impulserhaltungssätzen entspricht.
#
# - Zusatz: Falls die Umlaufbahn abweicht, experimentiere mit kleineren
#   Zeitschritten und vergleiche die Stabilität der Simulationsergebnisse.


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
# Erzeuge eine elliptische Umlaufbahn der Erde um die Sonne.
#
# - Ändere die Anfangsposition oder -geschwindigkeit der Erde. Versuche, 
#   eine elliptische Umlaufbahn zu erzeugen.
#
# - Experimentiere mit leichten Anpassungen der Startgeschwindigkeit 
#   und der Position, um eine stabile elliptische Bahn zu finden.

'''
Um eine elliptische Umlaufbahn zu erzeugen, ist es hilfreich, entweder die 
Anfangsposition oder die Anfangsgeschwindigkeit der Erde leicht zu verändern. 
Eine kleinere Anfangsgeschwindigkeit im Vergleich zur kreisförmigen Bahn führt 
in der Regel zu einer Ellipse, wobei die Erde sich auf ihrer Umlaufbahn an 
den sonnenfernen Punkten verlangsamt und an den sonnennahen Punkten beschleunigt.

    1.  Startgeschwindigkeit verringern: Wenn die Geschwindigkeit der Erde leicht 
        reduziert wird, führt dies zu einer elliptischen Umlaufbahn mit der Sonne 
        in einem Brennpunkt.

    2.  Startposition anpassen: Auch durch eine Änderung der Startposition 
        (etwas näher oder weiter von der Sonne entfernt) lässt sich eine Ellipse 
        erzeugen, wobei die Bahn durch die Kombination von Anfangsgeschwindigkeit 
        und Position gesteuert wird.

In der Simulation zeigt sich, dass eine geringfügige Anpassung der Geschwindigkeit 
meist ausreicht, um eine stabile, elliptische Umlaufbahn zu erreichen. Die Bahn 
kann dann durch Beobachtung der Positionen und Geschwindigkeiten auf ihre Stabilität 
überprüft werden.
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
# 
# Zeitschrittoptimierung für das Zweikörperproblem.
# 
# - Führe die Simulation mit verschiedenen Zeitschritten dt durch, z. B. 500, 
#   1000, 2000 und 5000 Sekunden.
#
# - Beobachte die Genauigkeit der Bahnkurven und die Rechengeschwindigkeit
#   für jeden Zeitschritt.
#
# - Finde einen optimalen Wert für dt, bei dem die Bahnkurve präzise bleibt,
#   ohne die Simulation zu stark zu verlangsamen.
#
# - Zusatz: Erkläre, warum ein kleiner Zeitschritt zwar genauere Ergebnisse 
#   liefert, aber auch die Berechnungszeit verlängert.

'''
Für diese Aufgabe wird die Simulation mit verschiedenen Zeitschritten  dt  
durchgeführt, z. B. 500, 1000, 2000 und 5000 Sekunden.

    1.  Beobachtungen bei kleineren Zeitschritten (z. B. 500 Sekunden): Ein 
        kleiner Zeitschritt bietet eine hohe Genauigkeit der Bahnkurven, die der 
        exakten Lösung nahekommt. Die Berechnungszeit steigt jedoch an, da viele 
        kleine Schritte notwendig sind, um die Simulation für einen bestimmten 
        Zeitraum zu durchlaufen.

    2.  Beobachtungen bei grösseren Zeitschritten (z. B. 2000–5000 Sekunden): 
        Ein grösserer Zeitschritt beschleunigt die Berechnung, da die Simulation 
        weniger Schritte benötigt. Allerdings können sich bei zu grossen 
        Zeitschritten signifikante numerische Fehler aufbauen, die die Bahnkurven 
        ungenauer machen und langfristig die Stabilität beeinträchtigen.

    3.  Optimierung des Zeitschritts: Ein Wert von etwa 1000 Sekunden bietet häufig 
        eine gute Balance zwischen Genauigkeit und Rechengeschwindigkeit.

Zusatz: Ein kleinerer Zeitschritt erhöht die Genauigkeit, da die numerischen Fehler 
bei jedem Schritt kleiner sind und sich daher langsamer akkumulieren. 
Der Nachteil ist jedoch eine längere Berechnungszeit, da mehr Schritte 
notwendig sind, um den gleichen Zeitraum zu simulieren.
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
# 
# Langzeitverhalten des Erde-Sonne-Systems.
#
# - Simuliere das Erde-Sonne-System über einen Zeitraum von 1 Million Jahren.
# 
# - Beobachte, ob die Erde ihre Bahn beibehält oder ob sich die Umlaufbahn
#   durch Akkumulation numerischer Fehler verändert.
#
# - Zeichne die resultierende Bahn und kommentiere, ob die Simulation den
#   Energie- und Impulserhaltungssätzen entspricht.
#
# - Zusatz: Falls die Umlaufbahn abweicht, experimentiere mit kleineren
#   Zeitschritten und vergleiche die Stabilität der Simulationsergebnisse.


'''
Bei dieser Aufgabe wird das Erde-Sonne-System für einen Zeitraum von 1 Million 
Jahren simuliert. Über eine lange Zeitspanne können sich numerische Fehler, 
die durch die Näherung der Berechnung entstehen, aufaddieren.
'''



# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

