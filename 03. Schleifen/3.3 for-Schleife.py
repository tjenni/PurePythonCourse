#              ___________________________
#       ______|                           |_____
#       \     |      3.3 FOR-SCHLEIFE     |    /
#        )    |___________________________|   (
#       /________)                    (________\       28.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Die `for`-Schleife wird verwendet, wenn wir eine Aktion eine bestimmte Anzahl 
# von Malen oder für jedes Element in einer Sammlung wiederholen möchten.
# In Python wird die `for`-Schleife häufig in Kombination mit der `range()`-Funktion 
# verwendet, um eine festgelegte Anzahl von Durchläufen zu erstellen.




# _______________________________
#                               /
# Die for-Schleife und range() (
# ______________________________\

# Die `range()`-Funktion erstellt eine Folge von Zahlen, die in der `for`-Schleife
# durchlaufen wird. In den meisten Fällen geben wir `start`, `stop` und `step` an
# (siehe Hinweis zur `range()`-Funktion). Einfache Verwendung der `for`-Schleife:

# Beispiel: Ausgabe der Zahlen 1 bis 5

for zahl in range(1, 6):  # `range(1, 6)` erzeugt die Zahlen 1 bis 5
    print(zahl)

# Die `for`-Schleife durchläuft hier alle Zahlen im Bereich 1 bis 5 und 
# gibt jede Zahl aus.




# ___________________________
#                           /
#  Die range()-Funktion    (
# __________________________\

# Die `range()`-Funktion wird oft in `for`-Schleifen verwendet, um eine Folge 
# von Zahlen zu erzeugen. Sie hat drei Parameter: `start`, `stop` und `step`.
# Je nach Einsatz der Parameter sieht die `range()`-Funktion folgendermassen aus:

# 1. `range(stop)`:  Erzeugt Zahlen von 0 bis `stop - 1`.
#    Beispiel: `range(5)` erzeugt die Zahlen 0, 1, 2, 3, 4.

# 2. `range(start, stop)`: Erzeugt Zahlen von `start` bis `stop - 1`.
#    Beispiel: `range(2, 6)` erzeugt die Zahlen 2, 3, 4, 5.

# 3. `range(start, stop, step)`: Erzeugt Zahlen von `start` bis `stop - 1`, 
#    wobei jede Zahl um `step` erhöht wird.
#    Beispiel: `range(1, 10, 2)` erzeugt die Zahlen 1, 3, 5, 7, 9.


#  _ MERKE ________________________________
# |                                        |
# | Der `stop`-Wert ist nie im erzeugten   |
# | Zahlenbereich enthalten.               |
# |________________________________________|


# Die `range()`-Funktion ist besonders nützlich, wenn du die Anzahl der
# Schleifendurchläufe kontrollieren oder bestimmte Zahlenfolgen erzeugen möchtest.

# Beispiel:
for i in range(2, 8): 
    print("i:", i)




# __________________________________________
#                                          /
# Iterieren über Listen und Zeichenketten (
# _________________________________________\

# Die `for`-Schleife kann auch über Listen, Zeichenketten und andere
# Sammlungen iterieren. Hier sind Beispiele für das Durchlaufen einer Liste und
# einer Zeichenkette.

# Beispiel: Iteration über eine Liste

obstliste = ["Apfel", "Banane", "Kirsche"]
for obst in obstliste:
    print(obst)

# Die Schleife gibt jedes Element der Liste `obstliste` nacheinander aus.
# Das Thema Listen wird im Kapitel `5. Listen` ausführlich behandelt. 


# Beispiel: Iteration über eine Zeichenkette

for buchstabe in "Python":
    print(buchstabe)

# Die Schleife gibt jeden Buchstaben im Wort "Python" einzeln aus.




# _______________________________
#                               /
# Verschachtelte for-Schleifen (
# ______________________________\

# `for`-Schleifen können auch ineinander verschachtelt werden.
# Dies ist nützlich, wenn du z. B. eine Tabelle oder ein Muster erstellen möchtest.

# Beispiel: Ausgabe eines 3x3-Musters mit Zahlen

