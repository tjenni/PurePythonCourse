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


ID_AI = 1
ID_PLAYER = -1

DEFAULT_SYMBOLS = {ID_AI: "O", 0: " ", ID_PLAYER: "X"}



def print_board(board, symbols=DEFAULT_SYMBOLS):
    """Gibt das Tic-Tac-Toe-Spielfeld formatiert auf der Konsole aus.

    Parameter:
        board (list): Das aktuelle Spielfeld als Liste von Listen.
        symbols (dict): Ein Dictionary, das die IDs (1, 0, -1) auf Symbole ("O", " ", "X") mappt.
    """

    col_sep = "|"             # Trennzeichen zwischen Spalten
    row_sep = "---+---+---"   # Trennzeichen zwischen Zeilen

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            print(f" {symbols[cell]} ", end="")

            # Falls wir nicht am Ende der Zeile sind, drucken wir noch ein Trennsymbol.
            if j < len(row) - 1:
                print(col_sep, end="")

        # Am Ende jeder Zeile, außer der letzten, fügen wir eine Trennlinie ein.
        if i < len(board) - 1:
            print("\n" + row_sep)

    print("\n")



def check_winner(board):
    """Prüft, ob ein Spieler gewonnen hat und gibt den Gewinner zurück.
    
    Parameter:
        board (list): Aktuelles Spielfeld.

    Rückgabe:
        int: Gewinner-ID (1 für O, -1 für X, 0 für Unentschieden)
    """
    
    for i in range(3):
        # Zeilen überprüfen
        if abs(board[i][0] + board[i][1] + board[i][2]) == 3:
            return board[i][0]
        # Spalten überprüfen
        if abs(board[0][i] + board[1][i] + board[2][i]) == 3:
            return board[0][i]

    # Hauptdiagonale überprüfen (links oben nach rechts unten)
    if abs(board[0][0] + board[1][1] + board[2][2]) == 3:
        return board[0][0]

    # Nebendiagonale überprüfen (rechts oben nach links unten)
    if abs(board[0][2] + board[1][1] + board[2][0]) == 3:
        return board[0][2]

    # Keine Gewinnkombination gefunden
    return 0



def evaluate(board):
    """
    Bewertet den Zustand des Boards aus Sicht der KI:
    
    Diese Bewertung wird für den Minimax-Algorithmus verwendet, um zu entscheiden,
    welche Züge vorteilhaft sind.

    Parameter:
        board (list): Das Spielfeld.

    Rückgabe:
        int: Bewertung des Boards (+10, -10 oder 0)
    """
    winner = check_winner(board)
    if winner == 1:
        return 10
    elif winner == -1:
        return -10
    return 0



def is_move_left(board):
    """
    Überprüft, ob es noch freie Felder (0) auf dem Board gibt.
    Ist das nicht der Fall, ist das Board voll, und weitere Züge sind unmöglich.

    Parameter:
        board (list): Das Spielfeld.

    Rückgabe:
        bool: True, wenn noch freie Felder vorhanden sind, sonst False.
    """
    for row in board:
        if 0 in row:
            return True
    return False



def minimax(board, depth, id):
    """
    Der Minimax-Algorithmus zur Bestimmung des optimalen Zugs.

    Parameter:
        board (list): Das Spielfeld.
        depth (int): Aktuelle Tiefe im Suchbaum (kann genutzt werden, um tiefe Züge zu bewerten).
        id (int): Entweder 1 (KI) oder -1 (Spieler), um zu wissen, wer gerade "dran" ist.

    Rückgabe:
        int: Der beste Score, den der jeweilige Spieler (oder die KI) erreichen kann.
    """
    
    score = evaluate(board)

    # Abbruchbedingung: Endzustand erreicht (Gewinn oder kein Move left)
    if score != 0:
        return score
    if not is_move_left(board):
        return 0  # Unentschieden

    # Best-Variable wird initialisiert:
    # Für die KI (id=1) wollen wir am Ende den maximalen Wert haben.
    # Für den Spieler (id=-1) den minimalen Wert.
    best = -id * math.inf

    # Alle Züge durchprobieren
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:

                # Zug platzieren
                board[i][j] = id  

                # Rekursiver Aufruf mit dem anderen Spieler (-id wechselt zwischen 1 und -1)
                value = minimax(board, depth + 1, -id)

                if id > 0:
                    # KI will maximalen Score
                    best = max(best, value)
                else:
                    # Spielerzug aus KI-Sicht: minimaler Score
                    best = min(best, value)

                # Zug zurücknehmen
                board[i][j] = 0  
    return best



