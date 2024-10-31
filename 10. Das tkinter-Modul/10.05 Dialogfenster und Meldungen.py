#              _______________________________________
#       ______|                                       |_____
#       \     |   10.5 DIALOGFENSTER UND MELDUNGEN    |    /
#        )    |_______________________________________|   (
#       /________)                                (________\      30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Dialogfenster und Meldungen sind spezielle Fenster, die Benutzern wichtige
# Informationen anzeigen oder ihnen erlauben, bestimmte Entscheidungen zu treffen.
# `tkinter` bietet eigene Dialog-Widgets für häufig verwendete Aktionen wie
# Benachrichtigungen, Datei- und Farbauswahl.


# ____________________________
#                            /
# 1. Das Modul `messagebox` (
# ___________________________\

# `tkinter.messagebox` stellt einfache Funktionen zur Verfügung, um Meldungen anzuzeigen.
# Hier ein paar nützliche Methoden aus `messagebox`:

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Messagebox Beispiele")
root.geometry("300x200")

# Beispiel für die verschiedenen Arten von Meldungen
def show_info():
    messagebox.showinfo("Info", "Das ist eine Information.")

def show_warning():
    messagebox.showwarning("Warnung", "Dies ist eine Warnung!")

def show_error():
    messagebox.showerror("Fehler", "Es ist ein Fehler aufgetreten!")

# Buttons erstellen, um die Meldungen anzuzeigen
btn_info = tk.Button(root, text="Info anzeigen", command=show_info)
btn_info.pack(pady=5)

btn_warning = tk.Button(root, text="Warnung anzeigen", command=show_warning)
btn_warning.pack(pady=5)

btn_error = tk.Button(root, text="Fehler anzeigen", command=show_error)
btn_error.pack(pady=5)

root.mainloop()

# Diese `messagebox`-Methoden stehen zur Verfügung:
# - `showinfo(title, message)`: Zeigt eine Informationsmeldung.
#
# - `showwarning(title, message)`: Zeigt eine Warnmeldung.
#
# - `showerror(title, message)`: Zeigt eine Fehlermeldung.




# ____________________________
#                            /
# 2. Bestätigungsdialoge    (
# ___________________________\

# Bestätigungsdialoge ermöglichen es, Benutzerentscheidungen abzufragen.
# `askquestion`, `askyesno`, und `askokcancel` sind die Hauptmethoden.

def confirm_exit():
    answer = messagebox.askyesno("Beenden", "Möchtest du wirklich beenden?")
    if answer:
        root.destroy()

root = tk.Tk()
root.title("Bestätigungsdialog Beispiel")

exit_button = tk.Button(root, text="Beenden", command=confirm_exit)
exit_button.pack(pady=20)

root.mainloop()

# In diesem Beispiel fragt `askyesno()` den Benutzer, ob er wirklich das Programm beenden möchte.
# Die Funktion gibt `True` (Ja) oder `False` (Nein) zurück.




# ____________________________
#                            /
# 3. Dateiauswahlfenster    (
# ___________________________\

# `tkinter.filedialog` bietet Funktionen, um Dateien zu öffnen oder zu speichern.

from tkinter import filedialog

root = tk.Tk()
root.title("Dateiauswahlfenster Beispiel")

def open_file():
    file_path = filedialog.askopenfilename(title="Datei öffnen", filetypes=[("Textdateien", "*.txt"), ("Alle Dateien", "*.*")])
    if file_path:
        print(f"Ausgewählte Datei: {file_path}")

def save_file():
    file_path = filedialog.asksaveasfilename(title="Datei speichern", defaultextension=".txt", filetypes=[("Textdateien", "*.txt"), ("Alle Dateien", "*.*")])
    if file_path:
        print(f"Speicherort: {file_path}")

btn_open = tk.Button(root, text="Datei öffnen", command=open_file)
btn_open.pack(pady=5)

btn_save = tk.Button(root, text="Datei speichern", command=save_file)
btn_save.pack(pady=5)

root.mainloop()

# `askopenfilename()` öffnet ein Dialogfenster, in dem der Benutzer eine Datei zum Öffnen auswählen kann.
# `asksaveasfilename()` öffnet ein Dialogfenster, in dem der Benutzer eine Datei speichern kann.



# ____________________________
#                            /
# 4. Farbauswahlfenster     (
# ___________________________\

