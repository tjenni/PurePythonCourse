#              ___________________________
#       ______|                           |_____
#       \     |       5.1 LISTEN          |    /
#        )    |___________________________|   (
#       /________)                    (________\       28.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Listen sind eine der nützlichsten Datenstrukturen in Python. Sie ermöglichen es, 
# mehrere Werte in einer geordneten Struktur zu speichern. Listen sind veränderbar 
# (mutabel), das heisst, wir können Elemente hinzufügen, entfernen oder ändern.

# Eine Liste erstellen wir mit eckigen Klammern `[]`. Hier ist ein Beispiel:

# Syntax:
# meine_liste = [element1, element2, element3]

# Beispiel einer Liste:
fruits = ["Apfel", "Banane", "Kirsche"]
print("Liste der Früchte:", fruits)




# ____________________________
#                            /
# Elemente in Listen        (
# ___________________________\

# Auf einzelne Elemente einer Liste können wir mit einem Index zugreifen.
# Der Index gibt die Position des Elements in der Liste an (beginnend bei 0).

# Beispiel:
print("Erstes Element:", fruits[0])  # Apfel
print("Zweites Element:", fruits[1])  # Banane

# Wir können die Liste auch verändern, indem wir ein Element mit einem bestimmten 
# Index ersetzen.

# Beispiel:
fruits[1] = "Orange"
print("Liste nach Änderung:", fruits)




# ____________________________________
#                                    /
# Elemente hinzufügen und entfernen (
# ___________________________________\

# Mit `append()` können wir ein Element am Ende der Liste hinzufügen.
fruits.append("Melone")
print("Nach Hinzufügen:", fruits)

# Mit `remove()` können wir ein Element aus der Liste entfernen.
fruits.remove("Apfel")
print("Nach Entfernen:", fruits)

# Mit `pop()` entfernen wir das letzte Element.
fruits.pop()  # Entfernt das letzte Element
print("Nach pop():", fruits)




# ___________________________
#                           /
# pop-Befehl               (
# __________________________\

# Der `pop()`-Befehl wird verwendet, um ein Element aus einer Liste zu entfernen 
# und zurückzugeben. Dies ist nützlich, wenn wir ein Element aus der Liste nehmen 
# und weiterverarbeiten möchten.

# Ohne einen Index entfernt `pop()` das letzte Element der Liste.

# Beispiel: Entfernt und gibt das letzte Element zurück
fruits = ["Apfel", "Banane", "Kirsche"]
last = fruits.pop()  # entfernt und speichert das letzte Element
print("Letztes Element:", last)
print("Liste nach pop():", fruits)


# Mit einem Index entfernt `pop(index)` das Element an der angegebenen Position.

# Beispiel: Entfernt und gibt das Element an der angegebenen Position zurück
fruits = ["Apfel", "Banane", "Kirsche"]
second = fruits.pop(1)  # entfernt und speichert das Element am Index 1
print("Entferntes Element:", second)
print("Liste nach pop(1):", fruits)




# ____________________________
#                            /
# Länge der Liste bestimmen (
# ___________________________\

# Mit `len()` können wir die Anzahl der Elemente in der Liste bestimmen.
num_fruits = len(fruits)
print("Anzahl der Früchte:", num_fruits)




# ____________________________
#                            /
# Liste sortieren           (
# ___________________________\

# Mit `sort()` können wir die Liste in alphabetischer Reihenfolge sortieren.
fruits.sort()
print("Nach sort():", fruits)

# Mit `reverse()` kehren wir die Reihenfolge der Liste um.
fruits.reverse()
print("Nach reverse():", fruits)




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# Listen sind veränderbar. Sie eignen sich hervorragend, um Sammlungen von Elementen
# zu speichern, deren Inhalt sich ändern kann. Sie können auch unterschiedliche 
# Datentypen enthalten, z. B. [1, "Apfel", True].




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine Liste namens `animals` mit den Elementen "Hund", "Katze" und "Vogel".
# Füge anschliessend "Fisch" zur Liste hinzu und gib die Liste auf der Konsole aus.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe ein Programm, das eine Liste namens `numbers` mit den Zahlen 5, 3, 8 und 6 erstellt.
# Sortiere die Liste, entferne das kleinste Element und gib die Liste aus.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Liste namens `menu` mit den Elementen "Pizza", "Burger" und "Salat".
# Ändere "Salat" in "Pasta" und füge dann "Suppe" am Ende hinzu. Gib die fertige Liste aus.


# Füge hier deine Lösung ein.




#  (\ 
#  \'\ 
#   \'\     __________  
#   / '|   ()_________)
#   \ '/    \ ~~~~~~~~ \           Gut gemacht. Du kannst nun mit  
#     \       \ ~~~~~~   \         Listen umgehen.
#     ==).      \__________\
#    (__)       ()__________)
#  ___ _  _ ___  ___ 
# | __| \| |   \| __|
# | _|| .` | |) | _| 
# |___|_|\_|___/|___|
#                
# -=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x




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
# Erstelle eine Liste namens `animals` mit den Elementen "Hund", "Katze" und "Vogel".
# Füge anschliessend "Fisch" zur Liste hinzu und gib die Liste auf der Konsole aus.

'''
animals = ["Hund", "Katze", "Vogel"]
animals.append("Fisch")
print("Liste der Tiere:", animals)
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe ein Programm, das eine Liste namens `numbers` mit den Zahlen 5, 3, 8 und 6 erstellt.
# Sortiere die Liste, entferne das kleinste Element und gib die Liste aus.

'''
numbers = [5, 3, 8, 6]
numbers.sort()  # Sortiert die Liste aufsteigend
numbers.pop(0)  # Entfernt das kleinste Element (erstes Element)
print("Zahlen nach Bearbeitung:", numbers)
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Liste namens `menu` mit den Elementen "Pizza", "Burger" und "Salat".
# Ändere "Salat" in "Pasta" und füge dann "Suppe" am Ende hinzu. Gib die fertige Liste aus.

'''
menu = ["Pizza", "Burger", "Salat"]
menu[2] = "Pasta"  # Ersetzt "Salat" durch "Pasta"
menu.append("Suppe")  # Fügt "Suppe" hinzu
print("Aktuelle Speisekarte:", menu)
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><





