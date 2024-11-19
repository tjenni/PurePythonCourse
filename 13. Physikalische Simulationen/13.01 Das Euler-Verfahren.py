#              __________________________________
#       ______|                                  |_____
#       \     |     13.1 DAS EULER-VERFAHREN     |    /
#        )    |__________________________________|   (
#       /________)                           (________\      11.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Physikalische Simulationen sind eine wichtige Methode, um reale Phänomene in 
# der Wissenschaft und Technik nachzustellen. Mit Python können wir einfache 
# Simulationen aufbauen, um Bewegungen, Kräfte und Energie zu modellieren.
# Dieses Kapitel erklärt die grundlegenden Schritte für Simulationen und zeigt, 
# wie das Euler-Verfahren für den freien Fall angewendet wird.


# _______________________________________
#                                       /
# Vorteile physikalischer Simulationen (
# ______________________________________\

# - Verständnis:
#   Simulationen machen Konzepte wie Bewegung, Kräfte und Energie greifbar.
# 
# - Experimentieren:
#   Wir können Parameter ändern und damit Szenarien simulieren, 
#   die schwer realisierbar sind.
#
# - Optimierung:
#   Simulationen werden oft genutzt, um Abläufe zu optimieren, bevor sie 
#   real umgesetzt werden.




# _________________________________
#                                 /
# Grundlegende Konzepte          (
# ________________________________\

# - Zeit und Zeitschritte:
#   Simulationen laufen in kleinen Zeitschritten, um Veränderungen genau abzubilden.
#  
# - Kräfte und Bewegung:
#   Veränderungen in der Position entstehen durch Kräfte wie zum Beispiel die 
#   Schwerkraft oder der Luftwiderstand.
#  
# - Energie und Impuls:
#   Diese Grössen werden oft verwendet, um zu beschreiben, wie sich Systeme verhalten.




# ____________________________________
#                                    /
# Physikalische Simulation starten  (
# ___________________________________\

# Die Schritte für eine physikalische Simulation umfassen:

# - Parameter festlegen:
#   Anfangswerte wie Position und Geschwindigkeit angeben.
#
# - Zeitschritt wählen:
#   Einen kleinen Zeitschritt definieren (z.B. 0.2 s).
#
# - Bewegung berechnen
#   In jedem Schritt berechnen, wie sich das Objekt durch Kräfte verändert.
# 
# - Visualisieren:
#   Die Ergebnisse aufzeichnen und anzeigen.




# _______________________
#                       /
# Das Euler-Verfahren  (
# ______________________\

# Das Euler-Verfahren ist ein numerisches Verfahren zur Annäherung an 
# Lösungen von Differentialgleichungen, welche die Grundlagen der 
# mathematischen Beschreibung der Natur sind. 

# Beim Euler-Verfahren wird die Zeit in diskrete Zeitschritte zerlegt. 
# Am Anfang hat ein Körper einen eine Anfangsgeschwindigekeit und
# einen Anfangsort. 
# 
#      v[0] = v_0
#      s[0] = s_0

# Nun wird Zeitschritte für Zeitschritte in die Zukunft gerechnet. 

# 1. Berechne die Geschwindigkeit zum i-ten Zeitschritt aus 
#    der vorherigen Geschwindigkeit beim Zeitschritt i-1 
#    und der Beschleunigung. 
#
#      v[i] = v[i-1] + a * dt
#
# 2. Berechne den Ort zum i-ten Zeitschritt aus dem vorherigen 
#    Ort und der vorherigen Geschwindigkeit beim Zeitschritt i-1. 
#
#      s[i] = s[i-1] + v[i-1] * dt
# 
# 3. Wiederhole die Schritte 1. und 2. solange, bis die gewünschte
#    Endzeit erreicht ist. 




# ___________________________________
#                                   /
# Freier Fall mit Euler-Verfahren  (
# __________________________________\

# In diesem Beispiel wird der freie Fall eines Körpers aus 100 m 
# Höhe simuliert. Dabei wird die Lösung des Euler-Verfahrens
# mit der exakten analytischen Lösung verglichen. 

import numpy as np
import matplotlib.pyplot as plt


# Parameter für den freien Fall
g = 9.81   # Erdbeschleunigung in m/s^2

m = 1.0    # Masse in kg

y_0 = 100  # Anfangshöhe in m
v_0 = 0    # Anfangsgeschwindigkeit in m/s

dt = 0.2   # Zeitschritt in s
t_end = 5  # Endzeit in s


# Listen erzeugen für die Darstellung mit matplotlib
t = np.arange(0, t_end, dt) # Liste mit den Zeiten erzeugen

y = np.zeros(len(t)) # Liste für alle Höhen
v = np.zeros(len(t)) # Liste für alle Geschwindigkeiten

y_exact = np.zeros(len(t)) # Liste für alle exakten Höhen
E = np.zeros(len(t)) # Liste für alle Energien


