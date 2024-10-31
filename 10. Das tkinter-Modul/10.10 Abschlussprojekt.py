#              ________________________________
#       ______|                                |_____
#       \     |     10.10 ABSCHLUSSPROJEKT     |    /
#        )    |________________________________|   (
#       /________)                         (________\      30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Dieses Abschlussprojekt vereint alle grundlegenden Konzepte von tkinter.
# Es stellt eine vollständige GUI-Anwendung dar, die Benutzeroberflächen,
# Ereignisbehandlung, Layouts, Frames und Speichermöglichkeiten beinhaltet.
# Das Ziel ist es, eine einfache Notizbuchanwendung zu erstellen, in der Benutzer
# Notizen hinzufügen, bearbeiten und speichern können.


# ____________________________
#                            /
# Projektbeschreibung       (
# ___________________________\

# Ziel: Erstelle eine Notizbuch-Anwendung, die es dem Benutzer ermöglicht:
# - Notizen zu erstellen, zu speichern und zu laden.
# - Notizen zu löschen oder zu bearbeiten.
# - Die Daten dauerhaft zu speichern (z.B. in einer JSON-Datei).

# GUI-Elemente:
# - Eingabefelder und Textbereich für Notizen.
# - Listbox zur Anzeige aller Notizen.
# - Buttons zum Hinzufügen, Speichern, Laden und Löschen von Notizen.




# ____________________________
#                            /
# Implementierung           (
# ___________________________\

import tkinter as tk
import json
from tkinter import messagebox, filedialog

class NotizbuchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notizbuch")
        
        # Hauptframe für Layout
        main_frame = tk.Frame(root)
        main_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Listbox und Scrollbar für Notizen
        self.notes_listbox = tk.Listbox(main_frame, width=40, height=10)
        self.notes_listbox.pack(side="left", padx=(0, 10))
        
        scrollbar = tk.Scrollbar(main_frame)
        scrollbar.pack(side="left", fill="y")
        self.notes_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.notes_listbox.yview)
        
        # Textfeld für Notizen-Inhalt
        self.note_text = tk.Text(main_frame, width=50, height=10)
        self.note_text.pack(pady=5, padx=5, fill="both", expand=True)
        
        # Button-Frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        
        # Buttons erstellen
        add_button = tk.Button(button_frame, text="Notiz hinzufügen", command=self.add_note)
        add_button.grid(row=0, column=0, padx=5)
        
        save_button = tk.Button(button_frame, text="Speichern", command=self.save_notes)
        save_button.grid(row=0, column=1, padx=5)
        
        load_button = tk.Button(button_frame, text="Laden", command=self.load_notes)
        load_button.grid(row=0, column=2, padx=5)
        
        delete_button = tk.Button(button_frame, text="Löschen", command=self.delete_note)
        delete_button.grid(row=0, column=3, padx=5)
        
        # Events für die Auswahl in der Listbox
        self.notes_listbox.bind("<<ListboxSelect>>", self.display_note)

    # Funktion zum Hinzufügen einer neuen Notiz
    def add_note(self):
        note_title = self.note_text.get("1.0", tk.END).strip().splitlines()[0]
        if note_title:
            self.notes_listbox.insert(tk.END, note_title)
            self.note_text.delete("1.0", tk.END)
        else:
            messagebox.showerror("Fehler", "Notiz darf nicht leer sein.")

    # Funktion zum Speichern der Notizen in einer JSON-Datei
    def save_notes(self):
        notes = {}
        for i in range(self.notes_listbox.size()):
            title = self.notes_listbox.get(i)
            content = self.note_text.get("1.0", tk.END).strip()
            notes[title] = content
        with open("notizbuch.json", "w") as file:
            json.dump(notes, file)
        messagebox.showinfo("Gespeichert", "Notizen wurden gespeichert.")

    # Funktion zum Laden von Notizen aus einer JSON-Datei
    def load_notes(self):
        try:
            with open("notizbuch.json", "r") as file:
                notes = json.load(file)
            self.notes_listbox.delete(0, tk.END)
            for title in notes:
                self.notes_listbox.insert(tk.END, title)
            messagebox.showinfo("Geladen", "Notizen wurden geladen.")
        except FileNotFoundError:
            messagebox.showerror("Fehler", "Keine gespeicherte Notiz gefunden.")

    # Funktion zum Anzeigen einer Notiz
    def display_note(self, event):
        try:
            selected_note = self.notes_listbox.get(self.notes_listbox.curselection())
            with open("notizbuch.json", "r") as file:
                notes = json.load(file)
            self.note_text.delete("1.0", tk.END)
            self.note_text.insert(tk.END, notes[selected_note])
        except IndexError:
            pass

    # Funktion zum Löschen einer Notiz
    def delete_note(self):
        try:
            selected_index = self.notes_listbox.curselection()[0]
            self.notes_listbox.delete(selected_index)
            self.note_text.delete("1.0", tk.END)
            messagebox.showinfo("Gelöscht", "Notiz wurde gelöscht.")
        except IndexError:
            messagebox.showerror("Fehler", "Keine Notiz ausgewählt.")

# Hauptprogramm starten
if __name__ == "__main__":
    root = tk.Tk()
    app = NotizbuchApp(root)
    root.mainloop()

# Erläuterungen:
# - `add_note()` fügt eine neue Notiz hinzu und speichert sie in der Listbox.
#
# - `save_notes()` speichert alle Notizen als Dictionary in einer JSON-Datei.
#
# - `load_notes()` lädt Notizen aus der JSON-Datei und zeigt sie in der Listbox an.
#
# - `display_note()` zeigt den Inhalt einer ausgewählten Notiz an.
#
# - `delete_note()` entfernt eine Notiz aus der Listbox und löscht deren Inhalt.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Ein Abschlussprojekt in tkinter hilft, alle Konzepte zu festigen und eine
#   interaktive Anwendung zu entwickeln.
#
# - Klassenstrukturen machen komplexe GUI-Anwendungen übersichtlich und leicht wartbar.
#
# - Die Verwendung von JSON-Dateien zur Datenspeicherung ist eine einfache Möglichkeit,
#   Benutzerinformationen zwischen Sitzungen zu speichern.




# ___________
#            \
# Aufgabe    /
# __________/
#
# Erweiterung des Projekts:
# - Ergänze die Notizbuch-Anwendung um eine Suchfunktion, bei der der Benutzer
#   einen Suchbegriff eingeben kann, um eine Notiz zu finden.
#
# - Implementiere eine Funktion zum Bearbeiten der Notizen direkt in der
#   Anwendung und speichere die Änderungen mit „Speichern“ ab.


#                   T~~
#                   |
#                  /"\
#          T~~     |'| T~~
#      T~~ |    T~ WWWW|
#      |  /"\   |  |  |/\T~~
#     /"\ WWW  /"\ |' |WW|
#    WWWWW/\| /   \|'/\|/"\
#    |   /__\/]WWW[\/__\WWWW
#    |"  WWWW'|I_I|'WWWW'  |
#    |   |' |/  -  \|' |'  |    Du hast bis am Ende durchgehalten. 
#    |'  |  |LI=H=LI|' |   |    Gratuliere. :-)
#    |   |' | |[_]| |  |'  |
#    |   |  |_|###|_|  |   |
#    '---'--'-/___\-'--'---'
#    
#  ___ _  _ ___  ___ 
# | __| \| |   \| __|
# | _|| .` | |) | _| 
# |___|_|\_|___/|___|
#                
# -=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=-=x=-=x=-=x=-=-=

