#              _________________________________________
#       ______|                                         |_____
#       \     |   14.5 MINIMAX ALGORITHMUS - Teil 2     |    /
#        )    |_________________________________________|   (
#       /________)                                  (________\     8.12.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# In den vorherigen Kapiteln haben wir gelernt, wie wir ein Tic-Tac-Toe-Spiel 
# programmieren und eine unbesiegbare KI mithilfe des Minimax-Algorithmus 
# erstellen können. Wir haben uns mit den Grundregeln des Spiels, der 
# Repräsentation des Spielbretts, der Erkennung von Gewinnzuständen sowie 
# dem Minimax-Algorithmus beschäftigt.
#
# In diesem Kapitel möchten wir nun alle Teile zusammenfügen, um ein 
# vollständiges, lauffähiges Spiel zu präsentieren. Dabei werden wir:
#
# 1. Das komplette Tic-Tac-Toe-Spiel inklusive Spiellogik, Ein- und 
#    Ausgaben sowie Gewinnerkennung implementieren.
#
# 2. Die bereits entwickelte Minimax-KI integrieren, sodass der Mensch 
#    gegen eine unbesiegbare KI antreten kann.
#
# 3. Optional: Erweiterungen einbauen, zum Beispiel das Ausprobieren 
#    verschiedener KI-Strategien oder die Darstellung des Entscheidungsbaums.
#
# Ziel ist es, am Ende ein eigenständiges Programm zu haben, das sich 
# problemlos starten lässt und in dem der Nutzer entweder selbst spielen 
# oder zwei KIs gegeneinander antreten lassen kann.
#
# Nachdem wir die Grundlagen erlernt haben, geht es nun um die praktische 
# Umsetzung all dieser Konzepte in ein fertiges Spiel.


import math


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



def evaluate(board):
    """Bewertet den Zustand des Boards:
       +10 für 'O' Gewinn (KI),
       -10 für 'X' Gewinn (Spieler),
       0 für niemanden."""
    winner = check_winner(board)
    if winner == 1:
        return 10
    elif winner == -1:
        return -10
    return 0



def is_moves_left(board):
    """Prüft, ob noch Züge möglich sind."""
    for row in board:
        if 0 in row:
            return True
    return False


def minimax(board, depth, id):
    """Implementiert den Minimax-Algorithmus, um die Spielzüge zu bewerten."""
    
    score = evaluate(board)

    # Endzustand erreicht oder keine Züge mehr
    if score in [10, -10] or not is_moves_left(board):
        return score

    best = -id * math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = id  # Zug platzieren

                if id > 0:
                    best = max(best, minimax(board, depth + 1, -id))
                else:
                    best = min(best, minimax(board, depth + 1, -id))

                board[i][j] = 0  # Zug zurücknehmen
    return best


def find_best_move(board, id):
    """Findet den besten Zug für die KI mittels Minimax."""
    best_value = -id * math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = id
                move_value = minimax(board, 0, -id)
                board[i][j] = 0
                if id > 0 and move_value > best_value or id < 0 and move_value < best_value:
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



def tic_tac_toe(symbols=DEFAULT_SYMBOLS, verbose=True):
    """Führt ein vollständiges Tic-Tac-Toe-Spiel durch.
       Spieler ist 'X', KI ist 'O'.
       Der Spieler beginnt."""

    if verbose:
        print("Willkommen zu Tic-Tac-Toe mit unbesiegbarer KI!")
        print("Spieler ist 'X', KI ist 'O'.")
        print("Spielfeld-Nummerierung:")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")

    board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

    for turn in range(9):
        if verbose:
            print_board(board)

        if turn % 2 == 0:
            # Spielerzug
            if verbose:
                print("Dein Zug:")
            player_turn(board)

        else:
            # KI-Zug
            if verbose:
                print("Zug der KI:")
            best_move = find_best_move(board, AI_ID)
            board[best_move[0]][best_move[1]] = AI_ID

        winner = check_winner(board)
        if winner != 0:
            if verbose:
                print_board(board)
                if winner == 1:
                    print("O hat gewonnen!")
                else:
                    print("X hat gewonnen!")

            return winner

    if verbose:
        print_board(board)
        print("Das Spiel endet unentschieden.")
    return 0



