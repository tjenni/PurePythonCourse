#              _______________________________
#       ______|                               |_____
#       \     |  8.9 EIGENE MODULE ERSTELLEN  |    /
#        )    |_______________________________|   (
#       /________)                        (________\       30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# In der objektorientierten Programmierung kann es nützlich sein, jede Klasse
# in einer eigenen Datei zu speichern. Dies ermöglicht eine bessere Organisation
# und Wiederverwendbarkeit des Codes. Wenn Klassen in einzelnen Dateien gespeichert
# sind, können sie einfach importiert und in anderen Projekten verwendet werden.


# _____________________________
#                             /
# Klassen in eigenen Dateien (
# ____________________________\

# Der erste Schritt zur Strukturierung des Codes besteht darin, jede Klasse in eine
# separate Datei zu schreiben. Zum Beispiel könnten wir eine `Car`- und eine `Engine`-
# Klasse in verschiedene Dateien aufteilen und dann in einem Hauptprogramm importieren.

# Beispiel: Erstellen einer Klasse `Car` in einer eigenen Datei

# In der Datei `car.py`
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def drive(self):
        print(f"The {self.brand} is driving.")

# In der Datei `engine.py`
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        print(f"Engine with {self.horsepower} horsepower is starting...")

# In einem Hauptprogramm `main.py` importieren wir die Klassen:
from car import Car
from engine import Engine

# Beispiel zur Verwendung der importierten Klassen:
car = Car("Toyota")
engine = Engine(150)
car.drive()
engine.start()




# ____________________________
#                            /
# Eigene Module erstellen   (
# ___________________________\

# Wenn mehrere Klassen und Funktionen eng miteinander verwandt sind, können sie zu
# einem Modul zusammengefasst werden. Ein Modul in Python ist einfach eine `.py`-Datei,
# die Klassen, Funktionen und Variablen enthält. 

# Zum Beispiel könnten wir die Dateien `car.py` und `engine.py` in einem Ordner
# namens `vehicles` ablegen und diesen Ordner als Modul verwenden. Der Ordner `vehicles`
# benötigt eine Datei `__init__.py`, um als Modul zu funktionieren.




# ____________________________
#                            /
# Erstellen eines Moduls    (
# ___________________________\

# 1. Erstelle einen Ordner `vehicles`.
# 2. Lege die Dateien `car.py` und `engine.py` darin ab.
# 3. Füge eine `__init__.py`-Datei hinzu, um das Modul zu kennzeichnen.

# Der Ordner `vehicles` könnte dann so aussehen:

# vehicles/
# ├── __init__.py
# ├── car.py
# └── engine.py

# Die Datei `__init__.py` kann leer sein oder importierte Klassen enthalten,
# um den Zugriff auf sie zu erleichtern:

# In `__init__.py`:
from .car import Car
from .engine import Engine

# In einem Hauptprogramm `main.py` können wir jetzt das Modul `vehicles` importieren:
from vehicles import Car, Engine

# Beispiel:
car = Car("Honda")
engine = Engine(200)
car.drive()
engine.start()




# ____________________________
#                            /
# Organisation und Wartung  (
# ___________________________\

# Durch das Speichern jeder Klasse in einer eigenen Datei und das Erstellen von
# Modulen wird der Code besser wartbar und wiederverwendbar. Diese Struktur ist
# besonders nützlich in größeren Projekten und ermöglicht das einfache Hinzufügen
# neuer Klassen, ohne den bestehenden Code zu ändern.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Modul namens `shapes`, das eine Klasse `Rectangle` und eine Klasse `Circle`
# enthält. Beide Klassen sollten eine Methode `area()` haben, die die Fläche berechnet.
# Importiere das Modul und erstelle ein Rechteck und einen Kreis, um ihre Flächen
# zu berechnen und auf der Konsole auszugeben.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Modul `library` mit den Klassen `Book` und `Library`. Die Klasse `Book`
# sollte die Attribute `title` und `author` enthalten, und die Klasse `Library` sollte
# Bücher zur Bibliothek hinzufügen und eine Liste aller Bücher anzeigen können.
# Verwende das Modul, um eine kleine Bibliothek mit ein paar Büchern zu erstellen.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Modul `university` mit den Klassen `Student` und `Course`. Die Klasse
# `Student` sollte die Attribute `name` und `id` enthalten, und die Klasse `Course`
# sollte eine Methode `enroll(student)` haben, die einen Studenten in den Kurs
# aufnimmt. Erstelle ein Beispiel, um einen Studenten zu registrieren.


