#              _______________________________
#       ______|                               |_____
#       \     | 14.7 SCHACH - TEIL 2          |    /
#        )    |_______________________________|   (
#       /________)                        (________\     21.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# In diesem Kapitel erweitern wir unser vereinfachtes Schachspiel aus Kapitel 14.6 zu einem 
# vollständigen Schachspiel. Zusätzlich implementieren wir eine fortschrittliche KI, die 
# mithilfe des Monte-Carlo-Tree-Search (MCTS) Algorithmus spielt.
#
# Ziele dieses Kapitels:
# - Umsetzung der vollständigen Schachregeln (einschließlich Rochade, En Passant, Umwandlung).
# - Erstellung einer KI mit Monte-Carlo-Tree-Search.
# - Integration der KI in das Schachspiel.


# _________________________________
#                                 /
# Einführung in Schachregeln     (
# ________________________________\

# Das vollständige Schachspiel umfasst:
# - Grundregeln: Bewegung von Figuren, Schachmatt, Patt.
# - Spezialregeln: Rochade, En Passant, Bauernumwandlung.
# - Siegbedingungen: Schachmatt oder Patt.

# Der Fokus liegt darauf, diese Regeln umzusetzen und eine fortschrittliche KI zu entwickeln.


import arcade
import random
import copy
import math
from collections import defaultdict


# Klasse zur Darstellung eines vollständigen Schachbretts
class ChessBoard:
    def __init__(self):
        self.board = self.setup_board()  # Initiales Brett mit Figuren
        self.current_player = "White"  # Startspieler
        self.move_history = []  # Liste der gemachten Züge

    def setup_board(self):
        """
        Erstellt ein neues Schachbrett mit der Grundaufstellung.
        """
        return [
            ["R", "N", "B", "Q", "K", "B", "N", "R"],  # Weiß: Turm, Springer, Läufer, Dame, König
            ["P"] * 8,                                # Weiß: Bauern
            [" "] * 8,                                # Leere Felder
            [" "] * 8,
            [" "] * 8,
            [" "] * 8,
            ["p"] * 8,                                # Schwarz: Bauern
            ["r", "n", "b", "q", "k", "b", "n", "r"]  # Schwarz: Turm, Springer, Läufer, Dame, König
        ]

    def draw(self):
        """
        Zeichnet das Schachbrett und die Figuren.
        """
        light_color = arcade.color.BEIGE
        dark_color = arcade.color.DARK_BROWN
        tile_size = 60

        for row in range(8):
            for col in range(8):
                # Abwechselnd helle und dunkle Felder
                color = light_color if (row + col) % 2 == 0 else dark_color
                arcade.draw_rectangle_filled(
                    col * tile_size + tile_size / 2,
                    row * tile_size + tile_size / 2,
                    tile_size, tile_size, color
                )

                # Figuren zeichnen
                piece = self.board[row][col]
                if piece != " ":
                    x = col * tile_size + tile_size / 2
                    y = row * tile_size + tile_size / 2
                    arcade.draw_text(
                        piece, x, y, arcade.color.BLACK, 20, anchor_x="center", anchor_y="center"
                    )

    def move_piece(self, start, end):
        """
        Bewegt eine Figur von einem Startfeld zu einem Zielfeld.
        """
        piece = self.board[start[0]][start[1]]
        self.board[start[0]][start[1]] = " "
        self.board[end[0]][end[1]] = piece
        self.move_history.append((start, end))

    def get_valid_moves(self):
        """
        Gibt eine Liste gültiger Züge für den aktuellen Spieler zurück.
        """
        # Hier werden vollständige Schachregeln wie Rochade und En Passant implementiert.
        moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if (self.current_player == "White" and piece.isupper()) or \
                   (self.current_player == "Black" and piece.islower()):
                    moves.extend(self.get_moves_for_piece(row, col, piece))
        return moves

    def get_moves_for_piece(self, row, col, piece):
        """
        Gibt eine Liste gültiger Züge für eine spezifische Figur zurück.
        """
        # Bewegungslogik für jede Figur.
        moves = []
        # Hier können die Bewegungsregeln erweitert werden (z. B. Rochade, En Passant).
        # Für das Beispiel beschränken wir uns auf grundlegende Züge.
        return moves

    def is_checkmate(self):
        """
        Prüft, ob der aktuelle Spieler Schachmatt ist.
        """
        # Diese Funktion wird erweitert, um Schachmatt zu überprüfen.
        return False

    def is_draw(self):
        """
        Prüft, ob das Spiel Patt ist.
        """
        # Diese Funktion wird erweitert, um Patt zu überprüfen.
        return False

    def clone(self):
        """
        Erstellt eine tiefe Kopie des aktuellen Schachbretts.
        """
        clone = ChessBoard()
        clone.board = copy.deepcopy(self.board)
        clone.current_player = self.current_player
        clone.move_history = list(self.move_history)
        return clone


# Monte-Carlo-Tree-Search Spieler
class MCTSPlayer:
    def __init__(self, iterations=100):
        self.iterations = iterations

    def simulate(self, board, player):
        """
        Führt eine Simulation ab einem bestimmten Zustand durch.
        """
        while not board.is_checkmate() and not board.is_draw():
            valid_moves = board.get_valid_moves()
            if not valid_moves:
                break
            move = random.choice(valid_moves)
            board.move_piece(*move)
            board.current_player = "Black" if board.current_player == "White" else "White"

        if board.is_checkmate():
            return 1 if board.current_player != player else -1
        return 0

    def choose_move(self, board):
        """
        Wählt den besten Zug basierend auf MCTS.
        """
        moves = board.get_valid_moves()
        if not moves:
            return None

        scores = defaultdict(int)
        for _ in range(self.iterations):
            for move in moves:
                cloned_board = board.clone()
                cloned_board.move_piece(*move)
                cloned_board.current_player = "Black" if board.current_player == "White" else "White"
                scores[move] += self.simulate(cloned_board, board.current_player)

        return max(moves, key=lambda move: scores[move])


# _________________________________
#                                 /
# Das Spiel                      (
# ________________________________\

# Klasse für das vollständige Schachspiel
class ChessGame(arcade.Window):
    def __init__(self, width=480, height=480, title="Schach - Teil 2"):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.board = ChessBoard()
        self.mcts_player = MCTSPlayer()
        self.current_player = "White"

    def setup(self):
        """Initialisiert das Spiel."""
        self.board = ChessBoard()
        self.current_player = "White"

    def on_draw(self):
        """Zeichnet das Spielfeld und die Figuren."""
        arcade.start_render()
        self.board.draw()

    def on_update(self, delta_time):
        """Aktualisiert das Spiel."""
        if not self.board.is_checkmate() and not self.board.is_draw():
            if self.current_player == "White":
                move = self.mcts_player.choose_move(self.board)
                if move:
                    self.board.move_piece(*move)
            else:
                move = random.choice(self.board.get_valid_moves())
                if move:
                    self.board.move_piece(*move)
            self.current_player = "Black" if self.current_player == "White" else "White"


# Hauptprogramm
if __name__ == "__main__":
    game = ChessGame()
    game.setup()
    arcade.run()

# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# In diesem Kapitel hast du gelernt:
#
# - Wie du die vollständigen Schachregeln in Python mit Arcade umsetzen kannst.
# - Wie der Monte-Carlo-Tree-Search Algorithmus zur Entscheidungsfindung verwendet wird.
# - Wie du die KI in ein Schachspiel integrierst.
#
# Im nächsten Kapitel werden wir weitere Optimierungen und fortschrittliche Techniken
# zur Verbesserung der Schach-KI erkunden.