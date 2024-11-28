#              _______________________________
#       ______|                               |_____
#       \     |   14.5 ALGORITHMEN ARENA      |    /
#        )    |_______________________________|   (
#       /________)                        (________\     21.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# In diesem Kapitel lassen wir verschiedene KI-Algorithmen aus den vorherigen Kapiteln in einer
# "Algorithmen Arena" gegeneinander antreten. Wir nutzen Tic-Tac-Toe als Spielfeld, um zu
# analysieren, welcher Algorithmus die besten Ergebnisse liefert. Ziel ist es, die Stärken
# und Schwächen der Algorithmen durch praktische Spiele zu verstehen.


# _________________________________
#                                 /
# Aufbau der Arena               (
# ________________________________\

# Wir definieren eine Klasse `AlgorithmArena`, die den Spielablauf zwischen zwei KI-Algorithmen
# organisiert. Beide Algorithmen können über eine Funktionsschnittstelle definiert werden, die den
# nächsten Zug basierend auf dem aktuellen Zustand zurückgibt.

import random


# Klasse zur Simulation von Spielen zwischen verschiedenen KI-Algorithmen
class AlgorithmArena:
    def __init__(self, player1, player2):
        """
        Initialisiert die Arena mit zwei Algorithmen.

        :param player1: Funktion, die den nächsten Zug für Spieler 1 (X) berechnet.
        :param player2: Funktion, die den nächsten Zug für Spieler 2 (O) berechnet.
        """
        self.player1 = player1  # Algorithmus für Spieler 1
        self.player2 = player2  # Algorithmus für Spieler 2
        self.board = [" "] * 9  # Startposition
        self.current_player = "X"  # Startspieler

    def reset(self):
        """Setzt das Spiel zurück."""
        self.board = [" "] * 9
        self.current_player = "X"

    def make_move(self, move):
        """
        Macht einen Zug auf dem Brett.

        :param move: Index des Zugs (0-8)
        :return: True, wenn der Zug erfolgreich ist, sonst False
        """
        if self.board[move] == " ":
            self.board[move] = self.current_player
            return True
        return False

    def switch_player(self):
        """Wechselt den aktuellen Spieler."""
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        """Prüft, ob es einen Gewinner gibt."""
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertikal
            [0, 4, 8], [2, 4, 6],            # Diagonal
        ]
        for pattern in win_patterns:
            if self.board[pattern[0]] == self.board[pattern[1]] == self.board[pattern[2]] != " ":
                return self.board[pattern[0]]  # Gewinner (X oder O)
        if " " not in self.board:
            return "Draw"  # Unentschieden
        return None  # Noch kein Gewinner

    def play_game(self, verbose=False):
        """
        Führt ein Spiel zwischen den Algorithmen aus.

        :param verbose: Wenn True, wird das Brett nach jedem Zug ausgegeben.
        :return: Gewinner ("X", "O" oder "Draw")
        """
        self.reset()
        while True:
            if verbose:
                self.print_board()

            if self.current_player == "X":
                move = self.player1(self.board, "X")
            else:
                move = self.player2(self.board, "O")

            if not self.make_move(move):
                raise ValueError(f"Ungültiger Zug: Spieler {self.current_player} wählte {move}")

            winner = self.check_winner()
            if winner:
                if verbose:
                    self.print_board()
                    print(f"Spiel beendet! Gewinner: {winner}")
                return winner

            self.switch_player()

    def print_board(self):
        """Zeigt das aktuelle Spielfeld an."""
        print("\n")
        for i in range(3):
            print(" | ".join(self.board[i * 3:(i + 1) * 3]))
            if i < 2:
                print("-" * 5)


# _________________________________
#                                 /
# KI-Strategien                  (
# ________________________________\

# Beispielstrategien für die Arena. Diese Funktionen bestimmen den nächsten Zug basierend
# auf dem aktuellen Brett.

def random_player(board, player):
    """Wählt zufällig einen gültigen Zug aus."""
    return random.choice([i for i in range(len(board)) if board[i] == " "])


def minimax_player(board, player):
    """Wählt den besten Zug mithilfe des Minimax-Algorithmus."""
    from minimax import minimax
    _, move = minimax(board, player)
    return move


def alpha_beta_player(board, player):
    """Wählt den besten Zug mithilfe von Alpha-Beta-Pruning."""
    from alpha_beta import alpha_beta_pruning
    _, move = alpha_beta_pruning(board, player)
    return move


def monte_carlo_player(board, player):
    """Wählt den besten Zug mithilfe von Monte-Carlo-Tree-Search."""
    from monte_carlo import monte_carlo_tree_search
    return monte_carlo_tree_search(board, player)


# _________________________________
#                                 /
# Ergebnisse und Analyse          (
# ________________________________\

# Um die Leistung der Algorithmen zu vergleichen, führen wir eine Reihe von Spielen durch.
# Jeder Algorithmus spielt gegen jeden anderen, einschließlich sich selbst.

def run_tournament(algorithms, games_per_pair=10):
    """
    Führt ein Turnier zwischen allen Algorithmen durch.

    :param algorithms: Liste von Algorithmen als (Name, Funktion)-Tupel.
    :param games_per_pair: Anzahl der Spiele pro Paar.
    :return: Ergebnisse als Wörterbuch.
    """
    results = {name: {"Wins": 0, "Losses": 0, "Draws": 0} for name, _ in algorithms}

    for i, (name1, algo1) in enumerate(algorithms):
        for j, (name2, algo2) in enumerate(algorithms):
            if i == j:
                continue  # Kein Spiel gegen sich selbst

            for _ in range(games_per_pair):
                arena = AlgorithmArena(algo1, algo2)
                winner = arena.play_game()

                if winner == "X":
                    results[name1]["Wins"] += 1
                    results[name2]["Losses"] += 1
                elif winner == "O":
                    results[name2]["Wins"] += 1
                    results[name1]["Losses"] += 1
                else:
                    results[name1]["Draws"] += 1
                    results[name2]["Draws"] += 1

    return results


# Beispiel: Algorithmen registrieren und Turnier starten
algorithms = [
    ("Random", random_player),
    ("Minimax", minimax_player),
    ("Alpha-Beta", alpha_beta_player),
    ("Monte Carlo", monte_carlo_player)
]

# Turnierergebnisse ausgeben
results = run_tournament(algorithms, games_per_pair=10)
for name, stats in results.items():
    print(f"{name}: {stats}")


# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# In diesem Kapitel hast du gelernt:
#
# - Wie du verschiedene KI-Algorithmen in einem Turnier vergleichst.
#
# - Wie du eine flexible Spielumgebung wie die `AlgorithmArena` aufbaust.
#
# - Wie du Ergebnisse analysierst, um die Stärken und Schwächen der Algorithmen zu verstehen.
#
# Die "Algorithmen Arena" kann leicht erweitert werden, um neue Strategien oder komplexere
# Spiele zu testen. Sie bietet eine praktische Möglichkeit, KI-Ansätze in realen Spielszenarien
# zu bewerten und weiterzuentwickeln.

# Viel Erfolg beim Experimentieren!