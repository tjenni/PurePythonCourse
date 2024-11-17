#              ____________________________
#       ______|                            |_____
#       \     |    12.7 SOUND UND MUSIK    |    /
#        )    |____________________________|   (
#       /________)                     (________\     4.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# Sound und Musik sind wichtige Elemente, die einem Spiel Tiefe und Atmosphäre verleihen.
# Die `arcade`-Bibliothek bietet eine einfache Möglichkeit, Soundeffekte und Musik in
# Python-Spiele zu integrieren. In diesem Kapitel lernst du die grundlegenden Funktionen
# zum Einfügen von Sounds und Musik.

import arcade


# ___________________________________
#                                   /
# Sound-Effekte laden und abspielen(
# __________________________________\

# Sounds lassen sich in Arcade als WAV-Dateien laden und durch die Funktion `play_sound()`
# abspielen. Für die Verwendung von Sounds sollte sich die Datei im selben Verzeichnis
# befinden oder der Pfad angepasst werden.

class SoundEffectExample(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Soundeffekte")
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

        # Lade den Sound-Effekt
        self.coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Drücke die LEERTASTE, um den Sound abzuspielen", 100, 300, arcade.color.BLACK, 16)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            arcade.play_sound(self.coin_sound)  # Sound abspielen

window = SoundEffectExample()
arcade.run()




# _________________________________
#                                 /
# Hintergrundmusik abspielen      (
# ________________________________\

# Arcade unterstützt das Abspielen von Musik im OGG-Format. Zum Abspielen von Musik
# wird die Methode `play_sound()` verwendet, allerdings kann Musik mit längerer
# Dauer zusätzliche Parameter wie `volume` und `loop` enthalten, um die Lautstärke
# und das wiederholte Abspielen zu steuern.

# Hinweis: Auf dem Mac lassen sich in Arcade keine mp3-Dateien abspielen. 
# Konvertiere daher die Hintergrundmusik ins WAV-Format. Leider benötigt
# das viel mehr Speicherplatz.

class BackgroundMusicExample(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Hintergrundmusik")
        arcade.set_background_color(arcade.color.LIGHT_YELLOW)

        # Lade die Hintergrundmusik
        self.background_music = arcade.load_sound("epic_strings.wav")
        arcade.play_sound(self.background_music, volume=0.3, looping=True)  # Musik mit 30% Lautstärke und Loop
        
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Hintergrundmusik spielt...", 300, 300, arcade.color.BLACK, 16)

    def on_close(self):
        arcade.stop_sound(self.background_music)  # Stoppt die Musik beim Schließen des Fensters
        super().on_close()

window = BackgroundMusicExample()
arcade.run()




# ______________________________
#                              /
# Interaktive Soundauslöser   (
# _____________________________\

# Sounds können auch basierend auf bestimmten Interaktionen ausgelöst werden, z. B.
# das Abspielen eines Sounds bei einer Kollision oder einem Punktgewinn.

class InteractiveSoundExample(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Interaktive Soundeffekte")
        arcade.set_background_color(arcade.color.LIGHT_GREEN)

        # Sprites und Sound laden
        self.player = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5, center_x=400, center_y=300)
        self.coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        
        self.coin_list = arcade.SpriteList()

        # Erstelle Münzen für das Sammeln
        for i in range(5):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", 0.5)
            coin.center_x = 150 * (i + 1)
            coin.center_y = 200
            self.coin_list.append(coin)
        
        self.player.speed_x = 0
        self.player.speed_y = 0

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.coin_list.draw()
        arcade.draw_text("Bewege die Spielfigur mit den Pfeiltasten", 250, 50, arcade.color.BLACK, 14)

    def on_key_press(self, key, modifiers):
        # Bewege den Spieler mit den Pfeiltasten
        if key == arcade.key.UP:
            self.player.speed_y = 5
        elif key == arcade.key.DOWN:
            self.player.speed_y = -5
        elif key == arcade.key.LEFT:
            self.player.speed_x = -5
        elif key == arcade.key.RIGHT:
            self.player.speed_x = 5
            
    def on_key_release(self, key, modifiers):
        # Stoppe die Bewegung, wenn die Taste losgelassen wird
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.player.speed_y = 0
        elif key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player.speed_x = 0
    
    def on_update(self, delta_time):
        self.player.center_x += self.player.speed_x
        self.player.center_y += self.player.speed_y
        
        coins_collected = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for coin in coins_collected:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.coin_sound)
            
window = InteractiveSoundExample()
arcade.run()




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - `arcade.load_sound()` lädt eine Sound-Datei, die mit `play_sound()` abgespielt
#   werden kann. Für Musik empfiehlt sich das OGG-Format.
#
# - Die Hintergrundmusik kann durch die Verwendung von `loop=True` dauerhaft
#   abgespielt werden.
#
# - Sounds lassen sich durch Interaktionen wie Kollisionen und Tastenanschläge
#   auslösen, um das Spiel dynamischer und spannender zu gestalten.


# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Füge einer Anwendung einen "Jump"-Sound hinzu, der abgespielt wird, wenn
# der Spieler eine Taste zum Springen drückt. Nutze eine Taste, wie z. B. 
# die LEERTASTE, um das Springen zu simulieren.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle eine Anwendung, die Hintergrundmusik abspielt und ein visuelles
# Element wie ein animiertes Icon zeigt, das anzeigt, dass Musik läuft. Füge
# einen Button hinzu, der die Musik stoppt und das Icon versteckt.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Anwendung, in der ein Sammelspiel aufgebaut ist. Erzeuge mehrere
# Objekte auf dem Bildschirm, die bei Kollision einen Sound abspielen und verschwinden.
# Zeige die Punktzahl an, die sich bei jedem gesammelten Objekt erhöht.


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
#  

# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Füge einer Anwendung einen "Jump"-Sound hinzu, der abgespielt wird, wenn
# der Spieler eine Taste zum Springen drückt. Nutze eine Taste, wie z. B. 
# die LEERTASTE, um das Springen zu simulieren.

'''
class JumpGame(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Jump Sound")
        self.jump_sound = arcade.load_sound("jump_sound.wav")  # Ersetze durch den Pfad zum Soundfile

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            arcade.play_sound(self.jump_sound)
            print("Jump!")

window = JumpGame()
arcade.run()
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle eine Anwendung, die Hintergrundmusik abspielt und ein visuelles
# Element wie ein animiertes Icon zeigt, das anzeigt, dass Musik läuft. Füge
# einen Button hinzu, der die Musik stoppt und das Icon versteckt.

'''
class MusicApp(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Musik-App")
        self.music = arcade.load_sound("background_music.mp3")  # Ersetze durch den Pfad zur Musikdatei
        self.music_playing = False
        self.icon = arcade.SpriteSolidColor(30, 30, arcade.color.GREEN)
        self.icon.center_x = 300
        self.icon.center_y = 200

    def on_draw(self):
        arcade.start_render()
        if self.music_playing:
            self.icon.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.P and not self.music_playing:  # Start
            self.music_playing = True
            arcade.play_sound(self.music, looping=True)
        elif key == arcade.key.S and self.music_playing:  # Stop
            arcade.stop_sound(self.music)
            self.music_playing = False

window = MusicApp()
arcade.run()
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Anwendung, in der ein Sammelspiel aufgebaut ist. Erzeuge mehrere
# Objekte auf dem Bildschirm, die bei Kollision einen Sound abspielen und verschwinden.
# Zeige die Punktzahl an, die sich bei jedem gesammelten Objekt erhöht.


'''
class CollectGame(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Sammelspiel")
        self.collect_sound = arcade.load_sound("collect_sound.wav")  # Ersetze durch den Pfad zum Soundfile
        self.score = 0
        self.player = arcade.SpriteSolidColor(20, 20, arcade.color.BLUE)
        self.player.center_x = 300
        self.player.center_y = 50
        self.objects = arcade.SpriteList()
        
        # Erzeuge Sammelobjekte
        for i in range(10):
            obj = arcade.SpriteSolidColor(15, 15, arcade.color.RED)
            obj.center_x = i * 50 + 50
            obj.center_y = 300
            self.objects.append(obj)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.objects.draw()
        arcade.draw_text(f"Punktzahl: {self.score}", 10, 10, arcade.color.BLACK, 14)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.player.center_x += 10
        elif key == arcade.key.LEFT:
            self.player.center_x -= 10
        elif key == arcade.key.UP:
            self.player.center_y += 10
        elif key == arcade.key.DOWN:
            self.player.center_y -= 10

    def on_update(self, delta_time):
        # Kollision mit Sammelobjekten prüfen
        hit_list = arcade.check_for_collision_with_list(self.player, self.objects)
        for obj in hit_list:
            obj.remove_from_sprite_lists()
            arcade.play_sound(self.collect_sound)
            self.score += 1

window = CollectGame()
arcade.run()
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