def find_best_move(board, id=ID_AI):
    """
    Findet den besten Zug für den gegebenen Spieler (Standard: KI),
    indem alle möglichen Züge ausprobiert und mit Minimax bewertet werden.

    Parameter:
        board (list): Das Spielfeld.
        id (int): ID des Spielers, für den der beste Zug gefunden werden soll (Standard: KI)

    Rückgabe:
        tuple: (i, j) - die Koordinaten des besten Zugs.
    """

    best_value = -id * math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = id # Zug platzieren
                move_value = minimax(board, 0, -id)
                board[i][j] = 0 # Zug zurücknehmen
                
                if id > 0 and move_value > best_value or id < 0 and move_value < best_value:
                    best_value = move_value
                    best_move = (i, j)

    return best_move



def player_turn(board, id=ID_PLAYER):
    """Lässt den menschlichen Spieler einen Zug machen.

    Parameter:
        board (list): Aktuelles Spielfeld.
        id (int): ID des Spielers (in diesem Fall -1 für 'X').
    """
    while True:
        try:
            move = int(input("Wähle ein Feld (1-9): ")) - 1

            # divmod teilt die Zahl durch 3 und gibt Quotient und Rest zurück,
            # um die Zeile (row) und Spalte (col) im Board zu bestimmen.
            row, col = divmod(move, 3)

            # Prüfen, ob das Feld frei ist.
            if board[row][col] == 0:
                board[row][col] = id
                return
            else:
                print("Dieses Feld ist bereits belegt. Wähle ein anderes.")

        except (ValueError, IndexError):
            # ValueError: Eingabe war keine Zahl
            # IndexError: Zahl entspricht keiner gültigen Feldposition (z. B. >9 oder <1)
            print("Ungültige Eingabe. Bitte gib eine Zahl zwischen 1 und 9 ein.")



def tic_tac_toe(symbols=DEFAULT_SYMBOLS, verbose=True):
    """
    Führt ein Tic-Tac-Toe-Spiel durch, bei dem der Spieler gegen eine KI mit Minimax spielt.

    Parameter:
        symbols (dict): Übersetzung von IDs in Symbole.
        verbose (bool): Wenn True, werden Ausgaben auf der Konsole angezeigt.

    Rückgabe:
        int: Gewinner-ID (1, -1) oder 0 bei Unentschieden.
    """

    if verbose:
        print("Willkommen zu Tic-Tac-Toe mit unbesiegbarer KI!")
        print("Spieler ist 'X', KI ist 'O'.")
        print("Spielfeld-Nummerierung:\n")
        print(" 1 | 2 | 3 ")
        print("---+---+---")
        print(" 4 | 5 | 6 ")
        print("---+---+---")
        print(" 7 | 8 | 9 \n")
    
    # Initialisiere das Spielbrett.
    board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

    # Es werden maximal 9 Züge gemacht (3x3 Feld).
    for turn in range(9):
        if verbose:
            print_board(board)

        if turn % 2 == 0:
            # Spielerzug (X) in geraden Zügen
            if verbose:
                print("Dein Zug:")

            player_turn(board, ID_PLAYER)

        else:
            # KI-Zug (O) in ungeraden Zügen
            if verbose:
                print("Zug der KI:")

            best_move = find_best_move(board, ID_AI)
            board[best_move[0]][best_move[1]] = ID_AI

        # Nach jedem Zug überprüfen wir, ob jemand gewonnen hat.
        winner = check_winner(board)
        if winner != 0:
            break

    # Am Ende des Spiels den finalen Zustand anzeigen
    if verbose:
        print_board(board)
        if winner !=0:
            print(f"{symbols[winner]} hat gewonnen!")
        else:
            print("Das Spiel endet unentschieden.")

    return winner



def simulate_player_vs_minimax(rounds=10):
    """
    Führt mehrere (Standard: 10) Runden Tic-Tac-Toe zwischen Spieler und KI aus
    und zeigt eine einfache Statistik der Ergebnisse.

    Parameter:
        rounds (int): Anzahl der zu simulierenden Spiele.
    """

    score = {"Spieler": 0, "KI": 0, "Unentschieden": 0}
    
    for game in range(1, 11):
        result = tic_tac_toe()

        # Auswerten, wer gewonnen hat
        if result == 1:
            score["KI"] += 1
        elif result == -1:
            score["Spieler"] += 1
        else:
            score["Unentschieden"] += 1

        # Zwischenstand ausgeben
        print(f"\nZwischenstand Runde {game+1}:")
        print("======================")

        for name, punkte in score.items():
            print(f"{name}: {punkte}")
        print()


# Wenn das Skript direkt ausgeführt wird, starten wir die Simulation.
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

    if score in [10, -10] or not is_move_left(board) or depth == max_depth:
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


