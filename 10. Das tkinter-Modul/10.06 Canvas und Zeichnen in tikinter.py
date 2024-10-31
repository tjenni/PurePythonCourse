#              ___________________________________________
#       ______|                                           |_____
#       \     |    10.6 CANVAS UND ZEICHNEN IN TKINTER    |    /
#        )    |___________________________________________|   (
#       /________)                                    (________\      30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Das `Canvas`-Widget in `tkinter` ist ein mächtiges Werkzeug zum Zeichnen von
# Formen, Linien, Text und sogar Bildern in einer grafischen Oberfläche.
# Es wird häufig für einfache Zeichnungen, Spiele oder Visualisierungen genutzt.


# ____________________________
#                            /
# Canvas-Widget erstellen   (
# ___________________________\

# Um ein `Canvas` zu verwenden, muss das `Canvas`-Widget im Fenster platziert werden.

import tkinter as tk

root = tk.Tk()
root.title("Canvas Beispiel")

# Ein Canvas-Widget mit einer festen Größe erstellen
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

root.mainloop()

# In diesem Beispiel erstellen wir ein leeres Canvas-Widget mit einer Größe
# von 400x300 Pixeln und einem weißen Hintergrund.




# ____________________________
#                            /
# Formen zeichnen           (
# ___________________________\

# Mit dem `Canvas`-Widget können wir verschiedene Formen zeichnen:
# - Linien: `create_line()`
#
# - Rechtecke: `create_rectangle()`
#
# - Ovale/Kreise: `create_oval()`
#
# - Polygone: `create_polygon()`

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Linie zeichnen
canvas.create_line(50, 50, 350, 50, fill="blue", width=3)

# Rechteck zeichnen
canvas.create_rectangle(50, 100, 200, 200, fill="green", outline="black")

# Oval (Kreis) zeichnen
canvas.create_oval(220, 100, 370, 200, fill="red")

# Dreieck (Polygon) zeichnen
canvas.create_polygon(200, 250, 300, 250, 250, 180, fill="purple", outline="black")

root.mainloop()

# Die ersten beiden Argumente für `create_line`, `create_rectangle`, `create_oval` und `create_polygon`
# sind immer die x- und y-Koordinaten, die die Position und Größe der Formen festlegen.




# ____________________________
#                            /
# Text zeichnen             (
# ___________________________\

# Neben Formen kann auch Text auf einem Canvas-Widget dargestellt werden.

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Text auf dem Canvas anzeigen
canvas.create_text(200, 150, text="Willkommen zu tkinter Canvas!", fill="black", font=("Arial", 16))

root.mainloop()

# In diesem Beispiel wird der Text „Willkommen zu tkinter Canvas!“ an der Position
# (200, 150) angezeigt. Der Parameter `font` ermöglicht die Einstellung der Schriftart und -größe.




# ____________________________
#                            /
# Bilder einfügen           (
# ___________________________\

# Mit `create_image()` können Bilder (z. B. PNG) auf dem Canvas-Widget platziert werden.

from tkinter import PhotoImage

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Bild laden und auf dem Canvas anzeigen
image = PhotoImage(file="beispiel.png")  # Ersetze "beispiel.png" durch den Pfad deines Bildes
canvas.create_image(200, 150, image=image)

root.mainloop()

# `PhotoImage()` lädt das Bild, und `create_image()` platziert es an den
# angegebenen Koordinaten auf dem Canvas. Das Bild muss im gleichen Verzeichnis
# liegen oder der Pfad muss korrekt angegeben sein.




# ____________________________
#                            /
# Dynamische Inhalte        (
# ___________________________\

# Das Canvas-Widget erlaubt es uns, dynamische Inhalte hinzuzufügen und zu
# verändern, was es ideal für interaktive Anwendungen und einfache Spiele macht.
# Mit der Methode `coords()` können die Positionen von Objekten geändert werden.

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Kreis zeichnen
circle = canvas.create_oval(180, 130, 220, 170, fill="orange")

# Funktion, um den Kreis zu bewegen
def move_circle(event):
    canvas.coords(circle, event.x - 20, event.y - 20, event.x + 20, event.y + 20)

# Ereignisbindung für Bewegung
canvas.bind("<Motion>", move_circle)

root.mainloop()

# In diesem Beispiel bewegt sich der Kreis mit der Maus. Die `coords()`-Methode ändert
# die Koordinaten des Objekts `circle`, und durch `bind("<Motion>", move_circle)` wird
# `move_circle()` aufgerufen, wenn die Maus bewegt wird.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\


