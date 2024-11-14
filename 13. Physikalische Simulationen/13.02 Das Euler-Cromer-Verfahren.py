#              ______________________________________________
#       ______|                                              |_____
#       \     |        13.2 DAS EULER-CROMER-VERFAHREN       |    /
#        )    |______________________________________________|   (
#       /________)                                       (________\      11.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Das Euler-Cromer-Verfahren ist eine Abwandlung des Euler-Verfahrens. 
# Es wird besonders für physikalische Simulationen genutzt, bei denen die 
# Energieerhaltung wichtig ist, wie bei Schwingungen und Kreisbewegungen.

# Im Unterschied zum klassischen Euler-Verfahren wird im Euler-Cromer-Verfahren 
# zur Berechnung des neuen Ortes die Geschwindigkeit des aktuellen Zeitschrittes 
# verwendet und nicht die des vorherigen. Dadurch kann das Verfahren in einigen 
# Fällen eine stabilere und genauere Lösung liefern.


# _____________________________
#                             /
# Das Euler-Cromer-Verfahren (
# ____________________________\

# Wir beginnen mit einem Objekt, das eine Anfangsgeschwindigkeit und 
# eine Anfangsposition hat:
# 
#      v[0] = v_0
#      s[0] = s_0
#
# Das Euler-Cromer-Verfahren berechnet dann Zeitschritt für Zeitschritt die 
# neue Geschwindigkeit und Position. Die Schritte sind wie folgt:

# 1. Berechne die Geschwindigkeit im i-ten Zeitschritt durch die vorherige 
#    Geschwindigkeit und die aktuelle Beschleunigung a:
#
#      v[i] = v[i-1] + a * dt
#
# 2. Berechne die Position im i-ten Zeitschritt mithilfe der aktuellen 
#    Geschwindigkeit v[i]:
#
#      s[i] = s[i-1] + v[i] * dt
#
# 3. Wiederhole diese Schritte bis zur gewünschten Endzeit.




# ______________________________________________
#                                              /
# Freier Fall mit dem Euler-Cromer-Verfahren  (
# _____________________________________________\

# Im folgenden Beispiel simulieren wir den freien Fall eines Objekts aus einer 
# Höhe von 100 Metern. Die berechnete Lösung wird mit der exakten Lösung verglichen, 
# um die Genauigkeit des Euler-Cromer-Verfahrens zu illustrieren.

import numpy as np
import matplotlib.pyplot as plt

# Parameter für den freien Fall
g = 9.81    # Erdbeschleunigung in m/s²
m = 1.0     # Masse in kg

y_0 = 100   # Anfangshöhe in Metern
v_0 = 0     # Anfangsgeschwindigkeit in m/s

dt = 0.2    # Zeitschritt in Sekunden
t_end = 5   # Endzeit in Sekunden

# Arrays für Zeit, Höhe, exakte Höhe, Geschwindigkeit und Energie
t = np.arange(0, t_end, dt)
y = np.zeros(len(t))
v = np.zeros(len(t))
y_exact = np.zeros(len(t))
E = np.zeros(len(t))

# Setze Anfangswerte
y[0] = y_0
v[0] = v_0
y_exact[0] = y_0
E[0] = m * g * y[0] + 0.5 * m * v[0]**2

# Berechnung der Bewegung mit dem Euler-Cromer-Verfahren
for i in range(1, len(t)):
    # Beschleunigung im freien Fall
    a = -g

    # Update der Geschwindigkeit und Position
    v[i] = v[i-1] + a * dt
    y[i] = y[i-1] + v[i] * dt

    # Exakte Lösung zur Verifikation
    y_exact[i] = y_0 + v_0 * t[i] - 0.5 * g * t[i]**2

    # Berechnung der Gesamtenergie
    E[i] = m * g * y[i] + 0.5 * m * v[i]**2

# Visualisierung der Bewegung und der Energie
plt.figure(figsize=(10, 6))

