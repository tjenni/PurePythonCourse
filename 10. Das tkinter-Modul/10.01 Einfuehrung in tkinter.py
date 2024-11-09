#              ______________________________
#       ______|                              |_____
#       \     |  10.1 EINFÜHRUNG IN TKINTER  |    /
#        )    |______________________________|   (
#       /________)                       (________\      30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# `tkinter` ist das Standardmodul in Python zur Erstellung grafischer Benutzer-
# oberflächen (GUIs). Es ermöglicht dir, interaktive Anwendungen mit Fenstern, 
# Schaltflächen, Texteingabefeldern und vielen weiteren Elementen zu erstellen.


# ____________________________
#                            /
# Ein einfaches Fenster     (
# ___________________________\

# Um `tkinter` zu verwenden, muss das Modul zuerst importiert werden. Das Hauptfenster
# ist die Grundlage jeder `tkinter`-Anwendung und wird mithilfe der `Tk()`-Klasse erstellt.

import tkinter as tk

# Ein Hauptfenster erstellen
root = tk.Tk()

# Eigenschaften des Fensters festlegen
root.title("Mein erstes tkinter Fenster")   # Titel des Fensters
root.geometry("400x300")                    # Grösse des Fensters: Breite x Höhe

# Das Fenster anzeigen
root.mainloop()

# In diesem Beispiel wird ein Fenster mit dem Titel „Mein erstes tkinter Fenster“ und einer
# Grösse von 400x300 Pixeln erstellt. Die Methode `mainloop()` startet die Hauptschleife,
# die das Fenster offen hält und auf Ereignisse reagiert.

# Hinweis: Ohne `mainloop()` würde das Fenster sofort geschlossen.




# ___________________________
#                           /
# Widgets in tkinter       (
# __________________________\

# `tkinter` bietet verschiedene Widgets, mit denen du interaktive Elemente in das
# Hauptfenster einfügen kannst. Die wichtigsten Widgets sind:

# - Label: Zeigt Text oder Bilder an.
#
# - Button: Führt eine Aktion aus, wenn darauf geklickt wird.
#
# - Entry: Ermöglicht die Eingabe von Text.
#
# - Text: Mehrzeiliges Texteingabefeld.
#
# - Checkbutton: Auswahlkästchen (Checkbox).
#
# - Radiobutton: Auswahltaste (Radiobutton) für mehrere Optionen.
#
# - Listbox: Liste von Elementen.
#
# - Canvas: Zeichenfläche für Grafiken und Formen.


# Beispiel: Hinzufügen einiger Widgets zum Fenster.
import tkinter as tk

root = tk.Tk()
root.title("tkinter Widgets")

# Einfache Widgets erstellen und zum Fenster hinzufügen
label = tk.Label(root, text="Hallo, tkinter!")  # Text-Label
label.pack()  # Mit .pack() im Fenster positionieren

button = tk.Button(root, text="Klick mich!")  # Button
button.pack()

entry = tk.Entry(root)  # Texteingabefeld
entry.pack()

# Hauptfenster anzeigen
root.mainloop()




# ___________________________
#                           /
# Wichtige Methoden        (
# __________________________\

# - title(): Legt den Titel des Fensters fest.
#
# - geometry(): Bestimmt die Grösse des Fensters im Format `"BreitexHöhe"`.
#
# - mainloop(): Startet die Hauptschleife und hält das Fenster offen.
#
# - pack(), grid(), place(): Methoden zur Positionierung von Widgets im Fenster
#   (hier gehen wir auf `pack()` ein, die anderen Methoden folgen im Layout-Kapitel).
#   `pack()` ist eine einfache Methode, um Widgets vertikal (standardmässig) anzuordnen,
#   während `grid()` und `place()` mehr Kontrolle über die Positionierung bieten.




# ____________________________
#                            /
# Beispiel: Einfache GUI    (
# ___________________________\

# Hier erstellen wir ein kleines Fenster mit einem Label und einem Button.
# Der Button gibt eine Nachricht auf der Konsole aus, wenn darauf geklickt wird.

import tkinter as tk

def on_button_click():
    print("Der Button wurde geklickt!")

root = tk.Tk()
root.title("Einfache GUI mit tkinter")
root.geometry("300x200")

