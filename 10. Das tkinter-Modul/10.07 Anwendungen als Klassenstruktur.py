#              ____________________________________________
#       ______|                                            |_____
#       \     |    10.7 ANWENDUNGEN ALS KLASSENSTRUKTUR    |    /
#        )    |____________________________________________|   (
#       /________)                                     (________\      30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Das Erstellen von tkinter-Anwendungen mit einer Klassenstruktur ist eine
# effiziente Methode, um umfangreiche und gut strukturierte GUI-Anwendungen
# zu entwickeln. Klassen helfen dabei, den Code übersichtlich zu halten,
# indem sie alle GUI-Elemente und Methoden in einer zentralen Klasse bündeln.


# _________________________________
#                                 /
# Vorteile einer Klassenstruktur (
# ________________________________\

# Die Verwendung einer Klasse für tkinter-Anwendungen hat einige Vorteile:
# - Bessere Struktur: Der gesamte Code ist in einer einzigen Klasse, was die 
#   Verwaltung erleichtert.
#
# - Wiederverwendbarkeit: Methoden und GUI-Elemente können wiederverwendet und 
#   angepasst werden.
#
# - Einfachere Wartung: Die GUI kann in Methoden unterteilt werden, was das 
#   Lesen und Anpassen erleichtert.




# _____________________________
#                             /
# Einfache tkinter-Anwendung (
# ____________________________\

# Im folgenden Beispiel erstellen wir eine Anwendung in einer Klasse, die ein
# `Label`, ein `Entry` und einen `Button` enthält. Der `Button` wird verwendet,
# um den Text aus dem `Entry` anzuzeigen.

import tkinter as tk

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Einfache tkinter-Anwendung")
        
        # GUI-Elemente erstellen
        self.label = tk.Label(root, text="Gib deinen Namen ein:")
        self.label.pack(pady=5)
        
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        
        self.button = tk.Button(root, text="Anzeigen", command=self.display_name)
        self.button.pack(pady=5)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=5)
    
    # Methode für Button-Funktionalität
    def display_name(self):
        name = self.entry.get()
        self.result_label.config(text=f"Hallo, {name}!")

# Hauptprogramm starten
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()

# Erläuterungen:
# - Die Klasse `SimpleApp` enthält alle GUI-Elemente und eine Methode `display_name`, 
#   um den Button zu steuern.
#
# - `self.root`, `self.label`, `self.entry`, und `self.result_label` sind alle 
#   Attribute der Klasse und können in verschiedenen Methoden aufgerufen werden.




# _____________________________
#                             /
# Erstellen komplexerer GUIs (
# ____________________________\

# Für größere Anwendungen kann eine Klasse Methoden enthalten, die verschiedene
# GUI-Komponenten und Logik kapseln. Hier ein Beispiel für eine Taschenrechner-GUI.

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Einfacher Taschenrechner")
        
        # Eingabefeld für Berechnungen
        self.entry = tk.Entry(root, width=16, font=("Arial", 18), borderwidth=2, relief="solid")
        self.entry.grid(row=0, column=0, columnspan=4)
        
        # Tasten erstellen
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]
        
        # Schleife für Tastenplatzierung
        row_val = 1
        col_val = 0
        for button_text in buttons:
            button = tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 14),
                               command=lambda b=button_text: self.on_button_click(b))
            button.grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    # Methode zur Tastenbehandlung
    def on_button_click(self, char):
        if char == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Fehler")
        else:
            self.entry.insert(tk.END, char)

# Hauptprogramm starten
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

# Erläuterungen:
# - Die Klasse `CalculatorApp` definiert das Layout und die Funktionalität eines 
#   einfachen Taschenrechners.

# - Die Methode `on_button_click()` behandelt das Drücken der Tasten. Wenn „=“ 
#   gedrückt wird, wird der Ausdruck berechnet.


# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - `self` ermöglicht es uns, auf alle Methoden und Attribute innerhalb der 
#   Klasse zuzugreifen.
#
# - Durch die Verwendung von Klassen lassen sich tkinter-Anwendungen besser 
#   organisieren, skalieren und warten.
# 
# - Komplexere Anwendungen sollten in Methoden aufgeteilt werden, um die 
#   Logik für jede Funktionalität zu kapseln.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine GUI-Klassenstruktur für eine Anwendung, die eine Checkliste darstellt.
# Die Anwendung soll eine Liste von Aufgaben anzeigen, und der Benutzer kann jede
# Aufgabe durch Ankreuzen eines Checkbuttons als erledigt markieren.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe eine Klasse `ToDoApp`, die ein `Entry`-Feld und einen `Button` enthält,
# um neue Aufgaben hinzuzufügen. Die Aufgaben werden in einer `Listbox` angezeigt,
# und der Benutzer kann eine Aufgabe auswählen und sie durch einen weiteren Button
# entfernen.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Entwickle eine `CounterApp`-Klasse, die eine einfache Zählfunktion bereitstellt.
# Die GUI soll zwei Buttons „Hochzählen“ und „Runterzählen“ sowie ein Label zur
# Anzeige des aktuellen Zählers beinhalten. Die Anwendung soll den Zählerwert
# aktualisieren, wenn die Buttons gedrückt werden.


