#              ____________________________________
#       ______|                                    |_____
#       \     |    14.2 MEHRZEILIGES NIM SPIEL     |    /
#        )    |____________________________________|   (
#       /________)                             (________\     1.12.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Nim mit mehreren Stapeln erweitert die Strategien und erfordert ein besseres 
# Verständnis der Spielmechanik. Spieler können nun von beliebigen Stapeln Objekte 
# entfernen. Die optimale Strategie wird komplexer, und der Gewinner hängt davon ab, 
# wie gut der Spieler oder die KI die Situation analysiert.

# Dieses Kapitel zeigt, wie ein mehrzeiliges Nim-Spiel in Python implementiert wird.
# Du lernst, wie mehrere Stapel verwaltet werden, und entwickelst Strategien, 
# um das Spiel zu gewinnen.




# ________________________________
#                                /
# Regeln von mehrzeiligem Nim   (
# _______________________________\

# - Es gibt mehrere Stapel mit einer bestimmten Anzahl von Objekten.
#
# - Zwei Spieler ziehen abwechselnd Objekte von einem beliebigen Stapel.
#
# - Der Spieler, der das letzte Objekt nimmt, gewinnt.
#
# - Die optimale Strategie hängt davon ab, die Stapel so zu verändern, dass die
#   Nim-Summe null wird.




# _______________________
#                       /
# Implementierung       (
# ______________________\

# Der folgende Code zeigt die grundlegende Implementierung eines mehrzeiligen Nim-Spiels.
# Spieler und KI können wählen, von welchem Stapel sie Objekte entfernen möchten.

import random


# Funktion für das mehrzeilige Nim-Spiel
def nim_multiline_game():
    print("Willkommen zu Mehrzeiligem Nim!\n")
    print("Regeln: Wähle einen Stapel und entferne 1 bis 3 Objekte.")
    print("Der Spieler, der das letzte Objekt nimmt, verliert.\n")
    
    # Erstelle mehrere Stapel mit zufälligen Größen
    piles = [random.randint(5, 10) for _ in range(3)]
    
    # Spielschleife
    while True:
        # Spielerzug
        player_pile, player_move = player_turn_multiline(piles)
        piles[player_pile] -= player_move
        
        print(f"Du hast {player_move} Objekte vom Stapel {player_pile + 1} genommen.")
        if all(pile == 0 for pile in piles):
            print("Du hast das letzte Objekt genommen. Du gewinnst!")
            return "Spieler"

        # KI-Zug
        print(f"\nAktuelle Stapel: {piles}")
        ai_pile, ai_move = ai_random(piles)
        piles[ai_pile] -= ai_move
        
        print(f"Die KI nimmt {ai_move} Objekte vom Stapel {ai_pile + 1}.")
        if all(pile == 0 for pile in piles):
            print("Die KI hat das letzte Objekt genommen. Du verlierst!")
            return "KI"


# Spielerzug für mehrzeiliges Nim
def player_turn_multiline(piles):
    while True:
        try:
            print(f"\nAktuelle Stapel: {piles}")
            pile = int(input(f"Wähle einen Stapel (1-{len(piles)}): ")) - 1
            if pile < 0 or pile >= len(piles) or piles[pile] == 0:
                print("Ungültige Wahl. Wähle einen Stapel, der nicht leer ist.")
                continue
            
            move = int(input(f"Wie viele Objekte möchtest du nehmen (1-{piles[pile]})? "))
            if move < 1 or move > piles[pile]:
                print("Ungültige Eingabe. Wähle eine Zahl zwischen 1 und 3, die im Stapel verfügbar ist.")
            else:
                return pile, move
            
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")


# KI-Zug mit optimaler Strategie für mehrzeiliges Nim
def ai_random(piles):
    while True:
        pile = random.randint(0, len(piles) - 1)
        if piles[pile] > 0:
            move = random.randint(1, min(3, piles[pile]))
            return pile, move


# Hauptprogramm: Mehrere Runden spielen
score = {"Spieler": 0, "KI": 0}
round = 1
while round <= 2:
    winner = nim_multiline_game()
    score[winner] += 1
    
    print(f"\nPUNKTESTAND Runde {round}")
    for name, points in score.items():
        print(f"{name}: {points}")
        
    print()
    round += 1



