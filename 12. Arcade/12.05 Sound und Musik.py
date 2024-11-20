#              ____________________________
#       ______|                            |_____
#       \     |    12.7 SOUND UND MUSIK    |    /
#        )    |____________________________|   (
#       /________)                     (________\     20.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# Sound und Musik sind wichtige Elemente, die einem Spiel Tiefe und Atmosphäre verleihen.
# Die `arcade`-Bibliothek bietet eine einfache Möglichkeit, Soundeffekte und Musik in
# Python-Spiele zu integrieren. In diesem Kapitel lernst du die grundlegenden Funktionen
# zum Einfügen von Sounds und Musik.

# Auf der Webseite https://opengameart.org kannst du Musik, Töne und Bilder finden, 
# die du in deinen Spielen verwenden darfst. 


# _____________________________________
#                                     /
# Sound-Effekte laden und abspielen  (
# ____________________________________\

# Sounds lassen sich in Arcade als WAV-Dateien laden und durch die Funktion `play_sound()`
# abspielen. Für die Verwendung von Sounds sollte sich die Datei im selben Verzeichnis
# befinden oder der Pfad angepasst werden.

import arcade

class SoundEffectExample(arcade.Window):

    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)

        arcade.set_background_color(arcade.color.LIGHT_BLUE)

        # Lade den Sound-Effekt
        self.coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")


    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Drücke die LEERTASTE, um den Sound abzuspielen", self.width//2, self.height//2, arcade.color.BLACK, font_size=16, anchor_x="center")


    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            arcade.play_sound(self.coin_sound)  # Sound abspielen


# Hauptprogramm
window = SoundEffectExample(title="Soundeffekte")
arcade.run()




# _________________________________
#                                 /
# Hintergrundmusik abspielen      (
# ________________________________\

# Arcade unterstützt das Abspielen von Musik in verschiedenen Formaten. 
# Zum Abspielen von Musik wird die Methode `play_sound()` verwendet, allerdings 
# kann Musik mit längerer Dauer zusätzliche Parameter wie `volume` und `loop` 
# enthalten, um die Lautstärke und das wiederholte Abspielen zu steuern.

# Hinweis: Auf dem Mac lassen sich in Arcade keine mp3-Dateien abspielen. 
# Konvertiere daher die Hintergrundmusik ins WAV-Format. Leider benötigt
# das viel mehr Speicherplatz.

import arcade

class BackgroundMusicExample(arcade.Window):

    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)

        arcade.set_background_color(arcade.color.LIGHT_YELLOW)

        # Lade die Hintergrundmusik, Quelle: https://opengameart.org/content/bossa-nova
        self.background_music = arcade.load_sound("_assets/8bit_bossa.wav")
        arcade.play_sound(self.background_music, volume=0.3, looping=True)  # Musik mit 30% Lautstärke und Loop

 
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Hintergrundmusik spielt...", self.width//2, self.height//2, arcade.color.BLACK, font_size=16, anchor_x="center")


    def on_close(self):
        arcade.stop_sound(self.background_music)  # Stoppt die Musik beim Schließen des Fensters
        super().on_close()


# Hauptprogramm
window = BackgroundMusicExample(title="Hintergrundmusik")
arcade.run()




# ______________________________
#                              /
# Sounds bei Interaktionen    (
# _____________________________\

# Sounds können auch basierend auf bestimmten Interaktionen ausgelöst werden, z. B.
# das Abspielen eines Sounds bei einer Kollision oder einem Punktgewinn.

import arcade

class InteractiveSoundExample(arcade.Window):

    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)

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


# Hauptprogramm      
window = InteractiveSoundExample(title="Interaktive Soundeffekte")
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




#     |\
#  |--|/----------------,~\-Billy Joel-(_)--
#  |--|---4-------------|~'------------|---
#  |-/|.-------|~~~~|--/|-----|~~~~|--/|--
#  |(-|-)-4---_|---_|--\|----_|---_|--\|-
#  |-`|'-----(_)--(_)-------(_)--(_)--
#    \|
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
# Füge einer Anwendung einen "Jump"-Sound hinzu, der abgespielt wird, wenn
# der Spieler eine Taste zum Springen drückt. Nutze eine Taste, wie z. B. 
# die LEERTASTE, um das Springen zu simulieren.

