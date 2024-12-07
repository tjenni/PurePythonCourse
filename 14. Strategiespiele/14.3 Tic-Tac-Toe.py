#              __________________________
#       ______|                          |_____
#       \     |    14.3 TIC-TAC-TOE      |    /
#        )    |__________________________|   (
#       /________)                   (________\     7.12.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

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



def ai_random(board, id=-1, verbose=True):
    """Funktion für die zufällige KI"""
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == 0:
            board[row][col] = id
            if verbose:
                print(f"Die KI wählt Feld {row * 3 + col + 1}.")
            return



def tic_tac_toe(verbose=True):
    """Führt ein vollständiges Tic-Tac-Toe-Spiel durch.
       Spieler ist 'X', KI ist 'O'.
       Der Spieler beginnt."""
    
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



def simulate_player_vs_minimax(rounds=10):
    """Simulation mehrer Runden."""

    score = {"Spieler": 0, "KI": 0, "Unentschieden": 0}
    for game in range(1, 11):
        result = tic_tac_toe()
        
        if result == 1:
            score["Spieler"] += 1
        elif result == -1:
            score["KI"] += 1
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
# Simuliere 500 Partien zwischen zwei Random-KI's.


# Füge hier deine Lösung ein.




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
# Simuliere 500 Partien zwischen zwei Random-KI's.


# Füge hier deine Lösung ein.




# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

