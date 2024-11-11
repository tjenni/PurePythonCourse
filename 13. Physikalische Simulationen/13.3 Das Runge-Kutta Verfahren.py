#              ______________________________________
#       ______|                                      |_____
#       \     |    13.3 DAS RUNGE-KUTTA-VERFAHREN    |    /
#        )    |______________________________________|   (
#       /________)                               (________\      11.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# In diesem Kapitel betrachten wir das Runge-Kutta-Verfahren 2. Ordung, eine 
# numerische Methode zur Lösung von Differentialgleichungen, die genauer ist 
# als das Euler-Verfahren. Das Runge-Kutta-Verfahren 2. Ordnung nähert die Lösung 
# mit einem zweistufigen Ansatz an, wodurch die Genauigkeit der Simulation 
# verbessert wird. 

# Wie in den letzten zwei Kapiteln, verwenden wir als Beispiel den freien Fall.


# _________________________________________
#                                         /
# Das Runge-Kutta-Verfahrens 2. Ordnung  (
# ________________________________________\

# Das Runge-Kutta-Verfahren 2. Ordnung basiert darauf, dass man 
# die Geschwindigkeit bei t + dt/2 abschätzt.
#
# Zusammengefasst:
#
# 1. Rechne einen ganzen Eulerschritt vorwärts und speichere die 
#    Geschwindigkeit und die Position. 
#      
#      k1_v = dt * a(y[i-1],v[i-1])
#      k1_y = dt * v[i-1]
#
# 2. Rechne nun einen halben Eulerschritt vorwärts.
#
#      k2_v = dt * acceleration(y[i-1] + 0.5 * k1_y, v[i-1] + 0.5 * k1_v)
#      k2_y = dt * (v[i-1] + 0.5 * k1_v)
#
# 3. Berechne die neue Geschwindigkeit und Position ausgehend von der
#    Geschwindigkeit und Position beim halben Eulerschritt.
#      
#      v[i] = v[i-1] + k2_v
#      y[i] = y[i-1] + k2_y
#
# 4. Wiederhole diese Schritte bis zur gewünschten Endzeit.




# ________________________________________________________
#                                                        /
# Freier Fall mit dem Runge-Kutta-Verfahren 2. Ordnung  (
# _______________________________________________________\
#
# Das Ziel ist, die Bewegung des fallenden Objekts mithilfe dieses Verfahrens 
# zu simulieren und die Genauigkeit mit der exakten Lösung zu vergleichen.


import numpy as np
import matplotlib.pyplot as plt

# Parameter für den freien Fall
g = 9.81    # Erdbeschleunigung in m/s²
m = 1.0     # Masse in kg

y_0 = 100   # Anfangshöhe in Metern
v_0 = 0     # Anfangsgeschwindigkeit in m/s

dt = 0.2    # Zeitschritt in Sekunden
t_end = 5   # Endzeit in Sekunden

# Listen für Zeit, Höhe, exakte Höhe und Geschwindigkeit
t = np.arange(0, t_end, dt)

y = np.zeros(len(t))
v = np.zeros(len(t))

y_exact = np.zeros(len(t))
E = np.zeros(len(t))

# Anfangswerte setzen
y[0] = y_0
y_exact[0] = y_0
v[0] = v_0
E[0] = m * g * y[0] + 0.5 * m * v[0]**2


# Funktion für die Beschleunigung (die rechte Seite der Differentialgleichung)
def acceleration(y, v):
    return -g # Beschleunigung ist konstant -g (Schwerkraft)


# Runge-Kutta 2. Ordnung
for i in range(1, len(t)):
    # Berechnung von k1 für Geschwindigkeit und Position
    k1_v = dt * acceleration(y[i-1], v[i-1])  # Änderung der Geschwindigkeit
    k1_y = dt * v[i-1]  # Änderung der Position
    
    # Berechnung der Zwischenschritte für k2
    k2_v = dt * acceleration(y[i-1] + 0.5 * k1_y, v[i-1] + 0.5 * k1_v)
    k2_y = dt * (v[i-1] + 0.5 * k1_v)
    
    # Update der Position und Geschwindigkeit
    v[i] = v[i-1] + k2_v
    y[i] = y[i-1] + k2_y

    # Berechnung der exakten Höhe zum Vergleich
    y_exact[i] = y_0 + v_0 * t[i] - 0.5 * g * t[i]**2

    # Berechnung der Gesamtenergie
    E[i] = m * g * y[i] + 0.5 * m * v[i]**2


# Berechnung des Fehlers
errors = y - y_exact

# Visualisierung der Bewegung und des Fehlers
plt.figure(figsize=(10, 6))

# Höhe über Zeit
plt.subplot(2, 1, 1)
plt.plot(t, y, label="Runge-Kutta 2. Ordnung")
plt.plot(t, y_exact, label="Exakte Lösung", linestyle="dashed")
plt.ylabel("Höhe [m]")
plt.title("Freier Fall mit dem Runge-Kutta-Verfahren")
plt.legend()

# Energie über Zeit
plt.subplot(2, 1, 2)
plt.plot(t, E, label="Gesamtenergie")
plt.xlabel("Zeit [s]")
plt.ylabel("Energie [J]")
plt.legend()

plt.tight_layout()
plt.show()




# ____________________________
#                            /
# Wichtige Konzepte          (
# ____________________________\

# - Runge-Kutta 2. Ordnung: 
#   Das Runge-Kutta-2-Verfahren verbessert die Genauigkeit durch Berechnung der 
#   mittleren Änderungsrate `k2` für jeden Zeitschritt.
#
# - Genauigkeit: 
#   Dieses Verfahren führt zu einer geringeren Fehlerakkumulation im Vergleich 
#   zum Euler-Verfahren.




