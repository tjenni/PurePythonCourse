#              ______________________________________
#       ______|                                      |_____
#       \     |   14.5 MONTE-CARLO-TREE-SEARCH (MCTS) |    /
#        )    |______________________________________|   (
#       /________)                               (________\     22.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Monte-Carlo-Tree-Search (MCTS) ist ein moderner Algorithmus, der häufig in Strategiespielen verwendet wird.
# Anders als Minimax oder Alpha-Beta-Pruning basiert MCTS auf zufälligen Simulationen, um gute Züge zu finden.

# ________________________
#                        /
# Funktionsweise         (
# ________________________\

# 1. **Zufällige Erkundung:**
#    - MCTS erkundet mögliche Züge, indem es zufällige Partien simuliert.
#
# 2. **Baumstruktur:**
#    - Jeder Knoten im Baum repräsentiert einen Spielzustand. Die Knoten werden mit
#      jeder Simulation erweitert.
#
# 3. **4 Schritte:**
#    - **Selektion:** Wähle vielversprechende Knoten basierend auf ihrer Erfolgsrate.
#    - **Expansion:** Füge neue Knoten hinzu, die noch nicht erkundet wurden.
#    - **Simulation:** Spiele eine zufällige Partie ab dem neuen Knoten.
#    - **Rückpropagation:** Aktualisiere die Erfolgswerte entlang des Baumes.

# ________________________________
#                                /
# Implementierung in Tic-Tac-Toe (
# ________________________________\

# Im folgenden Beispiel verwenden wir MCTS, um in Tic-Tac-Toe Züge zu simulieren.

import random
from math import sqrt, log


class Node:
    """
    Repräsentiert einen Knoten im Monte-Carlo-Baum.
    """
    def __init__(self, state, parent=None):
        self.state = state  # Spielfeldzustand
        self.parent = parent  # Vorgänger-Knoten
        self.children = []  # Nachfolger-Knoten
        self.visits = 0  # Anzahl der Besuche
        self.wins = 0  # Anzahl der Siege

    def is_fully_expanded(self):
        """
        Prüft, ob alle möglichen Züge von diesem Knoten bereits erkundet wurden.
        """
        return len(self.children) == len(get_legal_moves(self.state))

    def best_child(self, exploration_weight=1.4):
        """
        Wählt das beste Kind basierend auf der UCT-Formel.
        """
        return max(
            self.children,
            key=lambda child: (child.wins / child.visits) + exploration_weight * sqrt(log(self.visits) / child.visits)
        )


def get_legal_moves(board):
    """
    Gibt eine Liste der legalen Züge zurück.
    """
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i, j))
    return moves


def make_move(board, move, player):
    """
    Führt einen Zug auf dem Spielfeld aus.
    """
    new_board = [row[:] for row in board]
    new_board[move[0]][move[1]] = player
    return new_board


