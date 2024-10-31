#              ___________________________
#       ______|                           |_____
#       \     |    6.1 DAS MATH-MODUL     |    /
#        )    |___________________________|   (
#       /________)                    (________\       29.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Python bietet uns das `math`-Modul, das eine Vielzahl an Funktionen für 
# mathematische Berechnungen bereitstellt. Dieses Modul hilft uns, 
# Berechnungen effizient und mit wenigen Codezeilen durchzuführen.


# ____________________________
#                            /
# Modul importieren         (
# ___________________________\

# Um das `math`-Modul zu verwenden, müssen wir es zuerst importieren. 
# Das geht ganz einfach mit:

import math

# Jetzt haben wir Zugriff auf die Funktionen und Konstanten des `math`-Moduls.




# ____________________________
#                            /
# Wichtige Konstanten       (
# ___________________________\

# Das `math`-Modul enthält wichtige mathematische Konstanten wie Pi und die 
# Eulersche Zahl.

print("Pi:", math.pi)  # Pi ≈ 3.14159
print("Eulersche Zahl:", math.e)  # e ≈ 2.71828




# ___________________________
#                           /
# Wichtige Funktionen       (
# ___________________________\

# Das `math`-Modul enthält viele nützliche Funktionen. Hier sind einige 
# der wichtigsten:


# 1. Wurzelberechnung (`sqrt`): Berechnet die Quadratwurzel einer Zahl.
root = math.sqrt(25)
print("Die Quadratwurzel von 25 ist:", root)


# 2. Potenzen (`pow`): Berechnet die Potenz einer Zahl.
power = math.pow(2, 3)  # 2 hoch 3 = 8
print("2 hoch 3 ist:", power)


# 3. Runden (`floor` und `ceil`): 
# `floor` rundet eine Zahl auf die nächste ganze Zahl ab, `ceil` rundet sie auf.
number = 4.7
print("Abgerundet:", math.floor(number))  # Ergibt 4
print("Aufgerundet:", math.ceil(number))  # Ergibt 5


# 4. Trigonometrische Funktionen (`sin`, `cos`, `tan`):
# Berechnet den Sinus, Kosinus und Tangens eines Winkels (in Radiant).
alpha = math.pi / 4  # 45 Grad in Radiant
print("Sinus von 45°:", math.sin(alpha))
print("Kosinus von 45°:", math.cos(alpha))
print("Tangens von 45°:", math.tan(alpha))


# 5. Logarithmus (`log`): Berechnet den natürlichen Logarithmus.
# Man kann auch den Logarithmus zur Basis 10 mit `log10` berechnen.
number = 10
print("Natürlicher Logarithmus von 10:", math.log(number))  # Logarithmus zur Basis e
print("Logarithmus zur Basis 10 von 10:", math.log10(number))




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Mit `math.pi` und `math.e` stellt das math-Modul die Konstanten Pi und die
#   Eulersche Zahl bereit, die oft in mathematischen Berechnungen benötigt werden.
#
# - Das math-Modul bietet zahlreiche nützliche Funktionen, darunter:
#   - `sqrt()` für Quadratwurzeln,
#   - `pow()` für Potenzberechnungen,
#   - `floor()` und `ceil()` zum Abrunden und Aufrunden,
#   - `sin()`, `cos()` und `tan()` für trigonometrische Berechnungen,
#   - `log()` und `log10()` für Logarithmen.
#
# - Wichtig: Trigonometrische Funktionen wie `sin`, `cos` und `tan` erwarten den
#   Winkel im Bogenmass (Radiant). Mit `math.radians()` kann man Grad in Radiant umwandeln.
#
# - Eine vollständige Übersicht über die Funktionen des math-Moduls findest du unter
#   (https://docs.python.org/3/library/math.html).




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Berechne die Fläche eines Kreises mit einem Radius von 5, indem du Pi 
# aus dem `math`-Modul verwendest. Die Formel lautet: Fläche = pi * radius^2.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein kleines Programm, das den Benutzer nach einer Zahl fragt und dann die
# Quadratwurzel dieser Zahl berechnet. Verwende dazu die Funktion `math.sqrt()`.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Frage den Benutzer nach einem Winkel in Grad und berechne dann den Sinus,
# Kosinus und Tangens dieses Winkels, indem du ihn zuerst mit `math.radians()`
# in Radiant umwandelst. Zeige die Ergebnisse auf der Konsole an.


# Füge hier deine Lösung ein.



#     Mathemagier
#    
#        1+1=2    /\
#              \ c")
#               ;-/\>
#                 ||
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
# Berechne die Fläche eines Kreises mit einem Radius von 5, indem du Pi 
# aus dem `math`-Modul verwendest. Die Formel lautet: Fläche = pi * radius^2.

'''
radius = 5
area = math.pi * radius**2
print("Fläche des Kreises:", area)
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein kleines Programm, das den Benutzer nach einer Zahl fragt und dann die
# Quadratwurzel dieser Zahl berechnet. Verwende dazu die Funktion `math.sqrt()`.

'''
number = float(input("Gib eine Zahl ein, um ihre Quadratwurzel zu berechnen: "))
root = math.sqrt(zahl)
print("Die Quadratwurzel von", zahl, "ist:", root)
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Frage den Benutzer nach einem Winkel in Grad und berechne dann den Sinus,
# Kosinus und Tangens dieses Winkels, indem du ihn zuerst mit `math.radians()`
# in Radiant umwandelst. Zeige die Ergebnisse auf der Konsole an.

'''
alpha_grad = float(input("Gib einen Winkel in Grad ein: "))
alpha_rad = math.radians(grad_winkel)

sinus = math.sin(alpha_rad)
consinus = math.cos(alpha_rad)
tangens = math.tan(alpha_rad)

print("Sinus von", alpha_grad, "°:", sinus)
print("Kosinus von", alpha_grad, "°:", consinus)
print("Tangens von", alpha_grad, "°:", tangens)
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

