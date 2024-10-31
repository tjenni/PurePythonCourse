#              ____________________________________
#       ______|                                    |_____
#       \     |    10.9 DATEN SPEICHERN UND LADEN  |    /
#        )    |____________________________________|   (
#       /________)                             (________\      30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Um Benutzerdaten wie Notizen, Einstellungen oder Ergebnisse zwischen Sitzungen
# zu speichern und wieder zu laden, kann eine GUI mit Python Dateien nutzen. In
# diesem Kapitel sehen wir, wie man Daten mit JSON-Dateien speichern und laden kann.


# ___________________________
#                           /
# Wichtige Module           (
# ___________________________\

# Für das Speichern und Laden von Daten nutzen wir das `json`-Modul und tkinter 
# Widgets für die Benutzeroberfläche. JSON ist ein gängiges Datenformat, das von 
# vielen Anwendungen verwendet wird und sich gut zum Speichern von Einstellungen 
# und Listen eignet.




# ____________________________
#                            /
# Daten speichern           (
# ___________________________\

# Im folgenden Beispiel erstellen wir eine GUI, in der Benutzer Notizen eingeben
# können. Die Notizen werden in einer JSON-Datei gespeichert, sobald der Benutzer
# auf „Speichern“ klickt.

import tkinter as tk
import json

class NotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notizen App")
        
        # Textfeld für Notizen
        self.text_area = tk.Text(root, width=40, height=10)
        self.text_area.pack(pady=10)
        
        # Buttons zum Speichern und Laden
        save_button = tk.Button(root, text="Speichern", command=self.save_notes)
        save_button.pack(pady=5)
        
        load_button = tk.Button(root, text="Laden", command=self.load_notes)
        load_button.pack(pady=5)
        
    def save_notes(self):
        notes = self.text_area.get("1.0", tk.END).strip()
        with open("notes.json", "w") as file:
            json.dump({"notes": notes}, file)
        print("Notizen gespeichert.")

    def load_notes(self):
        try:
            with open("notes.json", "r") as file:
                data = json.load(file)
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, data.get("notes", ""))
            print("Notizen geladen.")
        except FileNotFoundError:
            print("Keine gespeicherten Notizen gefunden.")

# Hauptprogramm starten
if __name__ == "__main__":
    root = tk.Tk()
    app = NotesApp(root)
    root.mainloop()

# Erläuterungen:
# - Die Methode `save_notes` speichert den Inhalt des Textfelds in einer JSON-Datei.
#
# - Die Methode `load_notes` lädt die gespeicherten Notizen und zeigt sie im Textfeld an.




# _____________________________
#                             /
# Daten aus Listen speichern (
# ____________________________\

# Für Anwendungen, die mehrere Daten speichern (wie eine Aufgabenliste), kann ein
# JSON-Array genutzt werden. Hier erstellen wir eine ToDo-Liste, die mehrere Aufgaben
# speichert und lädt.

import tkinter as tk
import json

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ToDo App")
        
        # Eingabefeld für neue Aufgaben
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)
        
        # Listbox zur Anzeige der Aufgaben
        self.listbox = tk.Listbox(root, width=40, height=10)
        self.listbox.pack(pady=10)
        
        # Buttons für die Aufgabenverwaltung
        add_button = tk.Button(root, text="Aufgabe hinzufügen", command=self.add_task)
        add_button.pack(pady=5)
        
        save_button = tk.Button(root, text="Speichern", command=self.save_tasks)
        save_button.pack(pady=5)
        
        load_button = tk.Button(root, text="Laden", command=self.load_tasks)
        load_button.pack(pady=5)
        
    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
    
    def save_tasks(self):
        tasks = self.listbox.get(0, tk.END)
        with open("tasks.json", "w") as file:
            json.dump({"tasks": list(tasks)}, file)
        print("Aufgaben gespeichert.")
    
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                data = json.load(file)
                self.listbox.delete(0, tk.END)
                for task in data.get("tasks", []):
                    self.listbox.insert(tk.END, task)
            print("Aufgaben geladen.")
        except FileNotFoundError:
            print("Keine gespeicherten Aufgaben gefunden.")

# Hauptprogramm starten
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

