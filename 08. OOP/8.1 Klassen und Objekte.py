#              _____________________________
#       ______|                              |_____
#       \     |    8.1 KLASSEN UND OBJEKTE   |    /
#        )    |______________________________|   (
#       /________)                       (________\       30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Die Objektorientierte Programmierung (OOP) ist ein Ansatz in der Programmierung,
# der es uns ermöglicht, Code so zu organisieren, dass er einfacher wiederverwendet,
# erweitert und gewartet werden kann. In der OOP arbeiten wir mit "Objekten" und "Klassen".


# ___________________________
#                           /
# Was ist ein Objekt?      (
# __________________________\

# Ein Objekt ist eine "Instanz" einer Klasse, also eine Art "Ding" oder "Einheit",
# das Daten und Verhalten zusammenfasst.
#
# Beispiele aus der echten Welt:
#
# - Eine Person: Sie hat Eigenschaften (z.B. Name, Alter) und kann Verhalten zeigen
#   (z.B. reden, essen).
#
# - Ein Auto: Es hat Eigenschaften (z.B. Farbe, Marke) und kann bestimmte Dinge tun
#   (z.B. fahren, anhalten).
#
# In Python kann ein Objekt eine Kombination aus "Daten" (Variablen) und 
# "Methoden" (Funktionen) sein.




# ___________________________
#                           /
# Was ist eine Klasse?     (
# __________________________\

# Eine Klasse ist eine Art "Bauplan" oder "Schablone" für ein Objekt. In der OOP
# definieren wir Klassen, um Objekte zu erstellen. Die Klasse beschreibt, welche
# Eigenschaften und Methoden die Objekte haben.

# Schauen wir uns ein Beispiel an, um zu verstehen, wie man eine einfache Klasse erstellt
# und wie man Objekte daraus erzeugt.


# Beispiel: Wir definieren eine Klasse `Person`, welche die Eigenschaften `name`, 
# und `age` und eine Methode `introduce()` hat.

class Person:
    # Initialisierung der Eigenschaften (Konstruktor)
    def __init__(self, name, age):
        self.name = name  # Instanzvariable für den Namen
        self.age = age  # Instanzvariable für das Alter
    
    # Methode, um sich vorzustellen
    def introduce(self):
        print(f"Hallo, ich heiße {self.name} und bin {self.age} Jahre alt.")

# Erstellen eines Objekts der Klasse Person
person1 = Person("Max", 25)
person1.introduce()  # Ausgabe: "Hallo, ich heiße Max und bin 25 Jahre alt."




# ___________________________
#                           /
# Konstruktor              (
# __________________________\

# Die Methode `__init__()` wird als `Konstruktor` bezeichnet und wird immer
# automatisch aufgerufen, wenn ein neues Objekt einer Klasse erstellt wird.
# Mit ihr können wir Eigenschaften (Attribute) festlegen, die jedes Objekt
# beim Erstellen besitzen soll.




# ___________________________
#                           /
# Das Keyword self         (
# __________________________\

# Das `self`-Keyword bezieht sich auf das aktuelle Objekt der Klasse, also auf
# die Instanz, die gerade verwendet wird. In der Methode `__init__()` und anderen
# Methoden verwenden wir `self`, um auf die Attribute und Methoden des Objekts zuzugreifen.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Ein Objekt ist eine Instanz einer Klasse und kombiniert Daten und Verhalten.
#
# - Eine Klasse ist der Bauplan für ein Objekt und legt fest, welche Eigenschaften
#   und Methoden die Objekte haben.
#
# - In Python verwenden wir `__init__` als Konstruktor, um Attribute zu initialisieren,
#   wenn ein Objekt erstellt wird.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine Klasse `Auto` mit den Eigenschaften `brand`, `model` und `year`.
# Füge eine Methode `info()` hinzu, die eine Beschreibung des Autos auf der Konsole ausgibt.
# Erzeuge ein Objekt und rufe die `info()`-Methode auf.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Klasse `Book` mit den Eigenschaften `titel` und `author`. Schreibe eine Methode
# `read()`, die den Text „Lies das Buch [titel] von [autor]!“ ausgibt. Erzeuge ein Buch-Objekt
# und rufe die `read()`-Methode auf.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe eine Klasse `Rectangle` mit den Eigenschaften `width` und `height`.
# Füge eine Methode `area()` hinzu, die die Fläche des Rechtecks berechnet
# und auf der Konsole ausgibt. Erstelle ein Rechteck-Objekt und berechne die Fläche.


# Füge hier deine Lösung ein.




#
#    Dein erster Schritt in die Welt der objektorientierten Programmierung.
#
#                                                             _________________________   
#                        /\\      _____          _____       |   |     |     |    | |  \  
#         ,-----,       /  \\____/__|__\_    ___/__|__\___   |___|_____|_____|____|_|___\ 
#      ,--'---:---`--, /  |  _     |     `| |      |      `| |                    | |    \
#     ==(o)-----(o)==J    `(o)-------(o)=   `(o)------(o)'   `--(o)(o)--------------(o)--'  
#    `````````````````````````````````````````````````````````````````````````````````````
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
# Erstelle eine Klasse `Car` mit den Eigenschaften `brand`, `model` und `year`.
# Füge eine Methode `info()` hinzu, die eine Beschreibung des Autos auf der Konsole ausgibt.
# Erzeuge ein Objekt und rufe die `info()`-Methode auf.

'''
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def info(self):
        print(f"{self.year} {self.brand} {self.model}")

# Erstellen eines Auto-Objekts und Aufrufen der `info`-Methode
car1 = Car("Toyota", "Corolla", 2020)
car1.info()  # Ausgabe: "2020 Toyota Corolla"
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Klasse `Book` mit den Eigenschaften `titel` und `author`. Schreibe eine Methode
# `read()`, die den Text „Lies das Buch [titel] von [autor]!“ ausgibt. Erzeuge ein Buch-Objekt
# und rufe die `read()`-Methode auf.

'''
class Book:
    def __init__(self, titel, author):
        self.titel = titel
        self.author = author
    
    def read(self):
        print(f"Lies das Buch {self.titel} von {self.author}!")

# Erstellen eines Book-Objekts und Aufrufen der `read`-Methode
book1 = Book("1984", "George Orwell")
book1.read()  # Ausgabe: "Lies das Buch 1984 von George Orwell!"
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe eine Klasse `Rectangle` mit den Eigenschaften `width` und `height`.
# Füge eine Methode `area()` hinzu, die die Fläche des Rechtecks berechnet
# und auf der Konsole ausgibt. Erstelle ein Rechteck-Objekt und berechne die Fläche.

'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        flaeche = self.width * self.height
        print(f"Die Fläche des Rechtecks beträgt: {flaeche} Quadrat-Einheiten")

# Erstellen eines Rectangle-Objekts und Berechnung der Fläche
rechteck1 = Rectangle(5, 3)
rechteck1.area()  
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