# ___________________
#                   /
# Nim-Summe        (
# __________________\

# Die Nim-Summe ist das zentrale Konzept, um das mehrzeilige Nim-Spiel zu analysieren
# und optimale Strategien zu entwickeln. Sie wird berechnet, indem man die Anzahl 
# der Objekte in allen Stapeln bitweise mit XOR (^) verknüpft.
#
# Beispiel:
#
# Stapel: [3, 4, 5]
# Nim-Summe: 3 ^ 4 ^ 5 = 2 (binär: 011 ^ 100 ^ 101 = 010)
#
#
# XOR-Operation
# -------------
#   0 ^ 0 = 0
#   0 ^ 1 = 1
#   1 ^ 0 = 1
#   1 ^ 1 = 0
# 
#
# Regel
# -----
# - Wenn die Nim-Summe 0 ist, befindet sich der Spieler in einer verlierenden 
#   Position, vorausgesetzt, der Gegner spielt optimal.
# 
# - Wenn die Nim-Summe ungleich 0 ist, kann der Spieler in eine gewinnbringende 
#   Position wechseln, indem er einen Stapel so verändert, dass die Nim-Summe 0 wird.
#
#
# Begründung
# ----------
# Wenn die Nim-Summe 0 ist, bedeutet das, dass die Stapel in einer "symmetrischen" 
# Anordnung sind, die der Gegner nutzen kann, um den Spieler in eine verlierende 
# Position zu bringen.



# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# In diesem Kapitel hast du gelernt, wie du ein mehrzeiliges Nim-Spiel implementierst:
#
# 1. Regeln: Spieler entfernen abwechselnd Objekte von einem beliebigen Stapel.
#    Der Spieler, der das letzte Objekt nimmt, gewinnt.
#
# 2. Spielstrategie: Die optimale Strategie basiert auf der Nim-Summe.
#    Wenn die Nim-Summe 0 ist, befindet sich der Spieler in einer verlierenden Position.
#
# 3. KI-Entwicklung: Die KI nutzt die Nim-Summe, um den Stapel so zu verändern,
#    dass die Nim-Summe 0 wird. Dadurch wird der Gegner in eine verlierende Position gebracht.
#




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine Funktion `ai_optimal(piles)`, welche eine KI enhalt. Sie soll die 
# Stapel so zu verändern, dass die Nim-Summe 0 wird. Dadurch wird der Gegner in 
# eine verlierende Position gebracht.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Simuliere 100 Spiele zwischen der zufälligen KI (`ai_random`) und
# der optimalen KI (`ai_optimal`). Berechne den Punktestand.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erweiterung: Ändere die Regeln so, dass der Spieler, der das letzte Objekt 
# nimmt, verliert. Passe die KI-Strategien entsprechend an.

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
#                             |___/            


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine Funktion `ai_optimal(piles)`, welche eine KI enhalt. Sie soll die 
# Stapel so zu verändern, dass die Nim-Summe 0 wird. Dadurch wird der Gegner in 
# eine verlierende Position gebracht.

'''
def ai_optimal_multiline(piles):
    nim_sum = 0
    for pile in piles:
        nim_sum ^= pile  # Berechne die Nim-Summe
    
    if nim_sum == 0:
        # Zufälliger Zug, wenn die KI in einer verlierenden Position ist
        while True:
            pile = random.randint(0, len(piles) - 1)
            if piles[pile] > 0:
                move = random.randint(1, min(3, piles[pile]))
                return pile, move
    else:
        # Optimaler Zug: Stapel finden, der die Nim-Summe auf 0 bringt
        for i, pile in enumerate(piles):
            target = pile ^ nim_sum
            if target < pile:
                return i, pile - target
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Simuliere 100 Spiele zwischen der zufälligen KI (`ai_random`) und
# der optimalen KI (`ai_optimal`). Berechne den Punktestand.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erweiterung: Ändere die Regeln so, dass der Spieler, der das letzte Objekt 
# nimmt, verliert. Passe die KI-Strategien entsprechend an.

# Füge hier deine Lösung ein.





# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><