for i in range(1, 4):       # Äußere Schleife für Zeilen
    for j in range(1, 4):   # Innere Schleife für Spalten
        print(f"({i}, {j})", end=" ")
    print()  # Zeilenumbruch nach jeder Zeile

# Hier wird für jede Zahl in der äußeren Schleife (Zeilen) die innere Schleife
# (Spalten) dreimal ausgeführt. Das Ergebnis ist ein 3x3-Muster aus Koordinaten.




# ___________________________________
#                                   /
# Wann die for-Schleife verwenden? (
# __________________________________\

# Verwende die `for`-Schleife, wenn:

# - Du eine Aktion für jedes Element in einer Sammlung (z. B. Liste oder Zeichenkette) 
#   ausführen möchtest.

# - Die Anzahl der Wiederholungen festgelegt ist, wie bei einer `range()`-Funktion.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Schreibe eine `for`-Schleife, die die Zahlen von 1 bis 20 auf der Konsole ausgibt.
# Verwende die `range()`-Funktion.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/

# Schreibe eine `for`-Schleife, die alle geraden Zahlen von 2 bis 20 auf der 
# Konsole ausgibt. Verwende dazu die `range(start, stop, step)`-Funktion, 
# um nur gerade Zahlen zu erzeugen.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine `for`-Schleife, die alle Vokale im Wort "Programmieren"
# einzeln auf der Konsole ausgibt.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 4  /
# __________/
#
# Schreibe eine `for`-Schleife, die alle Zahlen von 1 bis 100 aufsummiert.
# Gib das Gesamtergebnis nach der Schleife auf der Konsole aus.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 5  /
# __________/
#
# Schreibe eine verschachtelte `for`-Schleife, die ein Rechteck aus Sternen
# auf der Konsole ausgibt. Die Größe des Rechtecks soll 5 Zeilen und 10 Spalten haben.

# Füge hier deine Lösung ein.



# <>================================<>     
# ||\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/||    
# ||<> <> <> <> <> <> <> <> <> <> <>|| 
# ||/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\||
# ||================================||
# ||<> <> <> <> <> <> <> <> <> <> <>||      Mit Wiederholungen kann
# ||================================||      man einen Teppich knüpfen.
# ||/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\||               
# ||<> <> <> <> <> <> <> <> <> <> <>||
# ||\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/||
# <>================================<> gfj/98
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
# Schreibe eine `for`-Schleife, die die Zahlen von 1 bis 20 auf der Konsole ausgibt.
# Verwende die `range()`-Funktion.

'''
for zahl in range(1, 21):
    print(zahl)
'''




# ___________
#            \
# Aufgabe 2  /
# __________/

# Schreibe eine `for`-Schleife, die alle geraden Zahlen von 2 bis 20 auf der 
# Konsole ausgibt. Verwende dazu die `range(start, stop, step)`-Funktion, 
# um nur gerade Zahlen zu erzeugen.

'''
for zahl in range(2, 21, 2):
    print(zahl)
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine `for`-Schleife, die alle Vokale im Wort "Programmieren"
# einzeln auf der Konsole ausgibt.

'''
word = "Programmieren"
vocals = "aeiou"

for letter in word:
    if letter.lower() in vocals:  # prüft, ob der Buchstabe ein Vokal ist
        print(letter)
'''




# ___________
#            \
# Aufgabe 4  /
# __________/
#
# Schreibe eine `for`-Schleife, die alle Zahlen von 1 bis 100 aufsummiert.
# Gib das Gesamtergebnis nach der Schleife auf der Konsole aus.

'''
result = 0

for i in range(101):
    result += i

print(result)
'''




# ___________
#            \
# Aufgabe 5  /
# __________/
#
# Schreibe eine verschachtelte `for`-Schleife, die ein Rechteck aus Sternen
# auf der Konsole ausgibt. Die Größe des Rechtecks soll 5 Zeilen und 10 Spalten haben.

'''
for row in range(5):           # 5 Zeilen
    for column in range(10):   # 10 Spalten
        print("*", end="")     # Stern ohne Zeilenumbruch ausgeben
    print()                    # Zeilenumbruch nach jeder Zeile
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><