# Setze Anfangswerte
y[0] = y_0
v[0] = v_0
y_exact[0] = y_0

# berechne die Gesamtenergie des Körpers mit der Formel
#
#   E = E_pot + E_kin = m * g * h  +  (1/2) * m * v^2
#
E[0] = m*g*y[0] + 0.5*m*v[0]**2


# Berechnung der Bewegung mit dem Euler-Verfahren
for i in range(1, len(t)):

    a = -g # Beschleunigung für den freien Fall

    # berechne einen Euler-Schritt
    v[i] = v[i-1] + a * dt
    y[i] = y[i-1] + v[i-1] * dt

    # exakte Höhe berechnen
    y_exact[i] = y_0 + v_0 * t[i] - 0.5 * g * t[i]**2

    # berechne die Gesamtenergie des Körpers
    E[i] = m*g*y[i] + 0.5*m*v[i]**2


# Visualisierung der Bewegung und der Energie
plt.subplot(2,1,1)
plt.plot(t, y, label="Euler")
plt.plot(t, y_exact, label="exakte Lösung", linestyle="dashed")
plt.ylabel("Höhe [m]")
plt.title("Freier Fall mit dem Euler-Verfahren")
plt.legend()

plt.subplot(2,1,2)
plt.plot(t, E)
plt.xlabel("Zeit [s]")
plt.ylabel("Energie [J]")

plt.show()




# __________________________________
#                                  /
# Fehleranalyse Euler-Verfahren   (
# _________________________________\

# Das Euler-Verfahren liefert beim freien Fall immer eine zu grosse Höhe.
# Wie zu sehen ist, wächst die Abweichung zur exakten Lösung mit der Zeit an. 
# Das Euler-Verfahren verletzt die Energieerhaltung, wie man im unteren Diagramm
# sehen kann. 

# In den Übungsaufgaben unten wird sich zeigen, dass die Genauigkeit des Euler-
# Verfahrens stark von der Grösse des Zeitschritts `dt` abhängt:
#
# - Bei kleineren Werten von `dt` wird die Berechnung präziser, da die Annäherung 
#   enger an der exakten Lösung liegt.
#
# - Grössere Werte von `dt` führen zu grösseren Abweichungen (numerischer Fehler), 
#   da das Euler-Verfahren die Veränderungen nur näherungsweise modelliert.






# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Grundlagen: 
#   Simulationen machen es möglich, physikalische Konzepte in der Programmierung umzusetzen.
#
# - Euler-Verfahren: 
#   Ermöglicht die Berechnung von Bewegung in Zeitschritten. Das Verfahren 
#   verletzt den Energieerhaltungssatz.
#
# - Module: `numpy` und `matplotlib` helfen bei Berechnungen und Visualisierungen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\

# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Untersuche den Einfluss des Zeitschritts `dt` auf den Fehler der Simulation.
# Ändere `dt` zu verschiedenen Werten wie 0.5, 0.1 und 0.01. Zeichne für jeden 
# Wert den absoluten Fehler auf, und untersuche, wie sich die Genauigkeit der 
# Simulation verändert.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Simuliere den freien Fall eines Objekts aus 200 Metern Höhe mit dem Euler-Verfahren.
# Zeichne den Verlauf der Höhe und Geschwindigkeit über die Zeit.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Ändere in der Simulation die Anfangsgeschwindigkeit. Mache sie mal positiv und
# mal negativ. Wie verändert sich die Kurve?

# Füge hier deine Lösung ein.




#          _____
#       _.'_____`._
#     .'.-'  12 `-.`.
#    /,' 11      1 `.\
#   // 10      /   2 \\
#  ;;         /       ::       Das Euler-Verfahren ist ein 
#  || 9  ----O      3 ||       Zeitschrittverfahren. 
#  ::                 ;;
#   \\ 8           4 //
#    \`. 7       5 ,'/
#     '.`-.__6__.-'.'
#      ((-._____.-))
#      _))       ((_
#     '--'SSt    '--'
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
# Untersuche den Einfluss des Zeitschritts `dt` auf den Fehler der Simulation.
# Ändere `dt` zu verschiedenen Werten wie 0.5, 0.1 und 0.01. Zeichne für jeden 
# Wert den absoluten Fehler auf, und untersuche, wie sich die Genauigkeit der 
# Simulation verändert.