# `tkinter.colorchooser` bietet eine einfache Möglichkeit, eine Farbe auszuwählen.

from tkinter import colorchooser

root = tk.Tk()
root.title("Farbauswahlfenster Beispiel")

def choose_color():
    color = colorchooser.askcolor(title="Farbe auswählen")
    if color[1]:  # Farbwert im HEX-Format
        print(f"Ausgewählte Farbe: {color[1]}")

btn_color = tk.Button(root, text="Farbe auswählen", command=choose_color)
btn_color.pack(pady=20)

root.mainloop()

# `askcolor()` öffnet ein Dialogfenster zur Farbauswahl und gibt eine Tupel-Rückgabe
# mit RGB- und Hex-Werten zurück.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - `messagebox` ist ideal für einfache Benachrichtigungen und Bestätigungsabfragen.
#
# - `filedialog` ermöglicht das Öffnen und Speichern von Dateien über ein Dialogfenster.
#
# - `colorchooser` öffnet eine Farbauswahl für die Benutzer.
#
# - Diese Dialoge erleichtern die Benutzerinteraktion und ermöglichen einfache Dateiverwaltung
#   und benutzerdefinierte Anpassungen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Programm mit einem Button „Info“, der eine Informationsmeldung anzeigt,
# und einem Button „Warnung“, der eine Warnmeldung anzeigt.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Programm mit einem Button „Datei öffnen“, der den Benutzer eine
# Datei auswählen lässt und den Dateipfad auf der Konsole anzeigt.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe ein Programm mit einem Button „Farbe wählen“, der eine Farbauswahl
# öffnet und die ausgewählte Farbe als Hex-Wert auf der Konsole anzeigt.


# Füge hier deine Lösung ein.




#     ______________________________
#   / \                             \.
#  |   |                            |.
#   \_ |                            |.
#      |     Jetzt kannst du        |.
#      |     Dialogfenster und      |.
#      |     Meldungen einsetzen.   |.
#      |                            |.
#      |   _________________________|___
#      |  /                            /.
#      \_/dc__________________________/.
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
#     


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Programm mit einem Button „Info“, der eine Informationsmeldung anzeigt,
# und einem Button „Warnung“, der eine Warnmeldung anzeigt.

'''
import tkinter as tk
from tkinter import messagebox

class MessageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Meldungen anzeigen")

        # Info-Button
        self.info_button = tk.Button(root, text="Info", command=self.show_info)
        self.info_button.pack(pady=10)

        # Warnung-Button
        self.warning_button = tk.Button(root, text="Warnung", command=self.show_warning)
        self.warning_button.pack(pady=10)

    def show_info(self):
        messagebox.showinfo("Information", "Das ist eine Informationsmeldung.")

    def show_warning(self):
        messagebox.showwarning("Warnung", "Achtung! Dies ist eine Warnmeldung.")

# Hauptprogramm
root = tk.Tk()
app = MessageApp(root)
root.mainloop()
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Programm mit einem Button „Datei öffnen“, der den Benutzer eine
# Datei auswählen lässt und den Dateipfad auf der Konsole anzeigt.

'''
import tkinter as tk
from tkinter import filedialog

class FileOpenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Datei öffnen")

        # Button zum Öffnen einer Datei
        self.open_button = tk.Button(root, text="Datei öffnen", command=self.open_file)
        self.open_button.pack(pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Wähle eine Datei")
        if file_path:
            print("Gewählter Dateipfad:", file_path)

# Hauptprogramm
root = tk.Tk()
app = FileOpenApp(root)
root.mainloop()
'''


# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe ein Programm mit einem Button „Farbe wählen“, der eine Farbauswahl
# öffnet und die ausgewählte Farbe als Hex-Wert auf der Konsole anzeigt.

'''
import tkinter as tk
from tkinter import colorchooser

class ColorChooserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Farbauswahl")

        # Button zum Wählen einer Farbe
        self.choose_color_button = tk.Button(root, text="Farbe wählen", command=self.choose_color)
        self.choose_color_button.pack(pady=10)

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Wähle eine Farbe")
        if color_code:
            print("Ausgewählte Farbe:", color_code[1])  # Hex-Wert der Farbe

# Hauptprogramm
root = tk.Tk()
app = ColorChooserApp(root)
root.mainloop()
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><



