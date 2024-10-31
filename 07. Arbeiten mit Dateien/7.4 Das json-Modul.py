#              ___________________________
#       ______|                           |_____
#       \     |     7.4 DAS JSON-MODUL    |    /
#        )    |___________________________|   (
#       /________)                    (________\       29.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Das `json`-Modul erlaubt es uns, mit JSON-Daten zu arbeiten, die häufig
# in Webanwendungen und zur Datenübertragung verwendet werden.
# JSON (JavaScript Object Notation) ist ein einfaches Datenformat, das
# auf der Struktur von Python-Dictionaries basiert. Es wird zur Speicherung
# und zum Austausch von Daten verwendet.


# ___________________________
#                           /
# JSON-Modul importieren   (
# __________________________\

# Um das `json`-Modul zu verwenden, muss es zuerst importiert werden:

import json




# ___________________________
#                           /
# JSON-Dateien schreiben   (
# __________________________\

# Mit `json.dump()` kann man Daten als JSON-Datei speichern.
# Die Datenstruktur kann ein Dictionary oder eine Liste sein.

# Beispiel: Ein Dictionary mit Benutzerinformationen in eine JSON-Datei schreiben
users = {
    "name": "Max Mustermann",
    "alter": 29,
    "hobbys": ["Lesen", "Radfahren", "Programmieren"]
}

with open("benutzer.json", "w") as file:
    json.dump(users, file, indent=4)  # `indent=4` formatiert das JSON leserlich

# Die Datei „benutzer.json“ wird erstellt und enthält die Informationen
# des Benutzers im JSON-Format.




# ___________________________
#                           /
# JSON-Dateien lesen       (
# __________________________\

# Mit `json.load()` können wir eine JSON-Datei in Python lesen und die Daten
# in einer Python-Datenstruktur speichern.

# Beispiel: Die zuvor gespeicherte JSON-Datei lesen
with open("benutzer.json", "r") as file:
    file = json.load(datei)
    print("Benutzerdaten aus JSON-Datei:", file)

# Die Daten werden als Dictionary geladen und können wie gewohnt in Python
# verarbeitet werden.




# ____________________________
#                            /
# JSON in Zeichenketten     (
# ___________________________\

# Das `json`-Modul bietet auch Funktionen, um JSON-Daten direkt als
# Zeichenkette zu verarbeiten.

# - `json.dumps()` konvertiert ein Dictionary oder eine Liste in eine JSON-Zeichenkette.
# - `json.loads()` konvertiert eine JSON-Zeichenkette zurück in eine Python-Datenstruktur.

# Beispiel: Ein Dictionary in eine JSON-Zeichenkette umwandeln und zurückkonvertieren
people = {
    "schueler": ["Anna", "Tom", "Lena"],
    "lehrer": ["Herr Schmidt", "Frau Müller"]
}

json_data = json.dumps(people, indent=2)  # JSON-Zeichenkette
print("Daten als JSON-Zeichenkette:", json_data)

# Zurück in ein Python-Dictionary konvertieren
recovered_data = json.loads(json_data)
print("Daten wiederhergestellt:", recovered_data)




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Verwende `json.dump()` und `json.load()` für das Schreiben und Lesen von JSON-Dateien.
#
# - Mit `json.dumps()` und `json.loads()` kannst du Daten in JSON-Zeichenketten umwandeln
#   und wieder in Python-Datenstrukturen konvertieren.
#
# - JSON ist besonders nützlich, um Daten im Web und für Konfigurationsdateien zu speichern.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Dictionary `buch` mit den Informationen:
# „titel“: „Python Programmieren“, „autor“: „Max Mustermann“, „seiten“: 350
# Speichere dieses Dictionary als JSON-Datei namens „buch.json“.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe ein Programm, das die Datei „buch.json“ liest und den Titel,
# Autor und die Anzahl der Seiten auf der Konsole ausgibt.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Dictionary `schule` mit einer Liste von Klassen, die jeweils
# mehrere Schülernamen enthalten. Konvertiere das Dictionary in eine JSON-Zeichenkette
# und gib es auf der Konsole aus.


# Füge hier deine Lösung ein.




#                .=.,
#               ;c =\
#             __|  _/
#           .'-'-._/-'-._
#          /..   ____    \              JSON ist der Superheld zur 
#         /' _  [<_->] )  \             Speicherung von Daten. 
#        (  / \--\_>/-/'._ )
#         \-;_/\__;__/ _/ _/
#          '._}|==o==\{_\/
#           /  /-._.--\  \_
#          // /   /|   \ \ \
#         / | |   | \;  |  \ \
#        / /  | :/   \: \   \_\
#       /  |  /.'|   /: |    \ \
#       |  |  |--| . |--|     \_\
#       / _/   \ | : | /___--._) \
#      |_(---'-| >-'-| |       '-'
#   snd       /_/     \_\
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
# Erstelle ein Dictionary `buch` mit den Informationen:
# „titel“: „Python Programmieren“, „autor“: „Max Mustermann“, „seiten“: 350
# Speichere dieses Dictionary als JSON-Datei namens „buch.json“.

'''
book = {
    "titel": "Python Programmieren",
    "autor": "Max Mustermann",
    "seiten": 350
}

with open("buch.json", "w") as file:
    json.dump(book, file, indent=4)
print("Die Datei 'buch.json' wurde erstellt und gespeichert.")
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe ein Programm, das die Datei „buch.json“ liest und den Titel,
# Autor und die Anzahl der Seiten auf der Konsole ausgibt.

'''
with open("buch.json", "r") as file:
    book = json.load(file)

print("Buchinformationen:")
print("Titel:", book["titel"])
print("Autor:", book["autor"])
print("Seiten:", book["seiten"])
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Dictionary `schule` mit einer Liste von Klassen, die jeweils
# mehrere Schülernamen enthalten. Konvertiere das Dictionary in eine JSON-Zeichenkette
# und gib es auf der Konsole aus.

'''
school = {
    "Klasse 10A": ["Anna", "Tom", "Lena"],
    "Klasse 10B": ["Max", "Eva", "Tim"],
    "Klasse 10C": ["Paul", "Sara", "Leo"]
}

school_json = json.dumps(school, indent=4)
print("Schule als JSON-Zeichenkette:")
print(school_json)
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


