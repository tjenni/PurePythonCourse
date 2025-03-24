#              ___________________________________
#       ______|                                   |_____
#       \     | 3.4 SCHLEIFEN UND EINFACHE SPIELE |    /
#        )    |___________________________________|   (
#       /________)                            (________\

# Schleifen sind besonders nützlich für einfache, interaktive Spiele, bei denen
# der Benutzer wiederholt Eingaben machen kann. Hier werden wir zwei einfache
# Spiele programmieren: ein „Zahlenraten“-Spiel und das klassische „Schere, Stein, Papier“.


# ___________________________
#                           /
# Zahlenraten              (
# __________________________\

# Im Zahlenratenspiel denkt sich der Computer eine Zahl zwischen 1 und 100 aus,
# und der Benutzer hat mehrere Versuche, die Zahl zu erraten. Nach jedem Versuch
# gibt das Programm Feedback, ob die gesuchte Zahl größer oder kleiner ist.

import random

# Eine Zufallszahl zwischen 1 und 100
secret_number = random.randint(1, 100)
trials = 0

print("Willkommen beim Zahlenraten!")
print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Kannst du sie erraten?")

while True:
    number = int(input("Gib eine Zahl ein: "))
    trials += 1

    if number < secret_number:
        print("Zu klein!")
    elif number > secret_number:
        print("Zu groß!")
    else:
        print(f"Glückwunsch! Du hast die Zahl in {trials} Versuchen erraten.")
        break




# ____________________________
#                            /
# Schere, Stein, Papier     (
# ___________________________\

# Das Spiel „Schere, Stein, Papier“ ist ein klassisches Spiel, bei dem der Benutzer
# eine Auswahl trifft und gegen den Computer spielt. Hier verwenden wir eine Schleife,
# damit das Spiel immer wieder gespielt werden kann, bis der Benutzer „Nein“ eingibt.

options = ["Schere", "Stein", "Papier"]

print("\nWillkommen bei Schere, Stein, Papier!")
print("Du spielst gegen den Computer.")

while True:
    player = input("Wähle Schere, Stein oder Papier: ")
    computer = random.choice(options)

    print(f"Computer wählt: {computer}")

    if player == computer:
        print("Unentschieden!")
    elif (player == "Schere" and computer == "Papier") or \
         (player == "Stein" and computer == "Schere") or \
         (player == "Papier" and computer == "Stein"):
        print("Du gewinnst!")
    else:
        print("Computer gewinnt!")

    again = input("Möchtest du nochmal spielen? (ja/nein): ").lower()
    if again != "ja":
        print("Danke fürs Spielen!")
        break




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Eine `while`-Schleife ermöglicht, dass das Spiel solange läuft, bis eine
#   Bedingung erfüllt ist.
#
# - Schleifen eignen sich besonders für interaktive Programme, die mehrere
#   Versuche oder Wiederholungen erfordern.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/

# Erstelle ein Mathematik-Quiz.

# In diesem Quiz stellt der Computer dem Benutzer eine Serie einfacher mathematischer
# Fragen. Der Benutzer soll Antworten eingeben, und das Spiel zeigt am Ende die Anzahl
# der richtigen Antworten an. Jede Frage ist zufällig und kann eine Addition,
# Subtraktion, Multiplikation oder Division beinhalten.


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

# Erstelle ein Mathematik-Quiz.

# In diesem Quiz stellt der Computer dem Benutzer eine Serie einfacher mathematischer
# Fragen. Der Benutzer soll Antworten eingeben, und das Spiel zeigt am Ende die Anzahl
# der richtigen Antworten an. Jede Frage ist zufällig und kann eine Addition,
# Subtraktion, Multiplikation oder Division beinhalten.

'''
import random

questions = 5
points = 0

print("Willkommen zum Math Quiz!")
print("Du bekommst 5 zufällige Mathematikfragen. Versuche sie korrekt zu beantworten.\n")

for i in range(questions):
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)

    operation = random.choice(["+", "-", "*", "/"])

    if operation == "+":
        solution = number1 + number2
        question = f"{number1} + {number2} = "

    elif operation == "-":
        solution = number1 - number2
        question = f"{number1} - {number2} = "

    elif operation == "*":
        solution = number1 * number2
        question = f"{number1} * {number2} = "

    else:
        solution = round(number1 / number2, 2)
        question = f"{number1} / {number2} = (auf zwei Dezimalstellen gerundet) "

    answer = float(input(question))

    if antwort == solution:
        points += 1
        print("Richtig!")
    else:
        print(f"Falsch. Die richtige Antwort ist {correct}.")

print(f"\nQuiz beendet! Du hast {points} von {questions} Fragen richtig beantwortet.")
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><