def simulate_player_vs_minimax(rounds=10):
    """Simulation mehrer Runden."""

    score = {"Spieler": 0, "KI": 0, "Unentschieden": 0}
    for game in range(1, 11):
        result = tic_tac_toe()

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
    simulate_player_vs_minimax()




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
# vorletzten Kapitel gegen die Minimax-KI antritt. Lass sie 100 Spiele spielen und
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




#                                            |
#                                            |
#      _______                   ________    |
#     |ooooooo|      ____       | __  __ |   |
#     |[]+++[]|     [____]      |/  \/  \|   |
#     |+ ___ +|     ]()()[      |\__/\__/|   |
#     |:|   |:|   ___\__/___    |[][][][]|   |
#     |:|___|:|  |__|    |__|   |++++++++|   |
#     |[]===[]|   |_|_/\_|_|    | ______ |   |
#   _ ||||||||| _ | | __ | | __ ||______|| __|
#     |_______|   |_|[::]|_|    |________|   \
#                 \_|_||_|_/               jro\
#                   |_||_|                     \
#                  _|_||_|_                     \
#         ____    |___||___|                     \
#        /  __\          ____                     \
#        \( oo          (___ \                     \
#        _\_o/           oo~)/
#       / \|/ \         _\-_/_      Die KI ist unbesiegbar !!!
#      / / __\ \___    / \|/  \
#      \ \|   |__/_)  / / .- \ \
#       \/_)  |       \ \ .  /_/
#        ||___|        \/___(_/
#        | | |          | |  |
#        | | |          | |  |
#        |_|_|          |_|__|
#        [__)_)        (_(___]
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


def tic_tac_toe_random_vs_minimax(symbols=DEFAULT_SYMBOLS):
    """Führt ein vollständiges Tic-Tac-Toe-Spiel durch.
       Random KI ist 'X', Minimax KI ist 'O'.
       Die Random KI beginnt."""


    board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

    for turn in range(9):

        if turn % 2 == 0:
            # Random KI
            ai_random(board, PLAYER_ID, False)

        else:
            # Minimax KI
            best_move = find_best_move(board, AI_ID)
            board[best_move[0]][best_move[1]] = AI_ID

        winner = check_winner(board)
        if winner != 0:
            return winner

    return 0



def simulate_random_vs_minimax(rounds=100):
    """Simulation mehrer Runden."""

    score = {"Minimax KI": 0, "Random KI": 0, "Unentschieden": 0}
    for game in range(rounds):
        result = tic_tac_toe_random_vs_minimax()

        if result == 1:
            score["Minimax KI"] += 1
        elif result == -1:
            score["Random KI"] += 1
        else:
            score["Unentschieden"] += 1

        print(f"\nErgebnisse nach Runde {game+1}:")
        for name, punkte in score.items():
            print(f"{name}: {punkte}")
        print()


# Hauptprogramm starten
if __name__ == "__main__":
    simulate_random_vs_minimax()

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
def minimax_with_depth(board, depth, max_depth, id):

    score = evaluate(board)

    if score in [10, -10] or not is_moves_left(board) or depth == max_depth:
        return score

    best = -id * math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = id  # Zug platzieren

                if id > 0:
                    best = max(best, minimax_with_depth(board, depth + 1, max_depth, -id))
                else:
                    best = min(best, minimax_with_depth(board, depth + 1, max_depth, -id))

                board[i][j] = 0  # Zug zurücknehmen
    return best


# Funktion für die KI mit Tiefe
def find_best_move_with_depth(board, id, max_depth):
    best_value = -id * math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = id
                move_value = minimax_with_depth(board, 0, max_depth, -id)
                board[i][j] = 0
                if id > 0 and move_value > best_value or id < 0 and move_value < best_value:
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
                move = find_best_move_with_depth(board, 1, depth1)
                board[move[0]][move[1]] = 1
            else:
                move = find_best_move_with_depth(board, -1, depth2)
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
if __name__ == "__main__":
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
        return 10 - depth
    elif winner == -1:
        return -10 + depth
    return 0

# Anpassung von minimax(), um evaluate_v2() zu verwenden
def minimax(board, depth, is_maximizing):
    score = evaluate_v2(board, depth)

    ...


'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

