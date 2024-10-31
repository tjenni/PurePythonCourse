#              ______________________________________________
#       ______|                                              |_____
#       \     |  8.6 KLASSENMETHODEN UND STATISCHE METHODEN  |    /
#        )    |______________________________________________|   (
#       /________)                                       (________\       30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# In Python gibt es neben regulären Methoden auch Klassenmethoden und statische
# Methoden. Beide werden oft verwendet, um Funktionen in einer Klasse zu definieren,
# die keinen Zugriff auf das Objekt selbst benötigen.


# ___________________________
#                           /
# Klassenmethoden          (
# __________________________\

# Eine Klassenmethode wird auf der Klasse selbst und nicht auf einem bestimmten
# Objekt der Klasse aufgerufen. Klassenmethoden sind nützlich, wenn wir Informationen
# über die Klasse verarbeiten möchten, anstatt auf die Instanz zuzugreifen.

# Um eine Klassenmethode zu definieren, verwenden wir den Dekorator `@classmethod`.
# Die erste Parameter einer Klassenmethode ist `cls`, das auf die Klasse selbst
# verweist (anstatt wie bei Instanzmethoden `self`, das auf das Objekt verweist).

class Car:
    total_cars = 0  # Klassenattribut, das die Anzahl der Autos zählt

    def __init__(self, brand):
        self.brand = brand
        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

# Beispiel:
car1 = Car("Toyota")
car2 = Car("BMW")
print(Car.get_total_cars())  # Ausgabe: 2, da zwei Autos erstellt wurden

# Hier wird `get_total_cars()` als Klassenmethode aufgerufen, und es wird die
# Gesamtzahl aller erzeugten Autos zurückgegeben.




# ___________________________
#                           /
# Statische Methoden       (
# __________________________\

# Statische Methoden sind unabhängig von einer Instanz oder der Klasse und
# werden für allgemeine Hilfsfunktionen verwendet, die keine Informationen
# über die Klasse oder das Objekt benötigen.

# Statische Methoden verwenden den Dekorator `@staticmethod` und haben keinen
# `self` oder `cls` Parameter.

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

# Beispiel:
print(MathOperations.add(3, 5))        # Ausgabe: 8
print(MathOperations.multiply(4, 7))   # Ausgabe: 28

# Hier werden `add()` und `multiply()` als statische Methoden definiert, die
# unabhängig von Instanzen der Klasse MathOperations verwendet werden können.




# ____________________________
#                            /
# Unterschiede und Einsatz  (
# ___________________________\

# - Instanzmethoden: Zugriff auf Instanzdaten, werden durch `self` aufgerufen.
#
# - Klassenmethoden: Zugriff auf Klassendaten, verwenden `cls`.
#
# - Statische Methoden: Eigenständige Funktionen, die keine Referenz auf die
#   Klasse oder das Objekt benötigen.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Verwende Klassenmethoden, wenn die Funktion mit der Klasse und nicht
#   spezifisch mit Instanzdaten arbeitet.
#
# - Statische Methoden eignen sich für allgemeine Hilfsfunktionen, die keine
#   Informationen über Klasse oder Instanz benötigen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine Klasse `Library` mit einem Klassenattribut `total_books`, das die
# Anzahl der Bücher zählt. Füge eine Klassenmethode `get_total_books()` hinzu, die
# die Anzahl der Bücher zurückgibt. Erzeuge einige `Library`-Objekte und prüfe, ob
# die Gesamtzahl korrekt ist.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Klasse `Calculator` mit zwei statischen Methoden `add(a, b)` und
# `subtract(a, b)`, die die Summe bzw. Differenz der beiden Argumente zurückgeben.
# Rufe die Methoden auf, ohne ein Objekt der Klasse zu erstellen, und gib die
# Ergebnisse aus.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Klasse `Employee` mit einem Klassenattribut `company_name`.
# Füge eine Klassenmethode `set_company_name(cls, name)` hinzu, die den Namen der
# Firma festlegt. Verwende die Klassenmethode, um den Firmennamen festzulegen, und
# prüfe, ob er korrekt gespeichert wurde.


# Füge hier deine Lösung ein.




#             'x|`
#           '|xx| `          '|x|
#   `   '    |xx|    `   '    |x|`        Deine Methoden sind so statisch
#            |xx|             |x|         wie diese Brücke.
#   ============|===============|===--
#   ejm ~~~~~|xx|~~~~~~~~~~~~~|x|~~~ ~~  ~   ~
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
# Erstelle eine Klasse `Library` mit einem Klassenattribut `total_books`, das die
# Anzahl der Bücher zählt. Füge eine Klassenmethode `get_total_books()` hinzu, die
# die Anzahl der Bücher zurückgibt. Erzeuge einige `Library`-Objekte und prüfe, ob
# die Gesamtzahl korrekt ist.

'''
class Library:
    total_books = 0  # Klassenattribut zur Buchanzahl

    def __init__(self):
        # Erhöht die Gesamtzahl der Bücher bei jeder Objekterstellung
        Library.total_books += 1

    @classmethod
    def get_total_books(cls):
        """Gibt die Gesamtzahl der Bücher zurück."""
        return cls.total_books

# Erzeugen einiger Library-Objekte
library1 = Library()
library2 = Library()
library3 = Library()

# Gesamtzahl der Bücher ausgeben
print("Gesamtzahl der Bücher:", Library.get_total_books())  # Erwartet: 3
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Klasse `Calculator` mit zwei statischen Methoden `add(a, b)` und
# `subtract(a, b)`, die die Summe bzw. Differenz der beiden Argumente zurückgeben.
# Rufe die Methoden auf, ohne ein Objekt der Klasse zu erstellen, und gib die
# Ergebnisse aus.

'''
class Calculator:
    @staticmethod
    def add(a, b):
        """Gibt die Summe der beiden Argumente zurück."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Gibt die Differenz der beiden Argumente zurück."""
        return a - b

# Methoden ohne ein Objekt der Klasse aufrufen
result_add = Calculator.add(10, 5)
result_subtract = Calculator.subtract(10, 5)

print("Additionsergebnis:", result_add)          # Erwartet: 15
print("Subtraktionsergebnis:", result_subtract)  # Erwartet: 5
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Klasse `Employee` mit einem Klassenattribut `company_name`.
# Füge eine Klassenmethode `set_company_name(cls, name)` hinzu, die den Namen der
# Firma festlegt. Verwende die Klassenmethode, um den Firmennamen festzulegen, und
# prüfe, ob er korrekt gespeichert wurde.

'''
class Employee:
    company_name = "Unbekannt"

    @classmethod
    def set_company_name(cls, name):
        """Setzt den Firmennamen auf den angegebenen Namen."""
        cls.company_name = name

# Firmennamen mit Klassenmethode festlegen
Employee.set_company_name("Tech Solutions")

# Überprüfen, ob der Firmenname korrekt gespeichert wurde
print("Firmenname der Mitarbeiter:", Employee.company_name)  # Erwartet: "Tech Solutions"
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


