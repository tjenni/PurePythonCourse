#              ________________________________
#       ______|                                |_____
#       \     |    14.5 ALPHA-BETA PRUNING     |    /
#        )    |________________________________|   (
#       /________)                          (________\     9.12.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

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



def evaluate(board, depth):
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
        return 10 - depth  # Schnellerer Verlust weniger schwerwiegend
    elif winner == -1:
        return -10 + depth  # Schnellerer Sieg besser bewertet
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



def alpha_beta_pruning(board, depth, alpha, beta, id):
    """
    Der Minimax-Algorithmus zur Bestimmung des optimalen Zugs.

    Parameter:
        board (list): Das Spielfeld.
        depth (int): Aktuelle Tiefe im Suchbaum (kann genutzt werden, um tiefe Züge zu bewerten).
        id (int): Entweder 1 (KI) oder -1 (Spieler), um zu wissen, wer gerade "dran" ist.

    Rückgabe:
        int: Der beste Score, den der jeweilige Spieler (oder die KI) erreichen kann.
    """
    
    score = evaluate(board, depth)

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
                value = alpha_beta_pruning(board, depth + 1, alpha, beta, -id)

                if id > 0:
                    # KI will maximalen Score
                    best = max(best, value)
                    alpha = max(alpha, best)
                else:
                    # Spielerzug aus KI-Sicht: minimaler Score
                    best = min(best, value)
                    beta = min(beta, best)

                # Zug zurücknehmen
                board[i][j] = 0  

                # Pruning
                if beta <= alpha:
                    return best
                
    return best



def find_best_move_alpha_beta(board, id=ID_AI):
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
                move_value = alpha_beta_pruning(board, 0, -math.inf, math.inf, -id)
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



def tic_tac_toe_with_alpha_beta(symbols=DEFAULT_SYMBOLS, verbose=True):
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
        print(f"Spieler ist '{symbols[ID_PLAYER]}', KI ist '{symbols[ID_AI]}'.")
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

            best_move = find_best_move_alpha_beta(board, ID_AI)
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
