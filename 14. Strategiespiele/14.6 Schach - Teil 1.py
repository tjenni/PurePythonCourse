#              _______________________________
#       ______|                               |_____
#       \     | 14.6 SCHACH - TEIL 1          |    /
#        )    |_______________________________|   (
#       /________)                        (________\     21.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# Schach ist eines der komplexesten und faszinierendsten Spiele, das seit Jahrhunderten
# Strategen und KI-Entwickler gleichermaßen herausfordert. In diesem Kapitel starten wir
# mit einer vereinfachten Version von Schach und einer zufälligen KI ("Random Player").
#
# Ziel ist es, das Schachbrett und die grundlegenden Regeln zu implementieren und zu zeigen,
# wie einfache Züge von einer KI generiert werden können.


# _________________________________
#                                 /
# Grundregeln und Aufbau          (
# ________________________________\

# Für unser vereinfachtes Schachspiel implementieren wir:
# - Ein 8x8-Schachbrett.
# - Grundlegende Bewegungsregeln für Bauern, Türme, Springer, Läufer, Damen und Könige.
# - Einen Zufallsalgorithmus, der gültige Züge generiert.


import arcade
import random


# Klasse zur Darstellung eines Schachbretts
class ChessBoard:
    def __init__(self):
        self.board = self.setup_board()  # Initiales Brett mit Figuren

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
        # Farben für das Brett
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

    def get_valid_moves(self, player):
        """
        Gibt eine Liste gültiger Züge für den aktuellen Spieler zurück.
        """
        moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if (player == "White" and piece.isupper()) or (player == "Black" and piece.islower()):
                    moves.extend(self.get_moves_for_piece(row, col, piece))
        return moves

    def get_moves_for_piece(self, row, col, piece):
        """
        Gibt eine Liste gültiger Züge für eine spezifische Figur zurück.
        """
        moves = []
        directions = []

        # Bewegungslogik für verschiedene Figuren
        if piece.lower() == "p":  # Bauern
            direction = -1 if piece.isupper() else 1
            start_row = 1 if piece.islower() else 6
            if self.board[row + direction][col] == " ":
                moves.append(((row, col), (row + direction, col)))
            if row == start_row and self.board[row + 2 * direction][col] == " ":
                moves.append(((row, col), (row + 2 * direction, col)))
        elif piece.lower() == "r":  # Türme
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        elif piece.lower() == "n":  # Springer
            directions = [
                (-2, -1), (-2, 1), (-1, -2), (-1, 2),
                (1, -2), (1, 2), (2, -1), (2, 1)
            ]
        elif piece.lower() == "b":  # Läufer
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        elif piece.lower() == "q":  # Dame
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
        elif piece.lower() == "k":  # König
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]

        # Bewegungen basierend auf Richtungen generieren
        for dx, dy in directions:
            x, y = row + dx, col + dy
            while 0 <= x < 8 and 0 <= y < 8:
                if self.board[x][y] == " ":
                    moves.append(((row, col), (x, y)))
                elif (piece.isupper() and self.board[x][y].islower()) or \
                     (piece.islower() and self.board[x][y].isupper()):
                    moves.append(((row, col), (x, y)))
                    break
                else:
                    break
                if piece.lower() in "rnbqk":
                    break
                x, y = x + dx, y + dy

        return moves


# Zufälliger Spieler, der gültige Züge auswählt
def random_player(board, player):
    """
    Wählt zufällig einen gültigen Zug aus.
    """
    valid_moves = board.get_valid_moves(player)
    return random.choice(valid_moves)


# _________________________________
#                                 /
# Das Spiel                      (
# ________________________________\

# Klasse für das vereinfachte Schachspiel
class ChessGame(arcade.Window):
    def __init__(self, width=480, height=480, title="Schach - Teil 1"):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.board = ChessBoard()
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
        move = random_player(self.board, self.current_player)
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
# - Wie du ein vereinfachtes Schachspiel in Python mit Arcade implementierst.
# - Wie du die Bewegungen von Schachfiguren definierst.
# - Wie du einen zufälligen Spieler ("Random Player") für Schach erstellst.
#
# Im nächsten Kapitel werden wir dieses Schachspiel erweitern, um strategischere KI-Ansätze wie
# Minimax oder Monte-Carlo-Tree-Search zu integrieren.