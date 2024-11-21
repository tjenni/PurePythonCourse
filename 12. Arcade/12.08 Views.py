#              ____________________
#       ______|                    |_____
#       \     |     12.8 VIEWS     |    /
#        )    |____________________|   (
#       /________)             (________\     21.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# 
# Spiele bestehen oft aus verschiedenen Ansichten, die den Spieler durch das 
# Spiel führen. Beispiele hierfür sind ein Hauptmenü, eine Spielansicht und eine 
# Game-Over-Ansicht. Um solche Übergänge sauber und effizient zu implementieren, 
# bietet `arcade` die Möglichkeit, sogenannte "Views" (Ansichten) zu erstellen.
# 
# Jede Ansicht ist eine eigenständige Klasse, die von `arcade.View` erbt und 
# spezifische Inhalte sowie Interaktionslogik enthält. Dies ermöglicht die 
# Trennung der Logik für verschiedene Bereiche eines Spiels, wodurch das 
# Gesamtdesign übersichtlicher und wartbarer wird.
# 
# Mit "Views" kannst du:
# - Den Spielablauf strukturieren, z. B. mit Start-, Pausen- und Endbildschirmen.
#
# - Daten wie Punktestände oder Einstellungen zwischen Ansichten übergeben.
#
# - Animationen oder Übergänge zwischen verschiedenen Abschnitten nahtlos 
#   gestalten.




# _________________________________
#                                 /
# Grundkonzept von Views         (
# ________________________________\
#
#
# Was sind Views?
# ---------------
#
# Eine Ansicht in `arcade` ist eine Klasse, die speziell dafür ausgelegt ist, 
# bestimmte Zustände eines Spiels darzustellen. Sie kann verschiedene Methoden 
# enthalten, um Inhalte zu zeichnen `on_draw()`, Benutzerinteraktionen zu 
# verarbeiten `on_key_press()`, oder andere Spielmechaniken zu steuern 
# `on_update()`.
# 
#
# Wie erstellt man eine View?
# ---------------------------
#
# Um eine Ansicht zu erstellen, muss eine Klasse von `arcade.View` erben. 
# Die wichtigsten Methoden, die du in einer Ansicht definieren kannst, sind:
#
# - `on_draw()`: Wird aufgerufen, um Inhalte auf den Bildschirm zu zeichnen.
#
# - `on_key_press()` und `on_key_release()`: Verarbeitet Tasteneingaben.
#
# - `on_update(delta_time)`: Aktualisiert den Zustand der Ansicht regelmässig
#.
# - `on_mouse_press()`, `on_mouse_release()`: Verarbeitet Mausinteraktionen.
# 
#
# Übergang zwischen Ansichten
# ---------------------------
#
# Der Wechsel zwischen Ansichten erfolgt mit der Methode `window.show_view(view)`, 
# wobei `view` die nächste Ansicht ist, die angezeigt werden soll. Jede Ansicht 
# hat Zugriff auf das Fenster, in dem das Spiel läuft, und kann so den Wechsel 
# steuern.
# 
#
# Warum Views verwenden?
# ----------------------
# 
# - Modularität: Jede Ansicht hat ihre eigene Logik und ist unabhängig von 
#   anderen Bereichen des Spiels.
#
# - Wiederverwendbarkeit: Ansichten können für verschiedene Projekte angepasst 
#   und wiederverwendet werden.
#
# - Einfachheit: Der Wechsel zwischen Ansichten erfolgt durch einen einzigen 
#   Methodenaufruf.


import arcade


# Diese Klasse repräsentiert das Hauptmenü des Spiels.
# Sie zeigt den Titel und eine Aufforderung zum Starten des Spiels an.
class MainMenuView(arcade.View):

    def __init__(self):
        super().__init__()
        self.title = "Hauptmenü"  # Titel des Hauptmenüs


    def on_show(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)


    # Zeichnet den Titel und eine Anweisung zum Starten des Spiels.
    def on_draw(self):
        arcade.start_render()
        # Zeichnet den Titel in der Mitte des Bildschirms
        arcade.draw_text(self.title, 400, 300, arcade.color.BLACK, font_size=30, anchor_x="center")
        # Zeichnet eine Anweisung zum Starten des Spiels
        arcade.draw_text("Drücke ENTER, um zu starten", 400, 250, arcade.color.BLACK, font_size=15, anchor_x="center")


    #  Reagiert auf Tasteneingaben. Startet das Spiel, wenn ENTER gedrückt wird.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            # Wechsel zur Spielansicht
            game_view = GameView()
            self.window.show_view(game_view)


