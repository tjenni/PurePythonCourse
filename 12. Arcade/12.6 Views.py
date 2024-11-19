#              _______________________________
#       ______|                               |_____
#       \     |     12.6 VIEWS IN ARCADE      |    /
#        )    |_______________________________|   (
#       /________)                        (________\     4.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# In `arcade` sind "Views" (Ansichten) nützlich, um verschiedene Bildschirme innerhalb
# eines Spiels zu erstellen, wie z.B. das Hauptmenü, das Spiel und den Game-Over-Bildschirm.
# Ansichten erleichtern das Wechseln zwischen verschiedenen Abschnitten der Anwendung.


# _________________________________
#                                 /
# Grundkonzept von Views         (
# ________________________________\

# Eine Ansicht in Arcade ist eine Klasse, die von `arcade.View` erbt und die Methoden
# `on_draw()` und `on_show()` sowie Interaktionsmethoden wie `on_key_press()` 
# überschreiben kann. Jede Ansicht kann eigene Inhalte und Logik haben und durch 
# `window.show_view(view)` aktiviert werden.

import arcade


class MainMenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.title = "Hauptmenü"

    def on_show(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(self.title, 400, 300, arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Drücke ENTER, um zu starten", 400, 250, arcade.color.DARK_GRAY, font_size=15, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            game_view = GameView()
            self.window.show_view(game_view)  # Wechsel zum Spiel-View


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.player_x = 50

    def on_show(self):
        arcade.set_background_color(arcade.color.LIGHT_GREEN)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Drücke ESC, um zum Menü zurückzukehren", 10, 10, arcade.color.DARK_GRAY, font_size=12)
        arcade.draw_circle_filled(self.player_x, 300, 15, arcade.color.RED)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            menu_view = MainMenuView()
            self.window.show_view(menu_view)  # Wechsel zurück zum Menü
        elif key == arcade.key.RIGHT:
            self.player_x += 10


# Startet die Anwendung und zeigt das Hauptmenü an
window = arcade.Window(800, 600, "Spiel mit Views")
menu_view = MainMenuView()
window.show_view(menu_view)
arcade.run()




# _________________________________
#                                 /
# Übergaben zwischen Views       (
# ________________________________\

# Ansichten können Parameter an andere Ansichten übergeben, z.B. den Punktestand.
# Dazu kann man den Wert direkt beim Erstellen der nächsten Ansicht übergeben.

import arcade


class GameOverView(arcade.View):
    def __init__(self, score):
        super().__init__()
        self.score = score

    def on_show(self):
        arcade.set_background_color(arcade.color.RED)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Game Over", 400, 300, arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text(f"Dein Punktestand: {self.score}", 400, 250, arcade.color.DARK_GRAY, font_size=20, anchor_x="center")
        arcade.draw_text("Drücke ENTER, um neu zu starten", 400, 200, arcade.color.BLACK, font_size=15, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            game_view = ScoringGameView()
            self.window.show_view(game_view)


class ScoringGameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.score = 0

    def on_show(self):
        arcade.set_background_color(arcade.color.LIGHT_GREEN)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Drücke ESC, um das Spiel zu beenden", 10, 10, arcade.color.DARK_GRAY, font_size=12)
        arcade.draw_text(f"Punkte: {self.score}", 10, 50, arcade.color.BLACK, font_size=14)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            game_over_view = GameOverView(self.score)
            self.window.show_view(game_over_view)
        elif key == arcade.key.RIGHT:
            self.score += 1

# Startet die Anwendung und zeigt das Hauptmenü an
window = arcade.Window(800, 600, "Spiel mit Views")
scoring_game_view = ScoringGameView()
window.show_view(scoring_game_view)
arcade.run()


# _________________________________
#                                 /
# Weitere nützliche View-Funktionen(
# ________________________________\

# 1. `on_update()`: Diese Methode kann in einer Ansicht implementiert werden, um regelmäßig
#    die Ansicht zu aktualisieren, z.B. für Animationen oder Zeitmechaniken.

# 2. `on_mouse_press()`, `on_mouse_release()`, `on_mouse_motion()`: Diese Methoden fangen
#    Mausklicks und -bewegungen ab und ermöglichen interaktive Inhalte.

# 3. `window.show_view(view)`: Die wichtigste Methode zum Wechseln der Ansicht. Der übergebene
#    Parameter `view` gibt die nächste Ansicht an.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Ansichten bieten eine einfache Möglichkeit, verschiedene Bildschirme innerhalb einer
#   `arcade`-Anwendung zu erstellen.
#
# - Das Wechseln zwischen Ansichten erfolgt durch `window.show_view(view)`.
#
# - Ansichten lassen sich leicht erweitern, um Punktestand, Level oder Einstellungen zwischen
#   den Bildschirmen zu übergeben.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine Anwendung mit drei Ansichten: einem Hauptmenü, einem Spielfeld und
# einem Game-Over-Bildschirm. Wechsle von Ansicht zu Ansicht mithilfe von Tasten.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle ein Punktespiel mit zwei Views: einem Spielfeld und einem Endbildschirm.
# Übergebe den Punktestand des Spiels an den Endbildschirm und zeige ihn dort an.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Anwendung mit einem Startbildschirm, einem Spielfeld und einem
# Spielmodus-Wahlbildschirm. Lasse den Benutzer zwischen zwei Spielmodi wählen,
# z. B. „Einfach“ und „Schwierig“, und passe das Spielfeld entsprechend an.


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
# Erstelle eine Anwendung mit drei Ansichten: einem Hauptmenü, einem Spielfeld und
# einem Game-Over-Bildschirm. Wechsle von Ansicht zu Ansicht mithilfe von Tasten.

'''
import arcade

class MainMenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Hauptmenü", self.window.width / 2, self.window.height / 2 + 50,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Drücke S für Spielstart", self.window.width / 2, self.window.height / 2,
                         arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.S:
            game_view = GameView()
            self.window.show_view(game_view)


class GameView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.GREEN_YELLOW)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Spielfeld", self.window.width / 2, self.window.height / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Drücke G für Game Over", self.window.width / 2, self.window.height / 2 - 40,
                         arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.G:
            game_over_view = GameOverView()
            self.window.show_view(game_over_view)


class GameOverView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.RED)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Game Over", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("Drücke M für Hauptmenü", self.window.width / 2, self.window.height / 2 - 40,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.M:
            main_menu_view = MainMenuView()
            self.window.show_view(main_menu_view)


# Anwendung starten
window = arcade.Window(600, 400, "Ansicht-Wechsel Anwendung")
window.show_view(MainMenuView())
arcade.run()
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle ein Punktespiel mit zwei Views: einem Spielfeld und einem Endbildschirm.
# Übergebe den Punktestand des Spiels an den Endbildschirm und zeige ihn dort an.

'''
import arcade

class ScoreGameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.score = 0

    def on_show(self):
        arcade.set_background_color(arcade.color.LIGHT_GRAY)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(f"Punkte: {self.score}", 50, 50, arcade.color.BLACK, font_size=20)
        arcade.draw_text("Drücke E für Ende", self.window.width / 2, self.window.height / 2,
                         arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.E:
            end_view = EndScreenView(self.score)
            self.window.show_view(end_view)

    def on_update(self, delta_time):
        self.score += 1  # Punktestand erhöhen


class EndScreenView(arcade.View):
    def __init__(self, score):
        super().__init__()
        self.score = score

    def on_show(self):
        arcade.set_background_color(arcade.color.DARK_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Ende des Spiels", self.window.width / 2, self.window.height / 2 + 30,
                         arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text(f"Erreichte Punkte: {self.score}", self.window.width / 2, self.window.height / 2 - 20,
                         arcade.color.WHITE, font_size=20, anchor_x="center")


# Anwendung starten
window = arcade.Window(600, 400, "Punktespiel")
window.show_view(ScoreGameView())
arcade.run()
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Anwendung mit einem Startbildschirm, einem Spielfeld und einem
# Spielmodus-Wahlbildschirm. Lasse den Benutzer zwischen zwei Spielmodi wählen,
# z. B. „Einfach“ und „Schwierig“, und passe das Spielfeld entsprechend an.

'''
class StartScreenView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.YELLOW_ORANGE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Startbildschirm", self.window.width / 2, self.window.height / 2 + 50,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Drücke M für Modusauswahl", self.window.width / 2, self.window.height / 2,
                         arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.M:
            mode_view = ModeSelectionView()
            self.window.show_view(mode_view)


class ModeSelectionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Modusauswahl", self.window.width / 2, self.window.height / 2 + 50,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Drücke E für Einfach, S für Schwierig", self.window.width / 2, self.window.height / 2,
                         arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.E:
            game_view = GameModeView(mode="Einfach")
            self.window.show_view(game_view)
        elif key == arcade.key.S:
            game_view = GameModeView(mode="Schwierig")
            self.window.show_view(game_view)


class GameModeView(arcade.View):
    def __init__(self, mode):
        super().__init__()
        self.mode = mode

    def on_show(self):
        arcade.set_background_color(arcade.color.GREEN_YELLOW if self.mode == "Einfach" else arcade.color.ORANGE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(f"Spielfeld - Modus: {self.mode}", self.window.width / 2, self.window.height / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Drücke Q für Startbildschirm", self.window.width / 2, self.window.height / 2 - 50,
                         arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.Q:
            start_view = StartScreenView()
            self.window.show_view(start_view)


# Anwendung starten
window = arcade.Window(600, 400, "Spiel mit Modusauswahl")
window.show_view(StartScreenView())
arcade.run()
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


