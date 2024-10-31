#              ____________________
#       ______|                    |_____
#       \     |    10.8 FRAMES     |    /
#        )    |____________________|   (
#       /________)             (________\      30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# In tkinter können komplexe Layouts durch den Einsatz von `Frames` und
# fortgeschrittenem Layout-Management erstellt werden. `Frames` sind wie
# Container, die andere Widgets gruppieren und helfen, eine strukturierte
# und übersichtliche GUI zu erstellen.


# ___________________________
#                           /
# Was sind Frames?         (
# __________________________\

# Ein `Frame` ist ein Widget, das als Container für andere Widgets dient.
# Durch das Gruppieren von Widgets in verschiedenen `Frames` kann die Anordnung
# auf dem Bildschirm flexibel gesteuert werden. `Frames` ermöglichen die
# Organisation von Widgets in Zeilen, Spalten oder separaten Bereichen.

import tkinter as tk

root = tk.Tk()
root.title("Fortgeschrittene Layouts und Frames")

# Erstellen eines Frames
top_frame = tk.Frame(root, bg="lightblue", pady=10)
top_frame.pack(fill="x")

# Labels im Frame
label1 = tk.Label(top_frame, text="Label 1 im oberen Frame")
label1.pack(side="left", padx=5)

label2 = tk.Label(top_frame, text="Label 2 im oberen Frame")
label2.pack(side="left", padx=5)

root.mainloop()

# In diesem Beispiel wird `top_frame` als Container verwendet, in dem zwei Labels
# platziert sind. `fill="x"` sorgt dafür, dass der `Frame` die gesamte Breite des
# Fensters ausfüllt.




# ____________________________
#                            /
# Mehrere Frames verwenden  (
# ___________________________\

# Mit mehreren `Frames` kann die GUI in separate Abschnitte unterteilt werden,
# was die Verwaltung und Anpassung erleichtert.

root = tk.Tk()
root.title("Mehrere Frames Beispiel")

# Oberer Frame
top_frame = tk.Frame(root, bg="lightgreen", pady=10)
top_frame.pack(fill="x")

label1 = tk.Label(top_frame, text="Oberes Label 1")
label1.pack(side="left", padx=5)

label2 = tk.Label(top_frame, text="Oberes Label 2")
label2.pack(side="left", padx=5)

# Unterer Frame
bottom_frame = tk.Frame(root, bg="lightyellow", pady=10)
bottom_frame.pack(fill="x")

label3 = tk.Label(bottom_frame, text="Unteres Label")
label3.pack(pady=5)

root.mainloop()

# Hier wurden zwei Frames erstellt, `top_frame` und `bottom_frame`, die jeweils
# unterschiedliche Farben und Inhalte haben. Dadurch wird das Layout der GUI
# klar und strukturiert.




# ____________________________
#                            /
# Grid-Layout mit Frames    (
# ___________________________\

# Die `grid()`-Methode kann in Kombination mit `Frames` verwendet werden,
# um komplexe Layouts zu erstellen, die Widgets wie Tasten und Labels in
# einem Raster anordnen.

class GridApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Grid-Layout mit Frames")

        # Frame für das Grid erstellen
        grid_frame = tk.Frame(root)
        grid_frame.pack(pady=10)
        
        # Buttons im Grid anordnen
        for row in range(3):
            for col in range(3):
                button = tk.Button(grid_frame, text=f"Button {row},{col}", width=10, height=3)
                button.grid(row=row, column=col, padx=5, pady=5)

# Hauptprogramm starten
if __name__ == "__main__":
    root = tk.Tk()
    app = GridApp(root)
    root.mainloop()

# **Erläuterungen**:
# - `grid()` ermöglicht die Platzierung von Widgets in einem Rasterformat.
#
# - `grid_frame` fungiert als Container für die Buttons und wird zentral positioniert.
#




# ____________________________
#                            /
# Nützliche Layoutoptionen  (
# ___________________________\

# `tkinter` bietet mehrere Layoutoptionen zur Feinabstimmung von Widgets innerhalb
# von `Frames`:

# - padx/pady: Fügt Abstände in x- und y-Richtung hinzu.
#
# - fill="x"/fill="y": Erzwingt, dass ein Frame die gesamte Breite oder Höhe
#   des Fensters ausfüllt.
#
# - expand=True: Dehnt den Frame aus, um den gesamten verfügbaren Platz zu füllen.
#
# - sticky="nsew": Wird mit `grid()` verwendet, um Widgets an einer bestimmten
#   Position (Nord, Süd, Ost, West) auszurichten.

