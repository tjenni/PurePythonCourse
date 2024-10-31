#              _______________________________
#       ______|                               |_____
#       \     |    9.3 DEBUGGING-TECHNIKEN    |    /
#        )    |_______________________________|   (
#       /________)                        (________\       30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Debugging ist der Prozess, mit dem Programmfehler identifiziert und behoben werden.
# Fehler können in jeder Phase der Programmierung auftreten und Debugging ist eine
# wichtige Fähigkeit, um das gewünschte Verhalten des Codes zu erreichen.

# In diesem Kapitel werden wir verschiedene Debugging-Techniken kennenlernen und
# erproben, die dabei helfen, Fehler effizient zu finden und zu lösen.


# ____________________________
#                            /
# 1. Verwenden von print()  (
# ___________________________\

# Eine der einfachsten Techniken ist das Einfügen von `print()`-Anweisungen an
# bestimmten Stellen im Code. Durch die Ausgabe von Variablen und Zwischenergebnissen
# auf der Konsole kann man den Ablauf des Programms und die Werte im Detail beobachten.

# Beispiel:
def addiere(a, b):
    print(f"a: {a}, b: {b}")  # Debug-Ausgabe
    return a + b

ergebnis = addiere(5, 3)
print(f"Ergebnis: {ergebnis}")

# Erläuterung:
# - Durch `print(f"a: {a}, b: {b}")` können wir prüfen, welche Werte die Parameter 
#   `a` und `b` haben.
#
# - `print()` kann an beliebigen Stellen im Code verwendet werden, um Variablen 
#   und Ausgaben zu überprüfen.




# _____________________________
#                             /
# 2. Kommentare und Struktur (
# ____________________________\

# Kommentare helfen beim Verständnis und Erklären des Codes. Durch gut platzierte
# Kommentare können wir den Ablauf des Programms festhalten, was das Debugging erleichtert.

def berechne_fakultaet(n):
    if n == 0:
        return 1
    else:
        # Der Wert von n wird durch die Rekursion reduziert
        return n * berechne_fakultaet(n - 1)

# Kommentare geben hier an, dass der Wert von n durch die Rekursion reduziert wird.
# Ein Fehler im Rekursionsfall könnte durch fehlende oder unzureichende Kommentare
# schwieriger zu identifizieren sein.




# ____________________________
#                            /
# 3. Verwenden von assert   (
# ___________________________\

# Mit `assert` kann überprüft werden, ob eine Bedingung wahr ist. Falls sie
# falsch ist, stoppt das Programm mit einer Fehlermeldung. Diese Technik eignet sich
# gut, um Annahmen zu überprüfen und potenzielle Fehlerquellen einzugrenzen.

def teile(x, y):
    assert y != 0, "Division durch Null ist nicht erlaubt!"
    return x / y

# Test
try:
    print(teile(10, 2))  # Gibt 5.0 aus
    print(teile(10, 0))  # Löst AssertionError aus
except AssertionError as e:
    print(e)

# Erläuterung:
# - `assert y != 0` stellt sicher, dass der Nenner nicht null ist.
#
# - Falls doch, wird der Fehler „Division durch Null ist nicht erlaubt!“ angezeigt.




# ____________________________
#                            /
# 4. Verwendung von pdb     (
# ___________________________\

# Das `pdb`-Modul (Python Debugger) bietet einen interaktiven Modus zum Debuggen.
# Man kann damit den Code Schritt für Schritt durchgehen und Variablen überprüfen.

# Beispiel:
import pdb

def multipliziere(x, y):
    pdb.set_trace()  # Startet den Debugger
    return x * y

print(multipliziere(3, 4))

# **Nützliche pdb-Befehle**:
# - `n`: Nächste Zeile ausführen
# - `c`: Weiter zum Ende oder zum nächsten Breakpoint
# - `p variable`: Variable anzeigen
# - `q`: Debugging beenden

# Erläuterung:
# - Mit `pdb.set_trace()` wird der Debugger an dieser Stelle gestartet.
#
# - Dies ist nützlich, wenn wir im Code pausieren und die Werte von 
#   Variablen inspizieren wollen.




# ____________________________
#                            /
# 5. Log-Dateien verwenden  (
# ___________________________\

# Das `logging`-Modul ermöglicht das Erstellen von Log-Dateien. Damit kann man
# Fehler und wichtige Informationen dauerhaft aufzeichnen, was besonders bei
# komplexen Programmen und Anwendungen nützlich ist.

import logging

logging.basicConfig(filename="debug.log", level=logging.DEBUG)

def quadrat(x):
    logging.debug(f"Berechne Quadrat von: {x}")
    return x * x

print(quadrat(3))