# _____________________________
#                             /
# Übungsaufgaben             (
# ____________________________\

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
# Vergleiche die Lösung des Runge-Kutta-Verfahrens mit der Lösung des Euler-Cromer-
# Verfahrens aus dem letzten Kapitel. 


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
# Vergleiche die Lösung des Runge-Kutta-Verfahrens mit der Lösung des Euler-Cromer-
# Verfahrens aus dem letzten Kapitel. 

'''
import numpy as np
import matplotlib.pyplot as plt

# Parameter für den freien Fall mit Luftwiderstand
g = 9.81   # Erdbeschleunigung in m/s^2
m = 1.0    # Masse in kg
y_0 = 100  # Anfangshöhe in m
v_0 = 0    # Anfangsgeschwindigkeit in m/s
dt = 0.5   # Zeitschritt in s
t_end = 10  # Endzeit in s
k = 0.2    # Reibungskonstante

# Listen für Zeit, Höhe, Geschwindigkeit
t = np.arange(0, t_end, dt)
y_rk2 = np.zeros(len(t))
v_rk2 = np.zeros(len(t))

# Anfangswerte setzen
y_rk2[0] = y_0
v_rk2[0] = v_0

# Funktion für die Beschleunigung mit Luftwiderstand
def acceleration_with_drag(y, v, k):
    return -g - (k / m) * v

# Runge-Kutta-Verfahren 2. Ordnung
for i in range(1, len(t)):
    # Berechnung von k1 für Geschwindigkeit und Position
    k1_v = dt * acceleration_with_drag(y_rk2[i-1], v_rk2[i-1], k)
    k1_y = dt * v_rk2[i-1]
    
    # Berechnung der Zwischenschritte für k2
    k2_v = dt * acceleration_with_drag(y_rk2[i-1] + 0.5 * k1_y, v_rk2[i-1] + 0.5 * k1_v, k)
    k2_y = dt * (v_rk2[i-1] + 0.5 * k1_v)
    
    # Update der Position und Geschwindigkeit
    v_rk2[i] = v_rk2[i-1] + k2_v
    y_rk2[i] = y_rk2[i-1] + k2_y

# Vergleich mit Euler-Cromer-Verfahren
y_ec = np.zeros(len(t))
v_ec = np.zeros(len(t))
y_ec[0] = y_0
v_ec[0] = v_0

for i in range(1, len(t)):
    a = acceleration_with_drag(y_ec[i-1], v_ec[i-1], k)
    v_ec[i] = v_ec[i-1] + a * dt
    y_ec[i] = y_ec[i-1] + v_ec[i] * dt

# Visualisierung
plt.subplot(2, 1, 1)
plt.plot(t, y_rk2, label="Runge-Kutta 2. Ordnung")
plt.plot(t, y_ec, label="Euler-Cromer", linestyle="dashed")
plt.xlabel("Zeit [s]")
plt.ylabel("Höhe [m]")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, v_rk2, label="Geschwindigkeit (RK2)", color="orange")
plt.plot(t, v_ec, label="Geschwindigkeit (Euler-Cromer)", color="red", linestyle="dashed")
plt.xlabel("Zeit [s]")
plt.ylabel("Geschwindigkeit [m/s]")
plt.legend()

plt.tight_layout()
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
m = 1.0         # Masse in kg
k_feder = 2.0   # Federkonstante in N/m
y_0 = 1.0       # Anfangsauslenkung in m
v_0 = 0         # Anfangsgeschwindigkeit in m/s
dt = 0.05       # Zeitschritt in s
t_end = 20      # Endzeit in s

# Listen für Zeit, Auslenkung, Geschwindigkeit und Energie
t = np.arange(0, t_end, dt)
y = np.zeros(len(t))
v = np.zeros(len(t))
E = np.zeros(len(t))

# Setze Anfangswerte
y[0] = y_0
v[0] = v_0
E[0] = 0.5 * m * v[0]**2 + 0.5 * k_feder * y[0]**2

# Funktion für die Beschleunigung der harmonischen Schwingung
def acceleration_spring(y):
    return -k_feder * y / m

# Runge-Kutta-Verfahren 2. Ordnung für harmonische Schwingung
for i in range(1, len(t)):
    # Berechnung von k1 für Geschwindigkeit und Position
    k1_v = dt * acceleration_spring(y[i-1])
    k1_y = dt * v[i-1]
    
    # Berechnung der Zwischenschritte für k2
    k2_v = dt * acceleration_spring(y[i-1] + 0.5 * k1_y)
    k2_y = dt * (v[i-1] + 0.5 * k1_v)
    
    # Update der Position und Geschwindigkeit
    v[i] = v[i-1] + k2_v
    y[i] = y[i-1] + k2_y

    # Berechnung der Gesamtenergie
    E[i] = 0.5 * m * v[i]**2 + 0.5 * k_feder * y[i]**2

# Visualisierung der Auslenkung und Energie über die Zeit
plt.subplot(2, 1, 1)
plt.plot(t, y, label="Position (RK2)", color="purple")
plt.xlabel("Zeit [s]")
plt.ylabel("Position [m]")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, E, label="Gesamtenergie", color="green")
plt.xlabel("Zeit [s]")
plt.ylabel("Energie [J]")
plt.legend()

plt.tight_layout()
plt.show()
'''

# -=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=-=x=-=x=-=x=-=-=



