#              _________________________________________
#       ______|                                         |_____
#       \     |   14.4 MINIMAX ALGORITHMUS - Teil 1     |    /
#        )    |_________________________________________|   (
#       /________)                                  (________\     8.12.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Der Minimax-Algorithmus ist ein rekursives Verfahren, mit dem zwei Spieler 
# abwechselnd agieren. Dabei versucht der eine Spieler (Maximizer) seine Gewinnchancen 
# zu maximieren, während der andere (Minimizer) diese minimiert.

# Der Algorithmus analysiert alle möglichen Züge und versucht, den optimalen Zug zu 
# finden, indem er die Züge des Gegners vorhersieht. In Tic-Tac-Toe kann der 
# Minimax-Algorithmus verwendet werden, um eine unbesiegbare KI zu erstellen.


# ____________________________________
#                                    /
# Erklärung des Minimax-Algorithmus (
# ___________________________________\

# Der Minimax-Algorithmus ist eine rekursive Methode zur Entscheidungsfindung.
# Das Ziel ist es, am Ende einen Zug auszuwählen, welcher aus Sicht der KI (Maximizer) 
# optimal ist, unter der Annahme, dass der Gegner (Minimizer) ebenfalls optimal spielt.
#
# - Rekursion: 
#   Simuliert alle möglichen Züge und geht tiefer in das Spiel, bis ein Endzustand 
#   (Gewinn, Verlust, Unentschieden) erreicht wird.
#
# - Bewertung
#   Jeder Endzustand wird mit einer Punktzahl bewertet. Wir nutzen +10, -10 und 0 
#   als einfache Punkteskala. +10 bedeutet ein eindeutiger Vorteil für die KI, -10 
#   ein Verlust, und 0 ein neutraler Ausgang wie ein Unentschieden.
#    - Gewinn für die KI: +10
#    - Gewinn für den Spieler: -10
#    - Unentschieden: 0
#
# - Maximierung und Minimierung
#   Die künstliche Intelligenz KI (Maximizer) versucht, die Punktzahl zu maximieren.
#   Der Spieler (Minimizer) versucht, die Punktzahl der KI zu minimieren.

# Betrachten wir ein Beispiel: Die KI spielt `O` und ist am Zug.
# Das Brett sieht aktuell wie folgt aus: 
# 
# (Start)
#  X | O | O  
# -----------
#  O | X | 
# -----------
#  X |   |  
# 
# Die KI `O` simuliert alle möglichen Züge für die freien Felder.
# 
# (1)            (2)             (3)
#    X | O | O       X | O | O       X | O | O  
#   -----------     -----------     -----------
#    O | X | O       O | X |         O | X |   
#   -----------     -----------     -----------
#    X |   |         X | O |         X |   | O
# 
# Ausgehend von diesen drei Zügen, ergeben sich dann für X die folgenden 
# sechs Möglichkeiten:
#
# (1.1)           (1.2)                       
#    X | O | O       X | O | O 
#   -----------     -----------
#    O | X | O       O | X | O 
#   -----------     -----------
#    X | X |         X |   | X 
#
# (2.1)           (2.2)           
#    X | O | O       X | O | O
#   -----------     -----------
#    O | X | X       O | X |   
#   -----------     -----------
#    X | O |         X | O | X 
#
# (3.1)           (3.2)           
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

# Die KI ist der Maximizer (will also hohe Punktzahlen erreichen), während der menschliche 
# Spieler der Minimizer ist. 



# _________________________________
#                                 /
# Implementierung in Tic-Tac-Toe (
# ________________________________\

# Im folgenden Beispiel implementieren wir den Minimax-Algorithmus, um eine unbesiegbare
# KI für Tic-Tac-Toe zu erstellen. Die KI bewertet alle möglichen Züge und wählt den besten.

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


def find_best_move(board, id=AI_ID):
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


def player_turn(board, id=PLAYER_ID):
    """Lässt den Spieler 'X' einen Zug machen, indem er eine Zahl (1-9) eingibt."""
    while True:
        try:
            move = int(input("Wähle ein Feld (1-9): ")) - 1
            row, col = divmod(move, 3)
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == 0:
                board[row][col] = id
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

    # Initialisiere das Spielbrett.
    #board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

    board = [[ -1,  1,  1],
             [  1,  0,  0],
             [ -1,  0,  0]]


    for turn in range(9):
        if verbose:
            print_board(board)

        if turn % 2 == 0:
            # Spielerzug
            if verbose:
                print("Dein Zug:")

            player_turn(board, PLAYER_ID)

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
                print(f"{symbols[winner]} hat gewonnen!")
            
            return winner

        elif not is_moves_left(board):
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
















# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# Zusammengefasst nutzt Minimax eine Baumdarstellung aller zukünftigen Züge, bewertet 
# jeden Endzustand und wählt dann - abhängig von der Spielerrolle (Maximizer oder Minimizer) 
# - den optimalen Zug aus. Damit erreicht man in Spielen wie Tic-Tac-Toe eine unbesiegbare KI, 
# solange der Suchraum vollständig berechnet werden kann.

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
# Ändere die Anfangsposition des Spielfeldes und versuche die Berechnungen von 
# Minimax nachzuvollziehen. 


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
# Ändere die Anfangsposition des Spielfeldes und versuche die Berechnungen von 
# Minimax nachzuvollziehen. 


# Füge hier deine Lösung ein.




# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