label = tk.Label(root, text="Willkommen zur GUI!")
label.pack(pady=10)  # Platzierung mit Abstand von 10 Pixeln nach oben und unten

button = tk.Button(root, text="Klick mich", command=on_button_click)  # Button mit Aktion
button.pack(pady=10)

root.mainloop()

# In diesem Beispiel erstellt die Funktion `on_button_click()` die Aktion, die beim Klick auf den
# Button ausgeführt wird. Durch `command=on_button_click` wird die Funktion mit dem Button verknüpft.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - `tkinter`-Anwendungen starten immer mit dem Erstellen eines Hauptfensters `Tk()`.
#
# - Widgets wie `Label`, `Button` und `Entry` sind die Bausteine einer GUI.
#
# - Die Methode `mainloop()` ist entscheidend, um das Fenster aktiv zu halten.
#
# - Durch die Methode `command` lässt sich eine Funktion beim Klick auf einen Button ausführen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Fenster mit dem Titel „Meine erste GUI“. Füge ein `Label` hinzu,
# das „Hallo, Welt!“ anzeigt, und einen `Button`, der „Willkommen!“ auf der
# Konsole ausgibt, wenn er gedrückt wird.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine GUI-Anwendung mit einem `Entry`-Widget, in das der Benutzer
# seinen Namen eingeben kann, und einem `Button`, der „Hallo, [Name]!“ auf
# der Konsole ausgibt.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine GUI-Anwendung, die ein `Label` mit einem Text und einen `Button`
# enthält. Wenn der Button gedrückt wird, ändert sich der Text im `Label` zu „Willkommen!“.
#
# Hinweis: Um den Text von label zu ändern, schreibe `label.config(text="Willkommen!")`.


# Füge hier deine Lösung ein.




#            ___________
#           |.---------.|
#           ||         ||
#           ||         ||
#           ||         ||           Gratuliere zu deinem ersten 
#           |'---------'|           grafischen Benutzer-Interface.
#            `)__ ____('
#            [=== -- o ]--.
#          __'---------'__ \
#     jgs [::::::::::: :::] )
#          `""'"""""'""""`/T\
#                         \_/
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
# Erstelle ein Fenster mit dem Titel „Meine erste GUI“. Füge ein `Label` hinzu,
# das „Hallo, Welt!“ anzeigt, und einen `Button`, der „Willkommen!“ auf der
# Konsole ausgibt, wenn er gedrückt wird.

'''
import tkinter as tk

# Hauptfenster erstellen
window = tk.Tk()
window.title("Meine erste GUI")

# Label hinzufügen
label = tk.Label(window, text="Hallo, Welt!")
label.pack()

# Funktion für den Button
def button_click():
    print("Willkommen!")

# Button hinzufügen
button = tk.Button(window, text="Klick mich!", command=button_click)
button.pack()

# GUI starten
window.mainloop()
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine GUI-Anwendung mit einem `Entry`-Widget, in das der Benutzer
# seinen Namen eingeben kann, und einem `Button`, der „Hallo, [Name]!“ auf
# der Konsole ausgibt.

'''
import tkinter as tk

# Hauptfenster erstellen
window = tk.Tk()
window.title("Namens-Eingabe")

# Eingabefeld (Entry) hinzufügen
entry = tk.Entry(window)
entry.pack()

# Funktion für den Button
def greet_user():
    name = entry.get()
    print(f"Hallo, {name}!")

# Button hinzufügen
button = tk.Button(window, text="Begrüßen", command=greet_user)
button.pack()

# GUI starten
window.mainloop()
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine GUI-Anwendung, die ein `Label` mit einem Text und einen `Button`
# enthält. Wenn der Button gedrückt wird, ändert sich der Text im `Label` zu „Willkommen!“.
#
# Hinweis: Um den Text von label zu ändern, schreibe `label.config(text="Willkommen!")`.

'''
import tkinter as tk

# Hauptfenster erstellen
window = tk.Tk()
window.title("Willkommens-Nachricht")

# Label hinzufügen
label = tk.Label(window, text="Hallo!")
label.pack()

# Funktion für den Button
def update_label():
    label.config(text="Willkommen!")

# Button hinzufügen
button = tk.Button(window, text="Ändere den Text", command=update_label)
button.pack()

# GUI starten
window.mainloop()
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><