# Füge hier deine Lösung ein.




#                             ,     
#                         ,   |     
#      _,,._              |  0'     
#    ,'     `.__,--.     0'         
#   /   .--.        |           ,,,        Eigene Module sind 
#   | [=========|==|==|=|==|=|==___]       wie selbst komponierte Musik. 
#   \   "--"  __    |           '''         
#    `._   _,'  `--'                
#       ""'     ,   ,0     ,        
#   hjm         |)  |)   ,'|        
#     ____     0'   '   | 0'        
#     |  |             0'           
#    0' 0'
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
# Erstelle ein Modul namens `shapes`, das eine Klasse `Rectangle` und eine Klasse `Circle`
# enthält. Beide Klassen sollten eine Methode `area()` haben, die die Fläche berechnet.
# Importiere das Modul und erstelle ein Rechteck und einen Kreis, um ihre Flächen
# zu berechnen und auf der Konsole auszugeben.


# Datei shapes.py
'''
import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Berechnet die Fläche des Rechtecks."""
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Berechnet die Fläche des Kreises."""
        return math.pi * (self.radius ** 2)
'''


# Datei main.py
'''
from shapes import Rectangle, Circle

# Erstelle ein Rechteck und berechne die Fläche
rect = Rectangle(5, 3)
print(f"Fläche des Rechtecks: {rect.area()}")  # Erwartet: 15

# Erstelle einen Kreis und berechne die Fläche
circle = Circle(4)
print(f"Fläche des Kreises: {circle.area():.2f}")  # Erwartet ungefähr: 50.27
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Modul `library` mit den Klassen `Book` und `Library`. Die Klasse `Book`
# sollte die Attribute `title` und `author` enthalten, und die Klasse `Library` sollte
# Bücher zur Bibliothek hinzufügen und eine Liste aller Bücher anzeigen können.
# Verwende das Modul, um eine kleine Bibliothek mit ein paar Büchern zu erstellen.


# Datei library.py
'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} von {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Fügt ein Buch zur Bibliothek hinzu."""
        self.books.append(book)

    def list_books(self):
        """Gibt eine Liste aller Bücher in der Bibliothek aus."""
        if not self.books:
            print("Die Bibliothek ist leer.")
        else:
            print("Bücher in der Bibliothek:")
            for book in self.books:
                print(book)
'''


# Datei main.py
'''
from library import Book, Library

# Erstelle eine Bibliothek und füge Bücher hinzu
lib = Library()
lib.add_book(Book("Python Programmieren", "Max Mustermann"))
lib.add_book(Book("Datenstrukturen", "Erika Beispiel"))
lib.add_book(Book("Einführung in KI", "Albert Schlau"))

# Zeige alle Bücher in der Bibliothek an
lib.list_books()
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Modul `university` mit den Klassen `Student` und `Course`. Die Klasse
# `Student` sollte die Attribute `name` und `id` enthalten, und die Klasse `Course`
# sollte eine Methode `enroll(student)` haben, die einen Studenten in den Kurs
# aufnimmt. Erstelle ein Beispiel, um einen Studenten zu registrieren.


# Datei university.py
'''
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return f"Student: {self.name}, ID: {self.student_id}"

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def enroll(self, student):
        """Meldet einen Studenten im Kurs an."""
        self.students.append(student)
        print(f"{student.name} wurde für den Kurs {self.course_name} registriert.")

    def list_students(self):
        """Listet alle Studenten im Kurs auf."""
        if not self.students:
            print(f"Keine Studenten im Kurs {self.course_name}.")
        else:
            print(f"Studenten im Kurs {self.course_name}:")
            for student in self.students:
                print(student)
'''


# main.py
'''
from university import Student, Course

# Erstelle einen Kurs und melde einen Studenten an
course = Course("Informatik")
student1 = Student("Anna Müller", "S1234")
student2 = Student("Max Mustermann", "S5678")

course.enroll(student1)
course.enroll(student2)

# Liste alle Studenten im Kurs auf
course.list_students()
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

