#              ___________________________
#       ______|                           |_____
#       \     |    6.2 DAS RANDOM-MODUL   |    /
#        )    |___________________________|   (
#       /________)                    (________\

# Das `random`-Modul in Python bietet uns eine Sammlung nützlicher Funktionen,
# um Zufallszahlen zu generieren und zufällige Elemente auszuwählen. Das Modul
# eignet sich besonders gut für Spiele, Simulationen oder jede Anwendung, bei
# der zufällige Werte benötigt werden.


# ____________________________
#                            /
# Modul importieren         (
# ___________________________\

# Um das `random`-Modul zu verwenden, muss es zuerst importiert werden:

import random




# ____________________________
#                            /
# Zufallszahlen             (
# ___________________________\

# 1. `random.randint(a, b)`: Generiert eine ganzzahlige Zufallszahl zwischen `a` und `b` (beide inklusive).
random_number = random.randint(1, 10)  # Zufallszahl zwischen 1 und 10
print("Ganzzahlige Zufallszahl (1 bis 10):", random_number)

# 2. `random.random()`: Gibt eine zufällige Fließkommazahl zwischen 0.0 und 1.0 zurück.
random_number_float = random.random()
print("Fließkommazahl (zwischen 0 und 1):", random_number_float)

# 3. `random.uniform(a, b)`: Gibt eine zufällige Fließkommazahl zwischen `a` und `b` zurück.
random_float_range = random.uniform(5, 10)  # Zufallszahl zwischen 5.0 und 10.0
print("Fließkommazahl (zwischen 5 und 10):", random_float_range)




# ____________________________
#                            /
# Auswahl aus Listen        (
# ___________________________\

# Mit `random` können wir auch Elemente aus Listen auswählen oder Listen mischen:

colors = ["Rot", "Blau", "Grün", "Gelb", "Lila"]

# 1. `random.choice(seq)`: Wählt ein zufälliges Element aus der Liste `seq`.
random_color = random.choice(colors)
print("Zufällige Farbe:", random_color)

# 2. `random.shuffle(seq)`: Mischt die Elemente einer Liste `seq` in zufälliger Reihenfolge.
random.shuffle(colors)
print("Zufällig gemischte Farben:", colors)

# 3. `random.sample(seq, k)`: Wählt `k` zufällige, eindeutige Elemente aus der Liste `seq`.
random_colors = random.sample(colors, 2)
print("Zufällige Auswahl von 2 Farben:", random_colors)




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - `randint(a, b)` erzeugt eine Zufallszahl zwischen `a` und `b`.
#
# - `random()` erzeugt eine zufällige Fließkommazahl zwischen 0.0 und 1.0.
#
# - Mit `choice`, `shuffle` und `sample` können wir zufällig auf Elemente 
#   on Listen zugreifen. Das ist besonders nützlich für Spiele und Simulationen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Schreibe ein Programm, das eine Zufallszahl zwischen 1 und 100 generiert
# und den Benutzer raten lässt, bis er die richtige Zahl gefunden hat.
# Gib Feedback, ob die Zahl höher oder niedriger ist.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Spiel, bei dem das Programm zufällig zwischen den Befehlen
# „Schere“, „Stein“ und „Papier“ wählt. Der Benutzer soll ebenfalls einen dieser
# Begriffe eingeben, und das Programm entscheidet, wer gewinnt.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe ein Programm, das eine Liste mit zehn zufälligen Zahlen zwischen 1
# und 50 erstellt und die höchste Zahl in der Liste ausgibt.


# Füge hier deine Lösung ein.



#                   (( _______
#         _______     /\O    O\
#        /O     /\   /  \      \
#       /   O  /O \ / O  \O____O\ ))    Du hast die Zufallszahlen
#    ((/_____O/    \\    /O     /       im Griff.
#      \O    O\    / \  /   O  /
#       \O    O\ O/   \/_____O/
#        \O____O\/ )) mrf      ))
#      ((
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
# Schreibe ein Programm, das eine Zufallszahl zwischen 1 und 100 generiert
# und den Benutzer raten lässt, bis er die richtige Zahl gefunden hat.
# Gib Feedback, ob die Zahl höher oder niedriger ist.

'''
import random

secret_number = random.randint(1, 100)
print("Willkommen beim Zahlenraten! Ich habe eine Zahl zwischen 1 und 100 gewählt.")

while True:
    guess = int(input("Rate die Zahl: "))
    
    if guess < secret_number:
        print("Zu niedrig!")
    elif guess > secret_number:
        print("Zu hoch!")
    else:
        print("Richtig! Du hast die Zahl erraten.")
        break
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Spiel, bei dem das Programm zufällig zwischen den Befehlen
# „Schere“, „Stein“ und „Papier“ wählt. Der Benutzer soll ebenfalls einen dieser
# Begriffe eingeben, und das Programm entscheidet, wer gewinnt.

'''
import random

options = ["Schere", "Stein", "Papier"]
computer_choice = random.choice(options)

user_choice = input("Wähle Schere, Stein oder Papier: ")

print(f"Computer wählt: {computer_choice}")

if user_choice == computer_choice:
    print("Unentschieden!")
elif (user_choice == "Schere" and computer_choice == "Papier") or \
     (user_choice == "Stein" and computer_choice == "Schere") or \
     (user_choice == "Papier" and computer_choice == "Stein"):
    print("Du gewinnst!")
else:
    print("Computer gewinnt!")
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe ein Programm, das eine Liste mit zehn zufälligen Zahlen zwischen 1
# und 50 erstellt und die höchste Zahl in der Liste ausgibt.

'''
numbers = []

for i in range(10):
	numbers.append(random.randint(1, 50))

print("Liste der zufälligen Zahlen:", numbers)

max_number = max(numbers)
print("Die höchste Zahl in der Liste ist:", max_number)
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


