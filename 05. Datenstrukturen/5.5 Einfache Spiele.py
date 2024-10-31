#              _______________________
#       ______|                       |_____
#       \     |  5.5 EINFACHE SPIELE  |    /
#        )    |_______________________|   (
#       /________)                (________\       30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Listen sind besonders hilfreich, wenn es darum geht, mehrere ähnliche Elemente in
# einem Spiel zu speichern und zu verwalten. Hier sehen wir, wie Listen in einfachen
# Spielen verwendet werden können. Beispiele hierfür sind das Speichern von
# Wörterlisten oder das zufällige Auswählen von Elementen.


# _____________________________
#                             /
# Beispiel 1: Wort-Ratespiel (
# ____________________________\

# Im Wort-Ratespiel wählt der Computer zufällig ein Wort aus einer Liste, und der
# Spieler muss das Wort erraten, indem er Buchstaben eingibt. Für jeden falschen
# Buchstaben verliert der Spieler einen Versuch.

import random

# Wörterliste
words = ["apfel", "banane", "kirsche", "pfirsich", "traube"]
secret_word = random.choice(words)
guessed_letters = []
trials = 6

print("Willkommen zum Wort-Ratespiel!")
print("Du hast 6 Versuche, das geheime Wort zu erraten.\n")

while trials > 0:
    output = ""
    for letter in secret_word:
        if letter in guessed_letters:
            output += letter + " "
        else:
            output += "_ "

    print("Geheimes Wort:", output.strip())
    hint = input("Rate einen Buchstaben: ").lower()

    if hint in guessed_letters:
        print("Diesen Buchstaben hast du schon erraten!")

    elif hint in secret_word:
        guessed_letters.append(hint)
        print(f"Gut gemacht! '{hint}' ist im Wort.")

    else:
        trials -= 1
        print(f"Leider falsch! Du hast noch {trials} Versuche.")
    
    # Überprüfe, ob das Wort korrekt erraten wurde. 
    finished = True
    for letter in secret_word:
        if letter not in guessed_letters:
            finished = False
    
    if finished:
        print("\nHerzlichen Glückwunsch! Du hast das Wort erraten:", secret_word)
        break
    elif trials == 0:
        print("\nSchade, das Spiel ist vorbei. Das Wort war:", secret_word)




# _____________________________________
#                                     /
# Beispiel 2: Einfaches Memory-Spiel (
# ____________________________________\

# Im Memory-Spiel sollen gleiche Kartenpaare gefunden werden. In diesem Beispiel
# wird eine Liste mit Karten gemischt, und der Spieler muss Kartenpaare aufdecken.

karten = ["🍎", "🍌", "🍒", "🍇", "🍎", "🍌", "🍒", "🍇"]
random.shuffle(karten)  # Mische die Karten zufällig

print("\nWillkommen zum Memory-Spiel!")
print("Versuche, gleiche Kartenpaare zu finden.\n")

# Setze die verdeckten Karten mit '_'
verdeckte_karten = ["_" for _ in karten]
versuche = 0

while "_" in verdeckte_karten:
    for i, karte in enumerate(verdeckte_karten):
        print(f"{i}: {karte}", end="  ")
    print()

    try:
        # Wähle zwei Karten zum Aufdecken
        erste_auswahl = int(input("Wähle die erste Karte (Index): "))
        zweite_auswahl = int(input("Wähle die zweite Karte (Index): "))
    except ValueError:
        print("Bitte gib eine gültige Zahl ein.")
        continue

    if erste_auswahl == zweite_auswahl or \
       not (0 <= erste_auswahl < len(karten)) or \
       not (0 <= zweite_auswahl < len(karten)):
        print("Ungültige Auswahl. Versuche es erneut.")
        continue

    # Zeige die Karten, die ausgewählt wurden
    verdeckte_karten[erste_auswahl] = karten[erste_auswahl]
    verdeckte_karten[zweite_auswahl] = karten[zweite_auswahl]
    versuche += 1

    for i, karte in enumerate(verdeckte_karten):
        print(f"{i}: {karte}", end="  ")
    print()

    # Prüfe, ob die Karten gleich sind
    if karten[erste_auswahl] != karten[zweite_auswahl]:
        print("Leider kein Paar!")
        # Decke die Karten wieder zu
        verdeckte_karten[erste_auswahl] = "_"
        verdeckte_karten[zweite_auswahl] = "_"
    else:
        print("Paar gefunden!")

print(f"\nHerzlichen Glückwunsch! Du hast alle Paare in {versuche} Versuchen gefunden.")




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Listen eignen sich gut, um Spielobjekte wie Wörter oder Karten zu speichern.
#
# - Wir können mit `random.choice()` ein zufälliges Element aus einer Liste auswählen.
#
# - `random.shuffle()` mischt eine Liste zufällig – nützlich für Spiele wie Memory.


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Quiz mit fünf Fragen. Speichere die Fragen in eine Liste `questions`
# und die Antworten in eine Liste `answers`. Für jede korrekt beantwortete Frage
# erhält der Spieler einen Punkt. Für jede falsche Anwort wird ihm ein Punkt abgezogen. 


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein einfaches Blackjack-Spiel, bei dem der Spieler gegen den Computer antritt.
# Die Regeln sind vereinfacht:
# - Das Ziel ist es, so nah wie möglich an 21 Punkte zu kommen, ohne diese zu überschreiten.
#
# - Bildkarten (Bube, Dame, König) zählen als 10 Punkte, ein Ass kann als 1 oder 11 Punkte gezählt werden.
#
# - Der Spieler kann „ziehen“ oder „passen“, bis er entscheidet zu stoppen oder über 21 Punkte kommt.
#
# Hinweise:
# - Verwende eine Liste `deck`, die die Karten enthält.
#
# - Verwende Listen, um die Karten des Spielers und des Computers zu speichern.
#
# - Die Punktwerte der Karten können in einem Dictionary `card_values` gespeichert werden.
#
# - Nutze zufälliges Ziehen aus der Kartenliste für das Spiel.


