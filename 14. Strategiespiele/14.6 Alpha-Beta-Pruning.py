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

# 1. Ziel: 
#    Reduziere die Anzahl der untersuchten Spielzüge, indem bereits bekannte
#    schlechtere Züge ausgeschlossen werden.

# 2. Alpha und Beta:
#    `Alpha` repräsentiert den besten Wert, den der Maximizer garantieren kann.
#    `Beta` repräsentiert den besten Wert, den der Minimizer garantieren kann.

# 3. Pruning: 
#    Sobald ein Knoten gefunden wird, der schlechter ist als ein zuvor analysierter
#    Knoten (basierend auf `Alpha` und `Beta`), werden weitere Knoten ignoriert.

# 4. Effizienz: 
#    Alpha-Beta-Pruning kann die Berechnung auf bis zu die Hälfte der Knoten
#    reduzieren, die im ursprünglichen Minimax-Algorithmus untersucht werden.




# ________________________________
#                                /
# Implementierung in Tic-Tac-Toe (
# ________________________________\

# Im folgenden Beispiel erweitern wir den Minimax-Algorithmus mit Alpha-Beta-Pruning,
# um die Effizienz der KI in Tic-Tac-Toe zu verbessern.

import math


def print_board(board):
    """Gibt das Tic-Tac-Toe-Spielfeld formatiert auf der Konsole aus."""
    tags = {1: "O", 0: " ", -1: "X"}
    row_separator = "-" * (len(board[0]) * 4 - 1)

    # Erzeuge den auszugebenden Text für das Brett
    rows = []
    for i, row in enumerate(board):
        row_text = "|".join(f" {tags[cell]} " for cell in row)
        if i < len(board) - 1:
            row_text += "\n" + row_separator
        rows.append(row_text)

    output = "\n".join(rows)
    print("\n" + output + "\n")



def check_winner(board):
    """Prüft, ob ein Spieler gewonnen hat."""
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]

    return None



def evaluate_v2(board, depth):
    """Erweiterte Bewertungsfunktion"""
    winner = check_winner(board)
    if winner == 1:
        return 10 - depth  # Schnellerer Verlust weniger schwerwiegend
    elif winner == -1:
        return -10 + depth  # Schnellerer Sieg besser bewertet
    return 0



def is_moves_left(board):
    """Prüft, ob noch Züge möglich sind."""
    for row in board:
        if 0 in row:
            return True
    return False



def alpha_beta_pruning(board, depth, alpha, beta, is_maximizing):
    """Minimax-Algorithmus mit Alpha-Beta-Pruning."""
    score = evaluate(board, depth)

    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1
                    value = alpha_beta_pruning(board, depth + 1, alpha, beta, False)
                    best = max(best, value)
                    alpha = max(alpha, best)
                    board[i][j] = 0

                    # Pruning
                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = -1
                    value = alpha_beta_pruning(board, depth + 1, alpha, beta, True)
                    best = min(best, value)
                    beta = min(beta, best)
                    board[i][j] = 0

                    # Pruning
                    if beta <= alpha:
                        break
        return best



def find_best_move_alpha_beta(board):
    """Findet den besten Zug für die KI mit Alpha-Beta-Pruning."""
    best_value = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 1
                move_value = alpha_beta_pruning(board, 0, -math.inf, math.inf, False)
                board[i][j] = 0
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)

    return best_move



def player_turn(board):
    """Lässt den Spieler 'X' einen Zug machen, indem er eine Zahl (1-9) eingibt."""
    while True:
        try:
            move = int(input("Wähle ein Feld (1-9): ")) - 1
            row, col = divmod(move, 3)
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == 0:
                board[row][col] = -1
                return
            else:
                print("Ungültiger Zug. Versuche es erneut.")
        except ValueError:
            print("Bitte eine gültige Zahl eingeben (1-9).")



def tic_tac_toe_with_alpha_beta(verbose=True):
    """Führt ein vollständiges Tic-Tac-Toe-Spiel durch.
       Spieler ist 'X', KI ist 'O'.
       Der Spieler beginnt."""
    if verbose:
        print("Willkommen zu Tic-Tac-Toe mit KI und Alpha-Beta-Pruning!")
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
            if verbose:
                print("Zug der KI:")

            best_move = find_best_move_alpha_beta(board)
            board[best_move[0]][best_move[1]] = 1

        winner = check_winner(board)
        if winner != 0 and verbose:
            print_board(board)
            
            if winner == 1:
                print("O hat gewonnen!")
            elif winner == -1:
                print("X hat gewonnen!")
                
            return winner

    if verbose:
        print_board(board)
        print("Das Spiel endet unentschieden.")
        
    return 0


def simulate_player_vs_alpha_beta(rounds=10):
    """Simulation mehrer Runden."""

    score = {"Spieler": 0, "KI": 0, "Unentschieden": 0}
    for game in range(1, 11):
        result = tic_tac_toe_with_alpha_beta()

        if result == 1:
            score["KI"] += 1
        elif result == -1:
            score["Spieler"] += 1
        else:
            score["Unentschieden"] += 1

        print(f"\nErgebnisse nach Runde {game}:")
        for name, punkte in score.items():
            print(f"{name}: {punkte}")
        print()


# Hauptprogramm starten
if __name__ == "__main__":
    simulate_player_vs_alpha_beta()




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# In diesem Kapitel hast du gelernt, wie Alpha-Beta-Pruning den Minimax-Algorithmus 
# optimiert:
#
# 1. Effizienz: Durch Pruning werden unnötige Berechnungen vermieden, indem 
#    schlecht bewertete Züge ausgeschlossen werden.
#
# 2. Alpha und Beta: Alpha repräsentiert den besten Wert für den Maximizer, Beta 
#    den besten Wert für den Minimizer.
#
# 3. Flexibilität: Alpha-Beta-Pruning ist eine universelle Technik, die in vielen
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








# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><