# Erläuterungen:
# - `save_tasks()` speichert die Aufgaben als JSON-Array.
#
# - `load_tasks()` liest die JSON-Datei und lädt die Aufgaben in die `Listbox`.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\
#
# - JSON-Dateien eignen sich hervorragend zum Speichern von einfachen Daten in
#   einer GUI, wie Notizen oder Aufgabenlisten.
#
# - Der JSON-Datenaustausch ist plattformunabhängig und leicht zu verarbeiten.
#
# - Verwende `json.dump()` zum Speichern und `json.load()` zum Laden von 
#   JSON-Dateien.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine GUI-Anwendung mit einem Text-Widget und zwei Buttons: `Speichern` 
# und `Laden`. Der Benutzer kann in das Text-Widget einen beliebigen Text eingeben. 
# Beim Klicken auf `Speichern` soll der Text in einer Datei namens `text_data.json` 
# gespeichert werden. Beim Klicken auf „Laden“ soll der Inhalt der Datei in das 
# Text-Widget geladen werden.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle eine GUI-Anwendung, die eine Liste von Namen speichert und lädt.
# Erstelle ein Entry-Widget für die Namenseingabe und eine Listbox, um die Namen anzuzeigen. 
# Mit einem Button `Hinzufügen` soll ein eingegebener Name zur Liste hinzugefügt und in der 
# Listbox angezeigt werden. Ein `Speichern`-Button speichert die Namen in einer Datei 
# `namelist.json`, und ein `Laden`-Button lädt die Namen und zeigt sie in der Listbox an.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine GUI für ein einfaches Notensystem.
# Die GUI sollte Entry-Widgets für den Namen des Schülers und seine Note enthalten. 
# Mit einem Button `Hinzufügen` soll das System den Schüler und seine Note in eine 
# Listbox hinzufügen. Ein `Speichern`-Button soll die Daten als JSON-Datei `noten.json`
# speichern, und ein `Laden`-Button soll die Noten aus der Datei laden und in der 
# Listbox anzeigen.


# Füge hier deine Lösung ein.




#         ____________
#        /\  ________ \
#       /  \ \______/\ \
#      / /\ \ \  / /\ \ \
#     / / /\ \ \/ / /\ \ \
#    / / /__\ \ \/_/__\_\ \__________
#   / /_/____\ \__________  ________ \
#   \ \ \____/ / ________/\ \______/\ \
#    \ \ \  / / /\ \  / /\ \ \  / /\ \ \
#     \ \ \/ / /\ \ \/ / /\ \ \/ / /\ \ \
#      \ \/ / /__\_\/ / /__\ \ \/_/__\_\ \        Super gemacht. Nun weisst du,
#       \  /_/______\/_/____\ \___________\       wie man in einer GUI-Anwendung
#       /  \ \______/\ \____/ / ________  /       Daten abspeichern und laden kann.
#      / /\ \ \  / /\ \ \  / / /\ \  / / /
#     / / /\ \ \/ / /\ \ \/ / /\ \ \/ / /
#    / / /__\ \ \/_/__\_\/ / /__\_\/ / /
#   / /_/____\ \_________\/ /______\/ /
#   \ \ \____/ / ________  __________/
#    \ \ \  / / /\ \  / / /
#     \ \ \/ / /\ \ \/ / /
#      \ \/ / /__\_\/ / /
#       \  / /______\/ /
#        \/___________/BvG
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
# Erstelle eine GUI-Anwendung mit einem Text-Widget und zwei Buttons: `Speichern` 
# und `Laden`. Der Benutzer kann in das Text-Widget einen beliebigen Text eingeben. 
# Beim Klicken auf `Speichern` soll der Text in einer Datei namens `text_data.json` 
# gespeichert werden. Beim Klicken auf „Laden“ soll der Inhalt der Datei in das 
# Text-Widget geladen werden.

'''
import tkinter as tk
from tkinter import messagebox
import json

def save_text():
    text_content = text_widget.get("1.0", tk.END).strip()
    with open("text_data.json", "w") as file:
        json.dump({"content": text_content}, file)
    messagebox.showinfo("Speichern", "Text wurde erfolgreich gespeichert.")

def load_text():
    try:
        with open("text_data.json", "r") as file:
            data = json.load(file)
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, data.get("content", ""))
            messagebox.showinfo("Laden", "Text wurde erfolgreich geladen.")
    except FileNotFoundError:
        messagebox.showerror("Fehler", "Datei 'text_data.json' nicht gefunden.")
    except json.JSONDecodeError:
        messagebox.showerror("Fehler", "Datei konnte nicht geladen werden.")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Text speichern und laden")

# Text-Widget
text_widget = tk.Text(root, width=40, height=10)
text_widget.pack(pady=10)

# Buttons
save_button = tk.Button(root, text="Speichern", command=save_text)
save_button.pack(side=tk.LEFT, padx=10, pady=10)

load_button = tk.Button(root, text="Laden", command=load_text)
load_button.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle eine GUI-Anwendung, die eine Liste von Namen speichert und lädt.
# Erstelle ein Entry-Widget für die Namenseingabe und eine Listbox, um die Namen anzuzeigen. 
# Mit einem Button `Hinzufügen` soll ein eingegebener Name zur Liste hinzugefügt und in der 
# Listbox angezeigt werden. Ein `Speichern`-Button speichert die Namen in einer Datei 
# `namelist.json`, und ein `Laden`-Button lädt die Namen und zeigt sie in der Listbox an.

'''
import tkinter as tk
from tkinter import messagebox
import json

