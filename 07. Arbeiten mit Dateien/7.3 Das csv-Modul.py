#              ___________________________
#       ______|                           |_____
#       \     |      7.3 DAS CSV-MODUL    |    /
#        )    |___________________________|   (
#       /________)                    (________\       29.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Das `csv`-Modul in Python erlaubt uns das Lesen und Schreiben von CSV-Dateien.
# CSV steht für "Comma-Separated Values" und ist ein einfaches, textbasiertes
# Datenformat, das häufig zur Speicherung von Tabellen und Listen verwendet wird.


# ___________________________
#                           /
# Modul importieren         (
# ___________________________\

# Um das `csv`-Modul zu verwenden, muss es zuerst importiert werden:

import csv


# ___________________________
#                           /
# CSV-Datei schreiben       (
# ___________________________\

# Das `csv`-Modul stellt eine einfache Möglichkeit bereit, Daten in CSV-Dateien zu
# schreiben. Hierzu verwenden wir `csv.writer()`.

# Beispiel: Schreiben einer CSV-Datei mit einer Liste von Schülerdaten
with open("schueler.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    # Überschriften schreiben
    writer.writerow(["Name", "Alter", "Klasse"])
    
    # Daten schreiben
    writer.writerow(["Max", 16, "10A"])
    writer.writerow(["Anna", 15, "9B"])
    writer.writerow(["Lena", 16, "10C"])

# Hier erstellt das Programm eine Datei „schueler.csv“ und speichert eine
# einfache Tabelle mit Schülerdaten darin.


# ___________________________
#                           /
# CSV-Datei lesen           (
# ___________________________\

# Um Daten aus einer CSV-Datei zu lesen, verwenden wir `csv.reader()`. Die Daten
# werden dabei Zeile für Zeile ausgelesen und in Listen gespeichert.

# Beispiel: Lesen der Daten aus einer CSV-Datei
with open("schueler.csv", "r") as file:
    reader = csv.reader(file)
    
    # Daten Zeile für Zeile ausgeben
    for row in reader:
        print(row)

# Die Datei „schueler.csv“ wird geöffnet und jede Zeile wird in der Konsole angezeigt.


# ___________________________
#                           /
# CSV-Datei mit Dictionaries (
# ___________________________\

# Das `csv`-Modul bietet auch die Möglichkeit, CSV-Dateien als Dictionary
# zu lesen und zu schreiben. Mit `csv.DictWriter()` und `csv.DictReader()` können
# wir dabei jede Zeile als Dictionary speichern, was das Auslesen von
# Spaltenüberschriften erleichtert.

# Beispiel: Schreiben einer CSV-Datei mit `DictWriter`
with open("kurse.csv", "w", newline="") as datei:
    fieldnames = ["Kursname", "Lehrer", "Teilnehmerzahl"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Überschriften schreiben
    writer.writeheader()
    
    # Daten schreiben
    writer.writerow({"Kursname": "Mathe", "Lehrer": "Herr Müller", "Teilnehmerzahl": 20})
    writer.writerow({"Kursname": "Physik", "Lehrer": "Frau Schmidt", "Teilnehmerzahl": 15})

# Beispiel: Lesen der CSV-Datei mit `DictReader`
with open("kurse.csv", "r") as file:
    reader = csv.DictReader(file)
    
    # Jede Zeile als Dictionary ausgeben
    for row in reader:
        print(row)


# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - `csv.writer()` und `csv.DictWriter()` dienen zum Schreiben in CSV-Dateien.
# - `csv.reader()` und `csv.DictReader()` werden zum Lesen von CSV-Dateien verwendet.
# - Beim Schreiben und Lesen einer CSV-Datei ist `newline=""` im `open()`-Befehl
#   notwendig, um doppelte Leerzeilen zu vermeiden.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Programm, das eine Datei „produkte.csv“ erstellt und die folgenden
# Daten speichert:
# - Überschriften: „Produkt“, „Preis“, „Menge“
# - Daten: „Stift“, 1.50, 100; „Heft“, 2.00, 50; „Lineal“, 1.00, 75


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe ein Programm, das die Daten aus der Datei „produkte.csv“ liest und
# für jedes Produkt ausgibt: „Produkt: [Produktname], Preis: [Preis], Menge: [Menge]“


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Programm, das eine Datei „noten.csv“ mit den Noten von Schülern
# in verschiedenen Fächern erstellt. Verwende `DictWriter`, um die Daten zu schreiben
# und `DictReader`, um die Daten auszulesen und die Noten auf der Konsole anzuzeigen.


# Füge hier deine Lösung ein.


#                       ,%;,
#                       ,%%,
#          ______________)(______________
#         /             (__)             \
#        /________________________________\
#        [________________________________]
#           \ \  / /            \ \  / /         Nun weisst du, wie man 
#            \ \/ /              \ \/ /          mit `tables` umgeht. ;-)
#            _\/ /________________\ \/_
#           [_/o/__________________\o\_]
#            / /\ \              / /\ \
#           lc/  \_\            /_/  \_\
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



