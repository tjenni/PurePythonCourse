#              _________________________________________
#       ______|                                         |_____
#       \     |   14.4 MINIMAX ALGORITHMUS - Teil 1     |    /
#        )    |_________________________________________|   (
#       /________)                                  (________\     5.12.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Der Minimax-Algorithmus ist eine Methode der Entscheidungsfindung in Spielen mit zwei
# Spielern, die sich abwechseln. Er analysiert alle möglichen Züge und versucht, den
# optimalen Zug zu finden, indem er die Züge des Gegners vorhersieht. In Tic-Tac-Toe 
# kann der Minimax-Algorithmus verwendet werden, um eine unbesiegbare KI zu erstellen.


# ________________________
#                        /
# Funktionsweise         (
# ________________________\

# 1. Ziel: 
#    - Der Algorithmus maximiert die Punkte für den eigenen Spieler (Maximizer) und
#      minimiert die Punkte für den Gegner (Minimizer).

# 2. Bewertung:
#    - Gewinnt der Maximizer, wird ein positiver Wert zurückgegeben (z. B. +10).
#    - Gewinnt der Minimizer, wird ein negativer Wert zurückgegeben (z. B. -10).
#    - Ein Unentschieden wird mit 0 bewertet.

# 3. Rekursion: 
#    - Der Algorithmus simuliert alle möglichen Züge, bewertet deren Ergebnis und wählt
#      den Zug mit der besten Bewertung.

# 4. Optimierung: 
#    - Mithilfe von Alpha-Beta-Pruning kann der Algorithmus effizienter gestaltet werden,
#      indem unnötige Züge ausgeschlossen werden, siehe nächstes Kapitel.




# ____________________________________
#                                    /
# Erklärung des Minimax-Algorithmus (
# ___________________________________\

# Der Minimax-Algorithmus ist eine rekursive Methode zur Entscheidungsfindung:
#
# - Rekursion: Simuliert alle möglichen Züge und geht tiefer in das Spiel, 
#   bis ein Endzustand (Gewinn, Verlust, Unentschieden) erreicht wird.
#
# - Bewertung: Jeder Endzustand wird mit einer Punktzahl bewertet:
#    - Gewinn für die KI: +10
#    - Gewinn für den Spieler: -10
#    - Unentschieden: 0
#
# - Maximierung und Minimierung: 
#    - Die künstliche Intelligenz KI (Maximizer) versucht, die Punktzahl zu maximieren.
#    - Der Spieler (Minimizer) versucht, die Punktzahl der KI zu minimieren.

# Betrachten wir ein Beispiel: Die KI spielt `O` und ist am Zug.
# Das Brett sieht aktuell wie folgt aus: 
# 
# Start)
#  X | O | O  
# -----------
#  O | X | 
# -----------
#  X |   |  
# 
# Die KI `O` simuliert alle möglichen Züge für die freien Felder.
# 
# 1)              2)              3)
#    X | O | O       X | O | O       X | O | O  
#   -----------     -----------     -----------
#    O | X | O       O | X |         O | X |   
#   -----------     -----------     -----------
#    X |   |         X | O |         X |   | O
# 
# Ausgehend von diesen drei Zügen, ergeben sich dann für X die folgenden 
# sechs Möglichkeiten:
#
# 1.1)            1.2)                       
#    X | O | O       X | O | O 
#   -----------     -----------
#    O | X | O       O | X | O 
#   -----------     -----------
#    X | X |         X |   | X 
#
# 2.1)            2.2)           
#    X | O | O       X | O | O
#   -----------     -----------
#    O | X | X       O | X |   
#   -----------     -----------
#    X | O |         X | O | X 
#
# 3.1)            3.2)           
#    X | O | O       X | O | O 
#   -----------     -----------
#    O | X | X       O | X |   
#   -----------     -----------
#    X |   | O       X | X | O 
#
# Bewertung:
#
# - Die Züge 1.1), 3.2) bringen für die KI `O` den sicheren Gewinn. 
#   Sie werden daher mit +10 bewertet.
#
# - Die Züge 1.2), 2.2)bringen für den Spieler `X` den Gewinn. Sie 
#   werden mit -10 bewertet.
# 
# - Die Züge 2.1), 3.1) führen zu einem Unentschieden und ergeben 0 Punkte.


