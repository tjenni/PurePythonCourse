#              __________________________
#       ______|                          |_____
#       \     |    14.3 TIC-TAC-TOE      |    /
#        )    |__________________________|   (
#       /________)                   (________\     8.12.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Tic-Tac-Toe, auch bekannt als „Kreis und Kreuz“, ist eines der bekanntesten
# Strategiespiele der Welt. Es bietet eine einfache Möglichkeit, grundlegende
# Konzepte wie Zuglogik, Siegbedingungen und künstliche Intelligenz (KI) zu
# implementieren.

# In diesem Kapitel lernst du, wie du Tic-Tac-Toe in Python umsetzt. Wir starten
# mit einer textbasierten Version des Spiels und erweitern sie, um einfache
# KI-Strategien hinzuzufügen.


# _____________________________
#                             /
# Regeln von Tic-Tac-Toe     (
# ____________________________\

# - Tic-Tac-Toe wird auf einem 3x3-Gitter gespielt.
#
# - Zwei Spieler (X und O) setzen abwechselnd ihre Markierungen auf leere Felder.
#
# - Ziel ist es, eine horizontale, vertikale oder diagonale Linie mit drei
#   eigenen Markierungen zu bilden.
#
# - Das Spiel endet unentschieden, wenn alle Felder belegt sind und kein Spieler
#   eine Linie bilden konnte.



# _____________________________
#                             /
# Kodierung des Spielfelds   (
# ____________________________\

# In unserem Tic-Tac-Toe-Spiel werden die Spieler und das Spielfeld wie folgt kodiert:

#  1  : Die künstliche Intelligenz (O)
# -1  : Der menschliche Spieler (X)
#  0  : Ein leeres Feld

# Diese Zahlenwerte haben mehrere Vorteile:

# 1. Mathematische Verarbeitung:
#    Gewinnkombinationen lassen sich leicht überprüfen, da ihre Summe eindeutig ist.
#    Beispiel: Drei aufeinanderfolgende 1-Werte ergeben 3 (KI gewinnt),
#    während drei (-1)-Werte -3 ergeben (Spieler gewinnt).

# 2. Kompakte Darstellung:
#    Das Spielfeld wird als Liste von Listen gespeichert, was speichereffizient ist
#    und gut in Schleifen verarbeitet werden kann.

# 3. Flexibilität:
#    Diese Kodierung lässt sich problemlos auf größere Spielfelder erweitern,
#    z. B. für ein 4x4- oder 5x5-Spiel.

# Beispiel: Eine Spielsituation wird wie folgt kodiert:
'''
board = [
    [1, -1,  0],
    [0,  1,  0],
    [-1,  0,  1]
]
'''
# Diese Matrix repräsentiert das Spielfeld:
# X | O |  
# --+---+--
#   | X |  
# --+---+--
# O |   | X

# Hinweis:
# Um diese interne Kodierung für den Benutzer verständlich zu machen,
# wird die Spielfeldanzeige durch die Funktion `print_board` so angepasst,
# dass die Zahlenwerte wie folgt übersetzt werden:
#   -  1  → "O"
#   - -1  → "X"
#   -  0  → " " (leeres Feld)



# _____________________________
#                              /
# Implementierung des Spiels  (
# _____________________________\

# Im folgenden Beispiel wird Tic-Tac-Toe in der Konsole gespielt. Ein Spieler
# tritt gegen eine einfache KI an, die zufällig gültige Züge auswählt.
# Das Spielfeld wird durch eine Liste von Listen 


import random


DEFAULT_SYMBOLS = {1: "O", 0: " ", -1: "X"}
AI_ID = 1
PLAYER_ID = -1


def print_board(board, symbols=DEFAULT_SYMBOLS):
    """Gibt das Tic-Tac-Toe-Spielfeld formatiert auf der Konsole aus."""
    row_separator = "-" * (len(board[0]) * 4 - 1)

    # Erzeuge den auszugebenden Text für das Brett
    rows = []
    for i, row in enumerate(board):
        row_text = "|".join(f" {symbols[cell]} " for cell in row)
        if i < len(board) - 1:
            row_text += "\n" + row_separator
        rows.append(row_text)

    output = "\n".join(rows)
    print("\n" + output + "\n")
            


