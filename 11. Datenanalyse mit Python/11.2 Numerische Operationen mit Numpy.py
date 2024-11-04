#              ________________________________________________
#       ______|                                                |_____
#       \     |    11.2 NUMERISCHE OPERATIONEN MIT NUMPY       |    /
#        )    |________________________________________________|   (
#       /________)                                         (________\      1.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Das `NumPy`-Modul bietet leistungsstarke Funktionen für numerische Berechnungen
# und die Arbeit mit Arrays. `NumPy` ist besonders nützlich, wenn es um mathematische
# Berechnungen mit großen Datenmengen geht.

# Um `NumPy` zu verwenden, importieren wir es mit dem Kürzel `np`.

import numpy as np


# _________________________________
#                                 /
# NumPy-Arrays erstellen         (
# ________________________________\

# Ein Array ist eine spezielle Datenstruktur, die in `NumPy` verwendet wird,
# um große Mengen numerischer Daten effizient zu speichern. Hier einige Wege,
# wie du ein Array erstellen kannst:

# 1. Aus einer Liste ein Array erstellen
array1 = np.array([1, 2, 3, 4, 5])
print("Array aus Liste:\n", array1)

# 2. Ein Array mit Nullen erstellen
array2 = np.zeros((3, 3))
print("\n3x3 Null-Array:\n", array2)

# 3. Ein Array mit Einsen erstellen
array3 = np.ones((2, 5))
print("\n2x5 Einsen-Array:\n", array3)




# _________________________________
#                                 /
# Grundrechenoperationen         (
# ________________________________\

# `NumPy` ermöglicht einfache und schnelle mathematische Operationen auf Arrays.

# Array-Addition
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
summe = array_a + array_b
print("\nArray-Addition:\n", summe)

# Array-Multiplikation
produkt = array_a * array_b
print("\nArray-Multiplikation:\n", produkt)




# _________________________________
#                                 /
# Mathematische Funktionen       (
# ________________________________\

# `NumPy` bietet viele mathematische Funktionen, die auf Arrays angewendet
# werden können. Hier einige Beispiele:

# Quadratwurzel
array_c = np.array([4, 9, 16])
wurzel = np.sqrt(array_c)
print("\nQuadratwurzel von Array:\n", wurzel)

# Sinus und Kosinus
winkel = np.array([0, np.pi/2, np.pi])
sinus = np.sin(winkel)
kosinus = np.cos(winkel)
print("\nSinus von Winkeln:\n", sinus)
print("\nKosinus von Winkeln:\n", kosinus)




# _________________________________
#                                 /
# Aggregationsfunktionen         (
# ________________________________\

# NumPy bietet einfache Möglichkeiten, statistische Werte zu berechnen.

# Beispiel-Array
data = np.array([1, 2, 3, 4, 5])

# Mittelwert berechnen
mittelwert = np.mean(data)
print("\nMittelwert des Arrays:", mittelwert)

# Summe und Standardabweichung
summe = np.sum(data)
std_abweichung = np.std(data)
print("\nSumme des Arrays:", summe)
print("Standardabweichung des Arrays:", std_abweichung)




# _________________________________
#                                 /
# Mehrdimensionale Arrays        (
# ________________________________\

# `NumPy` erlaubt die Erstellung von mehrdimensionalen Arrays (z.B. Matrizen).

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n3x3 Matrix:\n", matrix)

# Zugriff auf Elemente und Slicing
element = matrix[1, 1]  # Element in Zeile 2, Spalte 2
sub_matrix = matrix[:2, 1:]  # Teilmatrix
print("\nElement in Zeile 2, Spalte 2:", element)
print("\nTeilmatrix:\n", sub_matrix)




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - NumPy bietet Arrays zur effizienten Speicherung und Verarbeitung numerischer Daten.
#
# - Grundlegende Operationen wie Addition, Multiplikation und mathematische Funktionen
#   sind direkt auf Arrays anwendbar.
#
# - `NumPy` bietet viele nützliche Funktionen für Statistik, wie Mittelwert und
#   Standardabweichung.
#
# - Mehrdimensionale Arrays und Slicing machen das Arbeiten mit größeren Datenmengen einfach.


# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Array `a` mit den Zahlen 1 bis 10 und berechne die Summe, das Minimum
# und das Maximum.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein 3x3 Array mit Zufallszahlen zwischen 0 und 1 und berechne den Mittelwert
# der Zahlen.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle zwei Arrays `x` und `y` mit je 5 Elementen und berechne das Skalarprodukt.
# Tipp: Verwende `np.dot()`.


# Füge hier deine Lösung ein.


#   __________
#  | ________ |
#  ||12345678||
#  |""""""""""|         Numpy ist ein power-house.
#  |[M|#|C][-]|
#  |[7|8|9][+]|
#  |[4|5|6][x]|
#  |[1|2|3][%]|
#  |[.|O|:][=]|
#  "----------"  hjw
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
# Erstelle ein Array `a` mit den Zahlen 1 bis 10 und berechne die Summe, das Minimum
# und das Maximum.

'''
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
summe = np.sum(a)
minimum = np.min(a)
maximum = np.max(a)

print("Array:", a)
print("Summe:", summe)
print("Minimum:", minimum)
print("Maximum:", maximum)
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein 3x3 Array mit Zufallszahlen zwischen 0 und 1 und berechne den Mittelwert
# der Zahlen.

'''
array_3x3 = np.random.rand(3, 3)
mittelwert = np.mean(array_3x3)

print("\n3x3 Array mit Zufallszahlen:\n", array_3x3)
print("Mittelwert:", mittelwert)
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle zwei Arrays `x` und `y` mit je 5 Elementen und berechne das Skalarprodukt.
# Tipp: Verwende `np.dot()`.

'''
x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 8, 9, 10])
skalarprodukt = np.dot(x, y)

print("\nArray x:", x)
print("Array y:", y)
print("Skalarprodukt:", skalarprodukt)
'''



# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


