#              ____________________________________________
#       ______|                                            |_____
#       \     |        11.4 REGRESSION MIT SCIPY           |    /
#        )    |____________________________________________|   (
#       /________)                                     (________\      4.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Die `scipy`-Bibliothek bietet eine erweiterte Funktionalität für wissenschaftliche 
# Berechnungen in Python. Für Regressionen, also das Anpassen einer Kurve an gegebene 
# Daten, stellt `scipy` die Funktion `curve_fit()` zur Verfügung. Diese Methode erlaubt 
# es, beliebige Funktionen an die Daten anzupassen, sodass auch nicht-lineare Zusammenhänge 
# modelliert werden können.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# _________________________________
#                                 /
# Grundlagen der Funktion curve_fit(
# ________________________________\

# Die Funktion `curve_fit()` passt eine beliebige Funktion an die Daten an.
# Der Anwender definiert eine Modellfunktion mit den Parametern, die die Kurve 
# charakterisieren, und `curve_fit()` berechnet die besten Werte für diese Parameter.

# Syntax von `curve_fit`:
# `curve_fit(funktion, x_daten, y_daten, p0)`
#
# - `funktion`: Die Modellfunktion, die an die Daten angepasst werden soll.
# - `x_daten` und `y_daten`: Die Werte der unabhängigen und abhängigen Variablen.
# - `p0`: Ein optionaler Startwert für die Parameter (z. B. für `a` und `b` in `a * x + b`).




# _________________________________
#                                 /
# Beispiel: Lineare Anpassung     (
# ________________________________\

# Angenommen, wir haben eine einfache lineare Funktion der Form `f(x) = a * x + b`.
# Wir verwenden `curve_fit()`, um `a` und `b` so anzupassen, dass die Funktion die 
# Daten bestmöglich beschreibt.

# Beispiel-Daten
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.2, 4.1, 6.3, 7.9, 9.6])

# Definieren der Modellfunktion
def lineare_funktion(x, a, b):
    return a * x + b

# Anwenden von curve_fit
params, covariance = curve_fit(lineare_funktion, x, y)
a, b = params
print("Steigung (a):", a)
print("Y-Achsenabschnitt (b):", b)

# Visualisierung der Anpassung
plt.scatter(x, y, label="Datenpunkte")
plt.plot(x, lineare_funktion(x, a, b), color="red", label="Angepasste Linie")
plt.xlabel("x-Werte")
plt.ylabel("y-Werte")
plt.legend()
plt.title("Lineare Anpassung mit curve_fit()")
plt.show()




# _________________________________
#                                 /
# Nicht-lineare Anpassung         (
# ________________________________\

# Nicht-lineare Beziehungen können ebenfalls angepasst werden, indem eine
# nicht-lineare Modellfunktion definiert wird, wie z.B. eine quadratische Funktion.

# Beispiel: Quadratische Funktion
def quadratische_funktion(x, a, b, c):
    return a * x**2 + b * x + c

# Quadratische Beispiel-Daten
x = np.array([1, 2, 3, 4, 5])
y = np.array([1.2, 4.5, 9.1, 16.3, 25.8])

# Anwenden von curve_fit
params, covariance = curve_fit(quadratische_funktion, x, y)
a, b, c = params
print("Parameter a:", a)
print("Parameter b:", b)
print("Parameter c:", c)

# Visualisierung der Anpassung
plt.scatter(x, y, label="Datenpunkte")
plt.plot(x, quadratische_funktion(x, a, b, c), color="green", label="Angepasste Kurve")
plt.xlabel("x-Werte")
plt.ylabel("y-Werte")
plt.legend()
plt.title("Quadratische Anpassung mit curve_fit()")
plt.show()




# _________________________________
#                                 /
# Modellgüte und Fehlerschätzung  (
# ________________________________\

# Neben den optimalen Parametern liefert `curve_fit()` auch eine Kovarianzmatrix,
# die Informationen über die Unsicherheit der Parameter enthält. Die Diagonalelemente 
# der Kovarianzmatrix sind die Varianzen der Parameter, die Wurzel daraus gibt 
# die Standardabweichungen.

