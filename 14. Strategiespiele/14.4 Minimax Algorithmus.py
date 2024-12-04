#              _________________________________________
#       ______|                                         |_____
#       \     |   14.3 MINIMAX ALGORITHMUS - Teil 1     |    /
#        )    |_________________________________________|   (
#       /________)                                  (________\     22.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

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
#    - Die KI (Maximizer) versucht, die Punktzahl zu maximieren.
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
# Ausgehend von diesen drei Zügen, ergeben sich dann für X die folgenden Möglichkeiten:
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
# - Die Züge 1.1), 3.2) bringen für die KI `O` den Gewinn. Sie werden daher mit +10 bewertet.
#
# - Die Züge 1.2), 2.2)bringen für den Spieler `X` den Gewinn. Sie werden mit -10 bewertet.
# 
# - Die Züge 2.1), 3.1) führen zu einem Unentschieden und ergeben 0 Punkte.

#
# Die KI wählt nun die Züge aus, welcher für den Spieler `X` am besten sind. Das sind die Züge 
# mit einer möglichst kleinen Zahl. Am besten sieht man das an dem Spielbaum. 
#
#                      Start  
#           ____________/|\____________
#          /             |             \
#         |              |              |
#        (1) -10        (2) -10        (3) -10          O wählt den grössten Wert. (Maximizer)
#        / \            / \            / \
#       /   \          /   \          /   \
#   (1.1)  (1.2)    (2.1) (2.2)    (3.1) (3.2)        X wählt den kleinesten Wert. (Minimizer)
#    +10    -10      -10   -10       -10     +10
#
# Nun weiss die KI, dass sie das Spiel nicht gewinnen kann. Bei Zug 1 und 2, wird der Spieler
# gewinnen. Sie entscheidet sich daher für den Zug 3. 




# ________________________________
#                                /
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

    score = evaluate(board),

    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0
    
    if depth >= 0:
        print(f"{move})")
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

        print(best)
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

        print(best)
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

        

def tic_tac_toe(verbose=True):
    
    if verbose:
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

#  X | O | O  
# -----------
#  O | X | 
# -----------
#  X |   |  

    for turn in range(9):
        if verbose:
            print(f"---------- Zug {turn+1} ------------")
            print_board(board)

        if turn % 2 == 0:
            if verbose:
                print("Dein Zug:")
            
            player_turn(board)
        else:
            print("Zug der KI:")
            best_move = find_best_move(board)
            board[best_move[0]][best_move[1]] = -1

        winner = check_winner(board)
        if winner != 0 and verbose:
            print_board(board)
            
            if winner == 1:
                print("X hat gewonnen!")
            elif winner == -1:
                print("O hat gewonnen!")
                
            return winner

    if verbose:
        print_board(board)
        print("Das Spiel endet unentschieden.")
        
    return 0
        
        
                


# Hauptprogramm
score = {"Spieler": 0, "KI": 0, "Unentschieden":0}
round = 1
while round <= 10:
    winner = tic_tac_toe()

    if winner == 1:
        score["Spieler"] += 1
    elif winner == -1:
        score["KI"] += 1
    else:
        score["Unentschieden"] += 1
    
    print(f"\nPUNKTESTAND Runde {round}")
    for name, points in score.items():
        print(f"{name}: {points}")
        
    print()
    round += 1


# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# In diesem Kapitel hast du gelernt, wie der Minimax-Algorithmus funktioniert und wie
# er in Tic-Tac-Toe angewendet wird:
#
# 1. **Grundkonzepte:** Maximieren der eigenen Punkte und Minimieren der Punkte des Gegners.
# 2. **Rekursive Bewertung:** Simulieren aller möglichen Züge, um den besten Zug zu finden.
# 3. **Bewertung des Spiels:** Gewinner und Unentschieden werden bewertet, um den Algorithmus
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
# Füge Alpha-Beta-Pruning zum Minimax-Algorithmus hinzu, um die Berechnungen
# effizienter zu gestalten.


# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erweitere den Minimax-Algorithmus für größere Spielfelder (z. B. 4x4 oder 5x5).


# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Implementiere eine grafische Version von Tic-Tac-Toe mit dem Minimax-Algorithmus
# als KI-Gegner.