'''
import numpy as np
import matplotlib.pyplot as plt

# Parameter für die Simulation
h_0 = 100  # Anfangshöhe in Metern
v_0 = 0  # Anfangsgeschwindigkeit in m/s
g = 9.81  # Erdbeschleunigung in m/s^2
t_end = 5  # Endzeit in Sekunden

# Verschiedene Zeitschritte zur Untersuchung
dt = [0.5, 0.1, 0.01]
colors = ['blue', 'green', 'orange']  # Farben für die Plots

for idx, dt in enumerate(dt):
    # Listen für Höhe und Zeit initialisieren
    t = np.arange(0, t_end, dt)
    y = np.zeros(len(t))
    v = np.zeros(len(t))
    y_exact = np.zeros(len(t))
    
    y[0] = h_0
    v[0] = v_0
    y_exact[0] = h_0
    
    # Euler-Verfahren zur Berechnung der Höhe mit dem aktuellen dt
    for i in range(1, len(t)):
        v[i] = v[i - 1] - g * dt
        y[i] = y[i - 1] + v[i - 1] * dt
        
        y_exact[i] = h_0 + v_0 * t[i] - 0.5 * g * t[i]**2

    # Absoluter Fehler zwischen der exakten Lösung und dem Euler-Verfahren
    abs_error = np.abs(y - y_exact)
    
    # Plotten des Fehlers
    plt.plot(t, abs_error, label=f'dt = {dt}', color=colors[idx])

plt.xlabel("Zeit [s]")
plt.ylabel("Absoluter Fehler [m]")
plt.title("Einfluss des Zeitschritts dt auf den Fehler der Simulation")
plt.legend()
plt.grid()
plt.show()
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Simuliere den freien Fall eines Objekts aus 200 Metern Höhe mit dem Euler-Verfahren.
# Zeichne den Verlauf der Höhe und Geschwindigkeit über die Zeit.

'''
import numpy as np
import matplotlib.pyplot as plt

# Parameter für die Simulation
g = 9.81  # Erdbeschleunigung in m/s^2
dt = 0.01  # Zeitschritt in Sekunden
t_end = 10  # Endzeit in Sekunden
t = np.arange(0, t_end, dt)  # Zeitwerte


# Anfangswerte
h_0 = 200  # Anfangshöhe in Metern
v_0 = 0  # Anfangsgeschwindigkeit in m/s


# Listen für Höhe und Geschwindigkeit initialisieren
y = np.zeros(len(t))
v = np.zeros(len(t))


# Setze Anfangswerte
y[0] = h_0
v[0] = v_0

# Euler-Verfahren zur Berechnung der Höhe und Geschwindigkeit
for i in range(1, len(t)):
    v[i] = v[i - 1] - g * dt  # Geschwindigkeit aktualisieren
    y[i] = y[i - 1] + v[i - 1] * dt  # Höhe aktualisieren

# Plot der Höhe und Geschwindigkeit
plt.subplot(2, 1, 1)
plt.plot(t, y)
plt.xlabel("Zeit [s]")
plt.ylabel("Höhe [m]")
plt.title("Freier Fall aus 200 m Höhe")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, v, color="orange")
plt.xlabel("Zeit [s]")
plt.ylabel("Geschwindigkeit [m/s]")
plt.legend()
plt.tight_layout()
plt.show()
'''





# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Ändere in der Simulation die Anfangsgeschwindigkeit. Mache sie mal positiv und
# mal negativ. Wie verändert sich die Kurve?

'''
import numpy as np
import matplotlib.pyplot as plt

# Parameter für die Simulation
g = 9.81  # Erdbeschleunigung in m/s^2
dt = 0.01  # Zeitschritt in Sekunden
t_end = 10  # Endzeit in Sekunden
t = np.arange(0, t_end, dt)  # Zeitwerte

# Anfangswerte
h_0 = 200  # Anfangshöhe in Metern
v_0 = 0  # Anfangsgeschwindigkeit in m/s

# berechne die Zeitschritte mit dem Euler-Verfahren
def euler(t, y, v):
    for i in range(1, len(t)):
        v[i] = v[i - 1] - g * dt
        y[i] = y[i - 1] + v[i - 1] * dt


t = np.arange(0, t_end, dt)

# v_0 = 0 m/s
y_1 = np.zeros(len(t))
v_1 = np.zeros(len(t))
y_1[0] = h_0
v_1[0] = 0
euler(t, y_1, v_1)

# v_0 = +20 m/s (aufwärts)
y_2 = np.zeros(len(t))
v_2 = np.zeros(len(t))
y_2[0] = h_0
v_2[0] = 20
euler(t, y_2, v_2)

# v_0 = -20 m/s (abwärts)
y_3 = np.zeros(len(t))
v_3 = np.zeros(len(t))
y_3[0] = h_0
v_3[0] = -20
euler(t, y_3, v_3)


# Plot für die verschiedenen Anfangsgeschwindigkeiten
plt.plot(t, y_1, label="v_0 = 0 m/s", linestyle="--")
plt.plot(t, y_2, label="v_0 = 20 m/s (aufwärts)")
plt.plot(t, y_3, label="v_0 = -20 m/s (abwärts)")
plt.xlabel("Zeit [s]")
plt.ylabel("Höhe [m]")
plt.title("Freier Fall mit unterschiedlicher Anfangsgeschwindigkeit")
plt.legend()
plt.show()
'''



# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


