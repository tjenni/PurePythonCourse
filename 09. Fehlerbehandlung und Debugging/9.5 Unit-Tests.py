#              ______________________
#       ______|                      |_____
#       \     |    9.5 UNIT-TESTS    |    /
#        )    |______________________|   (
#       /________)               (________\       30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Unit-Tests (Einheitentests) sind eine Möglichkeit, bestimmte Abschnitte
# eines Programms (wie Funktionen oder Methoden) auf korrekte Funktionsweise
# zu überprüfen. Sie sind ein wichtiger Bestandteil der Softwareentwicklung
# und helfen, Fehler frühzeitig zu erkennen.

# In Python wird Unit-Testing oft mit dem `unittest`-Modul durchgeführt, das
# eine strukturierte Methode bietet, um Tests zu schreiben und automatisch
# Ergebnisse zu überprüfen.


# ______________________________
#                              /
# Einfache Tests mit unittest (
# _____________________________\

# Das `unittest`-Modul stellt eine Reihe von Klassen und Methoden zur Verfügung,
# mit denen man Tests erstellen und ausführen kann. Ein Unit-Test prüft, ob
# eine bestimmte Funktion korrekt arbeitet, indem die Ausgabe mit einer
# erwarteten Ausgabe verglichen wird.

# Beispiel einer einfachen Funktion und eines dazugehörigen Tests:

# Funktion, die getestet werden soll
def addiere(a, b):
    return a + b

# Erstelle einen Test für die Funktion
import unittest

class TestMathFunctions(unittest.TestCase):

    def test_addiere(self):
        self.assertEqual(addiere(2, 3), 5)      # Erwartet: 5
        self.assertEqual(addiere(-1, 1), 0)     # Erwartet: 0
        self.assertEqual(addiere(0, 0), 0)      # Erwartet: 0

# Testaufruf
if __name__ == "__main__":
    unittest.main()

# **Erläuterung**:
# - Die `assertEqual()`-Methode vergleicht das Ergebnis der Funktion `addiere()`
#   mit dem erwarteten Ergebnis.
# - Wenn der erwartete Wert nicht dem tatsächlichen Ergebnis entspricht, wird ein Fehler gemeldet.




# ____________________________
#                            /
# Testmethoden im Detail    (
# ___________________________\

# Das `unittest`-Modul stellt verschiedene Methoden zur Verfügung, um
# unterschiedliche Aspekte des Codes zu testen:

# - `assertEqual(a, b)`: Überprüft, ob `a == b` ist.
#
# - `assertNotEqual(a, b)`: Überprüft, ob `a != b` ist.
#
# - `assertTrue(x)`: Überprüft, ob `x` wahr ist.
#
# - `assertFalse(x)`: Überprüft, ob `x` falsch ist.
#
# - `assertIn(a, b)`: Überprüft, ob `a` in `b` enthalten ist.
#
# - `assertIsNone(x)`: Überprüft, ob `x` `None` ist.

# Beispiel:
def ist_gerade(n):
    return n % 2 == 0

class TestMathFunctions(unittest.TestCase):

    def test_ist_gerade(self):
        self.assertTrue(ist_gerade(4))
        self.assertFalse(ist_gerade(3))

# Diese Tests überprüfen, ob die Funktion `ist_gerade()` bei geraden Zahlen
# `True` und bei ungeraden Zahlen `False` zurückgibt.


# ____________________________
#                            /
# Setup und Teardown        (
# ___________________________\

# In komplexeren Testszenarien kann es nützlich sein, Vorbereitungen für
# den Test zu treffen und nach dem Testen aufzuräumen. Dazu gibt es die
# `setUp()`- und `tearDown()`-Methoden in `unittest`.

class TestDatabaseFunctions(unittest.TestCase):

    def setUp(self):
        # Hier könnte eine Datenbankverbindung geöffnet werden
        print("Setup wird ausgeführt")

    def tearDown(self):
        # Hier könnte die Verbindung geschlossen werden
        print("Teardown wird ausgeführt")

    def test_example(self):
        self.assertTrue(True)

# **Erläuterung**:
# - `setUp()` wird vor jedem Test aufgerufen und kann genutzt werden, um z. B.
#   Verbindungen zu öffnen oder Daten vorzubereiten.
#
# - `tearDown()` wird nach jedem Test aufgerufen und kann zum Aufräumen genutzt werden.




# ____________________________
#                            /
# Testen von Ausnahmen      (
# ___________________________\

