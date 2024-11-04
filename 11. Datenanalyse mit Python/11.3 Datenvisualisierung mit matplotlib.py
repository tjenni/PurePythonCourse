#              ____________________________________________
#       ______|                                            |_____
#       \     |  11.3 DATENVISUALISIERUNG MIT MATPLOTLIB   |    /
#        )    |____________________________________________|   (
#       /________)                                     (________\      4.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# `matplotlib` ist eine Python-Bibliothek, die das Erstellen von Grafiken und Diagrammen
# für Datenvisualisierungen ermöglicht. Sie ist vielseitig einsetzbar und eignet sich gut, um 
# Datenmuster zu erkennen und anschaulich darzustellen. In diesem Kapitel lernst du, wie 
# du `matplotlib` zum Erstellen einfacher Diagramme verwenden kannst.

import matplotlib.pyplot as plt


# _________________________________
#                                 /
# Einfaches Liniendiagramm        (
# ________________________________\

# Ein Liniendiagramm ist eine der gängigsten Methoden zur Darstellung von Daten über 
# eine fortlaufende Zeit oder Reihenfolge. Hier ein einfaches Beispiel:

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o', color='blue', linestyle='--')
plt.title("Einfaches Liniendiagramm")
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")
plt.show()


# _________________________________
#                                 /
# Balkendiagramm                  (
# ________________________________\

# Balkendiagramme eignen sich, um Datenkategorien miteinander zu vergleichen.
# Im folgenden Beispiel erstellen wir ein Balkendiagramm mit Kategorien und Werten:

kategorien = ["A", "B", "C", "D"]
werte = [3, 7, 5, 2]

plt.bar(kategorien, werte, color='green')
plt.title("Balkendiagramm")
plt.xlabel("Kategorien")
plt.ylabel("Werte")
plt.show()


# _________________________________
#                                 /
# Histogramm                      (
# ________________________________\

# Histogramme sind hilfreich, um die Verteilung von Daten darzustellen.
# Im Beispiel erstellen wir ein Histogramm für Zufallsdaten.

import numpy as np

daten = np.random.randn(1000)  # 1000 Zufallszahlen
plt.hist(daten, bins=30, color='purple')
plt.title("Histogramm der Datenverteilung")
plt.xlabel("Wert")
plt.ylabel("Häufigkeit")
plt.show()


# _________________________________
#                                 /
# Streudiagramm                   (
# ________________________________\

# Streudiagramme werden verwendet, um die Beziehung zwischen zwei Variablen zu zeigen.
# Hier ein Beispiel für ein Streudiagramm:

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='red')
plt.title("Streudiagramm")
plt.xlabel("X-Werte")
plt.ylabel("Y-Werte")
plt.show()


# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - `plt.plot()` erstellt ein Liniendiagramm, ideal für Daten über Zeit oder Reihenfolgen.
#
# - `plt.bar()` erstellt ein Balkendiagramm, nützlich zum Vergleich verschiedener Kategorien.
#
# - `plt.hist()` erzeugt ein Histogramm, das Datenverteilungen zeigt.
#
# - `plt.scatter()` erstellt ein Streudiagramm, das Beziehungen zwischen Variablen visualisiert.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Liniendiagramm, das die quadratischen Werte der Zahlen von 1 bis 10 darstellt.
# Beschrifte die X- und Y-Achse und gib einen Titel für das Diagramm an.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Balkendiagramm für fünf Produkte (z.B. "Apfel", "Banane", "Orange", "Traube", "Mango")
# und deren Verkaufszahlen. Beschrifte die Achsen und füge einen Titel hinzu.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Histogramm von 500 Zufallszahlen, die normalverteilt sind. Verwende 20 Bins und 
# gib dem Diagramm einen Titel sowie Achsenbeschriftungen.


# Füge hier deine Lösung ein.




#        __________ __
#       |    ___  _|__|_
#       |  ,'   '. {'\)  
#       | :  O O  : )(         Mit matplotolib kannst du schöne
#       | :  ._\. :/ )\        Diagramme zeichnen. 
#       |  '.___\\/ / | 
#       |        '-'  |
#       |_________|   |
#          /-----\|___|
#    jrei /       \||| 
#                 .:;;             
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
#                               |___/           
# 


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Liniendiagramm, das die quadratischen Werte der Zahlen von 1 bis 10 darstellt.
# Beschrifte die X- und Y-Achse und gib einen Titel für das Diagramm an.

'''
x = list(range(1, 11))
y = [i**2 for i in x]

plt.plot(x, y, marker='o')
plt.title("Quadratische Werte")
plt.xlabel("Zahl")
plt.ylabel("Quadrat")
plt.show()
'''


# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Balkendiagramm für fünf Produkte (z.B. "Apfel", "Banane", "Orange", "Traube", "Mango")
# und deren Verkaufszahlen. Beschrifte die Achsen und füge einen Titel hinzu.

'''
produkte = ["Apfel", "Banane", "Orange", "Traube", "Mango"]
verkaufszahlen = [20, 35, 30, 35, 27]

plt.bar(produkte, verkaufszahlen, color='orange')
plt.title("Produkt-Verkaufszahlen")
plt.xlabel("Produkt")
plt.ylabel("Verkaufszahlen")
plt.show()
'''


# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Histogramm von 500 Zufallszahlen, die normalverteilt sind. Verwende 20 Bins und 
# gib dem Diagramm einen Titel sowie Achsenbeschriftungen.

'''
zufallszahlen = np.random.randn(500)

plt.hist(zufallszahlen, bins=20, color='blue')
plt.title("Normalverteilte Zufallszahlen")
plt.xlabel("Wert")
plt.ylabel("Häufigkeit")
plt.show()
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><