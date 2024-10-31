#              _____________________________
#       ______|                             |_____
#       \     |  WILLKOMMEN ZUM PYTHONKURS  |    /
#        )    |_____________________________|   (
#       /________)                      (________\       30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
#                                                     
                    
# Willkommen! Du beginnst hier eine spannende Reise in die Programmierung
# mit Python. 

# Vielleicht hast du schon mit der Sprache Scratch gearbeitet.Vom Prinzip 
# her ist Python ähnlich. Allerdings werden die Befehle nicht als Blöcke
# dargestellt, sondern müssen als Text geschrieben werden.

# Dabei kann es vorkommen, dass das Programm bei Schreibfehlern nicht
# richtig läuft. Für Anfänger ist das manchmal etwas frustrierend. 
# Wenn du nicht weiterkommst, zögere nicht, die Lehrperson oder
# auch ChatGPT zu Fragen.

# Dieser Kurs ist für Anfänger gedacht und behandelt die folgenden Themen: 

#    1. Variablen: Mit Variablen kannst du Daten speichern und verwalten. 
#       Ob es sich um eine Zahl, einen Text oder eine Liste handelt, mit 
#       Variablen kannst du wichtige Informationen für dein Programm sichern 
#       und später wieder abrufen.

#    2. Verzweigungen: Entscheidungen treffen ist ein wesentlicher Bestandteil 
#       jedes Programms. Verzweigungen (if-Anweisungen) helfen deinem Code, auf 
#       unterschiedliche Situationen zu reagieren, indem sie je nach Bedingung 
#       verschiedene Anweisungen ausführen.

#    3. Schleifen: Oftmals muss eine Aufgabe mehrere Male wiederholt werden. 
#       Mit Schleifen kannst du Codeabschnitte so oft ausführen, wie es notwendig ist, 
#       was Zeit spart und deinen Code effizienter macht.

#    4. Funktionen: Eine Funktion ist eine Art Mini-Programm in deinem Code. 
#       Sie fasst zusammen, was dein Code tun soll, und kann immer wieder aufgerufen 
#       werden. So bleibt dein Programm übersichtlich und du kannst den gleichen 
#       Code mehrmals verwenden, ohne ihn zu wiederholen.

#    5. Datenstrukturen: Datenstrukturen wie Listen, Dictionaries, Sets und Tupel 
#       helfen dir, komplexere Informationen zu organisieren und zu speichern. 
#       Sie sind grundlegende Bausteine für das Arbeiten mit größeren 
#       Datenmengen in Python.

#    6. Diverse Module: Python bietet eine Vielzahl an Modulen und Bibliotheken, 
#       die nützliche Funktionen und Werkzeuge enthalten, um dein Programm zu erweitern 
#       und spezielle Aufgaben zu lösen – von Matheberechnungen bis hin zur Arbeit 
#       mit Datumsangaben.

#    7. Arbeiten mit Dateien: Dateien sind eine zentrale Möglichkeit, Daten dauerhaft 
#       zu speichern. Hier lernst du, wie du Dateien in Python erstellst, liest, 
#       schreibst und verwaltest – eine wichtige Fähigkeit für viele Anwendungsfälle.

#    8. Objektorientierte Programmierung (OOP): Die objektorientierte Programmierung 
#       hilft, komplexere Programme zu strukturieren. Mit Klassen und Objekten kannst 
#       du Konzepte aus der realen Welt im Code abbilden und modular gestalten, 
#       um deinen Code wiederverwendbar und flexibel zu machen.

#    9. Fehlerbehandlung und Debugging: Fehler passieren – aber die richtige 
#       Fehlerbehandlung und Debugging-Techniken helfen dir, deinen Code robuster 
#       zu machen und Fehler systematisch zu identifizieren und zu beheben.

#   10. Grafische Benutzeroberflächen mit dem tkinter-Modul: Mit tkinter kannst 
#       du grafische Benutzeroberflächen (GUIs) erstellen, die dein Programm für 
#       Benutzer interaktiv und benutzerfreundlich machen. Hier lernst du die 
#       Grundlagen der GUI-Entwicklung in Python.


# Zu jedem Thema gibt es einen Ordner mit dazugehörigen Programmdateien und 
# Aufgaben. Du kannst den Code in diesen Dateien direkt ausführen und bearbeiten.

# Grundsätzlich können diese Programmdateien mit jedem Programmeditor geöffnet werden.
# Ich empfehle jedoch die Software Thonny (https://thonny.org) zu verwenden.
# Jede Datei enthält Erklärungen und kleine Aufgaben, welche direkt in der Datei
# gelöst werden können.



# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Öffne nun diese Datei in Thonny oder in einem anderen Python-Editor. 

# Unten habe ich das Spiel Wordle eingefügt. Es ist ein Spiel, welches
# texbasiert ist und in der Konsole gespielt werden kann. Führe das
# Programm aus, indem in Thonny auf den grünen Pfeil klickst.

# Schaffst du es, ein weiteres Wort zum Spiel hinzuzufügen?



# ~~~~~~~ WORDLE-SPIEL START ~~~~~~~ 

import random

# Word-Liste (du kannst sie anpassen)
words = ["apfel", "birne", "honig", "glanz", "wolke", "licht", "radio", "perle", "rosen", "blume"]

# Zufälliges Wort wählen
def choose_word():
    return random.choice(words)

# Spielerfeedback geben
def give_feedback(guess, word):
    feedback = []
    for i in range(5):
        if guess[i] == word[i]:
            feedback.append('🟩')  # Richtiger Buchstabe an der richtigen Position
        elif guess[i] in word:
            feedback.append('🟨')  # Richtiger Buchstabe, aber falsche Position
        else:
            feedback.append('⬜')  # Falscher Buchstabe
    return ''.join(feedback)

# Wordle-Spiel starten
def play_wordle():
    word = choose_word()
    attempts = 6
    
    print("Willkommen zu Wordle! Du hast 6 Versuche.")
    
    for attempt in range(1, attempts + 1):
        guess = input(f"Versuch {attempt}/6: ").lower()
        
        if len(guess) != 5:
            print("Dein Wort muss 5 Buchstaben lang sein!")
            continue
        
        if guess == word:
            print("Glückwunsch! Du hast das Wort erraten.")
            break
        
        feedback = give_feedback(guess, word)
        print("Feedback:", feedback)
        
        if attempt == attempts:
            print(f"Schade, das Wort war '{word}'. Versuch es nochmal!")

# Spiel starten
if __name__ == "__main__":
    play_wordle()

# ~~~~~~~ WORDLE-SPIEL ENDE ~~~~~~~



# Nun wünsche ich viel Spass beim Spielen und beim Programmieren mit Python. 

#            /^\/^\
#          _|__|  O|
# \/     /~     \_/ \
#  \____|__________/  \
#         \_______      \
#                 `\     \                 \
#                  |     |                  \
#                 /      /                    \
#                /     /                       \\
#              /      /                         \ \
#             /     /                            \  \
#           /     /             _----_            \   \
#          /     /           _-~      ~-_         |   |
#         (      (        _-~    _--_    ~-_     _/   |
#          \      ~-____-~    _-~    ~-_    ~-_-~    /
#            ~-_           _-~          ~-_       _-~
#               ~--______-~                ~-___-~
#                         
#  ___ _  _ ___  ___ 
# | __| \| |   \| __|
# | _|| .` | |) | _| 
# |___|_|\_|___/|___|
#                
# -=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-


