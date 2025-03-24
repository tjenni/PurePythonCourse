#              _______________________________________
#       ______|                                       |_____
#       \     |    12.4 SPRITES UND SPRITE-GRUPPEN    |    /
#        )    |_______________________________________|   (
#       /________)                                (________\     17.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Sprites sind zentrale Elemente in vielen Spielen und stellen Bilder oder Figuren
# dar, die sich auf dem Bildschirm bewegen können. In Arcade sind Sprites besonders
# einfach zu handhaben und zu gruppieren. In diesem Kapitel lernst du, wie du
# Sprites erstellst, bewegst und in Gruppen organisierst.


# _________________________________
#                                 /
# Einfache Sprites erstellen      (
# ________________________________\

# In Arcade können Grafiken und Animationen durch Sprites dargestellt werden.
# Ein Sprite ist ein Objekt, das ein Bild verwendet, um eine Figur, einen Gegenstand
# oder eine andere Grafik in einem Spiel darzustellen. Arcade bietet hierfür die Klasse
# `arcade.Sprite`, die eine einfache Möglichkeit bietet, mit Bildern zu arbeiten.

# Ressourcen:
# Arcade stellt eine umfangreiche Bibliothek mit Bildern, Schriftarten und Tönen bereit.

# Diese Ressourcen sind unter folgendem Link verfügbar:
#    https://api.arcade.academy/en/2.6.17/resources.html

# Um auf die Ressourcen zuzugreifen, verwende im Pfad das Präfix `:resources:`. 

# Beispiel:
# ":resources:images/animated_characters/female_person/femalePerson_idle.png"


# Im folgenden Beispiel wird ein Sprite aus einem Bild erstellt, auf dem Bildschirm 
# positioniert und bewegt:

import arcade

class SingleSpriteExample(arcade.Window):

    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        self.background_color = arcade.csscolor.LIGHT_SKY_BLUE
        
        
        # Erstelle ein Sprite mit einem Bild und einer Größe
        self.player = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)  
        self.player.center_x = 400
        self.player.center_y = 300
        
        # Erstelle eine Sprite-Liste
        self.player_list = arcade.SpriteList()
        
        # Füge Spieler zur Sprite-Liste hinzu
        self.player_list.append(self.player)

    def on_draw(self):
        self.clear()
        self.player_list.draw()  # Sprite zeichnen

    def on_update(self, delta_time):
        self.player.center_x += 1  # Bewegung des Sprites

window = SingleSpriteExample(title="Einzelner Sprite")
arcade.run()




# _________________________________
#                                 /
# Sprite-Gruppen und Listen      (
# ________________________________\

# In Arcade können mehrere Sprites effizient in einer `SpriteList` organisiert werden. 
# Dies ist besonders nützlich, wenn du mit Gruppen ähnlicher Objekte arbeitest, 
# wie Feinden, Hindernissen oder Gegenständen. Die `SpriteList` bietet Funktionen, 
# um alle enthaltenen Sprites zu zeichnen, zu aktualisieren oder mit anderen 
# Objekten auf Kollisionen zu prüfen.

# Warum Sprite-Listen verwenden?
#
# - Organisation: Ähnliche Objekte werden in einer einzigen Liste zusammengefasst.
#
# - Effizienz: Durch optimierte Funktionen wie `update()` und `draw()` können alle Sprites
#   in einer `SpriteList` gleichzeitig verarbeitet werden.
#
# - Einfache Kollisionserkennung: `SpriteList` unterstützt Methoden, um schnell
#   Kollisionen zwischen Sprites zu prüfen.


# Im folgenden Beispiel wird eine Sprite-Liste erstellt, die mehrere Münzen enthält.

import arcade

class SpriteGroupExample(arcade.Window):

    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)

        self.background_color = arcade.csscolor.LIGHT_BLUE

        # Erstelle eine Sprite-Liste
        self.coin_list = arcade.SpriteList()

        # Füge der Sprite-Liste mehrere Münzen hinzu
        for i in range(5):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", 0.5)
            coin.center_x = i * 100 + 200
            coin.center_y = 300
            self.coin_list.append(coin)

    def on_draw(self):
        self.clear()
        self.coin_list.draw()  # Zeichnet alle Sprites in der Liste

window = SpriteGroupExample(title="Sprite-Gruppen")
arcade.run()




# _________________________________
#                                 /
# Sprite-Bewegung                (
# ________________________________\