# Der Spielbaum
# =============

# Man kann sich ein Tic-Tac-Toe-Spiel als einen Baum vorstellen. 
# Die KI rechnet alle Spielzüge durch und bewertet dann jeden Zug. 
# Das Spiel aus dem obigen Beispiel sieht als Baum wie folgt aus:
#
#                      Start  
#           ____________/|\____________
#          /             |             \
#         |              |              |
#        (1)            (2)            (3)            
#        / \            / \            / \
#       /   \          /   \          /   \
#   (1.1)  (1.2)    (2.1) (2.2)    (3.1) (3.2)        X wählt jeweils den Zug mit
#    +10    -10       0   -10        0    +10         dem kleinesten Wert. (Minimizer)
#
# Die KI betrachtet nun jeden Zweig im Spielbaum. Die Zweigenden 
# enthalten jeweils die Information, wer das Spiel gewinnt oder 
# ob es unentschieden ist. 
#
# Zuerst wird der (1) Zweig berechnet. Am Ende finden wir die Positionen
# (1.1) und (1.2). Auf dieser Ebene ist der Spieler `X` (Minimizer) am Zug.  
# Er wählt er den Zug (1.2) aus, da dieser eine kleinere Bewertung hat als
# der Zug (1.1). Diese Bewertung wird auf den Elternknoten (1) übertragen. 

# Dann geht die KI durch die beiden anderen Zweige durch und berechnet die Bewertungen der 
# Elternknoten. Der Baum sieht anschliessend wie folgt aus:
#
#                      Start 0
#           ____________/|\____________
#          /             |             \
#         |              |              |
#        (1) -10        (2) -10        (3) 0          O wählt den grössten Wert. (Maximizer)
#        / \            / \            / \
#       /   \          /   \          /   \
#   (1.1)  (1.2)    (2.1) (2.2)    (3.1) (3.2)        X wählt den kleinesten Wert. (Minimizer)
#    +10    -10       0   -10        0    +10
#
# Nun betrachtet die KI die Knoten (1), (2) und (3). Auf dieser Ebene ist sie, 
# die KI `O` (Maximizer) am Zug. Sie wird sich für den Zug (3) mit der 
# grössten Punktzahl entscheiden. Damit vermeided die KI eine Niederlage und 
# erreicht ein Unentschieden. 



# _________________________________
#                                 /
# Implementierung in Tic-Tac-Toe (
# ________________________________\

# Im folgenden Beispiel implementieren wir den Minimax-Algorithmus, um eine unbesiegbare
# KI für Tic-Tac-Toe zu erstellen. Die KI bewertet alle möglichen Züge und wählt den besten.

import math

# Gibt das Spielfeld aus.
def print_board(board):
    tags = {1: "X", 0: " ", -1: "O"}
    row_separator = "-" * (len(board[0]) * 4 - 1)

    output = "\n".join(
        "|".join(f" {tags[cell]} " for cell in row) + ("\n" + row_separator if i < len(board) - 1 else "")
        for i, row in enumerate(board)
    )
    print("\n"+output+"\n")
           

# Prüft, ob ein Spieler gewonnen hat.
def check_winner(board):
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]

    return 0


# Bewertet den aktuellen Zustand des Spielfelds.
def evaluate(board):
    winner = check_winner(board)
    if winner == 1:
        return -10
    elif winner == -1:
        return 10
    return 0


# Prüft, ob noch Züge möglich sind.
def is_moves_left(board):
    for row in board:
        if 0 in row:
            return True
    return False


