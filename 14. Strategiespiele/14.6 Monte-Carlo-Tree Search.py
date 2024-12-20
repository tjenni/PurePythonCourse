#              ________________________________________
#       ______|                                        |_____
#       \     |   14.6 MONTE-CARLO-TREE-SEARCH (MCTS)  |    /
#        )    |________________________________________|   (
#       /________)                                 (________\     22.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Monte-Carlo-Tree-Search (MCTS) ist ein moderner Algorithmus, der häufig in Strategiespielen 
# verwendet wird. 

# Der Name "Monte Carlo" stammt aus dem Bereich des Glücksspiels und bezieht sich auf das berühmte 
# Casino in Monaco. Dieser Algorithmus verwendet zufällige Simulationen, ähnlich wie Glücksspiele 
# oft auf Wahrscheinlichkeiten basieren. Die Idee ist, durch viele Stichproben in zufälligen Szenarien 
# mögliche Entscheidungen zu bewerten und die beste Wahl zu treffen.

# https://youtu.be/msl0W4A2vIs?si=_oSX4C6iS7OS3XLg

# ________________________
#                        /
# Funktionsweise         (
# ________________________\

# 1. Zufällige Erkundung:
#    - MCTS erkundet mögliche Züge, indem es zufällige Partien simuliert.
#
# 2. Baumstruktur:
#    - Jeder Knoten im Baum repräsentiert einen Spielzustand. Die Knoten werden mit
#      jeder Simulation erweitert.
#
# 3. 4 Schritte:
#    - Selektion: Wähle vielversprechende Knoten basierend auf ihrer Erfolgsrate.
#    - Expansion: Füge neue Knoten hinzu, die noch nicht erkundet wurden.
#    - Simulation: Spiele eine zufällige Partie ab dem neuen Knoten.
#    - Rückpropagation: Aktualisiere die Erfolgswerte entlang des Baumes.


# _______________________________
#                                /
# Upper Confidence Bounds (UCT) (
# _______________________________\

# Um zu entscheiden, welcher Knoten im Spielbaum als nächstes erweitert wird, verwendet MCTS die sogenannte 
# Upper Confidence Bounds for Trees (UCT)-Formel. Diese Formel balanciert zwischen zwei Strategien:
#
# 1. Exploration: Neue Züge ausprobieren, um mehr über das Spiel zu lernen.
# 2. Exploitation: Die bisher am erfolgreichsten simulierten Züge weiterverfolgen.
#
# Die UCT-Formel lautet:
#
# UCT = (Gewinnrate des Knotens) / (Anzahl der Besuche) + c * sqrt(ln(Gesamtbesuche des Elternknotens) / Anzahl der Besuche)
#
# Parameter:
# - Gewinnrate: Gewinnrate = Gewinne / Besuche des Knotens. Ein hoher Wert bedeutet, dass dieser Knoten vielversprechend ist.
# - Explorationsfaktor (c): Ein frei wählbarer Wert (oft 1.41), der bestimmt, wie stark neue Züge bevorzugt werden.
# - Gesamtbesuche: Die Anzahl der Simulationen, die vom Elternknoten aus gestartet wurden.
# - Besuche: Die Anzahl der Simulationen, die diesen spezifischen Knoten untersucht haben.
#
# Beispiel für den UCT-Wert:
# Angenommen:
# - Der Knoten A hat 30 Gewinne bei 100 Besuchen (Gewinnrate = 0.3).
# - Der Elternknoten wurde 500-mal besucht.
# - Der Explorationsfaktor c = 1.41.
#
# Der UCT-Wert wird berechnet als:
# UCT = 0.3 + 1.41 * sqrt(ln(500) / 100) ≈ 0.3 + 1.41 * 0.083 ≈ 0.417



# ________________________________
#                                /
# Implementierung in Tic-Tac-Toe (
# ________________________________\

# Im folgenden Beispiel verwenden wir MCTS, um in Tic-Tac-Toe Züge zu simulieren.

import random
import math

ID_AI = 1
ID_PLAYER = -1

DEFAULT_SYMBOLS = {ID_AI: "O", 0: " ", ID_PLAYER: "X"}