# Manchmal möchten wir testen, ob bestimmte Ausnahmen ausgelöst werden.
# Dazu wird `assertRaises()` verwendet.

# Beispiel einer Funktion, die eine Ausnahme auslöst:
def teile(a, b):
    if b == 0:
        raise ValueError("Division durch null ist nicht erlaubt")
    return a / b

# Test für die Ausnahme
class TestMathFunctions(unittest.TestCase):

    def test_teile(self):
        self.assertRaises(ValueError, teile, 10, 0)

# **Erläuterung**:
# - `assertRaises()` prüft, ob die Funktion `teile()` bei einer Division durch
#   null die erwartete Ausnahme `ValueError` auslöst.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Verwende `unittest`, um Funktionen und Methoden in isolierten Tests zu
#   überprüfen.
#
# - `assert`-Methoden vergleichen die tatsächliche mit der erwarteten Ausgabe.
#
# - `setUp()` und `tearDown()` helfen, Tests vorzubereiten und aufzuräumen.
#
# - `assertRaises()` überprüft, ob eine bestimmte Ausnahme ausgelöst wird.





# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Schreibe eine Funktion `multipliziere(a, b)`, die zwei Zahlen multipliziert.
# Erstelle einen Unit-Test, um die Funktion auf verschiedene Eingaben zu testen,
# und überprüfe, ob sie die erwarteten Ergebnisse liefert.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle eine Funktion `get_alter(jahr)`, die das Alter einer Person
# berechnet. Verwende Unit-Tests, um die Funktion zu überprüfen und zu
# bestätigen, dass sie das richtige Alter berechnet.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe eine Funktion `calc_sqrt(x)`, die die Quadratwurzel berechnet.
# Erstelle Unit-Tests, um die Funktion zu testen, und überprüfe, ob eine
# ValueError-Ausnahme ausgelöst wird, wenn x negativ ist.


# Füge hier deine Lösung ein.




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
# Schreibe eine Funktion `multipliziere(a, b)`, die zwei Zahlen multipliziert.
# Erstelle einen Unit-Test, um die Funktion auf verschiedene Eingaben zu testen,
# und überprüfe, ob sie die erwarteten Ergebnisse liefert.

'''
# Funktion
def multipliziere(a, b):
    return a * b

# Unit-Test
import unittest

class TestMultipliziere(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multipliziere(5, 3), 15)
    
    def test_negative_numbers(self):
        self.assertEqual(multipliziere(-2, 3), -6)
    
    def test_zero(self):
        self.assertEqual(multipliziere(0, 10), 0)
        self.assertEqual(multipliziere(5, 0), 0)

if __name__ == "__main__":
    unittest.main()
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle eine Funktion `get_alter(jahr)`, die das Alter einer Person
# berechnet. Verwende Unit-Tests, um die Funktion zu überprüfen und zu
# bestätigen, dass sie das richtige Alter berechnet.

'''
from datetime import datetime

# Funktion
def get_alter(jahr):
    aktuelles_jahr = datetime.now().year
    return aktuelles_jahr - jahr

# Unit-Test
import unittest

class TestGetAlter(unittest.TestCase):
    def test_alter_berechnung(self):
        aktuelles_jahr = datetime.now().year
        self.assertEqual(get_alter(aktuelles_jahr - 20), 20)
        self.assertEqual(get_alter(aktuelles_jahr - 50), 50)
    
    def test_zukunft(self):
        aktuelles_jahr = datetime.now().year
        self.assertEqual(get_alter(aktuelles_jahr + 1), -1)

if __name__ == "__main__":
    unittest.main()
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe eine Funktion `calc_sqrt(x)`, die die Quadratwurzel berechnet.
# Erstelle Unit-Tests, um die Funktion zu testen, und überprüfe, ob eine
# ValueError-Ausnahme ausgelöst wird, wenn x negativ ist.

'''
import math

# Funktion
def calc_sqrt(x):
    if x < 0:
        raise ValueError("x darf nicht negativ sein")
    return math.sqrt(x)

# Unit-Test
import unittest

class TestCalcSqrt(unittest.TestCase):
    def test_positive_number(self):
        self.assertAlmostEqual(calc_sqrt(25), 5)
        self.assertAlmostEqual(calc_sqrt(9), 3)
    
    def test_zero(self):
        self.assertEqual(calc_sqrt(0), 0)
    
    def test_negative_number(self):
        with self.assertRaises(ValueError):
            calc_sqrt(-1)

if __name__ == "__main__":
    unittest.main()
'''



# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

