#              ___________________________
#       ______|                          |_____
#       \     |   15.1 URSINA EINFÜHRUNG  |    /
#        )    |__________________________|   (
#       /________)                    (________\     6.12.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Ursina ist ein einfaches und dennoch leistungsfähiges Python-Framework für 3D-Spiele und -Anwendungen.
# Es eignet sich besonders gut für Einsteiger, da es eine klare und intuitive API bietet. Ursina
# basiert auf Panda3D, einem bewährten Framework für Spieleentwicklung, und erweitert es um
# benutzerfreundliche Funktionen.

# Mit Ursina kannst du:
# - Interaktive 3D-Szenen erstellen.
# - Objekte und Charaktere bewegen und animieren.
# - Spiele und Simulationen entwickeln.

# Dieses Kapitel führt dich in die Grundlagen der Ursina-Entwicklung ein.


# __________________________
#                          /
# Installation             (
# _________________________\

# Bevor wir mit Ursina arbeiten können, musst du das Framework installieren.
# Gehe dazu in Thonny auf Werkzeuge > Verwaltete Packete und such nach ursina. 
# Klicke anschliessend auf `installiere`. Sobald die Installation abgeschlossen ist, 
# kannst du Ursina in deinem Python-Code verwenden.


# ___________________________
#                           /
# Erste Schritte mit Ursina (
# ___________________________\

# Ursina-Anwendungen starten mit dem Import des Frameworks und dem Erstellen einer Instanz
# der `Ursina`-Klasse. Du kannst dann Objekte wie Würfel, Kugeln oder Ebenen hinzufügen und
# diese rendern.

# Beispiel: Ein einfacher Würfel in einer 3D-Szene
from ursina import *

# Erstellen der Ursina-App
app = Ursina()

# Hinzufügen eines Würfels zur Szene
cube = Entity(model='cube', color=color.orange, scale=(2, 2, 2))

# Start der Anwendung
app.run()

# Wenn du dieses Skript ausführst, erscheint ein orangefarbener Würfel auf dem Bildschirm.




# _________________________________
#                                 /
# Wichtige Komponenten in Ursina (
# ________________________________\




# 1. Entity:
#    - Repräsentiert ein Objekt in der 3D-Szene.
#    - Hat Eigenschaften wie `model`, `color`, `position` und `rotation`.


# Beispiel: Ein rotierender Würfel
from ursina import *

def update():
    cube.rotation_y += 30 * time.dt  # Dreht den Würfel in jeder Frame-Aktualisierung
    cube.rotation_z += 30 * time.dt

app = Ursina()

cube = Entity(model='cube', color=color.red)

app.run()







# 2. Modelle:
#    - Ursina bietet vorgefertigte Modelle wie `cube`, `sphere`, `plane`, `quad` usw.
#    - Du kannst auch eigene 3D-Modelle im `.obj`-Format laden.


# Beispiel: Ein rotierender Apfel
from ursina import *

def update():
    apple.rotation_y += 30 * time.dt  # Dreht den Würfel in jeder Frame-Aktualisierung
    apple.rotation_z += 20 * time.dt

app = Ursina()

apple = Entity(model='_assets/15.1/apple.obj', texture='_assets/15.1/apple.jpg', scale=(30,30,-30))

app.run()



# Beispiel: Laden eines benutzerdefinierten Modells


# 3. Farben:
#    - Ursina bietet vordefinierte Farben wie `color.red`, `color.green`, `color.blue`.
#    - Du kannst eigene Farben mit RGB-Werten definieren: `color.rgb(255, 128, 0)`.




# 4. Ereignisse:
#    - Mit Funktionen wie `update()` und `input()` kannst du Animationen und Benutzerinteraktionen
#      erstellen.



# Beispiel: Interaktion mit der Tastatur

from ursina import *

def update():
    apple.rotation_y += 30 * time.dt  # Dreht den Würfel in jeder Frame-Aktualisierung
    apple.rotation_z += 20 * time.dt

app = Ursina()

apple = Entity(model='_assets/15.1/apple.obj', texture='_assets/15.1/apple.jpg', scale=(30,30,-30))

def input(key):
    if key == 'space':
        print("Leertaste gedrückt!")

app.run()





# _______________________
#                       /
# Arbeiten mit Kameras (
# ______________________\

# Ursina bietet eine Standardkamera, die du anpassen kannst:
#camera.position = (0, 10, -20)  # Kamera-Position
#camera.rotation = (30, 0, 0)    # Kamera-Rotation



from ursina import *

# Erstellen der Ursina-App
app = Ursina()

# Hinzufügen eines Würfels zur Szene
cube = Entity(model='cube', color=color.orange, scale=(2, 2, 2))

camera.position = (0, 0, -10)
camera.rotation = (0, 5, 0)

# Start der Anwendung
app.run()











# Du kannst auch eine First-Person-Kamera verwenden:

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


def update():
    cube.rotation_y += 1  # Dreht den Würfel in jeder Frame-Aktualisierung

app = Ursina()

sky = Sky()

cube = Entity(model='cube', color=color.red)

player = FirstPersonController(gravity=0.0, position=(0,-2,-5))
player.cursor.disable()

app.run()


# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# Ursina ist ein benutzerfreundliches Framework für die Entwicklung von 3D-Spielen.
# In diesem Kapitel hast du gelernt:
#
# 1. Wie du Ursina installierst und eine einfache 3D-Szene erstellst.
# 2. Wie du Objekte zur Szene hinzufügst und ihre Eigenschaften anpasst.
# 3. Wie du Animationen und Benutzerinteraktionen einbaust.
#
# Ursina bietet eine hervorragende Grundlage für Anfänger, die ihre eigenen Spiele oder
# Simulationen entwickeln möchten. Im nächsten Kapitel werden wir uns mit fortgeschritteneren
# Themen wie Physik und Animationen beschäftigen.

# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine Szene mit einem grünen Würfel, einer blauen Kugel und einer roten Ebene
# als Boden. Platziere die Objekte so, dass die Kugel auf dem Würfel liegt.

# Füge hier deine Lösung ein.



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle einen rotierenden Zylinder, der in jeder Frame-Aktualisierung um die X-Achse
# rotiert. Verwende die `update()`-Funktion, um die Rotation zu implementieren.

# Füge hier deine Lösung ein.



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Implementiere eine First-Person-Ansicht mit der `FirstPersonController`-Klasse. Erstelle
# ein einfaches Spielfeld mit Würfeln als Hindernisse, durch das sich der Spieler bewegen kann.

# Füge hier deine Lösung ein.