class Node:
    """
    Repräsentiert einen Knoten im Monte-Carlo-Baum. 
    Jeder Knoten repräsentiert einen spezifischen Zustand des Tic-Tac-Toe-Boards.
    """
    def __init__(self, state, player, parent=None):
        self.state = state   # Aktueller Spielzustand als 3x3-Liste
        self.player = player # Der Spieler, der als nächstes zieht (1 oder -1)
        self.parent = parent # Übergeordneter Knoten
        self.children = []   # Liste der Kindknoten
        self.visits = 0      # Wie oft wurde dieser Knoten besucht (simuliert)?
        self.wins = 0        # Angepasster Wert für Siege/Niederlagen aus Sicht des KI-Spielers (ID_AI=1)

    def is_fully_expanded(self):
        """
        Prüft, ob alle legalen Züge bereits Kindknoten erzeugt haben.
        """
        legal = get_legal_moves(self.state)
        return len(self.children) == len(legal)

    def best_child(self, exploration_weight=2):
        """
        Wählt das beste Kind basierend auf der Upper-Confidence-Bounds-Formel (UCT).
        """
        best_score = -math.inf
        best_node = None

        for child in self.children:

            exploit = child.wins / child.visits
            explore = math.sqrt(math.log(self.visits) / child.visits)
            score = exploit + exploration_weight * explore

            if score > best_score:
                best_score = score
                best_node = child

        return best_node


def print_board(board, symbols=DEFAULT_SYMBOLS):
    """Gibt das Tic-Tac-Toe-Spielfeld formatiert auf der Konsole aus."""
    col_sep = "|"
    row_sep = "---+---+---"

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            print(f" {symbols[cell]} ", end="")
            if j < len(row) - 1:
                print(col_sep, end="")
        if i < len(board) - 1:
            print("\n" + row_sep)
    print("\n")


def get_legal_moves(board):
    """Gibt eine Liste der legalen Züge (leere Felder) zurück."""
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                moves.append((i, j))
    return moves


def make_move(board, move, id):
    """Führt einen Zug auf dem Spielfeld aus und gibt das neue Board zurück."""
    
    # Erzeuge eine Kopie des Spielfelds, damit das Original nicht überschrieben wird.
    new_board = [row[:] for row in board]
    
    # Setze den Spielzug des aktuellen Spielers in die Board-Kopie.
    new_board[move[0]][move[1]] = id

    return new_board


def check_winner(board):
    """Prüft, ob ein Spieler gewonnen hat und gibt den Gewinner zurück (1, -1 oder 0)."""
    for i in range(3):
        # Zeilen
        if abs(board[i][0] + board[i][1] + board[i][2]) == 3:
            return board[i][0]
        # Spalten
        if abs(board[0][i] + board[1][i] + board[2][i]) == 3:
            return board[0][i]

    # Hauptdiagonale
    if abs(board[0][0] + board[1][1] + board[2][2]) == 3:
        return board[0][0]

    # Nebendiagonale
    if abs(board[0][2] + board[1][1] + board[2][0]) == 3:
        return board[0][2]

    return 0


def is_move_left(board):
    """
    Überprüft, ob es noch freie Felder (0) auf dem Board gibt.
    
    Parameter:
        board (list): Das Spielfeld.
    
    Rückgabe:
        bool: True, wenn noch freie Felder vorhanden sind, sonst False.
    """
    for row in board:
        if 0 in row:
            return True
    return False



def simulate_random_game(board, start_player):
    """
    Simuliert eine zufällige Partie ab gegebenem Zustand und Startspieler.
    Gibt den Gewinner zurück (1, -1) oder None bei Unentschieden.
    """
    current_player = start_player
    simulation_board = [row[:] for row in board]

    while True:
        winner = check_winner(simulation_board)
        if winner != 0:
            return winner
        if not is_move_left(simulation_board):
            return None  # Unentschieden

        moves = get_legal_moves(simulation_board)
        move = random.choice(moves)
        simulation_board = make_move(simulation_board, move, current_player)
        current_player = -current_player


def expand(node):
    """
    Erweitert den gegebenen Knoten um ein noch nicht betrachtetes Kind.
    Gibt das neu erstellte Kind zurück.
    """
    legal = get_legal_moves(node.state)
    
    # Finde einen Move, der noch nicht als Child existiert
    existing_states = [tuple(map(tuple, c.state)) for c in node.children]

    for move in legal:
        new_state = make_move(node.state, move, node.player)
        state_tuple = tuple(map(tuple, new_state))
        if state_tuple not in existing_states:
            # Nächster Spieler
            next_player = -node.player
            child = Node(new_state, next_player, parent=node)
            node.children.append(child)
            return child

    # Falls keine neuen Kinder erstellt wurden, ist der Knoten voll ausgebaut
    return None


