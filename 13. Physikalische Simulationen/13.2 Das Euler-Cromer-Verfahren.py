#              ____________________________________
#       ______|                                    |_____
#       \     |  13.2 Das Euler-Cromer Verfahren   |    /
#        )    |____________________________________|   (
#       /________)                             (________\      7.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Die Kinematik ist der Teil der Physik, der Bewegungen ohne Rücksicht auf die 
# verursachenden Kräfte untersucht. In diesem Kapitel lernen wir, einfache 
# Bewegungen wie gleichförmige und beschleunigte Bewegungen mithilfe des 
# Euler-Cromer-Verfahrens zu simulieren.




# ______________________________
#                              /
# Das Euler-Cromer-Verfahren  (
# _____________________________\

# Das Euler-Cromer-Verfahren ist fast identisch mit dem Euler-Verfahren.
# Der Unterschied ist, dass man bei der Ortsberechnung die schon 
# bereits berechnete Geschwindigkeit verwendet anstatt diejenige vom
# letzten Zeitschritt. 

# Am Anfang hat ein Körper einen eine Anfangsgeschwindigekeit und
# einen Anfangsort. 
# 
# v[0] = v_0
# s[0] = s_0

# Nun wird Zeitschritte für Zeitschritte in die Zukunft gerechnet. 

# 1. Berechne die Geschwindigkeit zum i-ten Zeitschritt aus 
#    der vorherigen Geschwindigkeit beim Zeitschritt i-1 
#    und der Beschleunigung. 
#
#      v[i] = v[i-1] + a * dt
#
# 2. Berechne den Ort zum i-ten Zeitschritt aus dem vorherigen 
#    Ort Zeitschritt i-1 und der unter 1. berechneten Geschwindigkeit 
#    zum Zeitpunkt i. 
#
#      s[i] = s[i-1] + v[i] * dt
# 
# 3. Wiederhole die Schritte 1. und 2. solange, bis die gewünschte
#    Endzeit erreicht ist. 




# __________________________________________
#                                          /
# Freier Fall mit Euler-Cromer-Verfahren  (
# _________________________________________\

# In diesem Beispiel wird, wie im letzten Kapitel, der freie Fall 
# eines Körper aus 100 m Höhe simuliert. Dabei wird die Lösung des 
# Euler-Cromer-Verfahrens mit der exakten analytischen Lösung verglichen. 


import numpy as np
import matplotlib.pyplot as plt

# Parameter für den freien Fall
y_0 = 100  # Anfangshöhe in Metern
v_0 = 0  # Anfangsgeschwindigkeit in m/s
g = 9.81  # Erdbeschleunigung in m/s^2
t_end = 5  # Endzeit in Sekunden
dt = 0.2  # Zeitschritt in Sekunden

# Listen für Zeit, Höhe, exakte Höhe und Geschwindigkeit
t = np.arange(0, t_end, dt)

y = np.zeros(len(t))
v = np.zeros(len(t))

y_exact = np.zeros(len(t))

# Anfangswerte setzen
y[0] = y_0
y_exact[0] = y_0
v[0] = v_0


# Berechnung der Bewegung mit dem Euler-Verfahren
for i in range(1, len(t)):
    # Geschwindigkeit und Höhe im nächsten Zeitschritt berechnen
    v[i] = v[i - 1] - g * dt
    y[i] = y[i - 1] + v[i] * dt

    # exakte Höhe berechnen
    y_exact[i] = y_0 + v_0 * t[i] - 0.5 * g * t[i]**2


errors = y - y_exact

# Visualisierung der Bewegung und des Fehlers
plt.subplot(2,1,1)
plt.plot(t, y, label="Euler-Cromer")
plt.plot(t, y_exact, label="exakte Lösung", linestyle="dashed")
plt.ylabel("Höhe (m)")
plt.title("Freier Fall")
plt.legend()

plt.subplot(2,1,2)
plt.plot(t, errors, label="Fehler")
plt.xlabel("Zeit (s)")
plt.ylabel("Fehler (m)")

plt.show()




# __________________
#                  /
# Fehleranalyse   (
# _________________\

# Wie beim Euler-Verfahren, hängt die Genauigkeit des Euler-Cromer-Verfahrens
# stark von der Grösse des Zeitschritts `dt` ab:

# Im Unterschied zum Euler-Verfahren, liefert das Euler-Cromer-Verfahren
# beim freien Fall immer eine zu kleine Höhe. Alles andere bleibt gleich.
# Es gibt ebenfalls einen kumulativen Fehler für lange Simulationszeiten
# und man kann den Fehler reduzieren, wenn man den Zeitschritt `dt` keliner macht. 




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Euler-Cromer-Verfahren: 
#   Stabilere Methode für numerische Simulationen.
#
# - Gleichförmige Bewegung: 
#   Das Objekt bewegt sich mit konstanter Geschwindigkeit.
#
# - Gleichmässig beschleunigte Bewegung: 
#   Die Geschwindigkeit wächst linear mit der Zeit.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Simuliere eine gleichmässig verzögerte Bewegung mit einer anfänglichen 
# Geschwindigkeit von 20 m/s und einer konstanten Verzögerung von -2 m/s². 
# Stelle die Strecke und die Geschwindigkeit über die Zeit dar.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Simulation einer zweidimensionalen Bewegung mit konstanter Geschwindigkeit
# in x-Richtung (5 m/s) und konstanter Beschleunigung in y-Richtung (-9.81 m/s²).
# Zeige die Bewegung als Trajektorie.

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
# Simuliere eine gleichmässig verzögerte Bewegung mit einer anfänglichen 
# Geschwindigkeit von 20 m/s und einer konstanten Verzögerung von -2 m/s². 
# Stelle die Strecke und die Geschwindigkeit über die Zeit dar.

'''
import numpy as np
import matplotlib.pyplot as plt

# Parameter für die verzögerte Bewegung
v_0 = 20  # Anfangsgeschwindigkeit in m/s
a = -2    # konstante Verzögerung in m/s²
t_end = 15  # Endzeit in Sekunden
dt = 0.1  # Zeitschritt in Sekunden

# Listen für Zeit, Geschwindigkeit und Strecke
t = np.arange(0, t_end, dt)
v = np.zeros(len(t))
s_values = np.zeros(len(t))

# Anfangswerte setzen
v[0] = v_0
s_values[0] = 0

# Berechnung der Bewegung mit dem Euler-Cromer-Verfahren
for i in range(1, len(t)):
    # Geschwindigkeit und Strecke im nächsten Zeitschritt berechnen
    v[i] = v[i - 1] + a * dt
    s_values[i] = s_values[i - 1] + v[i] * dt

    # Geschwindigkeit soll nicht negativ werden
    if v[i] < 0:
        v[i] = 0
        s_values[i] = s_values[i - 1]


# Visualisierung
plt.subplot(2, 1, 1)
plt.plot(t, s_values, label="Strecke")
plt.ylabel("Strecke in m")
plt.title("Gleichmässig verzögerte Bewegung")
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, v, label="Geschwindigkeit", color="orange")
plt.xlabel("Zeit in s")
plt.ylabel("Geschwindigkeit in m/s")
plt.grid()
plt.tight_layout()
plt.show()
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Simulation einer zweidimensionalen Bewegung mit konstanter Geschwindigkeit
# in x-Richtung (5 m/s) und konstanter Beschleunigung in y-Richtung (-9.81 m/s²).
# Zeige die Bewegung als Trajektorie.


'''
import numpy as np
import matplotlib.pyplot as plt

# Parameter für die 2D-Bewegung

ax = 0       # es gibt keine Beschleunigung in x-Richtung
ay = -9.81   # konstante Beschleunigung in y-Richtung (Schwerkraft) in m/s²

vx_0 = 5       # konstante Geschwindigkeit in x-Richtung in m/s
vy_0 = 2     # Anfangsgeschwindigkeit in y-Richtung in m/s

t_end = 2     # Endzeit in Sekunden
dt = 0.01     # Zeitschritt in Sekunden

# Listen für die Zeit und Positionen in x- und y-Richtung
t = np.arange(0, t_end, dt)
x_values = np.zeros(len(t))
vx_values = np.zeros(len(t))
y = np.zeros(len(t))
vy = np.zeros(len(t))

# Anfangswerte setzen
x_values[0] = 1
vx_values[0] = vx_0

y[0] = 1
vy[0] = vy_0

# Berechnung der Bewegung mit dem Euler-Cromer-Verfahren
for i in range(1, len(t)):
    # x-Richtung
    vx_values[i] = vx_values[i - 1] + ax * dt
    x_values[i] = x_values[i - 1] + vx_values[i] * dt
    
    # y-Richtung
    vy[i] = vy[i - 1] + ay * dt
    y[i] = y[i - 1] + vy[i] * dt

    # Bewegung soll enden, wenn das Objekt den Boden erreicht (y < 0)
    if y[i] < 0:
        y[i] = 0
        x_values[i] = x_values[i-1]
        

# Visualisierung der Trajektorie
plt.plot(x_values, y, label="Trajektorie")
plt.xlabel("x in m")
plt.ylabel("y in m")
plt.title("Schiefer Wurf")
plt.grid()
plt.show()
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><