# Diese Klasse repräsentiert die Hauptspielansicht.
#  Der Spieler kann eine rote Kugel steuern, die sich über den Bildschirm bewegt.
class GameView(arcade.View):

    def __init__(self):
        super().__init__()
        
        # Initialisiert die Spielerposition und -geschwindigkeit
        self.player_x = self.window.width // 2  # Startposition in der Mitte des Fensters
        self.player_y = self.window.height // 2
        self.speed_x = 0  # Geschwindigkeit in X-Richtung
        self.speed_y = 0  # Geschwindigkeit in Y-Richtung


    # Wird aufgerufen, wenn diese Ansicht angezeigt wird.
    # Setzt den Hintergrund auf Grün.
    def on_show(self):
        arcade.set_background_color(arcade.color.LIGHT_GREEN)


    # Zeichnet die Spielfläche und den Spieler.
    def on_draw(self):

        arcade.start_render()
        # Zeigt eine Anweisung zum Zurückkehren ins Menü an
        arcade.draw_text("Drücke ESC, um zum Menü zurückzukehren", 10, 10, arcade.color.BLACK, font_size=12)
        # Zeichnet den Spieler als roten Kreis
        arcade.draw_circle_filled(self.player_x, self.player_y, 15, arcade.color.RED)


    # Aktualisiert die Position des Spielers basierend auf der Geschwindigkeit.
    def on_update(self, delta_time):
        self.player_x += self.speed_x
        self.player_y += self.speed_y


    # Reagiert auf Tasteneingaben und bewegt den Spieler oder kehrt ins Menü zurück.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.speed_y = 5  # Bewegung nach oben
        elif key == arcade.key.DOWN:
            self.speed_y = -5  # Bewegung nach unten
        elif key == arcade.key.LEFT:
            self.speed_x = -5  # Bewegung nach links
        elif key == arcade.key.RIGHT:
            self.speed_x = 5  # Bewegung nach rechts
            
        elif key == arcade.key.ESCAPE:
            # Zurück zum Hauptmenü
            menu_view = MainMenuView()
            self.window.show_view(menu_view)


    # Stoppt die Bewegung des Spielers, wenn die entsprechende Taste losgelassen wird.
    def on_key_release(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.speed_y = 0
        elif key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.speed_x = 0


# Startet die Anwendung und zeigt das Hauptmenü an
window = arcade.Window(800, 600, "Spiel mit Views")  # Erstellt das Fenster
menu_view = MainMenuView()  # Erstellt die Hauptmenü-Ansicht
window.show_view(menu_view)  # Zeigt das Hauptmenü an
arcade.run()  # Startet die Arcade-Game-Loop




# _________________________________
#                                 /
# Übergaben zwischen Views       (
# ________________________________\

# Oft ist es notwendig, Daten zwischen Ansichten zu übergeben, wie z. B. den Punktestand 
# eines Spiels. Dazu können wir den Wert direkt beim Erstellen der nächsten Ansicht 
# als Parameter übergeben.


import arcade

# Ansicht für den Game-Over-Bildschirm
class GameOverView(arcade.View):

    # Initialisiert die Game-Over-Ansicht mit dem aktuellen Punktestand.
    def __init__(self, score):
        super().__init__()
        self.score = score  # Punktestand


    # Wird aufgerufen, wenn diese Ansicht angezeigt wird.
    # Setzt den Hintergrund auf eine rosa Farbe.
    def on_show(self):
        arcade.set_background_color(arcade.color.CHINA_PINK)


    # Zeichnet den Game-Over-Bildschirm.
    def on_draw(self):
        arcade.start_render()
        # Titel des Bildschirms
        arcade.draw_text("Game Over", 400, 300, arcade.color.BLACK, font_size=30, anchor_x="center")
        # Punktestand des Spielers
        arcade.draw_text(f"Dein Punktestand: {self.score}", 400, 250, arcade.color.BLACK, font_size=20, anchor_x="center")
        # Anweisung zum Neustarten des Spiels
        arcade.draw_text("Drücke ENTER, um neu zu starten", 400, 200, arcade.color.BLACK, font_size=15, anchor_x="center")

    # Reagiert auf Tastendrücke. Startet das Spiel neu, wenn ENTER gedrückt wird.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            # Wechsel zur Spielansicht
            game_view = ScoringGameView()
            self.window.show_view(game_view)



# Diese Ansicht repräsentiert das Hauptspiel. Der Spieler sammelt Punkte,
# indem er die rechte Pfeiltaste drückt.
class ScoringGameView(arcade.View):

    def __init__(self):
        super().__init__()
        self.score = 0  # Punktestand

    # Wird aufgerufen, wenn diese Ansicht angezeigt wird.
    # Setzt den Hintergrund auf eine grüne Farbe.
    def on_show(self):
        arcade.set_background_color(arcade.color.LIGHT_GREEN)


    # Zeichnet die Spielfläche und den aktuellen Punktestand.
    def on_draw(self):
        arcade.start_render()

        # Anweisung zum Beenden des Spiels
        arcade.draw_text("Drücke ESC, um das Spiel zu beenden", self.window.width // 2, self.window.height // 2,
                         arcade.color.BLACK, anchor_x="center", font_size=18)

        # Punktestand des Spielers
        arcade.draw_text(f"Punkte: {self.score}", self.window.width // 2, self.window.height // 2 - 50,
                         arcade.color.BLACK, anchor_x="center", font_size=24)


    # Reagiert auf Tastendrücke.
    # - ESC: Beendet das Spiel und zeigt den Game-Over-Bildschirm.
    # - RECHTE PFEILTASTE: Erhöht den Punktestand.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            # Wechsel zur Game-Over-Ansicht mit dem aktuellen Punktestand
            game_over_view = GameOverView(self.score)
            self.window.show_view(game_over_view)
        elif key == arcade.key.RIGHT:
            # Erhöht den Punktestand
            self.score += 1


# Startet die Anwendung und zeigt die erste Ansicht (das Hauptspiel) an
window = arcade.Window(800, 600, "Spiel mit Views")  # Erstellt das Fenster
scoring_game_view = ScoringGameView()  # Erstellt die Hauptspielansicht
window.show_view(scoring_game_view)  # Zeigt die Hauptspielansicht an
arcade.run()  # Startet die Arcade-Game-Loop




# ____________________________________
#                                     /
# Weitere nützliche View-Funktionen  (
# ____________________________________\

# 1. `on_update()`: Diese Methode kann in einer Ansicht implementiert werden, 
#    um regelmässig die Ansicht zu aktualisieren, z.B. für Animationen 
#    oder Zeitmechaniken.

# 2. `on_mouse_press()`, `on_mouse_release()`, `on_mouse_motion()`: Diese 
#    Methoden fangen Mausklicks und -bewegungen ab und ermöglichen 
#    interaktive Inhalte.

# 3. `window.show_view(view)`: Die wichtigste Methode zum Wechseln der Ansicht. 
#    Der übergebene Parameter `view` gibt die nächste Ansicht an.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\
#
# In diesem Kapitel hast du gelernt, wie man mit `arcade` verschiedene Ansichten 
# (Views) erstellt, um Spiele mit mehreren Bildschirmen effizient zu strukturieren. 
# Das Konzept der Views erlaubt:
#
# 1. Modularität: Jede Ansicht kann ihre eigene Logik, ihr eigenes Layout und ihre 
#    eigenen Inhalte haben.
#
# 2. Wechsel zwischen Ansichten: Mithilfe von `window.show_view(view)` können 
#    Ansichten nahtlos gewechselt werden.
#
# 3. Datenübergabe: Daten wie Punktestände oder Einstellungen können einfach 
#    zwischen Ansichten übergeben werden.
#
# 4. Flexibilität: Views können angepasst werden, um interaktive Menüs, 
#    Spielmodi und mehr zu erstellen.
#
# Mit diesen Grundlagen kannst du ein strukturiertes und flexibles Spiel entwickeln. 
# Nutze die Übungsaufgaben, um das Gelernte zu vertiefen und dein Wissen 
# praktisch anzuwenden!




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




#
#          _    .  ,   .           .
#      *  / \_ *  / \_      _  *        *   /\'__        *
#        /    \  /    \,   ((        .    _/  /  \  *'.
#   .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.
#      /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *
#    /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \
#   /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-
#  /jgs     `.  / /       `.~-^=-=~=^=.-'      '-._ `._
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
# Auf dem Spielfeld werden die Punkte hochgezählt. Drückt man die Taste E, wird
# das Spiel beendet und der Endbildschirm angezeig. Übergebe dazu den Punktestand 
# des Spiels an den Endbildschirm.

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
import arcade 

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