# Berechnung der Standardabweichungen
unsicherheiten = np.sqrt(np.diag(covariance))
print("Unsicherheiten der Parameter:", unsicherheiten)




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - `curve_fit()` in `scipy` passt eine Funktion an gegebene Daten an.
#
# - Sie ermöglicht die Anpassung von linearen und nicht-linearen Modellen.
#
# - Die Kovarianzmatrix gibt Aufschluss über die Unsicherheit der Parameter.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle einen Datensatz und passe eine lineare Funktion der Form `f(x) = a * x + b`
# an die Daten an. Gib die Werte für `a` und `b` sowie die Unsicherheiten an.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Verwende eine exponentielle Funktion `f(x) = a * np.exp(b * x)` und passe sie an 
# einen Datensatz an. Visualisiere die Datenpunkte und die angepasste Kurve.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Funktion `polynomiale_anpassung(x, y, grad)`, die eine polynomiale
# Anpassung eines bestimmten Grads an die Daten vornimmt und die Koeffizienten zurückgibt.


# Füge hier deine Lösung ein.



#       .-.      Nun kannst du Kurven an Datenpunkte anpassen.            .-.
#      /   \           .-.                                 .-.           /   \
#     /     \         /   \       .-.     _     .-.       /   \         /     \
#   -/-------\-------/-----\-----/---\---/-\---/---\-----/-----\-------/-------\--
#             \     /       \   /     `-'   `-'     \   /       \     /
#              \   /         `-'                     `-'         \   /
#               `-'                                               `-'
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
# Erstelle einen Datensatz und passe eine lineare Funktion der Form `f(x) = a * x + b`
# an die Daten an. Gib die Werte für `a` und `b` sowie die Unsicherheiten an.

'''
# Beispiel-Daten erstellen
x_data = np.linspace(0, 10, 50)
y_data = 3 * x_data + 5 + np.random.normal(0, 2, 50)  # Hinzufügen von etwas Rauschen

# Lineare Funktion definieren
def linear(x, a, b):
    return a * x + b

# Lineare Anpassung
params, covariance = curve_fit(linear, x_data, y_data)
a, b = params
unsicherheiten = np.sqrt(np.diag(covariance))

# Ergebnisse anzeigen
print(f"a = {a:.2f} ± {unsicherheiten[0]:.2f}")
print(f"b = {b:.2f} ± {unsicherheiten[1]:.2f}")

# Plot erstellen
plt.scatter(x_data, y_data, label="Daten")
plt.plot(x_data, linear(x_data, a, b), color="red", label="Anpassung: f(x) = {:.2f} * x + {:.2f}".format(a, b))
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Lineare Anpassung")
plt.show()
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Verwende eine exponentielle Funktion `f(x) = a * np.exp(b * x)` und passe sie an 
# einen Datensatz an. Visualisiere die Datenpunkte und die angepasste Kurve.

'''
# Beispiel-Daten erstellen
x_data = np.linspace(0, 4, 50)
y_data = 2 * np.exp(0.7 * x_data) + np.random.normal(0, 0.5, 50)  # Exponential mit Rauschen

# Exponentielle Funktion definieren
def exponential(x, a, b):
    return a * np.exp(b * x)

# Anpassung durchführen
params, covariance = curve_fit(exponential, x_data, y_data)
a, b = params

# Plot erstellen
plt.scatter(x_data, y_data, label="Daten")
plt.plot(x_data, exponential(x_data, a, b), color="orange", label="Anpassung: f(x) = {:.2f} * exp({:.2f} * x)".format(a, b))
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Exponentielle Anpassung")
plt.show()
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Funktion `polynomiale_anpassung(x, y, degree)`, die eine polynomiale
# Anpassung eines bestimmten Grads an die Daten vornimmt und die Koeffizienten zurückgibt.


'''
def polynomial_fit(x, y, degree):
    # Berechnet die Koeffizienten des Polynoms
    coefficients = np.polyfit(x, y, degree)
    return coefficients

# Beispiel-Daten
x_data = np.linspace(-10, 10, 100)
y_data = 0.01 * x_data**3 - 0.2 * x_data**2 + 3 * x_data + 5 + np.random.normal(0, 10, 100)

# Polynomiale Anpassung 3. Grades
coefficients = polynomial_fit(x_data, y_data, 3)
p = np.poly1d(coefficients)

# Ergebnisse anzeigen
print("Koeffizienten des Polynoms:", coefficients)

# Plot erstellen
plt.scatter(x_data, y_data, label="Daten")
plt.plot(x_data, p(x_data), color="green", label=f"Anpassung: Polynom Grad 3")
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Polynomiale Anpassung")
plt.show()
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

