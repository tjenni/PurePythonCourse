#              ___________________________
#       ______|                           |_____
#       \     |        5.2 TUPEL          |    /
#        )    |___________________________|   (
#       /________)                    (________\       28.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Ein Tupel (Tuple) ist eine unveränderliche (immutable) Datenstruktur in Python.
# Das bedeutet, dass ein einmal erstelltes Tupel nicht mehr verändert werden kann –
# also keine Elemente hinzugefügt, entfernt oder geändert werden können.

# Tupel sind besonders nützlich, wenn man eine feste Struktur braucht, wie z. B.
# Koordinaten, Farben oder andere Daten, die konstant bleiben sollen.


# ____________________________
#                            /
# Tupel erstellen           (
# ___________________________\

# Ein Tupel wird mit runden Klammern `()` erstellt, und die Elemente werden durch
# Kommata getrennt. 

# Beispiel:
colors = ("Rot", "Blau", "Grün")
print("Farben-Tupel:", colors)

# Hinweis: Wenn ein Tupel nur ein einziges Element enthält, muss das Element ein
# Komma am Ende haben, z. B. `numbers = (3,)`.


# ____________________________
#                            /
# Auf Elemente zugreifen    (
# ___________________________\

# Wir können auf einzelne Elemente eines Tupels mit einem Index zugreifen,
# ähnlich wie bei Listen. Da Tupel unveränderlich sind, können wir die Elemente
# aber nicht ändern.

# Beispiel:
first_color = colors[0]
print("Erste Farbe:", first_color)

# Versucht man, ein Element zu ändern, führt das zu einem Fehler:
# colors[0] = "Gelb"  # Das führt zu einem Fehler!




# ____________________________
#                            /
# Tupel entpacken           (
# ___________________________\

# Ein praktisches Feature von Tupeln ist das Entpacken (Unpacking). Wir können ein
# Tupel direkt in mehrere Variablen aufteilen.

coordinates = (10, 20)
x, y = coordinates

print("x:", x)
print("y:", y)

# Hinweis: Die Anzahl der Variablen muss mit der Anzahl der Elemente im 
# Tupel übereinstimmen.




# ____________________________
#                            /
# Tupel und Schleifen       (
# ___________________________\

# Wir können ein Tupel auch mit einer `for`-Schleife durchlaufen, um auf jedes
# Element nacheinander zuzugreifen.

for color in colors:
    print("Farbe:", color)




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Tupel sind unveränderlich, also können keine Elemente hinzugefügt, entfernt
#   oder geändert werden.
#
# - Sie sind nützlich für Daten, die fest und unveränderlich sein sollen.
#
# - Tupel unterstützen Entpacken und lassen sich in Schleifen durchlaufen.





# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Tupel namens `numbers` mit den Werten 1, 2, 3 und 4.
# Greife auf das zweite Element zu und gib es auf der Konsole aus.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Tupel `point` mit den Werten (5, 10).
# Entpacke das Tupel in die Variablen `x` und `y` und gib beide Werte aus.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Tupel `colors` mit den Elementen "Rot", "Grün" und "Blau".
# Durchlaufe das Tupel mit einer `for`-Schleife und gib jede Farbe aus.


# Füge hier deine Lösung ein.




#          _        ,..
#     ,--._\\_.--, (-00)
#    ; #         _:(  -)         Super gemacht!
#    :          (_____/
#    :            :
#     '.___..___.`dwb
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
# Erstelle ein Tupel namens `numbers` mit den Werten 1, 2, 3 und 4.
# Greife auf das zweite Element zu und gib es auf der Konsole aus.

'''
numbers = (1, 2, 3, 4)
print("Zweites Element:", numbers[1])
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Tupel `point` mit den Werten (5, 10).
# Entpacke das Tupel in die Variablen `x` und `y` und gib beide Werte aus.

'''
point = (5, 10)
x, y = point
print("x:", x)
print("y:", y)
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Tupel `colors` mit den Elementen "Rot", "Grün" und "Blau".
# Durchlaufe das Tupel mit einer `for`-Schleife und gib jede Farbe aus.

'''
colors = ("Rot", "Grün", "Blau")
for color in colors:
    print("Farbe:", color)
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