# Füge hier deine Lösung ein.




#             _____
#            |A .  | _____
#            | /.\ ||A ^  | _____
#            |(_._)|| / \ ||A _  | _____
#   ejm98    |  |  || \ / || ( ) ||A_ _ |       Lass uns eine Runde spielen.
#            |____V||  .  ||(_'_)||( v )|
#                   |____V||  |  || \ / |
#                          |____V||  .  |
#                                 |____V|
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
#        


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Quiz mit fünf Fragen. Speichere die Fragen in eine Liste `questions`
# und die Antworten in eine Liste `answers`. Für jede korrekt beantwortete Frage
# erhält der Spieler einen Punkt. Für jede falsche Anwort wird ihm ein Punkt abgezogen. 


'''
# Fragen und Antworten definieren
questions = [
    "Was ist die Hauptstadt von Frankreich?",
    "Wie viele Planeten gibt es in unserem Sonnensystem?",
    "Welches Element hat das chemische Symbol 'O'?",
    "Wer hat die Relativitätstheorie entwickelt?",
    "In welchem Jahr begann der Zweite Weltkrieg?"
]

answers = [
    "Paris",
    "8",
    "Sauerstoff",
    "Einstein",
    "1939"
]

# Variablen für den Punktestand
score = 0

# Quiz starten
print("Willkommen zum Quiz! Du erhältst 1 Punkt für jede richtige Antwort und verlierst 1 Punkt bei jeder falschen Antwort.\n")

for i in range(len(questions)):
    # Frage stellen und Antwort einlesen
    print(f"Frage {i+1}: {questions[i]}")
    user_answer = input("Deine Antwort: ").strip()

    # Antworten vergleichen und Punktestand anpassen
    if user_answer.lower() == answers[i].lower():
        print("Richtig! +1 Punkt")
        score += 1
    else:
        print(f"Falsch! Die richtige Antwort ist: {answers[i]} -1 Punkt")
        score -= 1
    
    print(f"Aktueller Punktestand: {score}\n")

# Endpunktzahl anzeigen
print(f"Quiz beendet! Deine Endpunktzahl ist: {score}")
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein einfaches Blackjack-Spiel, bei dem der Spieler gegen den Computer antritt.
# Die Regeln sind vereinfacht:
# - Das Ziel ist es, so nah wie möglich an 21 Punkte zu kommen, ohne diese zu überschreiten.
#
# - Bildkarten (Bube, Dame, König) zählen als 10 Punkte, ein Ass kann als 1 oder 11 Punkte gezählt werden.
#
# - Der Spieler kann „ziehen“ oder „passen“, bis er entscheidet zu stoppen oder über 21 Punkte kommt.
#
# Hinweise:
# - Verwende eine Liste `deck`, die die Karten enthält.
#
# - Verwende Listen, um die Karten des Spielers und des Computers zu speichern.
#
# - Die Punktwerte der Karten können in einem Dictionary `card_values` gespeichert werden.
#
# - Nutze zufälliges Ziehen aus der Kartenliste für das Spiel.


'''
import random

# 1. Erstelle ein Deck aus Karten und definiere die Werte.
deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass"] * 4
card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "Bube": 10, "Dame": 10, "König": 10, "Ass": 11
}

# Mische das Deck
random.shuffle(deck)

# Funktion zur Punkteberechnung
def calculate_points(hand):
    points = sum(card_values[card] for card in hand)
    # Wenn Punkte über 21, aber ein Ass in der Hand ist, kann Ass auch als 1 gezählt werden
    aces = hand.count("Ass")
    while points > 21 and aces:
        points -= 10
        aces -= 1
    return points

# Funktion zum Kartenziehen
def draw_card(deck):
    return deck.pop() if deck else None

# Hauptspiel
def blackjack():
    player_hand = [draw_card(deck), draw_card(deck)]
    computer_hand = [draw_card(deck), draw_card(deck)]
    
    while True:
        print(f"\nDeine Karten: {player_hand} - Punkte: {calculate_points(player_hand)}")
        action = input("Möchtest du ziehen oder passen? (z/p): ").strip().lower()
        
        if action == "z":
            player_hand.append(draw_card(deck))
            if calculate_points(player_hand) > 21:
                print(f"\nDeine Karten: {player_hand} - Punkte: {calculate_points(player_hand)}")
                print("Du hast überzogen! Der Computer gewinnt.")
                return
        elif action == "p":
            break
        else:
            print("Ungültige Eingabe. Bitte wähle 'ziehen' oder 'passen'.")

    # Zug des Computers
    while calculate_points(computer_hand) < 17:
        computer_hand.append(draw_card(deck))
    
    # Ergebnis anzeigen
    player_points = calculate_points(player_hand)
    computer_points = calculate_points(computer_hand)
    print(f"\nEndstand - Deine Punkte: {player_points}, Computer Punkte: {computer_points}")
    print(f"Deine Karten: {player_hand}")
    print(f"Computer Karten: {computer_hand}")
    
    if computer_points > 21 or player_points > computer_points:
        print("Herzlichen Glückwunsch, du hast gewonnen!")
    elif player_points < computer_points:
        print("Der Computer hat gewonnen!")
    else:
        print("Unentschieden!")

# Spiel starten
blackjack()
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