def backpropagate(node, winner):
    """
    Aktualisiert die visits und wins-Werte entlang des Pfades zurück zur Wurzel.
    winner: Der Gewinner der Simulation (1, -1 oder None für Unentschieden)
    """
    while node is not None:
        node.visits += 1
        if winner == ID_AI:
            # KI gewinnt -> +1
            node.wins += 1
        elif winner == ID_PLAYER:
            # Spieler gewinnt -> -1
            node.wins -= 1
        # Bei Unentschieden: Keine Änderung an wins
        node = node.parent


def mcts(root, iterations=1000):
    """
    Führt Monte-Carlo-Tree-Search ab dem gegebenen Wurzelknoten aus.
    """
    for _ in range(iterations):
        # 1. Selektion
        node = root
        while node.is_fully_expanded() and node.children:
            node = node.best_child()

        # 2. Expansion
        if not node.is_fully_expanded():
            node = expand(node) or node

        # 3. Simulation
        # Der Gewinner wird von der Perspektive des aktuellen players aus simuliert.
        winner = simulate_random_game(node.state, node.player)

        # 4. Rückpropagation
        backpropagate(node, winner)


def find_best_move_mcts(board, player=ID_AI, iterations=1000):
    """
    Findet den besten Zug mithilfe von Monte-Carlo-Tree-Search.
    Gibt ein neues Board nach dem besten Zug zurück.
    """
    # Erzeuge den Wurzelknoten
    # Angenommen, der übergebene player ist dran.
    root = Node(board, player)
    mcts(root, iterations)

    # Bestes Kind anhand der gewinn-Rate auswählen
    best_child_node = None
    best_winrate = -math.inf
    for child in root.children:
        # Vermeide Division durch Null
        if child.visits > 0:
            winrate = child.wins / child.visits
            if winrate > best_winrate:
                best_winrate = winrate
                best_child_node = child

    return best_child_node.state if best_child_node else board


def player_turn(board, id=ID_PLAYER):
    """Lässt den menschlichen Spieler 'X' einen Zug machen."""
    while True:
        try:
            move_input = int(input("Wähle ein Feld (1-9): ")) - 1
            row, col = divmod(move_input, 3)
            if board[row][col] == 0:
                board[row][col] = id
                return
            else:
                print("Dieses Feld ist bereits belegt. Wähle ein anderes.")
        except (ValueError, IndexError):
            print("Ungültige Eingabe. Bitte gib eine Zahl zwischen 1 und 9 ein.")


def tic_tac_toe_with_mcts(symbols=DEFAULT_SYMBOLS, verbose=True):
    """Hauptspielschleife für Tic-Tac-Toe mit MCTS."""
    print("Willkommen zu Tic-Tac-Toe mit Monte-Carlo-Tree-Search!")
    print(f"Spieler ist '{symbols[ID_PLAYER]}', KI ist '{symbols[ID_AI]}'.")
    print("Spielfeld-Nummerierung:\n")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")

    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    # Spieler beginnt (X)
    for turn in range(9):
        if verbose:
            print_board(board)

        if turn % 2 == 0:
            # Spielerzug
            print("Dein Zug:")
            player_turn(board, ID_PLAYER)
        else:
            # KI-Zug
            print("Zug der KI:")
            board = find_best_move_mcts(board, player=ID_AI, iterations=1000)

        winner = check_winner(board)
        if winner != 0:
            break

    if verbose:
        print_board(board)
        if winner != 0:
            print(f"{symbols[winner]} hat gewonnen!")
        else:
            print("Das Spiel endet unentschieden.")

    return winner


if __name__ == "__main__":
    tic_tac_toe_with_mcts()


# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# In diesem Kapitel hast du gelernt, wie Monte-Carlo-Tree-Search funktioniert:
#
# 1. Zufällige Simulationen: MCTS nutzt zufällige Partien, um Entscheidungen zu treffen.
#
# 2. Baumstruktur: Jeder Knoten im Baum repräsentiert einen Spielzustand, und 
#    die Werte der Knoten werden durch Simulationen aktualisiert.
#
# 3. Effizienz: MCTS findet gute Züge ohne den gesamten Spielbaum zu durchsuchen.

# MCTS ist besonders nützlich für Spiele mit großer Komplexität, wie z. B. Go oder Schach,
# und bildet die Grundlage vieler moderner KI-Systeme.


#  ___ _  _ ___  ___ 
# | __| \| |   \| __|
# | _|| .` | |) | _| 
# |___|_|\_|___/|___|
#                
# -=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=-=x=-=x=-=x=-=-=




