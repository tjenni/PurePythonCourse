#              ______________________________
#       ______|                              |_____
#       \     |         8.3 VERERBUNG        |    /
#        )    |______________________________|   (
#       /________)                       (________\       30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Vererbung ist ein zentrales Konzept der Objektorientierten Programmierung.
# Mit Vererbung können wir eine neue Klasse erstellen, die Eigenschaften und
# Methoden einer bereits existierenden Klasse übernimmt.
# Das reduziert den Code und ermöglicht das Organisieren verwandter Klassen.


# ____________________________
#                            /
# Die Basisklasse           (
# ___________________________\

# Die Basisklasse (oder "Elternklasse") enthält Eigenschaften und Methoden,
# die an eine abgeleitete Klasse (oder "Kindklasse") vererbt werden.

# Beispiel: Wir erstellen eine Basisklasse `Animal`, die allgemeine Eigenschaften
# wie `name` und `age` enthält, sowie eine Methode `info()`, die Informationen
# über das Tier ausgibt.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"{self.name} ist {self.age} Jahre alt.")


# ____________________________
#                            /
# Die abgeleiteten Klassen  (
# ___________________________\

# Eine abgeleitete Klasse (auch "Kindklasse" genannt) erbt die Attribute und Methoden
# der Basisklasse. Sie kann eigene Attribute und Methoden hinzufügen oder Methoden der
# Basisklasse überschreiben.

# Beispiel: Die Klasse `Insect` erbt von `Animal` und hat ein eigenes Attribut `has_wings`.
# Ebenso die Klasse `Mammal`, die ein Attribut `legs` besitzt.

class Insect(Animal):
    def __init__(self, name, age, has_wings):
        super().__init__(name, age)  # Aufruf des Konstruktors der Basisklasse
        self.has_wings = has_wings

    def fly(self):
        if self.has_wings:
            print(f"{self.name} kann fliegen.")
        else:
            print(f"{self.name} kann nicht fliegen.")


class Mammal(Animal):
    def __init__(self, name, age, legs):
        super().__init__(name, age)
        self.legs = legs

    def run(self):
        print(f"{self.name} läuft auf {self.legs} Beinen.")

# Test der Vererbung:
butterfly = Insekten("Schmetterling", 1, has_wings=True)
butterfly.info()         # Ausgabe der Basisklassenmethode
butterfly.fly()      # Ausgabe: "Schmetterling kann fliegen."

elefant = Mammal("Elefant", 15, legs=4)
elefant.info()               # Ausgabe der Basisklassenmethode
elefant.run()             # Ausgabe: "Elefant läuft auf 4 Beinen."




# ___________________________
#                           /
# Methoden überschreiben   (
# __________________________\

# Eine abgeleitete Klasse kann eine Methode der Basisklasse überschreiben.
# Das bedeutet, wir definieren die Methode in der Kindklasse neu.

# Beispiel: Die Klasse `Mammal` überschreibt die Methode `info()` der Basisklasse `Animal`,
# um speziellere Informationen anzuzeigen.

class Säugetiere(Animal):
    def __init__(self, name, age, anzahl_beine):
        super().__init__(name, age)
        self.anzahl_beine = anzahl_beine
    
    # Methode `info` überschreiben
    def info(self):
        print(f"{self.name} ist ein Säugetier, hat {self.anzahl_beine} Beine und ist {self.age} Jahre alt.")

elefant = Mammal("Elefant", 15, 4)
elefant.info()  # Ausgabe: "Elefant ist ein Säugetier, hat 4 Beine und ist 15 Jahre alt."


# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Vererbung ermöglicht die Wiederverwendung von Code und die Strukturierung
#   verwandter Klassen.
#
# - Die Basisklasse enthält allgemeine Eigenschaften und Methoden, die an
#   abgeleitete Klassen weitergegeben werden.
#
# - Mit `super().__init__()` rufen wir den Konstruktor der Basisklasse auf,
#   um Attribute zu erben.
#
# - Methoden der Basisklasse können in der abgeleiteten Klasse überschrieben
#   werden, um spezielles Verhalten zu definieren.


# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine Basisklasse `Animal` mit den Attributen `name` und `age`
# sowie einer Methode `greet()`, die den Namen und das Alter des Lebewesens
# ausgibt. Erstelle eine abgeleitete Klasse `Bird`, die von `Animal` erbt und
# eine zusätzliche Methode `fly()` besitzt, die „Ich fliege!“ ausgibt.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Basisklasse `Vehicle` mit dem Attribut `brand`. Erstelle
# eine abgeleitete Klasse `Motorcycle` mit den zusätzlichen Attributen `type` und
# `velocity`. Schreibe eine Methode `info()`, die alle Details des Motorrads ausgibt.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Klasse `Person` mit dem Attribut `name` und einer Methode `greet()`,
# die „Hallo, ich heiße [name]!“ ausgibt. Erstelle eine abgeleitete Klasse `Teacher`,
# die zusätzlich das Fach speichert und die Methode `greet()` überschreibt, um
# „Hallo, ich heiße [name] und unterrichte [subject].“ auszugeben.


# Füge hier deine Lösung ein.



#    O       o O       o O       o
#    | O   o | | O   o | | O   o |
#    | | O | | | | O | | | | O | |    Wie das mit der Vererbung geht, 
#    | o   O | | o   O | | o   O |    weisst du jetzt.
#    o       O o       O o       O
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
# Erstelle eine Basisklasse `Animal` mit den Attributen `name` und `age`
# sowie einer Methode `greet()`, die den Namen und das Alter des Lebewesens
# ausgibt. Erstelle eine abgeleitete Klasse `Bird`, die von `Animal` erbt und
# eine zusätzliche Methode `fly()` besitzt, die „Ich fliege!“ ausgibt.


'''
# Basisklasse `Animal` mit den Attributen `name` und `age` und einer Methode `greet`
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hallo, ich bin {self.name} und ich bin {self.age} Jahre alt.")

# Abgeleitete Klasse `Bird`, die von `Animal` erbt und eine zusätzliche Methode `fly` hat
class Bird(Animal):
    def fly(self):
        print("Ich fliege!")

# Test der Klassen Animal und Bird
bird = Bird("Spatz", 2)
bird.greet()  # Ausgabe: "Hallo, ich bin Spatz und ich bin 2 Jahre alt."
bird.fly()    # Ausgabe: "Ich fliege!"
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Basisklasse `Vehicle` mit dem Attribut `brand`. Erstelle
# eine abgeleitete Klasse `Motorcycle` mit den zusätzlichen Attributen `type` und
# `velocity`. Schreibe eine Methode `info()`, die alle Details des Motorrads ausgibt.


'''
# Basisklasse `Vehicle` mit dem Attribut `brand`
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

# Abgeleitete Klasse `Motorcycle` mit zusätzlichen Attributen `type` und `velocity` sowie einer Methode `info`
class Motorcycle(Vehicle):
    def __init__(self, brand, type, velocity):
        super().__init__(brand)  # Aufruf des Konstruktors der Basisklasse
        self.type = type
        self.velocity = velocity
    
    def info(self):
        print(f"Motorrad-Marke: {self.brand}, Typ: {self.type}, Geschwindigkeit: {self.velocity} km/h")


# Test der Klassen Vehicle und Motorcycle
motorcycle = Motorcycle("Yamaha", "Sport", 200)
motorcycle.info()  # Ausgabe: "Motorrad-Marke: Yamaha, Typ: Sport, Geschwindigkeit: 200 km/h"
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Klasse `Person` mit dem Attribut `name` und einer Methode `greet()`,
# die „Hallo, ich heiße [name]!“ ausgibt. Erstelle eine abgeleitete Klasse `Teacher`,
# die zusätzlich das Fach speichert und die Methode `greet()` überschreibt, um
# „Hallo, ich heiße [name] und unterrichte [subject].“ auszugeben.


'''
# Basisklasse `Person` mit dem Attribut `name` und der Methode `greet`
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hallo, ich heiße {self.name}!")

# Abgeleitete Klasse `Teacher` mit zusätzlichem Attribut `subject` und einer überschriebenen Methode `greet`
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    
    def greet(self):
        print(f"Hallo, ich heiße {self.name} und unterrichte {self.subject}.")

# Test der Klassen Person und Teacher
teacher = Teacher("Herr Müller", "Mathematik")
teacher.greet()  # Ausgabe: "Hallo, ich heiße Herr Müller und unterrichte Mathematik."
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

