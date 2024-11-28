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

# 1. **Ziel:** 
#    - Der Algorithmus maximiert die Punkte für den eigenen Spieler (Maximizer) und
#      minimiert die Punkte für den Gegner (Minimizer).

# 2. **Bewertung:**
#    - Gewinnt der Maximizer, wird ein positiver Wert zurückgegeben (z. B. +10).
#    - Gewinnt der Minimizer, wird ein negativer Wert zurückgegeben (z. B. -10).
#    - Ein Unentschieden wird mit 0 bewertet.

# 3. **Rekursion:** 
#    - Der Algorithmus simuliert alle möglichen Züge, bewertet deren Ergebnis und wählt
#      den Zug mit der besten Bewertung.

# 4. **Optimierung:** 
#    - Mithilfe von Alpha-Beta-Pruning kann der Algorithmus effizienter gestaltet werden,
#      indem unnötige Züge ausgeschlossen werden.


# ________________________________
#                                /
# Implementierung in Tic-Tac-Toe (
# ________________________________\

# Im folgenden Beispiel implementieren wir den Minimax-Algorithmus, um eine unbesiegbare
# KI für Tic-Tac-Toe zu erstellen. Die KI bewertet alle möglichen Züge und wählt den besten.

import math

def print_board(board):
    """
    Gibt das Spielfeld aus.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """
    Prüft, ob ein Spieler gewonnen hat.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def evaluate(board):
    """
    Bewertet den aktuellen Zustand des Spielfelds.
    """
    winner = check_winner(board)
    if winner == "X":
        return -10
    elif winner == "O":
        return 10
    return 0


def is_moves_left(board):
    """
    Prüft, ob noch Züge möglich sind.
    """
    for row in board:
        if " " in row:
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
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = min(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = " "
        return best


def find_best_move(board):
    """
    Findet den besten Zug für die KI.
    """
    best_value = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_value = minimax(board, 0, False)
                board[i][j] = " "
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)

    return best_move


def tic_tac_toe_with_minimax():
    """
    Hauptspielschleife mit unbesiegbarer KI.
    """
    print("Willkommen zu Tic-Tac-Toe mit unbesiegbarer KI!")
    print("Spieler ist 'X', KI ist 'O'.")
    print("Das Spielfeld hat folgende Nummerierung:")
    print("1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9\n")

    board = [[" " for _ in range(3)] for _ in range(3)]

    for turn in range(9):
        print_board(board)

        if turn % 2 == 0:
            print("Dein Zug:")
            while True:
                try:
                    move = int(input("Wähle ein Feld (1-9): ")) - 1
                    row, col = divmod(move, 3)
                    if board[row][col] == " ":
                        board[row][col] = "X"
                        break
                    else:
                        print("Dieses Feld ist bereits belegt.")
                except (ValueError, IndexError):
                    print("Ungültige Eingabe. Wähle eine Zahl zwischen 1 und 9.")
        else:
            print("Zug der KI:")
            best_move = find_best_move(board)
            board[best_move[0]][best_move[1]] = "O"

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} hat gewonnen!")
            return

    print_board(board)
    print("Das Spiel endet unentschieden.")


# Hauptprogramm starten
if __name__ == "__main__":
    tic_tac_toe_with_minimax()


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