# Die `SpriteList`-Klasse hat nützliche Funktionen für die gleichzeitige Bewegung 
# aller Sprites in der Liste. 

# Im folgenden Beispiel werden fallende Schneeflocken dargestellt. Die Schneeflocke 
# ist ein Sprite, dessen Bild `snowflake.png` heisst. Diese Bild-Datei liegt
# im Ordner `_assets`. 

# Am besten kopierst du den folgenden Programmcode nach Thonny und speicherst dann
# die Programmdatei in den gleichen Ordner wo sich auch dieses Kapitel befindet. 
# Dann sollte die Bild-Datei gefunden werden können. 


import arcade
import random
import math

class MovingSpriteGroupExample(arcade.Window):

    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        self.background_color = arcade.csscolor.LIGHT_BLUE
        
        # Erstelle eine Sprite-Liste für fallende Schneeflocken
        self.flake_list = arcade.SpriteList()

        # Füge 20 Schneeflocken zur Sprite-Liste hinzu
        for i in range(20):
            # Lade das Bild der Schneeflocke
            flake = arcade.Sprite("_assets/12.04/snowflake.png")
            
            # Setze einen zufälligen Startwinkel für die Schneeflocke (zwischen 0° und 360°)
            flake.angle = random.randint(0, 360)
            
            # Skaliere die Schneeflocke zufällig zwischen 0.05 und 0.1
            scale = 0.01 * random.randint(5, 10)
            flake.scale = (scale,scale)
            
            # Setze die Startposition der Schneeflocke zufällig:
            # - horizontal (x-Koordinate) innerhalb der Fensterbreite
            # - vertikal (y-Koordinate) oberhalb des sichtbaren Bereichs
            flake.center_x = random.randint(0, self.width)
            flake.center_y = 600 + random.randint(20, 800)
            
            # Füge die Schneeflocke der Sprite-Liste hinzu
            self.flake_list.append(flake)

    def on_draw(self):
        # Zeichne den Bildschirm
        self.clear()
        
        # Zeichne alle Schneeflocken in der Sprite-Liste
        self.flake_list.draw()
    
    # Aktualisiere die Position der Schneeflocken
    def on_update(self, delta_time):
        # Iteriere durch jede Schneeflocke in der Sprite-Liste
        for flake in self.flake_list:
            # Bewege die Schneeflocke nach unten (vertikal)
            flake.center_y -= 1
            
            # Füge eine leichte, sinusförmige Bewegung in horizontaler Richtung hinzu
            flake.center_x += 0.5 * math.sin(0.01 * flake.center_y + flake.scale[0])
            
            # Lasse die Schneeflocke leicht rotieren, abhängig von ihrer Position
            flake.angle += 0.1 * math.sin(0.01 * flake.center_y + flake.scale[0])
            
            # Wenn die Schneeflocke den unteren Bildschirmrand verlässt
            if flake.center_y < -50:
                # Setze ihre Position zurück:
                # - horizontal (x-Koordinate) zufällig innerhalb der Fensterbreite
                # - vertikal (y-Koordinate) oberhalb des sichtbaren Bereichs
                flake.center_x = random.randint(0, self.width)
                flake.center_y = 600 + random.randint(20, 800)

# Erstelle das Fenster und starte die Animation
window = MovingSpriteGroupExample(title="Schneeflocken")
arcade.run()




# _________________________________
#                                 /
# Kollisionserkennung            (
# ________________________________\

# Arcade ermöglicht eine einfache Kollisionserkennung zwischen Sprites und 
# Sprite-Gruppen, die mit `check_for_collision()` oder `check_for_collision_with_list()` 
# durchgeführt werden kann.

import arcade
import random