def add_name():
    name = entry_name.get().strip()
    if name:
        listbox.insert(tk.END, name)
        entry_name.delete(0, tk.END)
    else:
        messagebox.showwarning("Eingabefehler", "Bitte einen Namen eingeben.")

def save_names():
    names = list(listbox.get(0, tk.END))
    with open("namelist.json", "w") as file:
        json.dump(names, file)
    messagebox.showinfo("Speichern", "Namen wurden erfolgreich gespeichert.")

def load_names():
    try:
        with open("namelist.json", "r") as file:
            names = json.load(file)
        listbox.delete(0, tk.END)
        for name in names:
            listbox.insert(tk.END, name)
        messagebox.showinfo("Laden", "Namen wurden erfolgreich geladen.")
    except FileNotFoundError:
        messagebox.showerror("Fehler", "Datei 'namelist.json' nicht gefunden.")
    except json.JSONDecodeError:
        messagebox.showerror("Fehler", "Datei konnte nicht geladen werden.")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Namensliste")

# Entry und Buttons
entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=10)

add_button = tk.Button(root, text="Hinzufügen", command=add_name)
add_button.pack(pady=5)

save_button = tk.Button(root, text="Speichern", command=save_names)
save_button.pack(pady=5)

load_button = tk.Button(root, text="Laden", command=load_names)
load_button.pack(pady=5)

# Listbox zur Anzeige der Namen
listbox = tk.Listbox(root, width=30)
listbox.pack(pady=10)

root.mainloop()
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine GUI für ein einfaches Notensystem.
# Die GUI sollte Entry-Widgets für den Namen des Schülers und seine Note enthalten. 
# Mit einem Button `Hinzufügen` soll das System den Schüler und seine Note in eine 
# Listbox hinzufügen. Ein `Speichern`-Button soll die Daten als JSON-Datei `noten.json`
# speichern, und ein `Laden`-Button soll die Noten aus der Datei laden und in der 
# Listbox anzeigen.

'''
import tkinter as tk
from tkinter import messagebox
import json

def add_grade():
    name = entry_name.get().strip()
    try:
        grade = int(entry_grade.get().strip())
        if not (1 <= grade <= 6):
            raise ValueError("Die Note muss zwischen 1 und 6 liegen.")
        listbox.insert(tk.END, f"{name}: {grade}")
        entry_name.delete(0, tk.END)
        entry_grade.delete(0, tk.END)
    except ValueError as e:
        messagebox.showerror("Ungültige Eingabe", str(e))

def save_grades():
    grades = []
    for i in range(listbox.size()):
        item = listbox.get(i)
        name, grade = item.split(": ")
        grades.append({"name": name, "grade": int(grade)})
    with open("noten.json", "w") as file:
        json.dump(grades, file)
    messagebox.showinfo("Speichern", "Noten wurden erfolgreich gespeichert.")

def load_grades():
    try:
        with open("noten.json", "r") as file:
            grades = json.load(file)
        listbox.delete(0, tk.END)
        for entry in grades:
            listbox.insert(tk.END, f"{entry['name']}: {entry['grade']}")
        messagebox.showinfo("Laden", "Noten wurden erfolgreich geladen.")
    except FileNotFoundError:
        messagebox.showerror("Fehler", "Datei 'noten.json' nicht gefunden.")
    except json.JSONDecodeError:
        messagebox.showerror("Fehler", "Datei konnte nicht geladen werden.")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Noten-Eingabesystem")

# Entry-Widgets und Labels für Namen und Note
label_name = tk.Label(root, text="Schülername:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_grade = tk.Label(root, text="Note:")
label_grade.pack()
entry_grade = tk.Entry(root)
entry_grade.pack()

# Buttons für Hinzufügen, Speichern und Laden
add_button = tk.Button(root, text="Hinzufügen", command=add_grade)
add_button.pack(pady=5)

save_button = tk.Button(root, text="Speichern", command=save_grades)
save_button.pack(pady=5)

load_button = tk.Button(root, text="Laden", command=load_grades)
load_button.pack(pady=5)

# Listbox zur Anzeige der Schülernamen und Noten
listbox = tk.Listbox(root, width=30)
listbox.pack(pady=10)

root.mainloop()
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

