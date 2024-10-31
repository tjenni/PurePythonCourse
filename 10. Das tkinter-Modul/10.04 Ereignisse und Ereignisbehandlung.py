#              __________________________________________
#       ______|                                          |_____
#       \     |  10.4 EREIGNISSE UND EREIGNISBEHANDLUNG  |    /
#        )    |__________________________________________|   (
#       /________)                                   (________\      30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# In `tkinter` kann eine Anwendung auf Benutzerinteraktionen wie Mausklicks,
# Tastatureingaben und andere Ereignisse reagieren. Mit **Ereignisbehandlung**
# (Event Handling) können wir festlegen, was geschehen soll, wenn ein Benutzer
# mit der GUI interagiert.


# ____________________________
#                            /
# Ereignisse und `bind()`   (
# ___________________________\

# Die `bind()`-Methode ermöglicht es, Ereignisse mit bestimmten Widgets zu
# verknüpfen. So lässt sich etwa festlegen, was beim Klicken auf einen Button
# oder beim Drücken einer Taste geschieht.

import tkinter as tk

root = tk.Tk()
root.title("Ereignisbehandlung mit bind()")

# Ereignisbehandlungsfunktion
def on_click(event):
    print("Label wurde geklickt!")

# Label erstellen und Ereignis "Linksklick" binden
label = tk.Label(root, text="Klicke mich!")
label.bind("<Button-1>", on_click)  # <Button-1> steht für den linken Mausklick
label.pack(pady=10)

root.mainloop()

# `bind("<Button-1>", on_click)` bindet das Ereignis "linker Mausklick" an die
# Funktion `on_click()`, sodass diese Funktion ausgeführt wird, wenn auf das
# Label geklickt wird.




# _____________________________
#                             /
# Tastatureingaben behandeln (
# ____________________________\

# Um auf Tastatureingaben zu reagieren, kann ein `bind()` für bestimmte Tasten
# gesetzt werden. Hier ein Beispiel, bei dem der Benutzer eine Eingabe per
# Enter-Taste absendet.

def on_enter(event):
    print("Eingabe abgeschickt!")

root = tk.Tk()
root.title("Ereignisbehandlung für Tastatureingaben")

entry = tk.Entry(root)
entry.bind("<Return>", on_enter)  # <Return> steht für die Enter-Taste
entry.pack(pady=10)

root.mainloop()

# Sobald der Benutzer die Enter-Taste drückt, wird die Funktion `on_enter()` aufgerufen.




# ______________________________
#                              /
# Weitere wichtige Ereignisse (
# _____________________________\

# `tkinter` bietet eine Vielzahl von Ereignissen, die auf bestimmte Aktionen reagieren:
# - `<Button-1>`: Linker Mausklick
#
# - `<Button-3>`: Rechter Mausklick
#
# - `<Double-Button-1>`: Doppelklick mit der linken Maustaste
#
# - `<Return>`: Drücken der Enter-Taste
#
# - `<KeyPress>`: Beliebige Taste drücken
#
# - `<Motion>`: Mausbewegung über ein Widget


# Beispiel: Behandeln von Doppelklicks und Mausbewegungen

def on_double_click(event):
    print("Doppelklick erkannt!")

def on_motion(event):
    print(f"Maus bewegt: X={event.x}, Y={event.y}")

root = tk.Tk()
root.title("Weitere Ereignisse")

label = tk.Label(root, text="Doppelklicke oder bewege die Maus über mich")
label.bind("<Double-Button-1>", on_double_click)
label.bind("<Motion>", on_motion)
label.pack(pady=10)

root.mainloop()

# Bei einem Doppelklick auf das Label wird `on_double_click()` aufgerufen, und bei
# einer Mausbewegung wird die aktuelle Position angezeigt.




# ________________________________
#                                /
# Ereignisse für Button-Widgets (
# _______________________________\

# `Button`-Widgets haben auch das `command`-Attribut, um Funktionen direkt zu
# verknüpfen, ohne `bind()` zu verwenden.

def on_button_click():
    print("Button wurde geklickt!")

root = tk.Tk()
root.title("Button Ereignis")

button = tk.Button(root, text="Drücke mich", command=on_button_click)
button.pack(pady=10)

root.mainloop()

# Die Funktion `on_button_click()` wird ausgeführt, wenn der Button gedrückt wird.
# Dies ist eine einfache Möglichkeit, Ereignisse bei Buttons zu behandeln.




# ____________________________
#                            /
# Mehrere Ereignisse binden (
# ___________________________\

# Es ist auch möglich, mehrere Ereignisse mit verschiedenen Aktionen an ein
# Widget zu binden. Hier ein Beispiel, bei dem sowohl linker Mausklick als auch
# rechter Mausklick unterschiedliche Aktionen ausführen.

def on_left_click(event):
    print("Linksklick auf das Label")

def on_right_click(event):
    print("Rechtsklick auf das Label")

root = tk.Tk()
root.title("Mehrere Ereignisse")

label = tk.Label(root, text="Klicke mit linker oder rechter Maustaste")
label.bind("<Button-1>", on_left_click)   # Linksklick
label.bind("<Button-3>", on_right_click)  # Rechtsklick
label.pack(pady=10)

root.mainloop()

# Hier werden verschiedene Funktionen für linke und rechte Mausklicks gebunden.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\


# - Mit `bind()` können Widgets auf spezifische Ereignisse reagieren, z. B. Maus- oder
#   Tastatureingaben.
#
# - Jedes Ereignis wird mit einer bestimmten Zeichenkette in `bind()` angegeben
#   (z. B. `<Button-1>` für den linken Mausklick).
#
# - Widgets wie `Button` können das `command`-Attribut nutzen, um Funktionen
#   zu verknüpfen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine GUI mit einem `Label`, das den Text „Klicke mich!“ enthält.
# Wenn das Label mit der linken Maustaste geklickt wird, soll „Linksklick erkannt!“
# auf der Konsole erscheinen.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Fenster mit einem `Entry`-Widget, das auf Eingaben mit der
# Enter-Taste reagiert. Wenn der Benutzer Enter drückt, soll die eingegebene
# Nachricht auf der Konsole angezeigt werden.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine GUI mit einem `Label`, das bei einer Mausbewegung die aktuellen
# `x`- und `y`-Koordinaten der Maus auf der Konsole anzeigt.


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
# Erstelle eine GUI mit einem `Label`, das den Text „Klicke mich!“ enthält.
# Wenn das Label mit der linken Maustaste geklickt wird, soll „Linksklick erkannt!“
# auf der Konsole erscheinen.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Fenster mit einem `Entry`-Widget, das auf Eingaben mit der
# Enter-Taste reagiert. Wenn der Benutzer Enter drückt, soll die eingegebene
# Nachricht auf der Konsole angezeigt werden.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine GUI mit einem `Label`, das bei einer Mausbewegung die aktuellen
# `x`- und `y`-Koordinaten der Maus auf der Konsole anzeigt.


# Füge hier deine Lösung ein.






# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