# Höhe über Zeit
plt.subplot(2, 1, 1)
plt.plot(t, y, label="Euler-Cromer")
plt.plot(t, y_exact, label="Exakte Lösung", linestyle="dashed")
plt.ylabel("Höhe [m]")
plt.title("Freier Fall mit dem Euler-Cromer-Verfahren")
plt.legend()

# Energie über Zeit
plt.subplot(2, 1, 2)
plt.plot(t, E, label="Gesamtenergie")
plt.xlabel("Zeit [s]")
plt.ylabel("Energie [J]")
plt.legend()

plt.tight_layout()
plt.show()


# ___________________________________________
#                                           /
# Fehleranalyse des Euler-Cromer-Verfahrens (
# ___________________________________________\

# Beim freien Fall führt das Euler-Cromer-Verfahren typischerweise zu einer 
# Unterschätzung der Höhe. Der Fehler summiert sich im Laufe der Zeit, da das 
# Verfahren nur eine Näherung ist. Dies zeigt sich im wachsenden Unterschied 
# zwischen der numerischen und der exakten Lösung.

# Die Gesamtenergie bleibt jedoch tendenziell stabiler als beim klassischen 
# Euler-Verfahren, da das Euler-Cromer-Verfahren in der Regel Energie abzieht 
# (in konservativen Systemen wie Pendeln führt dies zu einem stabileren Verhalten).

# - Zeitschrittgröße `dt`: Je kleiner `dt` ist, desto genauer ist die Berechnung. 
#   Ein kleiner Zeitschritt führt zu einer besseren Annäherung an die exakte Lösung, 
#   da der numerische Fehler verringert wird.
#
# - Zeitschrittanpassung: Für hohe Genauigkeit und stabile Simulationen empfiehlt 
#   es sich, den Zeitschritt so klein wie möglich zu wählen, um die Fehlersummation zu minimieren.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Euler-Cromer-Verfahren: 
#   Liefert für Bewegungen mit konstanter Beschleunigung eine stabile numerische Lösung.
# 
# - Vorteil: Im Vergleich zum klassischen Euler-Verfahren ist das Euler-Cromer-Verfahren 
#   besser geeignet, die Energie in konservativen Systemen zu bewahren.
#
# - Module: `numpy` und `matplotlib` unterstützen die Berechnungen und die Visualisierung 
#   der Simulation.

# Das Euler-Cromer-Verfahren ist ein Einstieg in die numerische Physik und 
# bildet eine Grundlage für fortgeschrittenere Verfahren wie Runge-Kutta. 
# Es erlaubt eine realistische Simulation physikalischer Prozesse und eignet 
# sich für einfache Bewegungen mit Kräften.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Simuliere einen Ball, der unter dem Einfluss von Schwerkraft und einer
# Luftwiderstandskraft fällt. Die Luftwiderstandskraft ist proportional zur
# Geschwindigkeit und kann beschrieben werden als `F_reibung = -k * v`, wobei
# `k` eine Reibungskonstante ist. 
#
# Wähle einen geeigneten Wert für `k` und zeichne den Verlauf der Höhe und
# Geschwindigkeit über die Zeit. Beobachte, ob sich eine Endgeschwindigkeit
# einstellt.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Simuliere die Bewegung eines Objekts, das in einer harmonischen Schwingung
# verläuft. Die Rückstellkraft wird durch `F_feder = -k_feder * y` beschrieben,
# wobei `k_feder` die Federkonstante ist. 
#
# Wähle eine Anfangsauslenkung und eine Anfangsgeschwindigkeit und zeige den
# Verlauf der Position und der Energie des Objekts über die Zeit. Vergleiche,
# ob die Gesamtenergie während der Simulation annähernd erhalten bleibt.


# Füge hier deine Lösung ein.






#                        ___
#    o__        o__     |   |\       Auch Fussball-Simulationen
#   /|          /\      |   |X\      gelingen mit Euler-Cromer besser.
#   / > o        <\     |   |XX\
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
# Simuliere einen Ball, der unter dem Einfluss von Schwerkraft und einer
# Luftwiderstandskraft fällt. Die Luftwiderstandskraft ist proportional zur
# Geschwindigkeit und kann beschrieben werden als `F_reibung = -k * v`, wobei
# `k` eine Reibungskonstante ist. 
#
# Wähle einen geeigneten Wert für `k` und zeichne den Verlauf der Höhe und
# Geschwindigkeit über die Zeit. Beobachte, ob sich eine Endgeschwindigkeit
# einstellt.