# Erläuterung:
# - Mit `logging.debug()` werden Nachrichten im Log gespeichert.
#
# - Das `logging`-Modul bietet auch `info`, `warning`, `error`, und `critical`,
#   um verschiedene Arten von Meldungen festzuhalten. Siehe nächstes Kapitel.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Verwende `print()`-Ausgaben, um Zwischenergebnisse zu prüfen und 
#   Fehlerquellen einzugrenzen.
#
# - Kommentare sind wichtig für das Verständnis und die Struktur des Codes.
#
# - `assert` hilft, Annahmen über Variablen und Werte im Code zu überprüfen.
#
# - Mit `pdb` lässt sich der Code schrittweise debuggen.
#
# - `logging` ist nützlich für umfangreiche Programme und speichert 
#   Informationen in einer Log-Datei.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Schreibe eine Funktion, die zwei Zahlen multipliziert und `assert` verwendet,
# um sicherzustellen, dass die Eingaben positiv sind. Teste die Funktion mit einer
# negativen Zahl und überprüfe die Fehlermeldung.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle ein Programm, das eine Liste mit fünf Zahlen enthält. Verwende `pdb`,
# um den Inhalt der Liste zu inspizieren und jede Zahl um 1 zu erhöhen. Gib die
# Liste vor und nach der Erhöhung aus.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Funktion, die eine Nachricht in einer Log-Datei speichert,
# wenn sie aufgerufen wird. Verwende das `logging`-Modul, um die Nachricht
# „Funktion erfolgreich aufgerufen“ auf Debug-Ebene zu speichern und zeige
# die Log-Datei an, um den Eintrag zu prüfen.


# Füge hier deine Lösung ein.




#         ,_      _,
#           '.__.'
#      '-,   (__)   ,-'
#        '._ .::. _.'
#          _'(^^)'_          Jetzt bis du ein/-e Bug-Jäger/-in
#       _,` `>\/<` `,_
#      `  ,-` )( `-,  `
#         |  /==\  |
#       ,-'  |=-|  '-,
#            )-=(
#   jgs      \__/
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
# Schreibe eine Funktion, die zwei Zahlen multipliziert und `assert` verwendet,
# um sicherzustellen, dass die Eingaben positiv sind. Teste die Funktion mit einer
# negativen Zahl und überprüfe die Fehlermeldung.

'''
def multiply_positive_numbers(a, b):
    assert a > 0 and b > 0, "Beide Eingaben müssen positiv sein."
    return a * b

# Testaufrufe
try:
    print(multiply_positive_numbers(3, 4))  # Erwartet: 12
    print(multiply_positive_numbers(-2, 5))  # Erwartet: AssertionError

except AssertionError as e:
    print(f"Fehler: {e}")

# Wenn die Funktion mit einer negativen Zahl wie -2 aufgerufen wird,
# gibt der `assert`-Befehl die Nachricht „Beide Eingaben müssen positiv sein.“
# und das Programm wird an dieser Stelle abgebrochen.
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle ein Programm, das eine Liste mit fünf Zahlen enthält. Verwende `pdb`,
# um den Inhalt der Liste zu inspizieren und jede Zahl um 1 zu erhöhen. Gib die
# Liste vor und nach der Erhöhung aus.

'''
import pdb

# Liste erstellen
zahlen_liste = [1, 2, 3, 4, 5]
print("Liste vor der Erhöhung:", zahlen_liste)

# Setze einen Breakpoint für den Debugger
pdb.set_trace()

# Erhöhe jede Zahl um 1
for i in range(len(zahlen_liste)):
    zahlen_liste[i] += 1

print("Liste nach der Erhöhung:", zahlen_liste)

# In `pdb`-Modus kann man `zahlen_liste` inspizieren, `n` zum Fortsetzen eingeben
# und das Programm Zeile für Zeile durchlaufen, um Änderungen in der Liste zu überprüfen.
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Funktion, die eine Nachricht in einer Log-Datei speichert,
# wenn sie aufgerufen wird. Verwende das `logging`-Modul, um die Nachricht
# „Funktion erfolgreich aufgerufen“ auf Debug-Ebene zu speichern und zeige
# die Log-Datei an, um den Eintrag zu prüfen.

'''
import logging

# Log-Datei konfigurieren
logging.basicConfig(filename='log_datei.log', level=logging.DEBUG)

def logge_nachricht():
    logging.debug("Funktion erfolgreich aufgerufen")

# Funktionsaufruf
logge_nachricht()

# Nach dem Aufrufen der Funktion logge_nachricht() wird die Nachricht
# „Funktion erfolgreich aufgerufen“ in die Datei `log_datei.log` geschrieben.
# Öffne `log_datei.log`, um die Nachricht zu überprüfen.
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

