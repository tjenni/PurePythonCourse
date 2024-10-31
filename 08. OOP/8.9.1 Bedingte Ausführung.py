#              ________________________________
#       ______|                                |_____
#       \     |  8.9.1 Bedingte Ausführung     |    /
#        )    |________________________________|   (
#       /________)                         (________\       30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# In Python gibt es eine spezielle Anweisung, die es ermöglicht, ein Skript 
# sowohl als eigenständiges Programm als auch als wiederverwendbares Modul zu 
# verwenden. Diese Technik hilft, flexiblen und modularen Code zu schreiben, 
# der entweder direkt ausgeführt oder in andere Programme importiert werden kann.

# Die Anweisung lautet:

if __name__ == "__main__":

# Diese Zeile ist eine Standardmethode in Python, um den Hauptteil eines Skripts 
# nur dann auszuführen, wenn das Skript direkt ausgeführt wird, und nicht, wenn 
# es als Modul importiert wird.


# _______________________________
#                               /
# Funktionsweise von __name__  (
# ______________________________\

# In jedem Python-Skript gibt es eine spezielle Variable namens `__name__`, die 
# den Namen des Moduls speichert. Wenn das Skript jedoch direkt ausgeführt wird, 
# erhält `__name__` automatisch den Wert `"__main__"`. Das bedeutet:

# - Wird eine Datei **direkt ausgeführt** (`python mein_script.py`), ist 
#   `__name__` gleich `"__main__"`.
#
# - Wird eine Datei **importiert**, hat `__name__` den Namen des Moduls 
#   (z. B. `mein_script`), aber nicht `"__main__"`.


# Beispiel:

def sag_hallo():
    print("Hallo aus dem Modul!")

if __name__ == "__main__":
    print("Das Skript wird direkt ausgeführt.")
    sag_hallo()


# In diesem Beispiel wird die Funktion `sag_hallo()` nur dann ausgeführt, wenn 
# das Skript direkt ausgeführt wird. Wenn wir jedoch das Skript `mein_script.py` 
# in ein anderes Python-Skript importieren, bleibt der `if`-Block unberührt und 
# wird nicht ausgeführt.


# ___________________________________
#                                   /
# Warum diese Technik nützlich ist (
# __________________________________\

# Diese Konstruktion bietet mehrere Vorteile:
# - Flexibilität Ein Skript kann als eigenständiges Programm oder als Modul 
#   für andere Programme verwendet werden.
# 
# - Wiederverwendbarkeit Funktionen und Klassen im Skript sind für andere Skripte 
#   zugänglich, ohne dass der Hauptteil des Codes ausgeführt wird.
#
# - Struktur und Lesbarkeit: Das erleichtert das Testen und macht den 
#   Code modularer.




# _________________________________
#                                 /
# Beispiel: Modul für Mathematik (
# ________________________________\

# Angenommen, wir haben ein Modul namens `mathe_modul.py`, das einige einfache 
# mathematische Funktionen enthält:

def addiere(a, b):
    return a + b

def subtrahiere(a, b):
    return a - b

# Hier prüfen wir, ob das Modul direkt ausgeführt wird
if __name__ == "__main__":
    print("Direkte Ausführung von mathe_modul.py")
    ergebnis = addiere(5, 3)
    print(f"Ergebnis der Addition: {ergebnis}")

# - Wenn wir `mathe_modul.py` direkt ausführen: Der `if`-Block wird ausgeführt 
#   und gibt die Addition aus.

# - Wenn wir `mathe_modul.py` importieren: Nur die Funktionen `addiere()` 
#   und `subtrahiere()` sind verfügbar; der `if`-Block wird nicht ausgeführt.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - `if __name__ == "__main__":` überprüft, ob ein Skript direkt ausgeführt wird.
#
# - Diese Methode macht ein Skript sowohl als ausführbares Programm als auch als 
#   Modul nutzbar.
#
# - Funktionen und Klassen im Skript bleiben beim Import zugänglich, ohne dass 
#   der Hauptteil des Skripts ausgeführt wird.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Python-Skript `greeting.py` mit einer Funktion `greet(name)`, 
# die den Namen auf der Konsole ausgibt. Füge einen `if __name__ == "__main__":`-Block 
# hinzu, der die Funktion `greet()` nur aufruft, wenn das Skript direkt 
# ausgeführt wird.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe ein Modul `math_calculator.py` mit den Funktionen `add(a, b)` und `
# multiply(a, b)`. Erstelle einen `if __name__ == "__main__":`-Block, in dem 
# du einige Testrechnungen machst und die Ergebnisse ausgibst. Teste das Modul, 
# indem du es sowohl ausführst als auch in ein anderes Skript importierst.


# Füge hier deine Lösung ein.



#                           .-.
#            .-""`""-.    |(@ @)      Jetzt kommt dir `if __name__ == "__main__":`
#         _/`oOoOoOoOo`\_ \ \-/       nicht mehr fremd vor. 
#        '.-=-=-=-=-=-=-.' \/ \
#    jgs   `-=.=-.-=.=-'    \ /\
#             ^  ^  ^       _H_ \
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
# Erstelle ein Python-Skript `greeting.py` mit einer Funktion `greet(name)`, 
# die den Namen auf der Konsole ausgibt. Füge einen `if __name__ == "__main__":`-Block 
# hinzu, der die Funktion `greet()` nur aufruft, wenn das Skript direkt ausgeführt wird.

# greeting.py

'''
def greet(name):
    """Gibt eine Begrüßung mit dem Namen aus."""
    print(f"Hallo, {name}!")

# Überprüfen, ob das Skript direkt ausgeführt wird
if __name__ == "__main__":
    greet("Max")
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe ein Modul `math_calculator.py` mit den Funktionen `add(a, b)` und `multiply(a, b)`. 
# Erstelle einen `if __name__ == "__main__":`-Block, in dem du einige Testrechnungen 
# machst und die Ergebnisse ausgibst. Teste das Modul, indem du es sowohl ausführst 
# als auch in ein anderes Skript importierst.


# math_calculator.py

'''
def add(a, b):
    """Addiert zwei Zahlen und gibt das Ergebnis zurück."""
    return a + b

def multiply(a, b):
    """Multipliziert zwei Zahlen und gibt das Ergebnis zurück."""
    return a * b

# Überprüfen, ob das Skript direkt ausgeführt wird
if __name__ == "__main__":
    # Testfälle
    result_add = add(5, 7)
    result_multiply = multiply(3, 4)
    
    print("Ergebnis der Addition:", result_add)        # Erwartet: 12
    print("Ergebnis der Multiplikation:", result_multiply)  # Erwartet: 12
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