# - Das `Canvas`-Widget eignet sich hervorragend zum Zeichnen und für einfache Spiele.
#
# - Mit `create_line`, `create_rectangle`, `create_oval` und `create_polygon` lassen sich
#   verschiedene Formen zeichnen.
#
# - `create_text()` ermöglicht das Einfügen von Text, und `create_image()` fügt Bilder hinzu.
#
# - Mit `coords()` und `bind()` können wir dynamische und interaktive Inhalte erstellen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine GUI-Anwendung mit einem Canvas-Widget, das eine grüne Linie
# und einen blauen Kreis zeichnet. Der Kreis sollte in der Mitte des Canvas erscheinen.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe ein Programm, das ein Canvas mit der Nachricht „Klicke mich!“
# erstellt. Wenn der Benutzer auf das Canvas klickt, soll der Text zu
# „Danke fürs Klicken!“ wechseln.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Programm mit einem Canvas, das einen roten Kreis zeigt.
# Binde eine Funktion an das Canvas, die den Kreis bei jedem Klick an
# eine neue zufällige Position auf dem Canvas verschiebt.


# Füge hier deine Lösung ein.



#     ________________________
#    |.----------------------.|
#    ||                      ||
#    ||       ______         ||
#    ||     .;;;;;;;;.       ||
#    ||    /;;;;;;;;;;;\     ||
#    ||   /;/`    `-;;;;; . .||     Du bist nun ein/-e grosse/-r
#    ||   |;|__  __  \;;;|   ||     Künstler/-in. :-)
#    ||.-.|;| e`/e`  |;;;|   ||
#    ||   |;|  |     |;;;|'--||
#    ||   |;|  '-    |;;;|   ||
#    ||   |;;\ --'  /|;;;|   ||
#    ||   |;;;;;---'\|;;;|   ||
#    ||   |;;;;|     |;;;|   ||
#    ||   |;;.-'     |;;;|   ||
#    ||'--|/`        |;;;|--.||
#    ||;;;;    .     ;;;;.\;;||
#    ||;;;;;-.;_    /.-;;;;;;||
#    ||;;;;;;;;;;;;;;;;;;;;;;||
#    ||jgs;;;;;;;;;;;;;;;;;;;||
#    '------------------------'
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
# Erstelle eine GUI-Anwendung mit einem Canvas-Widget, das eine grüne Linie
# und einen blauen Kreis zeichnet. Der Kreis sollte in der Mitte des Canvas erscheinen.

'''
import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas-Zeichnung")

        # Canvas erstellen
        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack()

        # Grüne Linie zeichnen
        self.canvas.create_line(0, 150, 300, 150, fill="green", width=3)

        # Blauen Kreis in der Mitte des Canvas zeichnen
        self.canvas.create_oval(125, 125, 175, 175, fill="blue", outline="blue")

# Hauptprogramm
root = tk.Tk()
app = DrawingApp(root)
root.mainloop()
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe ein Programm, das ein Canvas mit der Nachricht „Klicke mich!“
# erstellt. Wenn der Benutzer auf das Canvas klickt, soll der Text zu
# „Danke fürs Klicken!“ wechseln.

'''
import tkinter as tk

class ClickMessageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Klick-Event auf Canvas")

        # Canvas erstellen
        self.canvas = tk.Canvas(root, width=300, height=200, bg="white")
        self.canvas.pack()

        # Text auf Canvas hinzufügen
        self.text_id = self.canvas.create_text(150, 100, text="Klicke mich!", font=("Arial", 16))

        # Klick-Event auf das Canvas binden
        self.canvas.bind("<Button-1>", self.change_text)

    def change_text(self, event):
        self.canvas.itemconfig(self.text_id, text="Danke fürs Klicken!")

# Hauptprogramm
root = tk.Tk()
app = ClickMessageApp(root)
root.mainloop()
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Programm mit einem Canvas, das einen roten Kreis zeigt.
# Binde eine Funktion an das Canvas, die den Kreis bei jedem Klick an
# eine neue zufällige Position auf dem Canvas verschiebt.

'''
import tkinter as tk
import random

class MovingCircleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Beweglicher Kreis")

        # Canvas erstellen
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        # Roten Kreis zeichnen
        self.circle_id = self.canvas.create_oval(180, 180, 220, 220, fill="red")

        # Klick-Event auf das Canvas binden
        self.canvas.bind("<Button-1>", self.move_circle)

    def move_circle(self, event):
        # Zufällige neue Position für den Kreis berechnen
        new_x = random.randint(20, 380)
        new_y = random.randint(20, 380)

        # Kreis zur neuen Position verschieben
        self.canvas.coords(self.circle_id, new_x - 20, new_y - 20, new_x + 20, new_y + 20)

# Hauptprogramm
root = tk.Tk()
app = MovingCircleApp(root)
root.mainloop()
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


