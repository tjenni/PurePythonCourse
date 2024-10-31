#              __________________________
#       ______|                          |_____
#       \     |   9.1 FEHLERBEHANDLUNG   |    /
#        )    |__________________________|   (
#       /________)                   (________\       30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# In der Programmierung können Fehler auftreten, die das Programm zum Absturz
# bringen oder unerwartete Ergebnisse liefern. Um sicherzustellen, dass Programme
# stabil laufen und Fehlermeldungen aussagekräftig sind, gibt es die sogenannte
# Fehlerbehandlung.

# Die häufigsten Fehlerarten in Python:
# - **Syntaxfehler**: Fehler im Codeaufbau, wie fehlende Klammern.
#
# - **Logische Fehler**: Fehler in der Logik, z. B. falsche Berechnungen.
#
# - **Laufzeitfehler**: Fehler, die zur Laufzeit auftreten, wie Division durch null.


# ___________________________
#                           /
# try-except               (
# __________________________\

# Python bietet mit `try-except` ein einfaches Werkzeug zur Fehlerbehandlung.
# Der Code in `try` wird ausgeführt, und falls ein Fehler auftritt, wird der
# `except`-Block ausgeführt. 

# Syntax:
# try:
#     Codeblock, der ausgeführt wird
# except Fehlerart:
#     Codeblock, der bei einem Fehler ausgeführt wird

# Beispiel:
try:
    number = int(input("Gib eine Zahl ein: "))
    result = 10 / number
    print(f"10 geteilt durch {number} ergibt {result}")

except ValueError:
    print("Das war keine Zahl. Bitte eine gültige Zahl eingeben.")

except ZeroDivisionError:
    print("Fehler: Division durch null ist nicht erlaubt.")

# **Erläuterungen**:
# - `try`-Block: Versucht, den Code auszuführen.
#
# - `except ValueError`: Wird ausgeführt, wenn der Benutzer keinen 
#   numerischen Wert eingibt.
#
# - `except ZeroDivisionError`: Wird ausgeführt, wenn die Zahl null ist.




# ______________________________
#                              /
# Allgemeine Fehlerbehandlung (
# _____________________________\

# Man kann einen `except`-Block ohne spezifischen Fehler verwenden, um alle
# Fehlerarten abzufangen.

try:
    value = int(input("Gib einen Wert ein: "))

except:
    print("Ein Fehler ist aufgetreten.")
    
# Hinweis: Allgemeine Fehlerabfangung ist praktisch, aber unspezifisch und
# sollte nur mit Bedacht eingesetzt werden, da sie keinen Hinweis auf die
# Ursache gibt.




# ___________________________
#                           /
# Fehlerarten anzeigen     (
# __________________________\

# Es kann hilfreich sein, die Fehlerart direkt anzuzeigen. Dafür verwendet man
# die Schlüsselwörter `as e`.

try:
    number = int(input("Gib eine Zahl ein: "))
    result = 10 / number

except Exception as e:
    print("Ein Fehler ist aufgetreten:", e)
    
# Hier wird der Fehler direkt in der Konsole angezeigt, was bei der
# Fehlersuche nützlich sein kann.




# ____________________________
#                            /
# Verwendung von else       (
# ___________________________\

# Der `else`-Block wird nur ausgeführt, wenn im `try`-Block kein Fehler
# auftritt. So kann man Code ausführen, der nur bei erfolgreichem Abschluss
# des `try`-Blocks benötigt wird.

try:
    zahl = int(input("Gib eine Zahl ein: "))
    ergebnis = 10 / zahl
except ZeroDivisionError:
    print("Fehler: Division durch null ist nicht erlaubt.")
except ValueError:
    print("Fehler: Bitte gib eine gültige Zahl ein.")
else:
    print(f"10 geteilt durch {zahl} ergibt {ergebnis}")

# Erläuterung:
# Der `else`-Block gibt das Ergebnis der Division nur dann aus, wenn keine
# Fehler aufgetreten sind. Das macht den Code klarer und strukturierter.




# ____________________________
#                            /
# Verwendung von finally    (
# ___________________________\

# Der `finally`-Block wird immer ausgeführt, egal ob im `try`-Block ein Fehler
# aufgetreten ist oder nicht. Dies ist nützlich, um z. B. Ressourcen wie Dateien
# oder Verbindungen zu schliessen.

try:
    file = open("test.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Datei wurde nicht gefunden.")
else:
    print("Datei erfolgreich gelesen.")
finally:
    file.close()
    print("Datei wurde geschlossen.")

# Erläuterung:
# Der `finally`-Block wird ausgeführt, um sicherzustellen, dass die Datei
# geschlossen wird, unabhängig davon, ob ein Fehler aufgetreten ist oder nicht.




# ____________________________
#                            /
# raise und eigene Fehler   (
# ___________________________\