def check_winner(board):
    """
    Prüft, ob ein Spieler gewonnen hat.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None


def is_draw(board):
    """
    Prüft, ob das Spiel unentschieden ist.
    """
    return all(cell != " " for row in board for cell in row)


def simulate_random_game(board, player):
    """
    Simuliert eine zufällige Partie.
    """
    current_player = player
    while True:
        winner = check_winner(board)
        if winner:
            return winner
        if is_draw(board):
            return None

        move = random.choice(get_legal_moves(board))
        board = make_move(board, move, current_player)
        current_player = "X" if current_player == "O" else "O"


def mcts(root, iterations=1000):
    """
    Führt Monte-Carlo-Tree-Search ab einem gegebenen Knoten aus.
    """
    for _ in range(iterations):
        # 1. Selektion
        node = root
        while node.is_fully_expanded() and node.children:
            node = node.best_child()

        # 2. Expansion
        if not node.is_fully_expanded():
            for move in get_legal_moves(node.state):
                child_state = make_move(node.state, move, "O" if len(get_legal_moves(node.state)) % 2 == 0 else "X")
                if all(child.state != child_state for child in node.children):
                    child = Node(child_state, parent=node)
                    node.children.append(child)
                    node = child
                    break

        # 3. Simulation
        winner = simulate_random_game(node.state, "O" if len(get_legal_moves(node.state)) % 2 == 0 else "X")

        # 4. Rückpropagation
        while node:
            node.visits += 1
            if winner == "O":
                node.wins += 1
            elif winner == "X":
                node.wins -= 1
            node = node.parent


def find_best_move_mcts(board, iterations=1000):
    """
    Findet den besten Zug mithilfe von Monte-Carlo-Tree-Search.
    """
    root = Node(board)
    mcts(root, iterations)
    return max(root.children, key=lambda child: child.visits).state


def tic_tac_toe_with_mcts():
    """
    Hauptspielschleife für Tic-Tac-Toe mit MCTS.
    """
    print("Willkommen zu Tic-Tac-Toe mit Monte-Carlo-Tree-Search!")
    print("Spieler ist 'X', KI ist 'O'.")
    print("Das Spielfeld hat folgende Nummerierung:")
    print("1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9\n")

    board = [[" " for _ in range(3)] for _ in range(3)]

    for turn in range(9):
        for row in board:
            print(" | ".join(row))
            print("-" * 5)

        if turn % 2 == 0:
            print("Dein Zug:")
            while True:
                try:
                    move = int(input("Wähle ein Feld (1-9): ")) - 1
                    row, col = divmod(move, 3)
                    if board[row][col] == " ":
                        board[row][col] = "X"
                        break
                    else:
                        print("Dieses Feld ist bereits belegt.")
                except (ValueError, IndexError):
                    print("Ungültige Eingabe. Wähle eine Zahl zwischen 1 und 9.")
        else:
            print("Zug der KI:")
            board = find_best_move_mcts(board)

        winner = check_winner(board)
        if winner:
            for row in board:
                print(" | ".join(row))
                print("-" * 5)
            print(f"{winner} hat gewonnen!")
            return

    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("Das Spiel endet unentschieden.")


# Hauptprogramm starten
if __name__ == "__main__":
    tic_tac_toe_with_mcts()


# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# In diesem Kapitel hast du gelernt, wie Monte-Carlo-Tree-Search funktioniert:
#
# 1. **Zufällige Simulationen:** MCTS nutzt zufällige Partien, um Entscheidungen zu treffen.
#
# 2. **Baumstruktur:** Jeder Knoten im Baum repräsentiert einen Spielzustand, und 
#    die Werte der Knoten werden durch Simulationen aktualisiert.
#
# 3. **Effizienz:** MCTS findet gute Züge ohne den gesamten Spielbaum zu durchsuchen.

# MCTS ist besonders nützlich für Spiele mit großer Komplexität, wie z. B. Go oder Schach,
# und bildet die Grundlage vieler moderner KI-Systeme.


# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Passe den Algorithmus an, um mit einem 4x4-Tic-Tac-Toe-Spielfeld zu funktionieren.


# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Optimiere den Algorithmus, indem du die Anzahl der Iterationen basierend auf der # verbleibenden Zeit für den Zug berechnest. Stelle sicher, dass MCTS auch in begrenzter Zeit gute Ergebnisse liefert.


# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erweitere MCTS, um einen zusätzlichen Parameter für die Spieltiefe einzuführen.
# Dieser Parameter sollte die Anzahl der Züge begrenzen, die in einer Simulation durchgeführt werden.


# ___________
#            \
# Aufgabe 4  /
# __________/
#
# Implementiere eine visuelle Ausgabe des MCTS-Baumes nach mehreren Iterationen.
# Zeige für jeden Knoten die Anzahl der Besuche, die Gewinnrate und die Spielzustände an.


# ___________
#            \
# Aufgabe 5  /
# __________/
#
# Wende MCTS auf ein anderes Spiel an, wie z. B. Connect Four oder ein 2D-Grid-Spiel,
# und analysiere, wie gut der Algorithmus in diesen Szenarien funktioniert.