class CollisionExample(arcade.Window):
    
    def __init__(self, width=800, height=600, title=""):
        super().__init__(width=width, height=height, title=title)
        
        self.background_color = arcade.csscolor.GREEN
        

        # Spieler-Sprite erstellen und initialisieren
        self.player = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.player.center_x = 400  # Startposition des Spielers (x-Koordinate)
        self.player.center_y = 100  # Startposition des Spielers (y-Koordinate)
        
        self.player.speed_x = 0  # Anfangsgeschwindigkeit des Spielers in x-Richtung
        self.player.speed_y = 0  # Anfangsgeschwindigkeit des Spielers in y-Richtung
        
        # Hindernisse als Sprite-Liste erstellen
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)
        

        # Hindernisse als Sprite-Liste erstellen
        self.obstacle_list = arcade.SpriteList()
        for i in range(10):
            # Erstelle ein Hindernis-Sprite (z. B. ein Stein)
            obstacle = arcade.Sprite(":resources:images/tiles/rock.png", 0.5)
            
            # Positioniere das Hindernis zufällig innerhalb des Fensters
            obstacle.center_x = random.randint(50, self.width - 50)
            obstacle.center_y = random.randint(150, self.height - 50)
            
            # Füge das Hindernis zur Sprite-Liste hinzu
            self.obstacle_list.append(obstacle)
    
    # Aktualisiere die Objekte
    def on_update(self, delta_time):
        # Aktualisiere die Position des Spielers basierend auf seiner Geschwindigkeit
        self.player.center_x += self.player.speed_x
        self.player.center_y += self.player.speed_y
        
        # Überprüfe, ob der Spieler mit einem Hindernis kollidiert
        if arcade.check_for_collision_with_list(self.player, self.obstacle_list):
            # Rückgängig machen der letzten Bewegung, wenn eine Kollision erkannt wird
            self.player.center_x -= self.player.speed_x
            self.player.center_y -= self.player.speed_y
    
    # Zeichne den Bildschirm
    def on_draw(self):
        self.clear()
        
        # Zeichne den Spieler
        self.player_list.draw()
        
        # Zeichne die Hindernisse
        self.obstacle_list.draw()

    # Bewege den Spieler basierend auf der gedrückten Taste
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.speed_y = 5  # Bewege nach oben
        elif key == arcade.key.DOWN:
            self.player.speed_y = -5  # Bewege nach unten
        elif key == arcade.key.LEFT:
            self.player.speed_x = -5  # Bewege nach links
        elif key == arcade.key.RIGHT:
            self.player.speed_x = 5  # Bewege nach rechts
    
    # Stoppe die Bewegung, wenn die Taste losgelassen wird
    def on_key_release(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.player.speed_y = 0  # Stoppe die vertikale Bewegung
        elif key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player.speed_x = 0  # Stoppe die horizontale Bewegung

# Erstelle das Fenster und starte das Programm
window = CollisionExample(title="Kollisionserkennung")
arcade.run()



# _________________________________
#                                 /
# Zusammenfassung                (
# ________________________________\

# - Sprites: 
#   Sprites sind fundamentale Bausteine in Arcade-Spielen und repräsentieren Figuren, 
#   Objekte oder andere visuelle Elemente. Sie basieren auf Bildern und können leicht 
#   positioniert, bewegt oder skaliert werden.

# - SpriteList:
#   Mit `SpriteList` lassen sich mehrere Sprites effizient organisieren. 
#   Sie ermöglicht:
#   - Gemeinsames Zeichnen aller Sprites (`draw()`).
#
#   - Gleichzeitige Aktualisierung (`update()`).
#
#   - Einfache Kollisionserkennung zwischen Sprites in der Liste.

# - Bewegung:
#   Sprites können individuell oder in Gruppen bewegt werden. Mit `SpriteList` kann 
#   dies für alle Sprites in der Liste gleichzeitig geschehen, wodurch Animationen 
#   wie fallende Schneeflocken oder Bewegungen von Feinden einfach umgesetzt werden.

# - Kollisionserkennung:
#   Arcade bietet eingebaute Methoden wie `check_for_collision()` und 
#   `check_for_collision_with_list()`, um die Interaktion zwischen Sprites zu prüfen.
#   Diese Funktionen sind besonders nützlich für Spielmechaniken wie das Erkennen 
#   von Zusammenstößen zwischen Spieler und Hindernissen.

# - Zusammenarbeit mit Ressourcen:
#   Mit Arcade kannst du auf eine umfangreiche Bibliothek von Ressourcen zugreifen, 
#   wie z. B. Bilder oder Töne. Verwende das Präfix `:resources:` im Dateipfad, 
#   um auf diese Inhalte zuzugreifen, z. B.:
#   `":resources:images/animated_characters/female_person/femalePerson_idle.png"`

# Hinweis:
# Achte darauf, dass alle verwendeten Bildressourcen korrekt im Projektordner 
# vorhanden sind. Für Windows- und Mac-Nutzer empfiehlt es sich, das Projekt und 
# die Bilder im gleichen Ordner zu speichern, um Zugriffsprobleme zu vermeiden.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Schreibe eine Anwendung, die ein animiertes Aquarium simuliert. Im Ordner
# hat es drei Fischgrafike. Jeder Fisch soll sich zufällig nach links oder rechts 
# bewegen. 

# Hinweis: Um das Bild horzizontal zu spiegeln, kannst du den folgenden Befehl verwenden.
#
#   fish.texture = arcade.load_texture("_assets/fish_1.png", flipped_horizontally=True)


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Anwendung, bei der eine Gruppe von Münz-Sprites vorhanden ist.
# Wenn der Spieler eine Münze berührt, soll die Münze verschwinden und ein Punkt
# zur Punktzahl hinzugefügt werden. Zeige die aktuelle Punktzahl in der Titelzeile an.
#
# Hinweise: 
#
# - Um die Münze aus der Münzliste zu entfernen, verwende den Befehl:
#
#        coin.remove_from_sprite_lists() 
#
# - Um den Fenstertitel zu verändern, verwende den Befehl:
#
#        self.set_caption(f"Münzspiel - Punktzahl: {self.score}")


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Anwendung, bei der ein Roboter den Spieler ständig verfolgt. 
# Der Spieler soll sich mit den Pfeiltasten bewegen können, während der Roboter 
# automatisch versucht, dem Spieler so nahe wie möglich zu kommen. Achte dabei 
# darauf, dass der Roboter in einer realistischen Geschwindigkeit auf den 
# Spieler zuläuft.


# Füge hier deine Lösung ein.




#  ================================================.
#       .-.   .-.     .--.                         |
#      | OO| | OO|   / _.-' .-.   .-.  .-.   .''.  |
#      |   | |   |   \  '-. '-'   '-'  '-'   '..'  |
#      '^^^' '^^^'    '--'                         |  Kennst du das Spiel 
#  ===============.  .-.  .================.  .-.  |  Pacman? https://freepacman.org
#                 | |   | |                |  '-'  |
#                 | |   | |                |       |
#                 | ':-:' |                |  .-.  |
#  l42            |  '-'  |                |  '-'  |
#  ==============='       '================'       |
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
# Schreibe eine Anwendung, die ein animiertes Aquarium simuliert. Im Ordner
# hat es drei Fischgrafike. Jeder Fisch soll sich zufällig nach links oder rechts 
# bewegen. 

# Hinweis: Um das Bild horzizontal zu spiegeln, kannst du den folgenden Befehl verwenden.
#
#   fish.texture = arcade.load_texture("_assets/fish_1.png", flipped_horizontally=True)

'''
import arcade
import random
import math

class AquariumApp(arcade.Window):
    """
    Eine Aquarium-Anwendung, die Fische animiert, die sich horizontal über den Bildschirm bewegen
    und eine leichte Wellenbewegung ausführen.
    """
    
    def __init__(self, width=800, height=600, title=""):
        """
        Initialisiert das Fenster und die Sprite-Liste für die Fische.
        """
        super().__init__(width=width, height=height, title=title)
        
        # Setze die Hintergrundfarbe auf eine aquatische Farbe
        arcade.set_background_color(arcade.color.CELADON_BLUE)
        
        # Erstelle eine Liste für die Fische
        self.fish_list = arcade.SpriteList()

    def setup(self):
        """
        Initialisiere die Fische im Aquarium. Jeder Fisch wird mit zufälligen Attributen erstellt.
        """
        for i in range(10):  # Erstelle 10 Fische
            
            # Wähle zufällig eine Fischgrafik aus den verfügbaren Dateien aus
            i = random.randint(1, 3)
            
            # Lade das Fisch-Sprite
            fish = arcade.Sprite(f"_assets/12.04/fish_{i}.png", 0.5)
            
            # Skaliere den Fisch zufällig
            fish.scale = 0.04 * random.randint(2, 8)
            
            # Positioniere den Fisch zufällig entlang der y-Achse
            fish.center_y = random.randint(0, self.height)
            
            # Setze die horizontale Geschwindigkeit proportional zur Skalierung
            fish.speed_x = 0.3 * fish.scale * random.randint(-10, 10)
            
            # Verhindere, dass der Fisch eine Geschwindigkeit von 0 hat
            if fish.speed_x == 0:
                fish.speed_x = 0.3 * fish.scale
                
            # Debugging: Zeige die Geschwindigkeit des Fisches in der Konsole an
            print(fish.speed_x)
                
            if fish.speed_x > 0:  # Der Fisch schwimmt nach rechts
                # Setze die Startposition außerhalb des linken Bildschirmenrands
                fish.center_x = random.randint(-150, -70)
                # Spiegele die Textur horizontal, damit der Fisch nach rechts schaut
                fish.texture = arcade.load_texture(f"_assets/fish_{i}.png", flipped_horizontally=True)
            
            else:  # Der Fisch schwimmt nach links
                # Setze die Startposition außerhalb des rechten Bildschirmenrands
                fish.center_x = self.width + random.randint(70, 150)
                
            # Füge den Fisch der Sprite-Liste hinzu
            self.fish_list.append(fish)

    def on_draw(self):
        """
        Zeichne den aktuellen Zustand des Aquariums, einschließlich aller Fische.
        """
        self.clear()
        self.fish_list.draw()  # Zeichne alle Fische

    def on_update(self, delta_time):
        """
        Aktualisiere die Position der Fische, um sie horizontal zu bewegen und
        ihnen eine leichte sinusförmige Bewegung zu geben.
        """
        for fish in self.fish_list:
            # Bewege den Fisch horizontal basierend auf seiner Geschwindigkeit
            fish.center_x += fish.speed_x
            
            # Füge eine sinusförmige Wellenbewegung entlang der y-Achse hinzu
            fish.center_y += 0.2 * math.sin(0.01 * abs(fish.speed_x) * fish.center_x + fish.scale)
            
            # Überprüfe, ob der Fisch den rechten Rand verlassen hat (schwimmt nach rechts)
            if fish.speed_x > 0 and fish.center_x > self.width + 100:
                # Setze die Position des Fisches zurück
                fish.center_y = random.randint(0, self.height)
                fish.center_x = random.randint(-200, -100)
                
            # Überprüfe, ob der Fisch den linken Rand verlassen hat (schwimmt nach links)
            if fish.speed_x < 0 and fish.center_x < -100:
                # Setze die Position des Fisches zurück
                fish.center_y = random.randint(0, self.height)
                fish.center_x = self.width + random.randint(100, 200)

# Anwendung starten
window = AquariumApp(title="Aquarium")
window.setup()  # Initialisiere die Fische
arcade.run()  # Starte das Aquarium
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Anwendung, bei der eine Gruppe von Münz-Sprites vorhanden ist.
# Wenn der Spieler eine Münze berührt, soll die Münze verschwinden und ein Punkt
# zur Punktzahl hinzugefügt werden. Zeige die aktuelle Punktzahl in der Titelzeile an.
#
# Hinweise: 
#
# - Um die Münze aus der Münzliste zu entfernen, verwende den Befehl:
#
#        coin.remove_from_sprite_lists() 
#
# - Um den Fenstertitel zu verändern, verwende den Befehl:
#
#        self.set_caption(f"Münzspiel - Punktzahl: {self.score}")


'''
import arcade
import random

# Klasse für die Münzspiel-Anwendung
class CoinApp(arcade.Window):
    
    def __init__(self, width=800, height=600, title=""):
        # Initialisiere das Fenster
        super().__init__(width=width, height=height, title=title)
        
        # Spieler-Sprite initialisieren
        self.player = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.player.center_x = 100  # Startposition des Spielers (x-Koordinate)
        self.player.center_y = 100  # Startposition des Spielers (y-Koordinate)
        
        # Sprite-Liste für Münzen
        self.coin_list = arcade.SpriteList()
        
        # Punktestand des Spielers
        self.score = 0
    
    # Erstelle eine einzelne Münze an einer zufälligen Position
    def create_coin(self):
        # Initialisiere eine Münze
        coin = arcade.Sprite(":resources:images/items/coinGold.png", 0.5)
        
        # Setze die Position der Münze zufällig innerhalb des Fensters
        coin.center_x = random.randint(50, self.width - 50)
        coin.center_y = random.randint(50, self.height - 50)
        
        # Füge die Münze zur Sprite-Liste hinzu
        self.coin_list.append(coin)
        
    # Setup-Methode: Erstellt die anfänglichen Münzen und setzt den Fenstertitel
    def setup(self):
        # Erstelle 10 Münzen
        for _ in range(10):
            self.create_coin()
        
        # Aktualisiere den Fenstertitel
        self.update_title()

    # Zeichne den Spieler und die Münzen
    def on_draw(self):
        self.clear()
        
        # Zeichne den Spieler
        self.player.draw()
        
        # Zeichne die Münzen
        self.coin_list.draw()

    # Aktualisiere den Fenstertitel mit dem aktuellen Punktestand
    def update_title(self):
        self.set_caption(f"Münzspiel - Punktzahl: {self.score}")

    # Reagiere auf Tastendrücke und bewege den Spieler
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.change_y = 5  # Bewege den Spieler nach oben
        elif key == arcade.key.DOWN:
            self.player.change_y = -5  # Bewege den Spieler nach unten
        elif key == arcade.key.LEFT:
            self.player.change_x = -5  # Bewege den Spieler nach links
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5  # Bewege den Spieler nach rechts

    # Stoppe die Bewegung des Spielers, wenn die Taste losgelassen wird
    def on_key_release(self, key, modifiers):
        if key in (arcade.key.UP, arcade.key.DOWN):
            self.player.change_y = 0  # Stoppe die vertikale Bewegung
        elif key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0  # Stoppe die horizontale Bewegung

    # Aktualisiere die Position des Spielers und prüfe auf Kollisionen mit Münzen
    def on_update(self, delta_time):
        # Aktualisiere die Position des Spielers
        self.player.update()
        
        # Prüfe, ob der Spieler eine oder mehrere Münzen berührt
        coins_hit = arcade.check_for_collision_with_list(self.player, self.coin_list)
        
        # Entferne getroffene Münzen und erhöhe den Punktestand
        for coin in coins_hit:
            coin.remove_from_sprite_lists()  # Entferne die Münze aus der Sprite-Liste
            self.score += 1  # Erhöhe den Punktestand
            self.update_title()  # Aktualisiere den Fenstertitel
        
        # Stelle sicher, dass immer mindestens 10 Münzen auf dem Spielfeld sind
        if len(self.coin_list) < 10:
            self.create_coin()


# Starte die Anwendung
window = CoinApp(title="Münzspiel")
window.setup()  # Setup der Münzen und Fenstertitel
arcade.run()
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Anwendung, bei der ein Roboter den Spieler ständig verfolgt. 
# Der Spieler soll sich mit den Pfeiltasten bewegen können, während der Roboter 
# automatisch versucht, dem Spieler so nahe wie möglich zu kommen. Achte dabei 
# darauf, dass der Roboter in einer realistischen Geschwindigkeit auf den 
# Spieler zuläuft.

'''
import arcade
import math


class ChasingRobotApp(arcade.Window):
    
    def __init__(self, width=800, height=600, title=""):
        # Initialisiere das Fenster
        super().__init__(width=width, height=height, title=title)
        
        # Hintergrundfarbe setzen
        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)
        
        # Spieler-Sprite initialisieren
        self.player = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.player.center_x = 400  # Startposition des Spielers (x-Koordinate)
        self.player.center_y = 300  # Startposition des Spielers (y-Koordinate)
        
        # Roboter-Sprite initialisieren
        self.robot = arcade.Sprite(":resources:images/animated_characters/robot/robot_idle.png", 0.5)
        self.robot.center_x = 100  # Startposition des Roboters (x-Koordinate)
        self.robot.center_y = 100  # Startposition des Roboters (y-Koordinate)
        
        # Geschwindigkeit des Roboters
        self.robot_speed = 2

    def on_draw(self):
        # Bildschirm rendern
        self.clear()
        
        # Spieler und Roboter zeichnen
        self.player.draw()
        self.robot.draw()

    def on_key_press(self, key, modifiers):
        # Spielerbewegung basierend auf den Pfeiltasten
        if key == arcade.key.UP:
            self.player.change_y = 5
        elif key == arcade.key.DOWN:
            self.player.change_y = -5
        elif key == arcade.key.LEFT:
            self.player.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5

    def on_key_release(self, key, modifiers):
        # Stoppe die Bewegung des Spielers, wenn die Taste losgelassen wird
        if key in (arcade.key.UP, arcade.key.DOWN):
            self.player.change_y = 0
        elif key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0

    def on_update(self, delta_time):
        # Aktualisiere die Position des Spielers
        self.player.update()
        
        # Berechne den Abstand und die Richtung zwischen dem Roboter und dem Spieler
        dx = self.player.center_x - self.robot.center_x
        dy = self.player.center_y - self.robot.center_y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        
        # Bewege den Roboter in Richtung des Spielers
        if distance > 0:  # Vermeide Division durch Null
            self.robot.center_x += self.robot_speed * (dx / distance)
            self.robot.center_y += self.robot_speed * (dy / distance)


# Starte die Anwendung
window = ChasingRobotApp(title="Roboter verfolgt Spieler")
arcade.run()

'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

