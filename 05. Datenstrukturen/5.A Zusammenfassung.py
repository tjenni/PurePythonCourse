#              ___________________________
#       ______|                           |_____
#       \     |    5 ZUSAMMENFASSUNG      |    /
#        )    |___________________________|   (
#       /________)                    (________\       11.12.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
#  


# Dieses Kapitel behandelt die verschiedenen Datensammlungen in Python,
# wie Listen, Tupel, Dictionaries und Sets. Diese Strukturen sind essenziell,
# um größere Datenmengen zu verwalten und darauf zuzugreifen.
#
# Wir beginnen mit Listen, der flexibelsten Datenstruktur in Python, und
# untersuchen Techniken wie Slicing, das Durchsuchen und Iterieren von Listen.
# Danach lernen wir die unveränderlichen Tupel, die strukturierten Dictionaries
# und die einzigartigen Elemente in Sets kennen.
#
# Zum Abschluss zeigt ein Praxisbeispiel, wie diese Datensammlungen in
# einfachen Spielen angewendet werden können.

# Ziel ist es, dir die wichtigsten Datenstrukturen in Python vorzustellen
# und dir zu zeigen, wie du sie in deinen Programmen einsetzen kannst.


# ___________________________
#                            /
#  Kapitelübersicht         (
# ___________________________\

# 5.1 Listen
#    - Einführung in Listen und deren grundlegende Methoden.
#    - Slicing und Techniken zum Durchsuchen und Iterieren.

# 5.2 Tupel
#    - Unveränderliche Listen.
#    - Anwendungsbereiche und typische Methoden.

# 5.3 Dictionaries
#    - Schlüssel-Wert-Paare zur Organisation von Daten.
#    - Zugriff und Manipulation von Dictionary-Einträgen.

# 5.4 Sets
#    - Mengen mit einzigartigen Elementen.
#    - Mengenoperationen wie Vereinigung, Schnittmenge und Differenz.

# 5.5 Einfache Spiele
#    - Anwendung von Listen, Dictionaries und Sets in Spielen.
#    - Beispiele: Wort-Ratespiel und Memory-Spiel.




# ___________________________
#                            /
#  Befehlsreferenz          (
# ___________________________\


# Listen
# ------
# Eine Liste ist eine geordnete Sammlung von Elementen, die veränderlich ist.

# Erstellung einer Liste:
# Syntax: [element1, element2, ...]
zahlen = [1, 2, 3, 4, 5]

# Zugriff auf Elemente:
# Syntax: liste[index]
print(zahlen[0])  # Ausgabe: 1

# Hinzufügen von Elementen:
zahlen.append(6)  # Fügt 6 ans Ende der Liste hinzu

# Entfernen von Elementen:
zahlen.remove(3)  # Entfernt das erste Vorkommen von 3

# Iteration:
for zahl in zahlen:
    print(zahl)

# Slicing:
print(zahlen[1:4])  # Gibt die Elemente von Index 1 bis 3 aus



# Tupel
# -----
# Ein Tupel ist eine geordnete, aber unveränderliche Sammlung von Elementen.

# Erstellung eines Tupels:
# Syntax: (element1, element2, ...)
koord = (10, 20, 30)

# Zugriff auf Elemente:
print(koord[1])  # Ausgabe: 20

# Iteration:
for wert in koord:
    print(wert)



# Dictionaries
# -------------
# Dictionaries sind Sammlungen von Schlüssel-Wert-Paaren.

# Erstellung eines Dictionaries:
# Syntax: {schlüssel: wert, ...}
person = {"name": "Lena", "alter": 25}

# Zugriff auf Werte:
print(person["name"])  # Ausgabe: Lena

# Hinzufügen oder Aktualisieren von Einträgen:
person["stadt"] = "Zug"

# Entfernen von Einträgen:
person.pop("alter")  # Entfernt den Eintrag mit Schlüssel "alter"

# Iteration über Schlüssel und Werte:
for schlüssel, wert in person.items():
    print(f"{schlüssel}: {wert}")



# Sets
# -----
# Ein Set ist eine ungeordnete Sammlung von einzigartigen Elementen.

# Erstellung eines Sets:
# Syntax: {element1, element2, ...}
farben = {"rot", "grün", "blau"}

# Hinzufügen von Elementen:
farben.add("gelb")

# Entfernen von Elementen:
farben.discard("rot")  # Entfernt "rot", wenn vorhanden

# Mengenoperationen:
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Vereinigung:
print(set1 | set2)  # {1, 2, 3, 4, 5}

# Schnittmenge:
print(set1 & set2)  # {3}

# Differenz:
print(set1 - set2)  # {1, 2}


# Anwendungen in Spielen
# -----------------------
# Listen und andere Datenstrukturen sind nützlich in Spielen.

# Zufällige Auswahl aus einer Liste:
import random
wörter = ["Apfel", "Banane", "Kirsche"]
geheimes_wort = random.choice(wörter)
print("Geheimes Wort:", geheimes_wort)

# Karten mischen:
karten = ["Herz Ass", "Pik König", "Kreuz Dame"]
random.shuffle(karten)
print("Gemischte Karten:", karten)