# Mit `raise` kann man eigene Fehler auslösen, um auf ungültige Bedingungen
# hinzuweisen.

def positive_zahl(zahl):
    if number <= 0:
        raise ValueError("Die Zahl muss positiv sein.")

    return number

try:
    print(positive_zahl(-5))

except ValueError as e:
    print(e)

# Mit `raise` kann man benutzerdefinierte Fehlermeldungen und Bedingungen
# festlegen, die für bestimmte Werte oder Eingaben gelten.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - `try`: Enthält den Code, der ausgeführt wird und auf Fehler überprüft wird.
#
# - `except`: Behandelt auftretende Fehler im `try`-Block.
#
# - `else`: Wird nur ausgeführt, wenn kein Fehler im `try`-Block auftritt.
#
# - `finally`: Wird immer ausgeführt und dient häufig zum Schliessen von Dateien
#   oder anderen Aufräumarbeiten.
#
# - `raise` ermöglicht es, eigene Fehler zu definieren und gezielte 
#   Bedingungen abzufangen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Programm, das den Benutzer nach zwei Zahlen fragt und ihre Division berechnet.
# Verwende try-except, um sicherzustellen, dass bei einer Eingabe von null oder bei einer
# falschen Eingabe eine passende Fehlermeldung ausgegeben wird.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe eine Funktion, die ein Alter als Parameter erhält und eine Fehlermeldung
# ausgibt, wenn das Alter kleiner als 0 oder grösser als 120 ist. Verwende try-except,
# um das Alter korrekt zu überprüfen.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Entwickle ein Programm, das versucht, eine Datei „daten.txt“ zu öffnen. Wenn die
# Datei nicht existiert, soll sie erstellt werden und eine Nachricht „Datei wurde erstellt“
# ausgegeben werden. Verwende dazu try-except und einen finally-Block.


# Füge hier deine Lösung ein.




#      ,--.       ,---. 
#      /    '.    /     \ 
#             \  ; 
#              \-| 
#             (o o)      (/ 
#             /'v'     ,-' 
#     ,------/ >< \---'            Jetzt weisst du Bescheid, wie man
#    /)     ;  --  :               mit Fehlern (Bugs) umgehen kann. 
#       ,---| ---- |--. 
#      ;    | ---- |   : 
#     (|  ,-| ---- |-. |) 
#        | /| ---- |\ | 
#        |/ | ---- | \| 
#        \  : ---- ;  | 
#         \  \ -- /  / 
#         ;   \  /  : 
#        /   / \/ \  \ 
#       /)           (\ -hrr-
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
# Erstelle ein Programm, das den Benutzer nach zwei Zahlen fragt und ihre Division berechnet.
# Verwende try-except, um sicherzustellen, dass bei einer Eingabe von null oder bei einer
# falschen Eingabe eine passende Fehlermeldung ausgegeben wird.

'''
try:
    zahl1 = float(input("Gib die erste Zahl ein: "))
    zahl2 = float(input("Gib die zweite Zahl ein: "))
    ergebnis = zahl1 / zahl2
    print(f"Das Ergebnis der Division ist: {ergebnis}")

except ValueError:
    print("Ungültige Eingabe! Bitte nur Zahlen eingeben.")

except ZeroDivisionError:
    print("Fehler: Division durch null ist nicht erlaubt.")
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe eine Funktion, die ein Alter als Parameter erhält und eine Fehlermeldung
# ausgibt, wenn das Alter kleiner als 0 oder grösser als 120 ist. Verwende try-except,
# um das Alter korrekt zu überprüfen.

'''
def check_age(age):
    try:
        if age < 0 or age > 120:
            raise ValueError("Das Alter muss zwischen 0 und 120 liegen.")
        print(f"Das eingegebene Alter ist gültig: {age}")

    except ValueError as e:
        print(e)

# Testaufrufe
check_age(25)  # Gültiges Alter
check_age(-5)  # Ungültiges Alter
check_age(150)  # Ungültiges Alter
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Entwickle ein Programm, das versucht, eine Datei „daten.txt“ zu öffnen. Wenn die
# Datei nicht existiert, soll sie erstellt werden und eine Nachricht „Datei wurde erstellt“
# ausgegeben werden. Verwende dazu try-except und einen finally-Block.

'''
try:
    # Versuche, die Datei "daten.txt" im Lese-Modus zu öffnen
    file = open("daten.txt", "r")
    print("Datei wurde erfolgreich geöffnet.")

except FileNotFoundError:
    # Datei existiert nicht, also im Schreibmodus erstellen
    file = open("daten.txt", "w")
    print("Datei wurde erstellt.")

finally:
    # Datei schliessen, wenn sie geöffnet ist
    file.close()
    print("Datei wurde geschlossen.")
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