# Minimax-Algorithmus zur Bewertung aller möglichen Züge.
def minimax(board, depth, is_maximizing, move=""):

    score = evaluate(board)
    if score in [10, -10] or not is_moves_left(board):
        return score
    
    if depth >= 0:
        if is_maximizing:
            print(f"{move}) Player")
        else:
            print(f"{move}) KI")
        print_board(board)

    # Suche den Zug mit der maximalen Bewertung
    if is_maximizing:
        best = -math.inf
        k = 1
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = -1
                    best = max(best, minimax(board, depth + 1, not is_maximizing, move+f".{k}"))
                    board[i][j] = 0
                    k += 1
        return best

    # Suche den Zug mit der minimalen Bewertung
    else:
        best = math.inf
        k = 1
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1
                    best = min(best, minimax(board, depth + 1, not is_maximizing, move+f".{k}"))
                    board[i][j] = 0
                    k += 1
        return best


# Findet den besten Zug für die KI.
def find_best_move(board):
    best_value = -math.inf
    best_move = (-1, -1)
    
    k = 1
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = -1
                move_value = minimax(board, 0, False, f"{k}")
                board[i][j] = 0
                k += 1
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)

    return best_move


# Führt den Zug des Spielers aus.
def player_turn(board):
    while True:
        try:
            move = int(input("Wähle ein Feld (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == 0:
                board[row][col] = 1
                return
            else:
                print("Dieses Feld ist bereits belegt. Wähle ein anderes.")
        except (ValueError, IndexError):
            print("Ungültige Eingabe. Wähle eine Zahl zwischen 1 und 9.")

        

def tic_tac_toe():
    
    print("Willkommen zu Tic-Tac-Toe mit unbesiegbarer KI!")
    print("Spieler ist 'X', KI ist 'O'.")
    print("Das Spielfeld hat folgende Nummerierung:")
    
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print()

    # board = [[0 for _ in range(3)] for _ in range(3)]

    board = [[  1, -1,  -1],
             [ -1,  0,  0],
             [  1,  0,  0]]

    for turn in range(9):
        
        print(f"---------- Zug {turn+1} ------------")
        print_board(board)

        if turn % 2 == 0:
            print("Dein Zug:")
            
            player_turn(board)
        else:
            print("Zug der KI:")
            best_move = find_best_move(board)
            board[best_move[0]][best_move[1]] = -1

        winner = check_winner(board)
        if winner != 0:
            print_board(board)
            
            if winner == 1:
                print("X hat gewonnen!")
            elif winner == -1:
                print("O hat gewonnen!")
            
            return winner

        elif not is_moves_left(board):
            print_board(board)
            print("Das Spiel endet unentschieden.")
            
            return 0
        


# Hauptprogramm
tic_tac_toe()




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# In diesem Kapitel hast du gelernt, wie der Minimax-Algorithmus funktioniert und wie
# er in Tic-Tac-Toe angewendet wird:
#
# 1. Grundkonzepte: Maximieren der eigenen Punkte und Minimieren der Punkte des Gegners.
#
# 2. Rekursive Bewertung: Simulieren aller möglichen Züge, um den besten Zug zu finden.
#
# 3. Bewertung des Spiels: Gewinner und Unentschieden werden bewertet, um den Algorithmus
#    zu steuern.

# Der Minimax-Algorithmus ist eine grundlegende Technik, die in vielen Spielen mit
# vollständiger Information (z. B. Schach) verwendet wird. Du kannst diesen Algorithmus
# erweitern, um komplexere Spiele zu lösen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Implementiere eine Simulation, in der die zufällige KI (`ai_random`) aus dem
# letzten Kapitel gegen die Minimax-KI antritt. Lass sie 100 Spiele spielen und
# zähle die Siege, Niederlagen und Unentschieden für beide KIs.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine neue Funktion `tic_tac_toe_ki_vs_ki()`, in der zwei Minimax-KIs gegeneinander spielen.
# Beide KIs sollen den Minimax-Algorithmus verwenden, jedoch mit unterschiedlicher Bewertungstiefe:
# - Die erste KI soll den Spielbaum bis zu einer Tiefe von 3 betrachten.
# - Die zweite KI soll den Spielbaum bis zu einer Tiefe von 5 betrachten.
#
# Lass die beiden KIs 100 Spiele gegeneinander spielen und bestimme die Ergebnisse:
# - Welche KI gewinnt häufiger?
# - Wie viele Spiele enden unentschieden?
#
# Hinweis: Passe die `minimax()`-Funktion so an, dass sie die maximale Rekursionstiefe berücksichtigt.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe eine Funktion `evaluate_v2(board)`, die die Bewertung des Spielfelds
# verbessert. Zusätzlich zu Gewinn, Verlust oder Unentschieden soll die Funktion
# auch berücksichtigen:
# 
# - Wie viele Züge nötig sind, um zu gewinnen oder zu verlieren.
# - Ein schnellerer Sieg oder ein langsamerer Verlust soll eine höhere Bewertung erhalten.
#
# Implementiere diese Funktion und ersetze die bisherige `evaluate(board)`-Funktion.


# Füge hier deine Lösung ein.





#        ;     /        ,--.     
#       ["]   ["]  ,<  |__**|    
#      /[_]\  [~]\/    |//  |    
#       ] [   OOO      /o|__|   Phs
#         
#  ╭━━━━╮╱╱╱╭━━━━╮╱╱╱╱╱╭━━━━╮
#  ┃╭╮╭╮┃╱╱╱┃╭╮╭╮┃╱╱╱╱╱┃╭╮╭╮┃
#  ╰╯┃┃┣╋━━╮╰╯┃┃┣┻━┳━━╮╰╯┃┃┣┻━┳━━╮
#  ╱╱┃┃┣┫╭━╯╱╱┃┃┃╭╮┃╭━╯╱╱┃┃┃╭╮┃┃━┫
#  ╱╱┃┃┃┃╰━╮╱╱┃┃┃╭╮┃╰━╮╱╱┃┃┃╰╯┃┃━┫
#  ╱╱╰╯╰┻━━╯╱╱╰╯╰╯╰┻━━╯╱╱╰╯╰━━┻━━╯
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
# Implementiere eine Simulation, in der die zufällige KI (`ai_random`) aus dem
# letzten Kapitel gegen die Minimax-KI antritt. Lass sie 100 Spiele spielen und
# zähle die Siege, Niederlagen und Unentschieden für beide KIs.

'''
import random

# Funktion für die zufällige KI
def ai_random(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == 0:
            return row, col

# Funktion, die die zufällige KI gegen die Minimax-KI antreten lässt
def simulate_random_vs_minimax(rounds=100):
    results = {"Random KI": 0, "Minimax KI": 0, "Draw": 0}

    for _ in range(rounds):
        board = [[0 for _ in range(3)] for _ in range(3)]

        for turn in range(9):
            if turn % 2 == 0:
                # Random KI
                move = ai_random(board)
                board[move[0]][move[1]] = 1
            else:
                # Minimax KI
                move = find_best_move(board)
                board[move[0]][move[1]] = -1

            winner = check_winner(board)
            if winner == 1:
                results["Random KI"] += 1
                break
            elif winner == -1:
                results["Minimax KI"] += 1
                break

        if not any(0 in row for row in board):
            results["Draw"] += 1

    return results

# Simulation starten
print(simulate_random_vs_minimax())
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine neue Funktion `tic_tac_toe_ki_vs_ki()`, in der zwei Minimax-KIs gegeneinander spielen.
# Beide KIs sollen den Minimax-Algorithmus verwenden, jedoch mit unterschiedlicher Bewertungstiefe:
# - Die erste KI soll den Spielbaum bis zu einer Tiefe von 3 betrachten.
# - Die zweite KI soll den Spielbaum bis zu einer Tiefe von 5 betrachten.
#
# Lass die beiden KIs 100 Spiele gegeneinander spielen und bestimme die Ergebnisse:
# - Welche KI gewinnt häufiger?
# - Wie viele Spiele enden unentschieden?
#
# Hinweis: Passe die `minimax()`-Funktion so an, dass sie die maximale Rekursionstiefe berücksichtigt.


'''
# Angepasster Minimax-Algorithmus mit Tiefe
def minimax_with_depth(board, depth, max_depth, is_maximizing):
    score = evaluate(board)

    if score in [10, -10] or not is_moves_left(board) or depth == max_depth:
        return score

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = -1
                    best = max(best, minimax_with_depth(board, depth + 1, max_depth, False))
                    board[i][j] = 0
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1
                    best = min(best, minimax_with_depth(board, depth + 1, max_depth, True))
                    board[i][j] = 0
        return best

# Funktion für die KI mit Tiefe
def find_best_move_with_depth(board, max_depth):
    best_value = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = -1
                move_value = minimax_with_depth(board, 0, max_depth, False)
                board[i][j] = 0
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)

    return best_move

# Simulation der Minimax-KIs mit unterschiedlicher Tiefe
def simulate_minimax_vs_minimax(depth1, depth2, rounds=100):
    results = {f"Minimax KI (Tiefe {depth1})": 0, f"Minimax KI (Tiefe {depth2})": 0, "Draw": 0}

    for _ in range(rounds):
        board = [[0 for _ in range(3)] for _ in range(3)]

        for turn in range(9):
            if turn % 2 == 0:
                move = find_best_move_with_depth(board, depth1)
                board[move[0]][move[1]] = 1
            else:
                move = find_best_move_with_depth(board, depth2)
                board[move[0]][move[1]] = -1

            winner = check_winner(board)
            if winner == 1:
                results[f"Minimax KI (Tiefe {depth1})"] += 1
                break
            elif winner == -1:
                results[f"Minimax KI (Tiefe {depth2})"] += 1
                break

        if not any(0 in row for row in board):
            results["Draw"] += 1

    return results

# Simulation starten
print(simulate_minimax_vs_minimax(3, 5))
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe eine Funktion `evaluate_v2(board)`, die die Bewertung des Spielfelds
# verbessert. Zusätzlich zu Gewinn, Verlust oder Unentschieden soll die Funktion
# auch berücksichtigen:
# 
# - Wie viele Züge nötig sind, um zu gewinnen oder zu verlieren.
# - Ein schnellerer Sieg oder ein langsamerer Verlust soll eine höhere Bewertung erhalten.
#
# Implementiere diese Funktion und ersetze die bisherige `evaluate(board)`-Funktion.


'''
# Erweiterte Bewertungsfunktion
def evaluate_v2(board, depth):
    winner = check_winner(board)
    if winner == 1:
        return -10 + depth  # Schnellerer Verlust weniger schwerwiegend
    elif winner == -1:
        return 10 - depth  # Schnellerer Sieg besser bewertet
    return 0

# Anpassung von minimax(), um evaluate_v2() zu verwenden
def minimax_with_evaluate_v2(board, depth, is_maximizing):
    score = evaluate_v2(board, depth)

    if score in [10, -10] or not is_moves_left(board):
        return score

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = -1
                    best = max(best, minimax_with_evaluate_v2(board, depth + 1, False))
                    board[i][j] = 0
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1
                    best = min(best, minimax_with_evaluate_v2(board, depth + 1, True))
                    board[i][j] = 0
        return best

# Neue KI mit evaluate_v2 verwenden
def find_best_move_with_evaluate_v2(board):
    best_value = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = -1
                move_value = minimax_with_evaluate_v2(board, 0, False)
                board[i][j] = 0
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)

    return best_move
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

