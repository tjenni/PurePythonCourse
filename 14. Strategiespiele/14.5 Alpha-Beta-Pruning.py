#              ________________________________
#       ______|                                |_____
#       \     |  14.4 ALPHA-BETA PRUNING       |    /
#        )    |________________________________|   (
#       /________)                          (________\     22.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Alpha-Beta-Pruning ist eine Erweiterung des Minimax-Algorithmus. Es verbessert die
# Effizienz, indem es unnötige Berechnungen vermeidet. Dadurch kann der Algorithmus
# schneller arbeiten, ohne die Genauigkeit der Entscheidung zu beeinträchtigen.

# ________________________
#                        /
# Funktionsweise         (
# ________________________\

# 1. **Ziel:** 
#    - Reduziere die Anzahl der untersuchten Spielzüge, indem bereits bekannte
#      schlechtere Züge ausgeschlossen werden.

# 2. **Alpha und Beta:**
#    - Alpha repräsentiert den besten Wert, den der Maximizer garantieren kann.
#    - Beta repräsentiert den besten Wert, den der Minimizer garantieren kann.

# 3. **Pruning:** 
#    - Sobald ein Knoten gefunden wird, der schlechter ist als ein zuvor analysierter
#      Knoten (basierend auf Alpha und Beta), werden weitere Knoten ignoriert.

# 4. **Effizienz:** 
#    - Alpha-Beta-Pruning kann die Berechnung auf bis zu die Hälfte der Knoten
#      reduzieren, die im ursprünglichen Minimax-Algorithmus untersucht werden.

# ________________________________
#                                /
# Implementierung in Tic-Tac-Toe (
# ________________________________\

# Im folgenden Beispiel erweitern wir den Minimax-Algorithmus mit Alpha-Beta-Pruning,
# um die Effizienz der KI in Tic-Tac-Toe zu verbessern.

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


def alpha_beta_pruning(board, depth, alpha, beta, is_maximizing):
    """
    Minimax-Algorithmus mit Alpha-Beta-Pruning.
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
                    value = alpha_beta_pruning(board, depth + 1, alpha, beta, False)
                    best = max(best, value)
                    alpha = max(alpha, best)
                    board[i][j] = " "
                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    value = alpha_beta_pruning(board, depth + 1, alpha, beta, True)
                    best = min(best, value)
                    beta = min(beta, best)
                    board[i][j] = " "
                    if beta <= alpha:
                        break
        return best


def find_best_move_alpha_beta(board):
    """
    Findet den besten Zug für die KI mit Alpha-Beta-Pruning.
    """
    best_value = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_value = alpha_beta_pruning(board, 0, -math.inf, math.inf, False)
                board[i][j] = " "
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)

    return best_move


def tic_tac_toe_with_alpha_beta():
    """
    Hauptspielschleife mit unbesiegbarer KI und Alpha-Beta-Pruning.
    """
    print("Willkommen zu Tic-Tac-Toe mit KI und Alpha-Beta-Pruning!")
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
            best_move = find_best_move_alpha_beta(board)
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
    tic_tac_toe_with_alpha_beta()


# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# In diesem Kapitel hast du gelernt, wie Alpha-Beta-Pruning den Minimax-Algorithmus 
# optimiert:
#
# 1. **Effizienz:** Durch Pruning werden unnötige Berechnungen vermieden, indem 
#    schlecht bewertete Züge ausgeschlossen werden.
#
# 2. **Alpha und Beta:** Alpha repräsentiert den besten Wert für den Maximizer, Beta 
#    den besten Wert für den Minimizer.
#
# 3. **Flexibilität:** Alpha-Beta-Pruning ist eine universelle Technik, die in vielen
#    Entscheidungsbäumen verwendet werden kann.

# Alpha-Beta-Pruning ist besonders bei Spielen mit vielen möglichen Zügen (z. B. Schach)
# nützlich. In Tic-Tac-Toe zeigt es bereits seine Stärke, indem es die Anzahl der 
# benötigten Berechnungen reduziert.


# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Verändere das Spielfeld auf eine Größe von 4x4. Passe den Algorithmus entsprechend an.


# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Messe die Effizienz von Alpha-Beta-Pruning im Vergleich zum klassischen Minimax-Algorithmus, 
# indem du die Anzahl der untersuchten Knoten zählst.


# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erweitere den Algorithmus, sodass er bei Spielen mit mehreren Runden lernt, indem er 
# die Ergebnisse früherer Spiele analysiert.