# Füge hier deine Lösung ein.



#      __         __
#     /.-'       `-.\               
#    //             \\               Dank der Klassenstruktur
#   /j_______________j\              sehen die Programme nun viel
#  /o.-==-. .-. .-==-.o\             schöner aus. :-)
#  ||      )) ((      ||
#   \\____//   \\____//   hjw
#    `-==-'     `-==-'
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
# Erstelle eine GUI-Klassenstruktur für eine Anwendung, die eine Checkliste darstellt.
# Die Anwendung soll eine Liste von Aufgaben anzeigen, und der Benutzer kann jede
# Aufgabe durch Ankreuzen eines Checkbuttons als erledigt markieren.

'''
import tkinter as tk

class ChecklistApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Checkliste")

        # Aufgabenliste
        self.tasks = ["Aufgabe 1", "Aufgabe 2", "Aufgabe 3"]
        self.check_vars = []

        # Erstelle Checkbuttons für jede Aufgabe
        for task in self.tasks:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(root, text=task, variable=var)
            chk.pack(anchor="w", padx=10, pady=5)
            self.check_vars.append(var)

# Hauptprogramm
root = tk.Tk()
app = ChecklistApp(root)
root.mainloop()
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe eine Klasse `ToDoApp`, die ein `Entry`-Feld und einen `Button` enthält,
# um neue Aufgaben hinzuzufügen. Die Aufgaben werden in einer `Listbox` angezeigt,
# und der Benutzer kann eine Aufgabe auswählen und sie durch einen weiteren Button
# entfernen.

'''
import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do Liste")

        # Eingabefeld und Hinzufügen-Button
        self.entry_task = tk.Entry(root, width=30)
        self.entry_task.pack(pady=5)
        
        self.button_add = tk.Button(root, text="Hinzufügen", command=self.add_task)
        self.button_add.pack(pady=5)

        # Listbox für Aufgabenanzeige
        self.listbox_tasks = tk.Listbox(root, width=40, height=10)
        self.listbox_tasks.pack(pady=5)

        # Entfernen-Button
        self.button_remove = tk.Button(root, text="Entfernen", command=self.remove_task)
        self.button_remove.pack(pady=5)

    def add_task(self):
        task = self.entry_task.get().strip()
        if task:
            self.listbox_tasks.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Eingabefehler", "Bitte eine Aufgabe eingeben.")

    def remove_task(self):
        try:
            selected_task = self.listbox_tasks.curselection()
            self.listbox_tasks.delete(selected_task)
        except:
            messagebox.showwarning("Fehler", "Bitte eine Aufgabe zum Entfernen auswählen.")

# Hauptprogramm
root = tk.Tk()
app = ToDoApp(root)
root.mainloop()
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Entwickle eine `CounterApp`-Klasse, die eine einfache Zählfunktion bereitstellt.
# Die GUI soll zwei Buttons „Hochzählen“ und „Runterzählen“ sowie ein Label zur
# Anzeige des aktuellen Zählers beinhalten. Die Anwendung soll den Zählerwert
# aktualisieren, wenn die Buttons gedrückt werden.

'''
import tkinter as tk

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zähler-Anwendung")
        
        # Initialer Zählerwert
        self.counter = 0

        # Label zur Anzeige des Zählers
        self.label_counter = tk.Label(root, text=f"Zähler: {self.counter}", font=("Helvetica", 16))
        self.label_counter.pack(pady=10)

        # Hochzählen- und Runterzählen-Buttons
        self.button_increment = tk.Button(root, text="Hochzählen", command=self.increment)
        self.button_increment.pack(pady=5)
        
        self.button_decrement = tk.Button(root, text="Runterzählen", command=self.decrement)
        self.button_decrement.pack(pady=5)

    def increment(self):
        self.counter += 1
        self.label_counter.config(text=f"Zähler: {self.counter}")

    def decrement(self):
        self.counter -= 1
        self.label_counter.config(text=f"Zähler: {self.counter}")

# Hauptprogramm
root = tk.Tk()
app = CounterApp(root)
root.mainloop()
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><



