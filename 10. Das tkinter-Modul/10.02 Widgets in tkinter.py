#              ______________________________
#       ______|                              |_____
#       \     |   10.2 WIDGETS IN TKINTER    |    /
#        )    |______________________________|   (
#       /________)                       (________\      30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# In `tkinter` sind Widgets die Bausteine einer GUI-Anwendung. Mit ihnen kann der 
# Benutzer interagieren und Eingaben tätigen. In diesem Kapitel werden einige der 
# wichtigsten Widgets in `tkinter` vorgestellt.


# ___________________________
#                           /
# 1. Label-Widget          (
# __________________________\

# Das `Label`-Widget zeigt einfachen Text oder Bilder an.

import tkinter as tk

root = tk.Tk()
root.title("Label Widget")

label = tk.Label(root, text="Hallo, tkinter!", font=("Arial", 16))
label.pack(pady=10)  # Abstand oben und unten

root.mainloop()

# In diesem Beispiel wird ein `Label` mit der Aufschrift "Hallo, tkinter!" und einer
# Schriftgröße von 16 angezeigt.




# ___________________________
#                           /
# 2. Button-Widget         (
# __________________________\

# Das `Button`-Widget führt eine Aktion aus, wenn darauf geklickt wird.

import tkinter as tk

def on_click():
    print("Button wurde geklickt!")

root = tk.Tk()
root.title("Button Widget")

button = tk.Button(root, text="Klick mich!", command=on_click)
button.pack(pady=10)

root.mainloop()

# Das `command`-Attribut verknüpft eine Funktion mit dem Button. Wenn der Button
# gedrückt wird, wird die Funktion `on_click()` ausgeführt.




# ___________________________
#                           /
# 3. Entry-Widget          (
# __________________________\

# Das `Entry`-Widget erlaubt dem Benutzer die Eingabe von Text (z. B. Name, Passwort).

import tkinter as tk

root = tk.Tk()
root.title("Entry Widget")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

button = tk.Button(root, text="Eingabe anzeigen", command=lambda: print("Eingegeben:", entry.get()))
button.pack(pady=10)

root.mainloop()

# Mit `entry.get()` wird der im `Entry`-Feld eingegebene Text abgerufen und in der
# Konsole ausgegeben.




# ___________________________
#                           /
# 4. Text-Widget           (
# __________________________\

# Das `Text`-Widget ermöglicht die Eingabe mehrzeiliger Texte.

import tkinter as tk

root = tk.Tk()
root.title("Text Widget")

text = tk.Text(root, height=5, width=40, font=("Arial", 12))
text.pack(pady=10)

button = tk.Button(root, text="Text anzeigen", command=lambda: print("Eingegebener Text:\n", text.get("1.0", tk.END)))
button.pack(pady=10)

root.mainloop()

# `text.get("1.0", tk.END)` gibt den gesamten Text im `Text`-Widget zurück. Die
# Angabe `"1.0"` gibt die Position der ersten Zeile, erstes Zeichen an.




# ___________________________
#                           /
# 5. Checkbutton-Widget    (
# __________________________\

# Das `Checkbutton`-Widget stellt eine Checkbox zur Verfügung, mit der der Benutzer
# eine Option aktivieren oder deaktivieren kann.

import tkinter as tk

root = tk.Tk()
root.title("Checkbutton Widget")

checked = tk.BooleanVar()

checkbutton = tk.Checkbutton(root, text="Option auswählen", variable=checked)
checkbutton.pack(pady=10)

button = tk.Button(root, text="Status anzeigen", command=lambda: print("Ausgewählt:", checked.get()))
button.pack(pady=10)

root.mainloop()

# `BooleanVar()` wird verwendet, um den Status (True oder False) des `Checkbutton` zu speichern.




# ___________________________
#                           /
# 6. Radiobutton-Widget    (
# __________________________\

# Das `Radiobutton`-Widget ermöglicht die Auswahl einer Option aus mehreren Möglichkeiten.

import tkinter as tk

root = tk.Tk()
root.title("Radiobutton Widget")

option = tk.StringVar(value="Option 1")

