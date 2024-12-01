#              __________________________________
#       ______|                                  |_____
#       \     |    14.1 EINZEILIGES NIM SPIEL    |    /
#        )    |__________________________________|   (
#       /________)                           (________\     1.12.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Nim ist ein einfaches Strategiespiel, bei dem zwei Spieler abwechselnd Objekte
# von einem oder mehreren Stapeln entfernen. Das Ziel ist es, entweder das letzte
# Objekt zu nehmen (Standardvariante) oder es zu vermeiden (Misère-Variante).

# Dieses Kapitel führt in die Regeln von Nim ein und zeigt, wie das Spiel
# mit Python und Arcade implementiert werden kann. Am Ende kannst du das Spiel
# Schritt für Schritt erweitern, z. B. um eine künstliche Intelligenz (KI) mit
# Strategien zur optimalen Spielweise zu integrieren.


# __________________________
#                          /
# Regeln von Nim          (
# _________________________\

# - Zu Beginn gibt es einen oder mehrere Stapel mit einer bestimmten Anzahl von Objekten.
#
# - Zwei Spieler ziehen abwechselnd 1 bis 3 Objekte (oder mehr, abhängig von den Regeln)
#   von einem der Stapel.
#
# - Der Spieler, der das letzte Objekt nimmt, gewinnt (Standardvariante).
#
# - Das Spiel endet, wenn alle Objekte genommen wurden.


# _______________________
#                       /
# Implementierung      ( 
# ______________________\

# Der folgende Code zeigt die grundlegende Implementierung eines einfachen Nim-Spiels
# mit einem Stapel. Das Spiel wird in der Konsole gespielt. 


import random


# Ein einfaches Nim-Spiel mit einem Stapel, bei dem zwei Spieler abwechselnd
# 1 bis 3 Objekte ziehen. Der Spieler, der das letzte Objekt nimmt, verliert.
def nim_game():

    print("Willkommen zu Nim!\n")
    print("Regeln: Nehme 1, 2 oder 3 Objekte vom Stapel.")
    print("Der Spieler, der das letzte Objekt nimmt, verliert.\n")
    
    # Anzahl der Objekte auf dem Stapel
    pile = random.randint(10, 20)
    
    # Spielschleife
    while True:
        
        # Spielerzug
        player_move = player_turn(pile)
        pile -= player_move
        
        print(f"Du hast {player_move} Objekte genommen.")
        if pile == 0:
            print("Du hast das letzte Objekt genommen. Du gewinnst!")
            return "Spieler"

        # KI-Zug
        print(f"\nEs bleiben {pile} Objekte.")
        
        ai_move = ai_random(pile)
        pile -= ai_move
        
        print(f"Die KI nimmt {ai_move} Objekte.")
        if pile == 0:
            print("Die KI hat das letzte Objekt genommen. Du verlierst!")
            return "KI"
        
        

# Führt den Zug des Spielers aus. Der Spieler wählt, wie viele Objekte er nehmen möchte.
def player_turn(pile):
    while True:
        try:
            print(f"\nEs bleiben {pile} Objekte.")
            move = int(input("Wie viele Objekte möchtest du nehmen (1-3)? "))
            if move < 1 or move > 3 or move > pile:
                print("Ungültige Eingabe. Wähle eine Zahl zwischen 1 und 3, die im Stapel verfügbar ist.")
            else:
                return move
            
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")



# Führt den Zug der KI aus. In dieser einfachen Version wählt die KI zufällig
# eine Anzahl von Objekten (1-3), die im Stapel verfügbar sind.
def ai_random(pile):
    move = random.randint(1, min(3, pile))
    return move



# Hauptprogramm
score = {"Spieler":0, "KI":0}
round  = 1
while round <= 10:
    winner = nim_game()
    
    score[winner]+=1
    
    print(f"\nPUNKTESTAND Runde {round}")
    for name, points in score.items():
        print(f"{name}: {points}")
        
    print()
    
    round += 1
    



# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# In diesem Kapitel hast du die grundlegenden Strategien und Regeln von Nim gelernt:
#
# 1. Spielregeln: Spieler entfernen abwechselnd Objekte, und derjenige, der das letzte
#    Objekt nimmt, verliert.
#
# 2. Spielstrategie: Eine optimale Strategie kann sicherstellen, dass der Gegner verliert,
#    wenn der Stapel immer auf ein Vielfaches von 4 + 1 reduziert wird.
#
# 3. KI-Entwicklung: Der Unterschied zwischen einer zufälligen KI und einer optimalen
#    Strategie zeigt die Bedeutung von Algorithmik und Logik in Spielen.
#
# Mit diesen Grundlagen kannst du das Spiel erweitern und anspruchsvollere Mechaniken
# wie mehrere Stapel (siehe nächstes Kapitel) oder eine grafische Oberfläche hinzufügen.


# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Schreibe eine Funktion `ai_optimal(pile)`, welche möglichst optimale 
# Spielzüge spielt. 

# Hinweis: Wenn man es schafft, den Stapel auf ein Vielfaches von 4 Objekten zu
# bringen (4, 8, 12, ...) , gewinnt man das Spiel auf sicher. 

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Lass die random-KI mehrere Runden gegen deine KI aus Aufgabe 1 spielen.
# Bestimme den Punktestand nach 100 Spielen.

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
# Schreibe eine Funktion `ai_optimal(pile)`, welche möglichst optimale 
# Spielzüge spielt. 

# Hinweis: Wenn es schafft, den Stapel auf ein Vielfaches von 4 + 1 Objekten zu
# bringen, gewinnt man das Spiel auf sicher. 

'''
def ai_optimal(pile):
    
    move = pile % 4
    
    if move == 0:
        move = random.randint(1,3)
        move = min(move, pile)
    
    return move
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Lass die random-KI mehrere Runden gegen deine KI aus Aufgabe 1 spielen.
# Bestimme den Punktestand nach 100 Spielen.

'''
def nim_game():
    ...

    while True:
        
        # Spielerzug
        player_move = ai_optimal(pile)

'''
# Wenn du das Programm laufen lässt, wird die optimale KI fast alle Spiele gegen
# die zufällige KI gewinnen.  


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><



