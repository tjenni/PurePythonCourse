#              ______________________________
#       ______|                              |_____
#       \     |  8.5 MAGISCHE METHODEN UND   |    /
#        \    |    OPERATORÜBERLADUNG        |   /
#        /    |______________________________|   \
#       /________)                       (________\       30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Magische Methoden (oder "dunder methods" für "double underscore") sind spezielle
# Methoden in Python, die durch doppelten Unterstrich beginnen und enden, wie z. B.
# `__init__()`, `__str__()`, `__len__()` und viele mehr. Sie ermöglichen uns, die
# Standardfunktionen und Operatoren in Python für eigene Klassen anzupassen.


# ___________________________
#                           /
# Die `__init__()` Methode  (
# ___________________________\

# Die `__init__()`-Methode ist eine der bekanntesten magischen Methoden. Sie
# wird beim Erstellen eines neuen Objekts automatisch aufgerufen und dient
# zur Initialisierung von Attributen.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Beispiel:
book1 = Book("1984", "George Orwell")
print(book1.title)  # Ausgabe: 1984




# ___________________________
#                           /
# Die `__str__()` Methode   (
# ___________________________\

# Die `__str__()`-Methode definiert, wie ein Objekt als Zeichenkette dargestellt wird.
# Sie wird z. B. bei `print()` verwendet und gibt eine benutzerfreundliche Darstellung
# des Objekts zurück.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' von {self.author}"

# Beispiel:
book2 = Book("1984", "George Orwell")
print(book2)  # Ausgabe: '1984' von George Orwell




# ___________________________
#                           /
# Operatoren überladen      (
# ___________________________\

# Magische Methoden ermöglichen es uns, Operatoren wie `+`, `-`, `*`, etc. für
# eigene Klassen zu überladen. Die Methode `__add__()` wird z. B. für den `+`-Operator
# verwendet.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Operatorüberladung für den `+`-Operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Darstellung für `print()` definieren
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Beispiel:
v1 = Vector(2, 3)
v2 = Vector(1, 4)
result = v1 + v2
print(result)  # Ausgabe: Vector(3, 7)




# ___________________________
#                           /
# Weitere magische Methoden (
# ___________________________\

# Es gibt viele weitere magische Methoden, die wir überladen können, um bestimmte
# Funktionalitäten anzupassen:
#
# - `__len__()`: Ermöglicht die Nutzung von `len()` auf einem Objekt.
#
# - `__getitem__()`: Macht ein Objekt indexierbar wie eine Liste.
#
# - `__eq__()`: Überlädt den `==`-Operator zum Vergleichen von Objekten.
#
# Beispiel für `__eq__()`:

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

# Beispiel:
book3 = Book("1984", "George Orwell")
book4 = Book("1984", "George Orwell")
print(book3 == book4)  # Ausgabe: True, da Titel und Autor übereinstimmen.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\


# - Magische Methoden beginnen und enden mit zwei Unterstrichen.
#
# - Mit magischen Methoden können wir die Standardfunktionen und Operatoren
#   für unsere eigenen Klassen anpassen.
#
# - `__init__()` und `__str__()` sind zwei der am häufigsten verwendeten
#   magischen Methoden.
#
# - Die Überladung von Operatoren ermöglicht es uns, mathematische Operationen
#   oder Vergleiche mit benutzerdefinierten Objekten durchzuführen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine Klasse `Person` mit den Attributen `name` und `age`. Implementiere
# die Methode `__str__()`, die eine benutzerfreundliche Darstellung der Person
# in folgendem Format zurückgibt: „Person [name], Alter: [age]“.
# Erzeuge ein Objekt der Klasse und verwende `print()` darauf.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Klasse `Fraction`, die die Attribute `numerator` und `denominator` hat.
# Überlade den `+`-Operator (`__add__()`), sodass zwei Brüche addiert werden können,
# und der neue Bruch zurückgegeben wird. Erstelle zwei Bruch-Objekte und addiere sie.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Klasse `Account` mit den Attributen `balance`. Überlade den
# `==`-Operator (`__eq__()`), um zwei Bankkonten als gleich zu betrachten, wenn
# sie denselben Kontostand haben. Erstelle zwei Bankkonto-Objekte und vergleiche sie.


# Füge hier deine Lösung ein.



#                 .-----.
#       \ ' /   _/    )/
#      - ( ) -('---''--)
#       / . \((()\^_^/)()          Du bist jetzt ein magischer
#        \\_\ (()_)-((()()         Methoden-Elf.
#         '- \ )/\._./(()
#           '/\/( X   ) \
#           (___)|___/ ) \
#                |.#_|(___)
#               /\    \ ( (_
#               \/\/\/\) \\
#               | / \ |
#               |(   \|
#              _|_)__|_\_
#              )...()...(
#               | (   \ |     
#            .-'__,)  (  \
#        mrf           '\_-,
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
# Erstelle eine Klasse `Person` mit den Attributen `name` und `age`. Implementiere
# die Methode `__str__()`, die eine benutzerfreundliche Darstellung der Person
# in folgendem Format zurückgibt: „Person [name], Alter: [age]“.
# Erzeuge ein Objekt der Klasse und verwende `print()` darauf.

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person [{self.name}], Alter: {self.age}"

# Objekt erstellen und ausgeben
person = Person("Max Mustermann", 30)
print(person)  # Erwartet: "Person [Max Mustermann], Alter: 30"
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Klasse `Fraction`, die die Attribute `numerator` und `denominator` hat.
# Überlade den `+`-Operator (`__add__()`), sodass zwei Brüche addiert werden können,
# und der neue Bruch zurückgegeben wird. Erstelle zwei Bruch-Objekte und addiere sie.

'''
from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            new_denominator = self.denominator * other.denominator
            common_divisor = gcd(new_numerator, new_denominator)
            return Fraction(new_numerator // common_divisor, new_denominator // common_divisor)
        return NotImplemented

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

# Bruch-Objekte erstellen und addieren
fraction1 = Fraction(1, 2)
fraction2 = Fraction(1, 3)
result = fraction1 + fraction2
print(result)  # Erwartet: "5/6"
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Klasse `Account` mit den Attributen `balance`. Überlade den
# `==`-Operator (`__eq__()`), um zwei Bankkonten als gleich zu betrachten, wenn
# sie denselben Kontostand haben. Erstelle zwei Bankkonto-Objekte und vergleiche sie.

'''
class Account:
    def __init__(self, balance):
        self.balance = balance

    def __eq__(self, other):
        if isinstance(other, Account):
            return self.balance == other.balance
        return NotImplemented

# Konto-Objekte erstellen und vergleichen
account1 = Account(1000)
account2 = Account(1000)
account3 = Account(500)

print(account1 == account2)  # Erwartet: True
print(account1 == account3)  # Erwartet: False
'''



# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

