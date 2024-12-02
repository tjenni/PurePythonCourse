#              ________________________________
#       ______|                                |_____
#       \     |   14.3 MINIMAX ALGORITHMUS     |    /
#        )    |________________________________|   (
#       /________)                          (________\     22.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

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
#      indem unnötige Züge ausgeschlossen werden.


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


def evaluate(board):
    """
    Bewertet den aktuellen Zustand des Spielfelds.
    """
    winner = check_winner(board)
    if winner == 1:
        return -10
    elif winner == -1:
        return 10
    return 0


def is_moves_left(board):
    """
    Prüft, ob noch Züge möglich sind.
    """
    for row in board:
        if 0 in row:
            return True
    return False


def minimax(board, depth, is_maximizing):
    """
    Minimax-Algorithmus zur Bewertung aller möglichen Züge.
    """
    score = evaluate(board)

    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = -1
                    best = max(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = 0
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1
                    best = min(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = 0
        return best


def find_best_move(board):
    """
    Findet den besten Zug für die KI.
    """
    best_value = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = -1
                move_value = minimax(board, 0, False)
                board[i][j] = 0
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

# Führt den Zug der KI aus. Wählt ein zufälliges, freies Feld.
def ai_random(board, id=-1, verbose=True):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == 0:
            board[row][col] = id
            if verbose:
                print(f"Die KI wählt Feld {row * 3 + col + 1}.")
            return
        
        

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

    board = [[0 for _ in range(3)] for _ in range(3)]

    for turn in range(9):
        if verbose:
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