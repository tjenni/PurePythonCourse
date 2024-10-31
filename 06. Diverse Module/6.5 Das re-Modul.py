#              ___________________________
#       ______|                           |_____
#       \     |     6.5 DAS RE-MODUL      |    /
#        )    |___________________________|   (
#       /________)                    (________\       30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Das `re`-Modul in Python ermöglicht die Verwendung von regulären Ausdrücken,
# um Muster in Text zu suchen, zu verarbeiten oder zu manipulieren. In diesem Kapitel
# lernst du die wichtigsten Funktionen und Anwendungsfälle des `re`-Moduls kennen.


# ____________________________
#                            /
# Reguläre Ausdrücke        (
# ___________________________\

# Reguläre Ausdrücke (Regex) verwenden Muster aus Zeichen und Symbolen,
# um Textstellen präzise zu definieren.
#
# Häufige Zeichen:
# - `.` - Ein beliebiges Zeichen
# - `*` - Null oder mehr Wiederholungen
# - `+` - Eine oder mehr Wiederholungen
# - `?` - Macht das Zeichen davor optional
# - `[]` - Zeichenklasse, z.B. [abc] für a, b oder c
# - `^` - Anfang des Textes
# - `$` - Ende des Textes
#
# Häufige Klassen:
# - `\d` - Ziffern
# - `\w` - Buchstaben und Zahlen (alphanumerisch)
# - `\s` - Leerzeichen
# - `\b` - Wortgrenze


# Beispiel: Suchen einer Telefonnummer
import re

text = "Ruf mich an unter 123-456-7890."
pattern = r"\d{3}-\d{3}-\d{4}"
match = re.search(pattern, text)

if match:
    print("Telefonnummer gefunden:", match.group())
else:
    print("Keine Telefonnummer gefunden.")




# ____________________________
#                            /
# re.search()               (
# ___________________________\

# Die Funktion `re.search()` durchsucht den Text und gibt das erste Vorkommen
# eines Musters zurück, falls gefunden. Gibt `None` zurück, falls kein Treffer vorhanden ist.
#
# Beispiel:
text = "Python ist vielseitig."
pattern = "Python"
result = re.search(pattern, text)

if result:
    print("Muster gefunden!")
else:
    print("Muster nicht gefunden.")




# ____________________________
#                            /
# re.findall()              (
# ___________________________\

# Mit `re.findall()` wird eine Liste aller Treffer des Musters zurückgegeben.

text = "Finde alle Zahlen: 12, 34, 56."
numbers = re.findall(r"\d+", text)
print("Gefundene Zahlen:", numbers)




# ____________________________
#                            /
# re.match()                (
# ___________________________\

# `re.match()` überprüft, ob der Text mit einem bestimmten Muster beginnt.

text = "Python ist großartig!"
if re.match(r"Python", text):
    print("Der Text beginnt mit 'Python'.")




# ____________________________
#                            /
# re.sub()                  (
# ___________________________\

# Die Funktion `re.sub()` ersetzt jedes Vorkommen eines Musters im Text
# durch eine andere Zeichenkette.

text = "Python ist toll! Python ist beliebt!"
new_text = re.sub(r"Python", "Programmieren", text)
print(new_text)




# ____________________________
#                            /
# re.split()                (
# ___________________________\

# `re.split()` teilt einen Text an einem Muster und gibt eine Liste der Teile zurück.

text = "Apfel, Banane; Kirsche, Orange"
fruits = re.split(r"[;,]", text)
print("Getrennte Wörter:", fruits)




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Das `re`-Modul erlaubt die Arbeit mit regulären Ausdrücken, um Muster
#   in Text zu suchen, zu finden oder zu ersetzen.
#
# - `re.search()`, `re.findall()`, `re.match()`, `re.sub()` und `re.split()`
#   sind nützliche Funktionen für verschiedene Anwendungsfälle.
#
# - Reguläre Ausdrücke bieten mit Zeichen wie `\d`, `\w`, `.` oder `*` eine
#   flexible und mächtige Möglichkeit, Textmuster zu beschreiben.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Schreibe ein Programm, das überprüft, ob ein Text eine E-Mail-Adresse enthält.
# Verwende `re.search()` und ein passendes Muster.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle ein Programm, das alle Wörter im Text findet, die mit einem Großbuchstaben
# beginnen. Verwende dazu `re.findall()`.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Programm, das Telefonnummern im Format „123-456-7890“ in einem Text
# ersetzt. Verwende `re.sub()`, um alle gefundenen Nummern durch „XXX-XXX-XXXX“
# zu ersetzen.


# Füge hier deine Lösung ein.




#            .n.                     |
#           /___\          _.---.  \ _ /
#           [|||]         (_._ ) )--;_) =-
#           [___]           '---'.__,' \           Reguläre Ausdrücke
#           }-=-{                    |             sind toll. Fast so
#           |-" |                                  entspannend, wie Ferien
#           |.-"|                p                 am Meer. ;-)
#    ~^=~^~-|_.-|~^-~^~ ~^~ -^~^~|\ ~^-~^~-
#    ^   .=.| _.|__  ^       ~  /| \
#     ~ /:. \" _|_/\    ~      /_|__\  ^
#    .-/::.  |   |""|-._    ^   ~~~~
#      `===-'-----'""`  '-.              ~
#                     __.-'      ^
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
# Schreibe ein Programm, das überprüft, ob ein Text eine E-Mail-Adresse enthält.
# Verwende `re.search()` und ein passendes Muster.

'''
import re

text = "Bitte kontaktiere uns unter info@beispiel.com für weitere Informationen."
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

if re.search(pattern, text):
    print("E-Mail-Adresse gefunden:", re.search(pattern, text).group())
else:
    print("Keine E-Mail-Adresse gefunden.")
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle ein Programm, das alle Wörter im Text findet, die mit einem Großbuchstaben
# beginnen. Verwende dazu `re.findall()`.

'''
import re

text = "Heute ist ein schöner Tag in Berlin, und Anna spielt im Park."
pattern = r"\b[A-Z][a-z]*\b"

capitalized_words = re.findall(pattern, text)
print("Wörter mit Großbuchstaben:", capitalized_words)
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Programm, das Telefonnummern im Format „123-456-7890“ in einem Text
# ersetzt. Verwende `re.sub()`, um alle gefundenen Nummern durch „XXX-XXX-XXXX“
# zu ersetzen.

'''
import re

text = "Kontaktieren Sie uns unter 123-456-7890 oder 987-654-3210."
pattern = r"\b\d{3}-\d{3}-\d{4}\b"

updated_text = re.sub(pattern, "XXX-XXX-XXXX", text)
print("Text mit ersetzten Telefonnummern:", updated_text)
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><