'''
import numpy as np
import matplotlib.pyplot as plt

# Parameter für den freien Fall mit Luftwiderstand
g = 9.81   # Erdbeschleunigung in m/s^2
m = 1.0    # Masse in kg

y_0 = 100  # Anfangshöhe in m
v_0 = 0    # Anfangsgeschwindigkeit in m/s

dt = 0.2   # Zeitschritt in s
t_end = 10  # Endzeit in s
k = 0.5    # Reibungskonstante

# Listen für Zeit, Höhe, Geschwindigkeit
t = np.arange(0, t_end, dt)
y = np.zeros(len(t))
v = np.zeros(len(t))

# Setze Anfangswerte
y[0] = y_0
v[0] = v_0

# Berechnung der Bewegung mit dem Euler-Cromer-Verfahren
for i in range(1, len(t)):
    # Berechnung der Luftwiderstandskraft und resultierender Beschleunigung
    F_grav = -m * g
    F_reib = -k * v[i-1]
    a = (F_grav + F_reib) / m

    # Euler-Cromer Schritt
    v[i] = v[i-1] + a * dt
    y[i] = y[i-1] + v[i] * dt

# Visualisierung der Höhe und Geschwindigkeit über die Zeit
plt.subplot(2, 1, 1)
plt.plot(t, y)
plt.ylabel("Höhe [m]")
plt.title("Freier Fall mit Luftwiderstand")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, v, color="orange")
plt.xlabel("Zeit [s]")
plt.ylabel("Geschwindigkeit [m/s]")
plt.legend()

plt.show()
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Simuliere die Bewegung eines Objekts, das in einer harmonischen Schwingung
# verläuft. Die Rückstellkraft wird durch `F_feder = -k_feder * y` beschrieben,
# wobei `k_feder` die Federkonstante ist. 
#
# Wähle eine Anfangsauslenkung und eine Anfangsgeschwindigkeit und zeige den
# Verlauf der Position und der Energie des Objekts über die Zeit. Vergleiche,
# ob die Gesamtenergie während der Simulation annähernd erhalten bleibt.

'''
import numpy as np
import matplotlib.pyplot as plt

# Parameter für harmonische Schwingung
m = 1.0      # Masse in kg
k_feder = 2.0  # Federkonstante in N/m
x_0 = 1.0    # Anfangsauslenkung in m
v_0 = 0      # Anfangsgeschwindigkeit in m/s
dt = 0.05    # Zeitschritt in s
t_end = 20   # Endzeit in s

# Listen für Zeit, Auslenkung, Geschwindigkeit und Energie
t = np.arange(0, t_end, dt)
x = np.zeros(len(t))
v = np.zeros(len(t))
E = np.zeros(len(t))

# Setze Anfangswerte
x[0] = x_0
v[0] = v_0
E[0] = 0.5 * m * v[0]**2 + 0.5 * k_feder * x[0]**2

# Berechnung der harmonischen Schwingung mit dem Euler-Cromer-Verfahren
for i in range(1, len(t)):
    # Berechnung der Beschleunigung (F_feder = -k * x)
    a = -k_feder * x[i-1] / m

    # Euler-Cromer Schritt
    v[i] = v[i-1] + a * dt
    x[i] = x[i-1] + v[i] * dt

    # Berechnung der Gesamtenergie
    E[i] = 0.5 * m * v[i]**2 + 0.5 * k_feder * x[i]**2

# Visualisierung der Auslenkung und Energie über die Zeit
plt.subplot(2, 1, 1)
plt.plot(t, x, color="purple")
plt.ylabel("Position [m]")
plt.title("Harmonische Schwingung mit Federkraft")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, E, color="green")
plt.xlabel("Zeit [s]")
plt.ylabel("Energie [J]")
plt.legend()

plt.show()
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><




