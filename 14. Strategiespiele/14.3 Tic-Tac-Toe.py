#              ____________________________
#       ______|                            |_____
#       \     |    14.2 TIC-TAC-TOE        |    /
#        )    |____________________________|   (
#       /________)                      (________\     22.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

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
#                              /
# Implementierung des Spiels  (
# _____________________________\

# Im folgenden Beispiel wird Tic-Tac-Toe in der Konsole gespielt. Ein Spieler
# tritt gegen eine einfache KI an, die zufällig gültige Züge auswählt.


import random



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
    # Horizontale und vertikale Linien
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != 0:
            return board[0][i]

    # Diagonale Linien
    if board[0][0] == board[1][1] and  board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] and  board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]

    return None


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


# Hauptspielschleife für Tic-Tac-Toe.
def tic_tac_toe(verbose=True):
    
    if verbose:
        print("Tic-Tac-Toe")
        print("===========")
        print("Spieler ist 'X', KI ist 'O'.")
        print("Das Spielfeld hat folgende Nummerierung:\n")
        
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")
        
    # Spielfeld initialisieren
    board = [[0 for _ in range(3)] for _ in range(3)]

    # Spielschleife
    for turn in range(9):
        if verbose:
            print(f"\nZug {turn+1}")
            print_board(board)

        if turn % 2 == 0:
            player_turn(board)
        else:
            ai_random(board, -1, verbose)

        winner = check_winner(board)
        if winner:
            if verbose:
                print_board(board)
                if winner == 1:
                    print("X hat gewonnen!")
                else:
                    print("O hat gewonnen!")
                
            return winner

    print_board(board)
    print("Das Spiel endet unentschieden.")
    return 0


# Hauptprogramm starten

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

# Tic-Tac-Toe bietet eine ideale Grundlage, um KI-Konzepte wie den Minimax-Algorithmus zu erlernen
# und Strategien für optimale Spielweisen zu entwickeln. Mit diesen Grundlagen kannst du das Spiel
# erweitern und anpassen.




# ____________________________
#                             /
# Erweiterungsmöglichkeiten  (
# ____________________________\

# 1. Minimax-Algorithmus für die KI:
#    - Implementiere eine KI, die den optimalen Zug mithilfe des Minimax-Algorithmus berechnet.
#      
#    - Diese Technik bewertet alle möglichen Züge und wählt den besten aus.

# 2. Grafische Oberfläche:
#    - Nutze `arcade`, um das Spielfeld grafisch darzustellen.
#
#    - Erlaube dem Spieler, Felder durch Klicken mit der Maus auszuwählen.

# 3. Variationen des Spiels:
#    - Ändere die Spielfeldgröße (z. B. 4x4 oder 5x5).
#
#    - Füge neue Siegbedingungen hinzu, wie z. B. vier Markierungen in einer Reihe.

# 4. Spieler vs. Spieler:
#    - Erstelle einen Modus, in dem zwei Spieler auf demselben Gerät spielen können.

# 5. Netzwerkspiel:
#    - Implementiere einen Online-Modus, in dem Spieler gegeneinander antreten können.

# 6. Zeitlimit:
#    - Füge eine Zeitbegrenzung für jeden Zug hinzu, um das Spiel dynamischer zu gestalten.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Lass zwei Random-KIs 500 Partien gegeneinander spielen. 








