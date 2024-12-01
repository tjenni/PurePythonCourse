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
# - Zwei Spieler (X und O) setzen abwechselnd ihre Markierungen auf leere Felder.
# - Ziel ist es, eine horizontale, vertikale oder diagonale Linie mit drei
#   eigenen Markierungen zu bilden.
# - Das Spiel endet unentschieden, wenn alle Felder belegt sind und kein Spieler
#   eine Linie bilden konnte.


# ____________________________
#                             /
# Implementierung des Spiels  (
# ____________________________\

# Im folgenden Beispiel wird Tic-Tac-Toe in der Konsole gespielt. Ein Spieler
# tritt gegen eine einfache KI an, die zufällig gültige Züge auswählt.

import random

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
    # Horizontale und vertikale Linien
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]

    # Diagonale Linien
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def player_turn(board):
    """
    Führt den Zug des Spielers aus.
    """
    while True:
        try:
            move = int(input("Wähle ein Feld (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = "X"
                return
            else:
                print("Dieses Feld ist bereits belegt. Wähle ein anderes.")
        except (ValueError, IndexError):
            print("Ungültige Eingabe. Wähle eine Zahl zwischen 1 und 9.")


def ai_turn(board):
    """
    Führt den Zug der KI aus. Wählt ein zufälliges, freies Feld.
    """
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = "O"
            print(f"Die KI wählt Feld {row * 3 + col + 1}.")
            return


def tic_tac_toe():
    """
    Hauptspielschleife für Tic-Tac-Toe.
    """
    print("Willkommen zu Tic-Tac-Toe!")
    print("Spieler ist 'X', KI ist 'O'.")
    print("Das Spielfeld hat folgende Nummerierung:")
    print("1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9\n")

    # Spielfeld initialisieren
    board = [[" " for _ in range(3)] for _ in range(3)]

    # Spielschleife
    for turn in range(9):
        print_board(board)

        if turn % 2 == 0:
            print("Dein Zug:")
            player_turn(board)
        else:
            print("Zug der KI:")
            ai_turn(board)

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} hat gewonnen!")
            return

    print_board(board)
    print("Das Spiel endet unentschieden.")


# Hauptprogramm starten
if __name__ == "__main__":
    tic_tac_toe()




# ____________________________
#                             /
# Erweiterungsmöglichkeiten  (
# ____________________________\

# 1. **Minimax-Algorithmus für die KI:**
#    - Implementiere eine KI, die den optimalen Zug mithilfe des Minimax-Algorithmus berechnet.
#    - Diese Technik bewertet alle möglichen Züge und wählt den besten aus.

# 2. **Grafische Oberfläche:**
#    - Nutze `arcade`, um das Spielfeld grafisch darzustellen.
#    - Erlaube dem Spieler, Felder durch Klicken mit der Maus auszuwählen.

# 3. **Variationen des Spiels:**
#    - Ändere die Spielfeldgröße (z. B. 4x4 oder 5x5).
#    - Füge neue Siegbedingungen hinzu, wie z. B. vier Markierungen in einer Reihe.

# 4. **Spieler vs. Spieler:**
#    - Erstelle einen Modus, in dem zwei Spieler auf demselben Gerät spielen können.

# 5. **Netzwerkspiel:**
#    - Implementiere einen Online-Modus, in dem Spieler gegeneinander antreten können.

# 6. **Zeitlimit:**
#    - Füge eine Zeitbegrenzung für jeden Zug hinzu, um das Spiel dynamischer zu gestalten.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# In diesem Kapitel hast du gelernt, wie man Tic-Tac-Toe umsetzt:
#
# 1. **Regeln und Spielablauf:** Spieler und KI setzen abwechselnd Markierungen auf ein 3x3-Gitter.
# 2. **Textbasierte Implementierung:** Du hast ein simples Tic-Tac-Toe-Spiel in der Konsole erstellt.
# 3. **Spielmechaniken:** Funktionen zur Spieler- und KI-Interaktion, zur Spielfeldanzeige und zur Siegprüfung.

# Tic-Tac-Toe bietet eine ideale Grundlage, um KI-Konzepte wie den Minimax-Algorithmus zu erlernen
# und Strategien für optimale Spielweisen zu entwickeln. Mit diesen Grundlagen kannst du das Spiel
# erweitern und anpassen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Füge eine Siegbedingung für ein größeres Spielfeld (z. B. 4x4 oder 5x5) hinzu.
# Schreibe eine Funktion `check_winner_large(board, n)`, die überprüft, ob ein Spieler
# n Markierungen in einer Reihe hat.


# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Implementiere den Minimax-Algorithmus für die KI. Die KI soll den optimalen Zug
# basierend auf allen möglichen Szenarien berechnen.


# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine grafische Version von Tic-Tac-Toe mit `arcade`. Zeichne das Spielfeld
# und die Markierungen und erlaube dem Spieler, Züge mit der Maus auszuführen.