radio1 = tk.Radiobutton(root, text="Option 1", variable=option, value="Option 1")
radio2 = tk.Radiobutton(root, text="Option 2", variable=option, value="Option 2")
radio3 = tk.Radiobutton(root, text="Option 3", variable=option, value="Option 3")

radio1.pack()
radio2.pack()
radio3.pack()

button = tk.Button(root, text="Auswahl anzeigen", command=lambda: print("Ausgewählt:", option.get()))
button.pack(pady=10)

root.mainloop()

# `StringVar` speichert den Wert des ausgewählten Radiobuttons, der mit `get()` abgerufen wird.




# ___________________________
#                           /
# 7. Listbox-Widget        (
# __________________________\

# Das `Listbox`-Widget zeigt eine Liste von Elementen an, von denen der Benutzer
# eines oder mehrere auswählen kann.

import tkinter as tk

root = tk.Tk()
root.title("Listbox Widget")

listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.insert(4, "JavaScript")

listbox.pack(pady=10)

button = tk.Button(root, text="Auswahl anzeigen", command=lambda: print("Ausgewählt:", listbox.get(listbox.curselection())))
button.pack(pady=10)

root.mainloop()

# Mit `listbox.curselection()` wird der Index des ausgewählten Elements abgerufen und
# das Element mit `listbox.get()` angezeigt.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Widgets wie `Label`, `Button`, `Entry` und `Text` sind grundlegende 
#   GUI-Elemente in `tkinter`.
#
# - Viele Widgets verwenden `pack()`, `grid()` oder `place()`, um die Position 
#   im Fenster festzulegen.
#
# - Widgets wie `Checkbutton` und `Radiobutton` verwenden `BooleanVar` oder 
#   `StringVar`, um ihren Zustand zu speichern.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine GUI-Anwendung mit einem Entry-Widget und zwei Buttons: „Speichern“ 
# und „Löschen“. Der „Speichern“-Button soll den Inhalt des Entry-Widgets in der 
# Konsole ausgeben, und der „Löschen“-Button soll das Entry-Feld leeren.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Fenster mit einem `Listbox`-Widget, das fünf verschiedene Farben
# enthält. Wenn der Benutzer eine Farbe auswählt und auf einen Button klickt, soll
# die ausgewählte Farbe auf der Konsole angezeigt werden.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein GUI-Fenster mit einem `Checkbutton` und einem `Label`. Wenn der
# `Checkbutton` aktiviert ist, soll der Text im `Label` auf „Option ausgewählt!“
# geändert werden. Wenn der `Checkbutton` deaktiviert ist, soll der Text auf
# „Option nicht ausgewählt.“ stehen.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 4  /
# __________/
#
# Erstelle eine einfache Taschenrechner-GUI mit zwei Entry-Widgets für Zahlen und 
# vier Buttons für die Grundrechenarten (Addieren, Subtrahieren, Multiplizieren, 
# Dividieren). Gib das Ergebnis in einem Label aus, wenn eine der Rechenoperationen 
# ausgewählt wird.


# Füge hier deine Lösung ein.




#
#   |========== Adresse ==========X| 
#   |                              |
#   |  Anrede  X Herr   O Frau     |
#   |          _________________   |
#   |  Name   [ Hans            ]  |    Nun kannst du eigene Dialog-
#   |                              |    Boxen erstellen. 
#   |          _________________   |
#   |  E-Mail [ hans@python.com ]  |
#   |                              |
#   |         [Abbrechen] [Senden] |
#   |______________________________|
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
# Erstelle eine GUI-Anwendung mit einem Entry-Widget und zwei Buttons: „Speichern“ 
# und „Löschen“. Der „Speichern“-Button soll den Inhalt des Entry-Widgets in der 
# Konsole ausgeben, und der „Löschen“-Button soll das Entry-Feld leeren.