'''
import arcade

class JumpGame(arcade.Window):
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.jump_sound = arcade.load_sound(":resources:sounds/jump3.wav")
    
        
    def on_draw(self):
        arcade.start_render()

        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            arcade.play_sound(self.jump_sound)
            print("Jump!")

# Hauptprogramm
window = JumpGame(title="Jump Sound")
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
import arcade

class MusicApp(arcade.Window):

    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)

        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.music = arcade.load_sound("_assets/8bit_bossa.wav")
        self.music_playing = False
        self.icon = arcade.SpriteSolidColor(30, 30, arcade.color.GREEN)
        self.icon.center_x = 300
        self.icon.center_y = 200
        self.music_player = None

    def on_draw(self):
        arcade.start_render()
        if self.music_playing:
            self.icon.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.P and not self.music_playing:  # Start
            self.music_playing = True
            self.music_player = arcade.play_sound(self.music, looping=True)
            
        elif key == arcade.key.S and self.music_playing:  # Stop
            if self.music_player is not None:
                arcade.stop_sound(self.music_player)
                self.music_playing = False

# Hauptprogramm
window = MusicApp(title="Musik-App")
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
import arcade
import random

# Klasse für das Sammelspiel
class CollectGame(arcade.Window):
    
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)

        arcade.set_background_color(arcade.color.SKY_BLUE)
  
        # Soundeffekt für das Einsammeln von Objekten laden
        self.collect_sound = arcade.load_sound(":resources:sounds/coin2.wav")
        
        # Punktzahl initialisieren
        self.score = 0
        
        # Spielfigur erstellen
        self.player = arcade.SpriteSolidColor(20, 20, arcade.color.BLUE)  # Blaue Spielfigur
        self.player.center_x = 300  # Startposition X
        self.player.center_y = 50  # Startposition Y
        self.player.speed_x = 0  # Horizontale Geschwindigkeit der Spielfigur
        self.player.speed_y = 0  # Vertikale Geschwindigkeit der Spielfigur
        
        # Liste für Sammelobjekte
        self.objects = arcade.SpriteList()
        
        # Sammelobjekte erstellen und zur Liste hinzufügen
        for i in range(10):
            obj = arcade.SpriteSolidColor(15, 15, arcade.color.RED)  # Rote Sammelobjekte
            obj.center_x = random.randint(50,self.width-100)  # Horizontale Verteilung der Objekte
            obj.center_y = random.randint(50,self.height-100)  # Vertikale Position der Objekte
            self.objects.append(obj)


    # Aktualisiert die Spiellogik, z. B. die Bewegung der Spielfigur und das Einsammeln der Objekte.  
    def on_update(self, delta_time):
        # Bewegung der Spielfigur basierend auf der Geschwindigkeit
        self.player.center_x += self.player.speed_x
        self.player.center_y += self.player.speed_y
        
        # Überprüfung auf Kollisionen zwischen Spielfigur und Sammelobjekten
        hit_list = arcade.check_for_collision_with_list(self.player, self.objects)
        for obj in hit_list:
            obj.remove_from_sprite_lists()  # Objekt aus der Liste entfernen (wird eingesammelt)
            arcade.play_sound(self.collect_sound)  # Soundeffekt abspielen
            self.score += 1  # Punktzahl erhöhen


    # Zeichnet die Spielfigur, Sammelobjekte und den Punktestand.   
    def on_draw(self):
        arcade.start_render()  # Bildschirm löschen und bereit zum Zeichnen
        self.player.draw()  # Spielfigur zeichnen
        self.objects.draw()  # Sammelobjekte zeichnen
        # Punktestand anzeigen
        arcade.draw_text(f"Punktzahl: {self.score}", 10, 10, arcade.color.BLACK, 14)


    # Verarbeitet Tastendrücke, um die Spielfigur zu bewegen.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.speed_y = 5  # Bewegung nach oben
        elif key == arcade.key.DOWN:
            self.player.speed_y = -5  # Bewegung nach unten
        elif key == arcade.key.LEFT:
            self.player.speed_x = -5  # Bewegung nach links
        elif key == arcade.key.RIGHT:
            self.player.speed_x = 5  # Bewegung nach rechts
    
    
    # Stoppt die Bewegung der Spielfigur, wenn die Taste losgelassen wird.   
    def on_key_release(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.player.speed_y = 0  # Stoppt die vertikale Bewegung
        elif key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player.speed_x = 0  # Stoppt die horizontale Bewegung


# Hauptprogramm
window = CollectGame(title="Sammelspiel")  # Instanziiert das Spiel
arcade.run()  # Startet die Arcade-Spielschleife

'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