def check_winner(board):
    """Prüft, ob ein Spieler gewonnen hat und gibt den Gewinner zurück."""

    # Wir schauen uns jede Zeile und jede Spalte an, ob die Summe der 
    # drei Felder dort 3 oder -3 ist.
    #   - Eine Summe von 3 bedeutet drei O-Felder (1+1+1=3), also hat O gewonnen.
    #   - Eine Summe von -3 bedeutet drei X-Felder (-1-1-1=-3), also hat X gewonnen.
    for i in range(3):
        # Zeilen überprüfen
        if abs(board[i][0] + board[i][1] + board[i][2]) == 3:
            return board[i][0]
        # Spalten überprüfen
        if abs(board[0][i] + board[1][i] + board[2][i]) == 3:
            return board[0][i]

    # Diagonalen überprüfen
    if abs(board[0][0] + board[1][1] + board[2][2]) == 3:
        return board[0][0]
    if abs(board[0][2] + board[1][1] + board[2][0]) == 3:
        return board[0][2]

    return 0



def player_turn(board, id=PLAYER_ID):
    """Lässt den Spieler einen Zug machen, indem er eine Zahl (1-9) eingibt."""
    while True:
        try:
            move = int(input("Wähle ein Feld (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == 0:
                board[row][col] = id
                return
            else:
                print("Dieses Feld ist bereits belegt. Wähle ein anderes.")
        except (ValueError, IndexError):
            print("Ungültige Eingabe. Bitte gib eine Zahl zwischen 1 und 9 ein.")



def ai_random(board, id=AI_ID, verbose=True):
    """Funktion für die zufällige KI"""
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == 0:
            board[row][col] = id
            if verbose:
                print(f"Die KI wählt Feld {row * 3 + col + 1}.")
            return



def tic_tac_toe(symbols=DEFAULT_SYMBOLS):
    """Führt ein Tic-Tac-Toe-Spiel durch."""

    # Spielfeld initialisieren
    board = [[0,0,0],[0,0,0],[0,0,0]]

    print("Tic-Tac-Toe")
    print("===========")
    print(f"Spieler ist '{symbols[-1]}', KI ist '{symbols[1]}'.")
    print("Das Spielfeld hat folgende Nummerierung:\n")
    
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    
    # Spielschleife
    for turn in range(9):
        print(f"\nZug {turn+1}")
        print_board(board, symbols)

        if turn % 2 == 0:
            player_turn(board)
        else:
            ai_random(board)

        winner = check_winner(board)
        if winner:
            print_board(board, symbols)
            if winner == 1:
                print(f"{symbols[1]} hat gewonnen!")
            else:
                print(f"{symbols[-1]} hat gewonnen!")
            
            return winner

    print_board(board, symbols)
    print("Das Spiel endet unentschieden.")
    return 0



def simulate_player_vs_random(rounds=10):
    """Simulation mehrer Runden."""

    score = {"Spieler": 0, "KI": 0, "Unentschieden": 0}
    for game in range(rounds):
        result = tic_tac_toe()
        
        if result == 1:
            score["KI"] += 1
        elif result == -1:
            score["Spieler"] += 1
        else:
            score["Unentschieden"] += 1

        print(f"\nErgebnisse nach Runde {game+1}:")
        for name, punkte in score.items():
            print(f"{name}: {punkte}")
        print()



# Hauptprogramm starten
if __name__ == "__main__":
    simulate_player_vs_random()




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# In diesem Kapitel hast du gelernt, wie man Tic-Tac-Toe umsetzt:
#
# 1. Regeln und Spielablauf: 
#    Spieler und KI setzen abwechselnd Markierungen auf ein 3x3-Gitter.
#
# 2. Textbasierte Implementierung: 
#    Du hast ein simples Tic-Tac-Toe-Spiel in der Konsole erstellt.
#
# 3. Spielmechaniken: 
#    Funktionen zur Spieler- und KI-Interaktion, zur Spielfeldanzeige und zur Siegprüfung.

# Tic-Tac-Toe bietet eine ideale Grundlage, um KI-Konzepte wie den Minimax-Algorithmus 
# zu erlernenund Strategien für optimale Spielweisen zu entwickeln. Mit diesen Grundlagen 
# kannst du das Spiel erweitern und anpassen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Schreibe eine Funktion `choose_side()`, mit der der Spieler auswählen kann, 
# ob er als 'X' oder als 'O' spielen möchte. Verwende diese Funktion vor dem Start 
# des Spiels, um festzulegen, wer zuerst zieht.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Füge nach jedem Spiel eine Ausgabe hinzu, in der die Gesamtanzahl der 
# gespielten Züge angezeigt wird. So kann der Spieler am Ende sehen, 
# wie lange die Partie gedauert hat.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Implementiere eine Funktion `simulate_random_vs_random(n)`, die `n` Spiele ohne 
# Benutzereingabe durchführt (zum Beispiel KI gegen KI) und am Ende eine 
# Statistik der Gewinne, Niederlagen und Unentschieden ausgibt. Lasse dabei 
# die Minimax-KI gegen sich selbst oder gegen eine andere Strategie spielen. 
# Bestimme, wie sich die Ergebnisse im Vergleich zu einer kleineren oder 
# größeren Anzahl von Spielen verändern.


# Füge hier deine Lösung ein.





#             X oder O ....
#                       \
#                            ,,,,,,
#                           /e   ''(
#                          (_ `     \
#                         ___>       \
#                        / ,_\-.___   \_
#                       /  _)/ /        \
#                       |  \  /  ` _     |
#                     __\____/    /    ' |
#                    /  _        /______/
#                   / _/ \,_____/o     (
#                   \__)/`              \
#                      /   \__________/_/_
#                    _/     \  \   )/     \
#                   /      /   |  /\      (
#                   \_____/ ___/  \ \  _/  \
#              ______/_/___|_|     ) \     /
#             /       o\     o\   /  /    /\
#     b'ger,,,'-----^--',,,,,,',,|_,,\_ ,,\/,,
#
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
# Schreibe eine Funktion `choose_side()`, mit der der Spieler auswählen kann, 
# ob er als 'X' oder als 'O' spielen möchte. Verwende diese Funktion vor dem Start 
# des Spiels, um festzulegen, wer zuerst zieht.


'''
def choose_side():
    while True:
        side = input("Möchtest du als 'X' oder als 'O' spielen? ").upper()
        if side in ['X', 'O']:
            print(f"Du spielst als '{side}'.")
            if side == 'X':
                return {1: "O", 0: " ", -1: "X"}
            else:
                return {1: "X", 0: " ", -1: "O"}
        else:
            print("Ungültige Eingabe. Bitte gib 'X' oder 'O' ein.")


def tic_tac_toe():
    ...
    symbols = choose_side()

'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Füge nach jedem Spiel eine Ausgabe hinzu, in der die Gesamtanzahl der 
# gespielten Züge angezeigt wird. So kann der Spieler am Ende sehen, 
# wie lange die Partie gedauert hat.


'''
def tic_tac_toe():
    ...

    winner = check_winner(board)
        if winner:
            print_board(board, symbols)

            print(f"Anzahl Spielzüge: {turn+1}")
            
            if winner == 1:
                print(f"{symbols[1]} hat gewonnen!")
            else:
                print(f"{symbols[-1]} hat gewonnen!")
                
            return winner

    print_board(board, symbols)
    
    print(f"Anzahl Spielzüge: {turn+1}")
    
    print("Das Spiel endet unentschieden.")
    return 0
    
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Implementiere eine Funktion `simulate_random_vs_random(n)`, die `n` Spiele ohne 
# Benutzereingabe durchführt (zum Beispiel KI gegen KI) und am Ende eine 
# Statistik der Gewinne, Niederlagen und Unentschieden ausgibt. Lasse dabei 
# die Minimax-KI gegen sich selbst oder gegen eine andere Strategie spielen. 
# Bestimme, wie sich die Ergebnisse im Vergleich zu einer kleineren oder 
# größeren Anzahl von Spielen verändern.


'''
def tic_tac_toe_random_vs_random(symbols=DEFAULT_SYMBOLS):
    
    board = [[0,0,0],[0,0,0],[0,0,0]]
    
    for turn in range(9):
        if turn % 2 == 0:
            ai_random(board, AI_ID, False)
        else:
            ai_random(board, PLAYER_ID, False)

        winner = check_winner(board)
        if winner:
            return winner

    return 0



def simulate_random_vs_random(rounds=100):
    """Simulation mehrer Runden."""

    score = {"KI O": 0, "KI X": 0, "Unentschieden": 0}
    for game in range(rounds):
        result = tic_tac_toe_random_vs_random()
        
        if result == AI_ID:
            score["KI O"] += 1
        elif result == PLAYER_ID:
            score["KI X"] += 1
        else:
            score["Unentschieden"] += 1

        print(f"\nErgebnisse nach Runde {game+1}:")
        for name, punkte in score.items():
            print(f"{name}: {punkte}")
        print()



# Hauptprogramm starten
if __name__ == "__main__":
    simulate_random_vs_random()

'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

