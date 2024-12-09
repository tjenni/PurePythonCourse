#              __________________________
#       ______|                          |_____
#       \     |    14.3 TIC-TAC-TOE      |    /
#        )    |__________________________|   (
#       /________)                   (________\     8.12.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Tic-Tac-Toe, auch bekannt als „Kreis und Kreuz“, ist eines der bekanntesten
# Strategiespiele der Welt. Es bietet eine einfache Möglichkeit, grundlegende
# Konzepte wie Zuglogik, Siegbedingungen und künstliche Intelligenz (KI) zu
# implementieren.

# In diesem Kapitel lernst du, wie du Tic-Tac-Toe in Python umsetzt. Wir starten
# mit einer textbasierten Version des Spiels und erweitern sie, um einfache
# KI-Strategien hinzuzufügen.


# _____________________________
#                             /
# Regeln von Tic-Tac-Toe     (
# ____________________________\

# - Tic-Tac-Toe wird auf einem 3x3-Gitter gespielt.
#
# - Zwei Spieler (X und O) setzen abwechselnd ihre Markierungen auf leere Felder.
#
# - Ziel ist es, eine horizontale, vertikale oder diagonale Linie mit drei
#   eigenen Markierungen zu bilden.
#
# - Das Spiel endet unentschieden, wenn alle Felder belegt sind und kein Spieler
#   eine Linie bilden konnte.



# _____________________________
#                             /
# Kodierung des Spielfelds   (
# ____________________________\

# In unserem Tic-Tac-Toe-Spiel werden die Spieler und das Spielfeld wie folgt kodiert:

#  1  : Die künstliche Intelligenz (O)
# -1  : Der menschliche Spieler (X)
#  0  : Ein leeres Feld

# Diese Zahlenwerte haben mehrere Vorteile:

# 1. Mathematische Verarbeitung:
#    Gewinnkombinationen lassen sich leicht überprüfen, da ihre Summe eindeutig ist.
#    Beispiel: Drei aufeinanderfolgende 1-Werte ergeben 3 (KI gewinnt),
#    während drei (-1)-Werte -3 ergeben (Spieler gewinnt).

# 2. Kompakte Darstellung:
#    Das Spielfeld wird als Liste von Listen gespeichert, was speichereffizient ist
#    und gut in Schleifen verarbeitet werden kann.

# 3. Flexibilität:
#    Diese Kodierung lässt sich problemlos auf größere Spielfelder erweitern,
#    z. B. für ein 4x4- oder 5x5-Spiel.

# Beispiel: Eine Spielsituation wird wie folgt kodiert:
'''
board = [
    [1, -1,  0],
    [0,  1,  0],
    [-1,  0,  1]
]
'''
# Diese Matrix repräsentiert das Spielfeld:
# X | O |  
# --+---+--
#   | X |  
# --+---+--
# O |   | X

# Hinweis:
# Um diese interne Kodierung für den Benutzer verständlich zu machen,
# wird die Spielfeldanzeige durch die Funktion `print_board` so angepasst,
# dass die Zahlenwerte wie folgt übersetzt werden:
#   -  1  → "O"
#   - -1  → "X"
#   -  0  → " " (leeres Feld)



# _____________________________
#                              /
# Implementierung des Spiels  (
# _____________________________\

# Im folgenden Beispiel wird Tic-Tac-Toe in der Konsole gespielt. Ein Spieler
# tritt gegen eine einfache KI an, die zufällig gültige Züge auswählt.
# Das Spielfeld wird durch eine Liste von Listen 


import random

# IDs zur Repräsentation der Spieler und der KI
# Wir verwenden Ganzzahlen anstelle von Zeichen:
#  1  : KI (O)
# -1 : Spieler (X)
#  0  : leeres Feld
ID_AI = 1
ID_PLAYER = -1

