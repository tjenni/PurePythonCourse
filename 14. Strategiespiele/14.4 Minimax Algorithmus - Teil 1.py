#              _________________________________________
#       ______|                                         |_____
#       \     |   14.4 MINIMAX ALGORITHMUS - Teil 1     |    /
#        )    |_________________________________________|   (
#       /________)                                  (________\     7.12.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

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

def print_board(board):
    """Gibt das Tic-Tac-Toe-Spielfeld formatiert auf der Konsole aus."""
    tags = {1: "X", 0: " ", -1: "O"}
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
    """Prüft, ob ein Spieler gewonnen hat und gibt den Gewinner zurück:
       1 für 'X', -1 für 'O', 0 für keinen Gewinner."""
    # Zeilen überprüfen
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]

    # Spalten überprüfen
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]

    # Diagonalen überprüfen
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]

    return 0


def evaluate(board):
    """Bewertet den Zustand des Boards:
       +10 für 'O' Gewinn (KI),
       -10 für 'X' Gewinn (Spieler),
       0 für niemanden."""
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



def minimax(board, depth, is_maximizing, move_path=""):
    """Implementiert den Minimax-Algorithmus, um die Spielzüge zu bewerten."""
    
    indent = "  " * depth  # 2 Leerzeichen pro Tiefe für bessere Übersicht
    
    score = evaluate(board)
    if score in [10, -10] or not is_moves_left(board):
        # Endzustand erreicht
        print(f"{indent}{move_path} Endzustand: score={score}")
        return score
    
    # Wer ist am Zug? KI (is_maximizing=True) = "O", sonst "X"
    if is_maximizing:
        current_player = "O"
    else:
        current_player = "X"
    
    if depth == 0:
        print_board(board)
    print(f"{indent}{move_path} Tiefe={depth}, Spieler={current_player}")

    if is_maximizing:
        best = -math.inf
        move_index = 1
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = -1
                    # Neue Tiefe, erweitere den move_path um ".ZugNr"
                    child_path = f"{move_path}.{move_index}"
                    val = minimax(board, depth + 1, not is_maximizing, child_path)
                    board[i][j] = 0
                    print(f"{indent}{child_path} Zug O->({i},{j}), Wert={val}")
                    best = max(best, val)
                    move_index += 1
        print(f"{indent}{move_path} Bester Wert für O (Maximizer) an Tiefe {depth}: {best}")
        return best
    else:
        best = math.inf
        move_index = 1
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1
                    child_path = f"{move_path}.{move_index}"
                    val = minimax(board, depth + 1, not is_maximizing, child_path)
                    board[i][j] = 0
                    print(f"{indent}{child_path} Zug X->({i},{j}), Wert={val}")
                    best = min(best, val)
                    move_index += 1
        print(f"{indent}{move_path} Bester Wert für X (Minimizer) an Tiefe {depth}: {best}")
        return best



def find_best_move(board):
    """Findet den besten Zug für die KI mittels Minimax."""

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



def player_turn(board):
    """Lässt den Spieler 'X' einen Zug machen, indem er eine Zahl (1-9) eingibt."""
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
    """Führt ein vollständiges Tic-Tac-Toe-Spiel durch.
       Spieler ist 'X', KI ist 'O'.
       Der Spieler beginnt."""

    print("Willkommen zu Tic-Tac-Toe mit unbesiegbarer KI!")
    print("Spieler ist 'X', KI ist 'O'.")
    print("Das Spielfeld hat folgende Nummerierung:")
    
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print()

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

# Hauptprogramm starten
if __name__ == "__main__":
    tic_tac_toe()




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
# Implementiere eine Simulation, in der die zufällige KI (`ai_random`) aus dem
# letzten Kapitel gegen die Minimax-KI antritt. Lass sie 100 Spiele spielen und
# zähle die Siege, Niederlagen und Unentschieden für beide KIs.


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

...


def ai_random(board):
    """Funktion für die zufällige KI"""
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == 0:
            return row, col



def simulate_random_vs_minimax(rounds=100):
    """Funktion, die die zufällige KI gegen die Minimax-KI antreten lässt."""
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


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