'''
import tkinter as tk

def speichern():
    eingabe = entry.get()
    print("Eingabe gespeichert:", eingabe)

def loeschen():
    entry.delete(0, tk.END)

# Hauptfenster erstellen
window = tk.Tk()
window.title("Eingabe speichern und löschen")

# Entry-Widget
entry = tk.Entry(window)
entry.pack()

# Speichern-Button
button_speichern = tk.Button(window, text="Speichern", command=speichern)
button_speichern.pack()

# Löschen-Button
button_loeschen = tk.Button(window, text="Löschen", command=loeschen)
button_loeschen.pack()

# GUI starten
window.mainloop()
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Fenster mit einem `Listbox`-Widget, das fünf verschiedene Farben
# enthält. Wenn der Benutzer eine Farbe auswählt und auf einen Button klickt, soll
# die ausgewählte Farbe auf der Konsole angezeigt werden.

'''
import tkinter as tk

def farbe_ausgeben():
    farbe = listbox.get(listbox.curselection())
    print("Ausgewählte Farbe:", farbe)

# Hauptfenster erstellen
window = tk.Tk()
window.title("Farbauswahl")

# Listbox erstellen und Farben hinzufügen
listbox = tk.Listbox(window)
farben = ["Rot", "Blau", "Grün", "Gelb", "Lila"]
for farbe in farben:
    listbox.insert(tk.END, farbe)
listbox.pack()

# Button zum Ausgeben der ausgewählten Farbe
button = tk.Button(window, text="Farbe anzeigen", command=farbe_ausgeben)
button.pack()

# GUI starten
window.mainloop()
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein GUI-Fenster mit einem `Checkbutton` und einem `Label`. Wenn der
# `Checkbutton` aktiviert ist, soll der Text im `Label` auf „Option ausgewählt!“
# geändert werden. Wenn der `Checkbutton` deaktiviert ist, soll der Text auf
# „Option nicht ausgewählt.“ stehen.


'''
import tkinter as tk

def checkbutton_geaendert():
    if var.get():
        label.config(text="Option ausgewählt!")
    else:
        label.config(text="Option nicht ausgewählt.")

# Hauptfenster erstellen
window = tk.Tk()
window.title("Checkbutton-Option")

# Checkbutton mit Variable
var = tk.BooleanVar()
checkbutton = tk.Checkbutton(window, text="Option auswählen", variable=var, command=checkbutton_geaendert)
checkbutton.pack()

# Label
label = tk.Label(window, text="Option nicht ausgewählt.")
label.pack()

# GUI starten
window.mainloop()
'''




# ___________
#            \
# Aufgabe 4  /
# __________/
#
# Erstelle eine einfache Taschenrechner-GUI mit zwei Entry-Widgets für Zahlen und 
# vier Buttons für die Grundrechenarten (Addieren, Subtrahieren, Multiplizieren, 
# Dividieren). Gib das Ergebnis in einem Label aus, wenn eine der Rechenoperationen 
# ausgewählt wird.


'''
import tkinter as tk

def berechne(operation):
    try:
        zahl1 = float(entry1.get())
        zahl2 = float(entry2.get())
        
        if operation == "add":
            result = zahl1 + zahl2
        elif operation == "subtract":
            result = zahl1 - zahl2
        elif operation == "multiply":
            result = zahl1 * zahl2
        elif operation == "divide":
            if zahl2 == 0:
                result_label.config(text="Division durch Null!")
                return
            result = zahl1 / zahl2
        
        result_label.config(text=f"Ergebnis: {result}")
    except ValueError:
        result_label.config(text="Bitte gültige Zahlen eingeben.")

# Hauptfenster erstellen
window = tk.Tk()
window.title("Taschenrechner")

# Eingabefelder für Zahlen
entry1 = tk.Entry(window)
entry2 = tk.Entry(window)
entry1.pack()
entry2.pack()

# Buttons für die Grundrechenarten
button_add = tk.Button(window, text="Addieren", command=lambda: berechne("add"))
button_subtract = tk.Button(window, text="Subtrahieren", command=lambda: berechne("subtract"))
button_multiply = tk.Button(window, text="Multiplizieren", command=lambda: berechne("multiply"))
button_divide = tk.Button(window, text="Dividieren", command=lambda: berechne("divide"))

button_add.pack()
button_subtract.pack()
button_multiply.pack()
button_divide.pack()

# Label für das Ergebnis
result_label = tk.Label(window, text="Ergebnis:")
result_label.pack()

# GUI starten
window.mainloop()
'''





# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><