# Dictionary zur Zuordnung der internen IDs zu Symbolen auf dem Spielfeld.
# Damit wird aus den Zahlen (1,0,-1) ein lesbarer Spielstein:
#  1  → "O"
#  0  → " " (leeres Feld)
# -1  → "X"
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

    Überprüft alle Gewinnmöglichkeiten (3 in einer Reihe: horizontal, vertikal, diagonal).

    Funktionsweise:
    - Jede Dreier-Reihe (Zeile, Spalte, Diagonale) wird auf ihre Summe geprüft.
    - Bei allen O-Feldern ist der Wert 1, bei allen X-Feldern -1.
    - Drei O in einer Reihe ergeben die Summe 3 (1+1+1),
    - Drei X in einer Reihe ergeben die Summe -3 (-1-1-1).

    Parameter:
        board (list): Aktuelles Spielfeld.

    Rückgabe:
        1  zurück, wenn die KI (O) gewonnen hat
       -1  zurück, wenn der Spieler (X) gewonnen hat
        0  wenn noch kein Gewinner feststeht
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


def player_turn(board, id=ID_PLAYER):
    """Lässt den menschlichen Spieler einen Zug machen.

    Der Spieler gibt eine Zahl zwischen 1 und 9 ein, um ein Feld zu wählen.
    Die Felder sind wie folgt nummeriert:
      1 | 2 | 3
      -----------
      4 | 5 | 6
      -----------
      7 | 8 | 9
    
    Dabei entsprechen die Zahlen Positionen auf dem 3x3-Board:
    Ein Zug "5" bedeutet z. B. Mitte des Spielfeldes (board[1][1]).

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


def moves_left(board):
    """Gibt eine Liste aller freien (leeren) Felder auf dem Spielfeld zurück.
    Jedes freie Feld wird als Tupel (zeile, spalte) in die Liste aufgenommen.
    
    Parameter:
        board (list): Das aktuelle Spielfeld.

    Rückgabe:
        list: Liste mit den Koordinaten der leeren Felder.
    """
    moves = []
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 0:
                moves.append((i,j))
            
    return moves


def ai_random(board, id=ID_AI):
    """Zufällige KI, die einen freien Platz per Zufall wählt.
    
    Wenn es keine freien Felder mehr gibt, wird ein Fehler ausgelöst, 
    was in diesem einfachen Beispiel aber nur bedeutet, dass das Spiel ohnehin vorbei ist.

    Parameter:
        board (list): Das aktuelle Spielfeld.
        id (int): ID der KI (normalerweise 1 für 'O').
    """
    
    moves = moves_left(board)

    assert(
        len(moves) > 0, 
        "AI: Ich kann nicht ziehen. Es gibt keine freien Felder mehr."
    )
    
    row, col = random.choice(moves)
    board[row][col] = id

    print(f"Die KI wählt Feld {row * 3 + col + 1}.")
    return


def tic_tac_toe(symbols=DEFAULT_SYMBOLS):
    """Führt ein einzelnes Tic-Tac-Toe-Spiel durch und gibt den Gewinner zurück.

    Spielablauf:
    - Es wird ein leeres 3x3-Brett erstellt.
    - Der Spieler (X) und die KI (O) führen abwechselnd Züge aus.
    - Nach jedem Zug wird geprüft, ob ein Gewinner feststeht.
    - Sollte nach 9 Zügen kein Gewinner vorhanden sein, endet das Spiel unentschieden.

    Parameter:
        symbols (dict): Dictionary zur Übersetzung der IDs in lesbare Zeichen.

    Rückgabe:
        int: Gewinner-ID (1 für O, -1 für X, 0 für Unentschieden)
    """

    print("Tic-Tac-Toe")
    print("===========")
    print(f"Spieler ist '{symbols[ID_PLAYER]}', KI ist '{symbols[ID_AI]}'.")
    print("Das Spielfeld hat folgende Nummerierung:\n")
    
    # Anleitung, wie die Felder nummeriert sind.
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    
    # Leeres Spielfeld initialisieren
    board = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    winner = 0 # 0 bedeutet noch kein Gewinner

    # max. 9 Züge (0 bis 8): Danach ist das Spielfeld voll.
    for turn in range(9):
        print(f"\nZug {turn+1}")
        print_board(board)

        if turn % 2 == 0:
            # Gerade Züge: Spieler ist dran
            player_turn(board)
        else:
            # Ungerade Züge: KI ist dran
            ai_random(board)

        # Nach jedem Zug überprüfen wir, ob jemand gewonnen hat.
        winner = check_winner(board)
        if winner != 0:
            break

    # Am Ende des Spiels den finalen Zustand anzeigen
    print_board(board)
    if winner !=0:
        print(f"{symbols[winner]} hat gewonnen!")
    else:
        print("Das Spiel endet unentschieden.")

    return winner


def simulate_player_vs_random(rounds=10):
    """Simuliert mehrere Spielrunden zwischen Spieler und KI und zeigt eine Statistik.

    Parameter:
        rounds (int): Anzahl der Runden, die gespielt werden sollen.
    
    Ablauf:
    - Es wird mehrmals hintereinander tic_tac_toe() ausgeführt.
    - Nach jeder Runde wird der Spielstand ausgegeben.
    """
    
    # Punkte-Stand halten fest, wie oft Spieler, KI oder Unentschieden herauskommen.
    score = {
        "Spieler": 0, 
        "KI": 0, 
        "Unentschieden": 0
    }

    for game in range(rounds):
        # Ein Spiel ausführen
        result = tic_tac_toe()
        
        # Auswerten, wer gewonnen hat
        if result == ID_AI:
            score["KI"] += 1
        elif result == ID_PLAYER:
            score["Spieler"] += 1
        else:
            score["Unentschieden"] += 1

        # Zwischenstand ausgeben
        print(f"\nZwischenstand Runde {game+1}:")
        print("======================")

        for name, punkte in score.items():
            print(f"{name}: {punkte}")

        print()


# Wenn das Skript direkt ausgeführt wird (nicht importiert), starten wir die Simulation.
if __name__ == "__main__":
    simulate_player_vs_random()




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# In diesem Kapitel hast du gelernt, wie man Tic-Tac-Toe umsetzt:
#
# 1. Regeln und Spielablauf: 
#    Spieler und KI setzen abwechselnd Markierungen auf ein 3x3-Gitter.
#
# 2. Textbasierte Implementierung: 
#    Du hast ein simples Tic-Tac-Toe-Spiel in der Konsole erstellt.
#
# 3. Spielmechaniken: 
#    Funktionen zur Spieler- und KI-Interaktion, zur Spielfeldanzeige und zur Siegprüfung.

# Tic-Tac-Toe bietet eine ideale Grundlage, um KI-Konzepte wie den Minimax-Algorithmus 
# zu erlernenund Strategien für optimale Spielweisen zu entwickeln. Mit diesen Grundlagen 
# kannst du das Spiel erweitern und anpassen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Schreibe eine Funktion `choose_side()`, mit der der Spieler auswählen kann, 
# ob er als 'X' oder als 'O' spielen möchte. Verwende diese Funktion vor dem Start 
# des Spiels, um festzulegen, wer zuerst zieht.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Füge nach jedem Spiel eine Ausgabe hinzu, in der die Gesamtanzahl der 
# gespielten Züge angezeigt wird. So kann der Spieler am Ende sehen, 
# wie lange die Partie gedauert hat.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Implementiere eine Funktion `simulate_random_vs_random(n)`, die `n` Spiele ohne 
# Benutzereingabe durchführt (zum Beispiel KI gegen KI) und am Ende eine 
# Statistik der Gewinne, Niederlagen und Unentschieden ausgibt. Lasse dabei 
# die Minimax-KI gegen sich selbst oder gegen eine andere Strategie spielen. 
# Bestimme, wie sich die Ergebnisse im Vergleich zu einer kleineren oder 
# größeren Anzahl von Spielen verändern.


# Füge hier deine Lösung ein.



#                   Wo soll ich setzen?
#                       \
#                            ,,,,,,
#      O | O |              /e   ''(
#      O | X | X           (_ `     \
#        | X |            ___>       \
#                        / ,_\-.___   \_
#                       /  _)/ /        \
#                       |  \  /  ` _     |
#                     __\____/    /    ' |
#                    /  _        /______/
#                   / _/ \,_____/o     (
#                   \__)/`              \
#                      /   \__________/_/_
#                    _/     \  \   )/     \
#                   /      /   |  /\      (
#                   \_____/ ___/  \ \  _/  \
#              ______/_/___|_|     ) \     /
#             /       o\     o\   /  /    /\
#     b'ger,,,'-----^--',,,,,,',,|_,,\_ ,,\/,,
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
# Schreibe eine Funktion `choose_side()`, mit der der Spieler auswählen kann, 
# ob er als 'X' oder als 'O' spielen möchte. Verwende diese Funktion vor dem Start 
# des Spiels, um festzulegen, wer zuerst zieht.


'''
def choose_side():
    while True:
        side = input("Möchtest du als 'X' oder als 'O' spielen? ").upper()
        if side in ['X', 'O']:
            print(f"Du spielst als '{side}'.")
            if side == 'X':
                return {1: "O", 0: " ", -1: "X"}
            else:
                return {1: "X", 0: " ", -1: "O"}
        else:
            print("Ungültige Eingabe. Bitte gib 'X' oder 'O' ein.")


def tic_tac_toe():
    ...
    symbols = choose_side()

'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Füge nach jedem Spiel eine Ausgabe hinzu, in der die Gesamtanzahl der 
# gespielten Züge angezeigt wird. So kann der Spieler am Ende sehen, 
# wie lange die Partie gedauert hat.


'''
def tic_tac_toe():
    ...
    # Spielschleife
    for turn in range(start, 9):
        print(f"\nZug {turn+1}")
        print_board(board)

        if turn % 2 == 0:
            player_turn(board)
        else:
            ai_random(board)

        winner = check_winner(board)
        if winner != 0:
            break

    # Spielende
    print_board(board)
    print(f"Anzahl Spielzüge: {turn+1}")
    if winner !=0:
        print(f"{symbols[winner]} hat gewonnen!")
    else:
        print("Das Spiel endet unentschieden.")

    return winner

'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Implementiere eine Funktion `simulate_random_vs_random(n)`, die `n` Spiele ohne 
# Benutzereingabe durchführt (zum Beispiel KI gegen KI) und am Ende eine 
# Statistik der Gewinne, Niederlagen und Unentschieden ausgibt. Lasse dabei 
# die Minimax-KI gegen sich selbst oder gegen eine andere Strategie spielen. 
# Bestimme, wie sich die Ergebnisse im Vergleich zu einer kleineren oder 
# größeren Anzahl von Spielen verändern.


'''
def tic_tac_toe_random_vs_random(symbols=DEFAULT_SYMBOLS):
    
    ...

    for turn in range(9):
        if turn % 2 == 0:
            ai_random(board, ID_AI, False)
        else:
            ai_random(board, ID_PLAYER, False)

        winner = check_winner(board)
        if winner:
            return winner

    return 0



def simulate_random_vs_random(rounds=100):
    """Simulation mehrer Runden."""

    score = {"KI O": 0, "KI X": 0, "Unentschieden": 0}
    for game in range(rounds):
        result = tic_tac_toe_random_vs_random()
        
        if result == ID_AI:
            score["KI O"] += 1
        elif result == ID_PLAYER:
            score["KI X"] += 1
        else:
            score["Unentschieden"] += 1

        print(f"\nErgebnisse nach Runde {game+1}:")
        for name, punkte in score.items():
            print(f"{name}: {punkte}")
        print()



# Hauptprogramm starten
if __name__ == "__main__":
    simulate_random_vs_random()

'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

