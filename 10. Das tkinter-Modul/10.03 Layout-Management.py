#              ________________________________
#       ______|                                |_____
#       \     |      10.3 LAYOUT-MANAGEMENT     |    /
#        )    |________________________________|   (
#       /________)                         (________\

# In `tkinter` gibt es drei Layout-Manager, um Widgets innerhalb des Fensters
# anzuordnen: `pack`, `grid` und `place`. Diese Manager legen fest, wie und
# wo Widgets im Fenster erscheinen.

# ___________________________
#                           /
# Der `pack()` Layout-Manager (
# ___________________________\

# Der `pack()`-Manager ordnet Widgets in vertikaler oder horizontaler Richtung an.
# Die Widgets werden automatisch oben oder linksbündig hinzugefügt.

import tkinter as tk

root = tk.Tk()
root.title("Layout mit pack()")

label1 = tk.Label(root, text="Label 1", bg="red")
label2 = tk.Label(root, text="Label 2", bg="blue")
label3 = tk.Label(root, text="Label 3", bg="green")

# Labels mit unterschiedlichen Ausrichtungen packen
label1.pack(side="top", fill="x")       # Oben ausrichten, horizontal strecken
label2.pack(side="left", fill="y")      # Links ausrichten, vertikal strecken
label3.pack(side="right", fill="both")  # Rechts ausrichten, beide Richtungen strecken

root.mainloop()

# Hier wird `side` verwendet, um die Ausrichtung der Widgets festzulegen:
# - `top` für oben
# - `left` für links
# - `right` für rechts
# - `bottom` für unten
# Die Option `fill` bestimmt, ob das Widget den verbleibenden Raum ausfüllt.


# ___________________________
#                           /
# Der `grid()` Layout-Manager (
# ___________________________\

# Der `grid()`-Manager ermöglicht die Anordnung von Widgets in einem Gitter aus Zeilen
# und Spalten. Dies ist nützlich für komplexere Layouts.

root = tk.Tk()
root.title("Layout mit grid()")

# Widgets erstellen und im Gitter anordnen
label1 = tk.Label(root, text="Label 1", bg="yellow")
label2 = tk.Label(root, text="Label 2", bg="orange")
label3 = tk.Label(root, text="Label 3", bg="lightblue")

label1.grid(row=0, column=0)          # Erste Zeile, erste Spalte
label2.grid(row=0, column=1)          # Erste Zeile, zweite Spalte
label3.grid(row=1, column=0, columnspan=2, sticky="we")  # Zweite Zeile, beide Spalten

root.mainloop()

# Im `grid()`-Manager wird die Position durch `row` und `column` festgelegt:
# - `row` ist die Zeile, in der das Widget erscheint.
# - `column` ist die Spalte.
# - `columnspan` ermöglicht, dass das Widget mehrere Spalten einnimmt.
# - `sticky` legt die Ausrichtung innerhalb der Zelle fest: `n`, `s`, `e`, `w`.


# ___________________________
#                           /
# Der `place()` Layout-Manager (
# ___________________________\

# Der `place()`-Manager platziert Widgets an einer exakten Position durch die
# Angabe von `x`- und `y`-Koordinaten. Dieser Manager bietet präzise Kontrolle,
# ist aber eher für kleine Layouts geeignet.

root = tk.Tk()
root.title("Layout mit place()")

label1 = tk.Label(root, text="Label 1", bg="pink")
label2 = tk.Label(root, text="Label 2", bg="lightgreen")

label1.place(x=50, y=50)   # Platziere das erste Label bei (50, 50)
label2.place(x=150, y=100) # Platziere das zweite Label bei (150, 100)

root.mainloop()

# Bei `place()` wird die exakte Position durch die Argumente `x` und `y` festgelegt.
# Dies ist praktisch für gezielte Platzierungen, jedoch nicht flexibel bei der
# Anpassung der Fenstergröße.


# ___________________________
#                           /
# Wann welchen Layout-Manager verwenden? (
# ___________________________\

# Jeder Layout-Manager hat seine Stärken:
# - `pack()`: Einfach zu verwenden für lineare Anordnungen und grundlegende Layouts.
# - `grid()`: Ideal für Formulare und Tabellenlayouts, bei denen Zeilen und Spalten erforderlich sind.
# - `place()`: Geeignet für exakte, pixelgenaue Positionierung, aber weniger flexibel.

# **Hinweis**: Es ist besser, in einem Container (wie `Frame`) immer nur einen Layout-Manager zu verwenden,
# um die Verwaltung des Layouts zu vereinfachen.


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine GUI mit drei Labels, die vertikal von oben nach unten angeordnet sind.
# Nutze den `pack()`-Manager und sorge dafür, dass die Labels die volle Breite des
# Fensters ausfüllen.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine GUI mit zwei Zeilen und zwei Spalten. Platziere ein Label in jeder Zelle
# des Gitters und nutze den `grid()`-Manager, um das Layout zu organisieren.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine GUI mit drei Labels an genau festgelegten Positionen im Fenster. Nutze
# den `place()`-Manager, um die Position jedes Labels festzulegen.


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



# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

