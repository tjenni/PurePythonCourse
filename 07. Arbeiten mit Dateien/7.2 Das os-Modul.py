#              ___________________________
#       ______|                           |_____
#       \     |      7.2 DAS OS-MODUL     |    /
#        )    |___________________________|   (
#       /________)                    (________\       29.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Das `os`-Modul bietet viele Funktionen, um mit dem Betriebssystem zu interagieren.
# Es erlaubt uns, auf Dateisysteme zuzugreifen, Verzeichnisse zu verwalten und
# Systeminformationen zu erhalten. Das Modul ist besonders nützlich für
# automatisierte Aufgaben, wie das Erstellen und Bearbeiten von Ordnern und Dateien.


# ____________________________
#                            /
# Modul importieren         (
# ___________________________\

# Um das `os`-Modul zu verwenden, muss es zuerst importiert werden:

import os


# _____________________________
#                              /
# Arbeiten mit Verzeichnissen (
# _____________________________\

# 1. `os.getcwd()`: Gibt das aktuelle Arbeitsverzeichnis zurück.
current_directory = os.getcwd()
print("Aktuelles Verzeichnis:", current_directory)

# 2. `os.listdir(pfad)`: Listet alle Dateien und Ordner im angegebenen Pfad auf.
content = os.listdir(current_directory)
print("Inhalt des aktuellen Verzeichnisses:", content)

# 3. `os.mkdir(pfad)`: Erstellt ein neues Verzeichnis an dem angegebenen Pfad.
# Beispiel: Erstellen eines neuen Verzeichnisses
new_directory = "Beispielordner"
if not os.path.exists(new_directory):  # Verzeichnis nur erstellen, wenn es noch nicht existiert
    os.mkdir(new_directory)
    print(f"Verzeichnis '{new_directory}' wurde erstellt.")

# 4. `os.rmdir(pfad)`: Löscht ein Verzeichnis, falls es leer ist.
# Beispiel: Löschen des Verzeichnisses
if os.path.exists(new_directory):  # Nur löschen, wenn das Verzeichnis existiert
    os.rmdir(new_directory)
    print(f"Verzeichnis '{new_directory}' wurde gelöscht.")




# ___________________________
#                           /
# Arbeiten mit Dateien     (
# __________________________\

# Das `os`-Modul enthält auch Funktionen zur Arbeit mit Dateien.

# 1. `os.path.exists(pfad)`: Überprüft, ob eine Datei oder ein Verzeichnis existiert.
filename = "beispiel.txt"
if os.path.exists(filename):
    print(f"Die Datei '{filename}' existiert.")
else:
    print(f"Die Datei '{filename}' existiert nicht.")

# 2. `os.rename(alter_name, neuer_name)`: Benennt eine Datei oder ein Verzeichnis um.
# Beispiel: Umbenennen einer Datei
old_filename = "alte_datei.txt"
new_filename = "neue_datei.txt"
if os.path.exists(old_filename):
    os.rename(old_filename, new_filename)
    print(f"Datei '{old_filename}' wurde in '{new_filename}' umbenannt.")

# 3. `os.remove(pfad)`: Löscht die angegebene Datei.
# Beispiel: Löschen einer Datei
if os.path.exists(new_filename):
    os.remove(new_filename)
    print(f"Datei '{new_filename}' wurde gelöscht.")




# ____________________________
#                            /
# Dateipfade bearbeiten     (
# ___________________________\

# Das `os.path`-Modul innerhalb von `os` bietet Funktionen zur Bearbeitung von Dateipfaden.

# 1. `os.path.join(pfad, datei)`: Verbindet Verzeichnis- und Dateinamen zu einem Pfad.
project_folder = "Projekt"
filename = "ergebnisse.txt"
path = os.path.join(project_folder, filename)
print("Voller Dateipfad:", path)

# 2. `os.path.abspath(datei)`: Gibt den absoluten Pfad einer Datei zurück.
absolute_path = os.path.abspath(filename)
print("Absoluter Pfad:", absolute_path)




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - `os.getcwd()` gibt das aktuelle Arbeitsverzeichnis zurück und `os.listdir()`
#   listet die Inhalte eines Verzeichnisses auf.
#
# - `os.mkdir()` und `os.rmdir()` können Verzeichnisse erstellen und löschen.
#
# - `os.path` enthält nützliche Funktionen zur Bearbeitung von Dateipfaden, wie
#   `os.path.join()` zum Kombinieren und `os.path.abspath()` zum Abrufen
#   des absoluten Pfads.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Programm, das ein neues Verzeichnis mit dem Namen „Testordner“ erstellt,
# überprüft, ob es erfolgreich erstellt wurde, und das Verzeichnis dann wieder löscht.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe ein Programm, das alle Dateien im aktuellen Verzeichnis auflistet und
# für jede Datei den vollständigen Pfad auf der Konsole ausgibt.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/

# Erstelle ein Programm, das eine Datei „log.txt“ erstellt und in einer
# Schleife jede Sekunde eine neue Zeile mit der aktuellen Uhrzeit hinzufügt.
# Das Programm soll nach fünf Einträgen enden.

# Füge hier deine Lösung ein.



#    .----.______
#    |mga        |
#    |    ___________    Du kannst nun auf das Dateisystem zureifen.
#    |   /          /    Nutze diese Macht mit Vorsicht. 
#    |  /          /
#    | /          /
#    |/__________/
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
# Erstelle ein Programm, das ein neues Verzeichnis mit dem Namen „Testordner“ erstellt,
# überprüft, ob es erfolgreich erstellt wurde, und das Verzeichnis dann wieder löscht.

'''
folder_name = "Testordner"

# Verzeichnis erstellen
os.mkdir(folder_name)
print(f"Verzeichnis '{folder_name}' wurde erstellt.")

# Überprüfen, ob das Verzeichnis existiert
if os.path.exists(folder_name):
    print(f"Überprüfung: Das Verzeichnis '{folder_name}' existiert.")

# Verzeichnis löschen
os.rmdir(folder_name)
print(f"Verzeichnis '{folder_name}' wurde gelöscht.")
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe ein Programm, das alle Dateien im aktuellen Verzeichnis auflistet und
# für jede Datei den vollständigen Pfad auf der Konsole ausgibt.

'''
current_directory = os.getcwd()
print("Dateien im aktuellen Verzeichnis:")

# Alle Dateien im aktuellen Verzeichnis auflisten
for file in os.listdir(current_directory):
    path = os.path.join(current_directory, file)
    if os.path.isfile(path):  # Nur Dateien anzeigen, keine Verzeichnisse
        print(path)
'''




# ___________
#            \
# Aufgabe 3  /
# __________/

# Erstelle ein Programm, das eine Datei „log.txt“ erstellt und in einer
# Schleife jede Sekunde eine neue Zeile mit der aktuellen Uhrzeit hinzufügt.
# Das Programm soll nach fünf Einträgen enden.

'''
with open("log.txt", "w") as file:
    for i in range(5):  # Schleife für 5 Einträge
        time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        file.write(f"Eintrag {i + 1}: {time}\n")
        print(f"Eintrag {i + 1}: {time}")  # Ausgabe zur Bestätigung
        time.sleep(1)  # Warte eine Sekunde
'''



# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