# Beispiel mit `padx`, `pady` und `expand`

root = tk.Tk()
root.title("Erweiterte Layoutoptionen")

frame = tk.Frame(root, bg="lightgray")
frame.pack(fill="both", expand=True, padx=10, pady=10)

label = tk.Label(frame, text="Label im erweiterten Frame", bg="white")
label.pack(fill="both", expand=True)

root.mainloop()

# Hier wird das `Frame`-Widget sowohl in der Breite als auch in der Höhe erweitert
# und das Label darin dehnt sich mit dem Frame aus.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - `Frames` helfen bei der Strukturierung komplexer GUIs und ermöglichen die
#   Gruppierung von Widgets.
#
# - Mit mehreren Frames kann die GUI in logisch getrennte Bereiche aufgeteilt werden.
#
# - Die `grid()`- und `pack()`-Methoden sowie Optionen wie `expand` und `fill`
#   erlauben flexible Layouts, die sich dynamisch an Fenstergrößen anpassen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine GUI-Anwendung mit zwei Frames: einem oberen Frame für eine
# Überschrift und einem unteren Frame mit zwei Buttons, die nebeneinander
# angezeigt werden.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle eine Taschenrechner-Oberfläche mit einem Frame für das Display
# und einem Frame für die Tasten. Verwende das `grid()`-Layout, um die Tasten
# in einem Raster anzuordnen.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine GUI mit einem zentralen Frame, der drei Labels in einer Spalte
# enthält. Der Frame sollte das gesamte Fenster ausfüllen und die Labels sollten
# mittig angeordnet sein.


# Füge hier deine Lösung ein.




#    (¯`·.¸¸.·´¯`·.¸¸.·´¯)
#    ( \                 / )
#   ( \ ) Du bist nun   ( / )
#  ( ) (      ein        ) ( )
#   ( / ) Rahmenprofi   ( \ )
#    ( /                 \ )
#     (_.·´¯`·.¸¸.·´¯`·.¸_)
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
# Erstelle eine GUI-Anwendung mit zwei Frames: einem oberen Frame für eine
# Überschrift und einem unteren Frame mit zwei Buttons, die nebeneinander
# angezeigt werden.

'''
import tkinter as tk

# Hauptfenster erstellen
root = tk.Tk()
root.title("Zweifach-Frame GUI")
root.geometry("300x200")

# Oberer Frame mit Überschrift
top_frame = tk.Frame(root)
top_frame.pack(pady=20)
label = tk.Label(top_frame, text="Willkommen zur Anwendung", font=("Arial", 16))
label.pack()

# Unterer Frame mit zwei Buttons nebeneinander
bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=20)

btn1 = tk.Button(bottom_frame, text="Button 1")
btn1.pack(side=tk.LEFT, padx=10)

btn2 = tk.Button(bottom_frame, text="Button 2")
btn2.pack(side=tk.LEFT, padx=10)

root.mainloop()
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle eine Taschenrechner-Oberfläche mit einem Frame für das Display
# und einem Frame für die Tasten. Verwende das `grid()`-Layout, um die Tasten
# in einem Raster anzuordnen.

'''
import tkinter as tk

# Hauptfenster erstellen
root = tk.Tk()
root.title("Taschenrechner")
root.geometry("300x400")

# Frame für das Display
display_frame = tk.Frame(root)
display_frame.pack(pady=10)
display = tk.Entry(display_frame, font=("Arial", 20), width=15, borderwidth=2)
display.pack()

# Frame für die Tasten
buttons_frame = tk.Frame(root)
buttons_frame.pack()

# Tastenbeschriftungen in einem Rasterlayout anordnen
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row, col = 0, 0
for button_text in buttons:
    button = tk.Button(buttons_frame, text=button_text, font=("Arial", 18), width=5, height=2)
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine GUI mit einem zentralen Frame, der drei Labels in einer Spalte
# enthält. Der Frame sollte das gesamte Fenster ausfüllen und die Labels sollten
# mittig angeordnet sein.

'''
import tkinter as tk

# Hauptfenster erstellen
root = tk.Tk()
root.title("Zentraler Frame")
root.geometry("300x200")

# Zentraler Frame erstellen und das Fenster füllen
central_frame = tk.Frame(root)
central_frame.pack(expand=True, fill=tk.BOTH)

# Labels erstellen und mittig anordnen
labels = ["Label 1", "Label 2", "Label 3"]
for label_text in labels:
    label = tk.Label(central_frame, text=label_text, font=("Arial", 14))
    label.pack(pady=10)

root.mainloop()
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

