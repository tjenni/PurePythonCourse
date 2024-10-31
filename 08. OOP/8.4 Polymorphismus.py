#              _____________________________
#       ______|                             |_____
#       \     |      8.4 POLYMORPHISMUS     |    /
#        )    |_____________________________|   (
#       /________)                      (________\       30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Polymorphismus ist ein Konzept in der Objektorientierten Programmierung (OOP),
# das bedeutet, dass Objekte unterschiedlichster Klassen auf die gleiche Art und
# Weise verwendet werden können. Dies ermöglicht es uns, Methoden auf Objekten
# aufzurufen, ohne genau zu wissen, von welcher Klasse sie stammen.


# ____________________________
#                            /
# Polymorphismus in der OOP (
# ___________________________\

# Polymorphismus ist nützlich, wenn verschiedene Klassen dieselbe Methode haben,
# die jedoch unterschiedlich implementiert ist. Mit Polymorphismus können wir die
# gleiche Methode auf Objekten unterschiedlicher Klassen aufrufen und dabei je
# nach Klasse ein anderes Verhalten erhalten.

# Beispiel: Eine Basisklasse `Animal` mit einer Methode `sound()`. Die abgeleiteten
# Klassen `Hund` und `Katze` erben von `Animal` und überschreiben die Methode `sound()`.
# Obwohl beide Klassen die gleiche Methode verwenden, gibt jede einen anderen Ton aus.

class Tier:
    def sound(self):
        pass  # Diese Methode wird in den Unterklassen überschrieben

class Dog(Tier):
    def sound(self):
        print("Wuff!")

class Cat(Tier):
    def sound(self):
        print("Miau!")

# Testen von Polymorphismus
animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()  # Gibt je nach Objekt "Wuff!" oder "Miau!" aus


# ______________________________
#                              /
# Das Prinzip der Abstraktion (
# _____________________________\

# Durch Polymorphismus können wir allgemeine Codeblöcke schreiben, die für mehrere
# Klassen funktionieren. Eine häufige Anwendung ist das Erstellen einer Methode
# in der Elternklasse, die in den abgeleiteten Klassen unterschiedlich implementiert wird.

# Beispiel: Eine Basisklasse `Vehicle` mit der Methode `accelerate()`.
# Die abgeleiteten Klassen `Car` und `Bike` implementieren die Methode auf ihre
# eigene Weise.

class Vehicle:
    def accelerate(self):
        pass  # Diese Methode wird in den Unterklassen überschrieben

class Car(Fahrzeug):
    def accelerate(self):
        print("Das Auto beschleunigt auf der Strasse.")

class Bike(Fahrzeug):
    def accelerate(self):
        print("Das Fahrrad beschleunigt mit Muskelkraft.")

# Testen von Polymorphismus
vehicles = [Auto(), Fahrrad()]

for vehicle in vehicles:
    vehicle.accelerate()  # Ausgabe je nach Objekt: "Das Auto beschleunigt auf der Strasse." oder "Das Fahrrad beschleunigt mit Muskelkraft."


# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Polymorphismus ermöglicht das Schreiben von Code, der für Objekte
#   unterschiedlicher Klassen funktioniert.
#
# - Durch das Überschreiben von Methoden in den abgeleiteten Klassen können
#   wir für jede Klasse ein spezielles Verhalten festlegen.
#
# - Polymorphismus ist besonders nützlich, wenn mehrere Klassen eine
#   gemeinsame Methode benötigen, die jeweils leicht angepasst ist.



# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine Basisklasse `Instrument` mit einer Methode `play()`, die nichts
# ausgibt. Erstelle zwei abgeleitete Klassen `Guitar` und `Piano`, die jeweils die
# Methode `play()` so implementieren, dass sie entweder „Die Gitarre wird gespielt.“
# oder „Das Klavier wird gespielt.“ ausgibt. Erzeuge ein Objekt von jeder Klasse und
# rufe die Methode `play()` auf.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Basisklasse `Animal` mit der Methode `sound()`. Erstelle abgeleitete
# Klassen `Cow` und `Sheep`, die jeweils „Muuu!“ und „Bäää!“ ausgeben. Schreibe ein
# Programm, das Objekte dieser Klassen in einer Liste speichert und für jedes Tier
# die Methode `sound()` aufruft.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe eine Basisklasse `Sport` mit einer Methode `train()`, die nichts tut.
# Erstelle die abgeleiteten Klassen `Soccer` und `Tennis`, die `train()` so
# überschreiben, dass sie „Trainiere Fussball!“ oder „Trainiere Tennis!“ ausgeben.
# Erstelle Objekte der beiden Klassen und rufe `train()` auf.


# Füge hier deine Lösung ein.




#                    __
#                   / _\ #
#                   \c /  #
#                   / \___ #                Polymorphe Kreaturen
#                   \`----`#==>             erschrecken dich nicht mehr.
#                   |  \  #
#        ,%.-"""---'`--'\#_
#       %%/             |__`\
#      .%'\     |   \   /  //
#      ,%' >   .'----\ |  [/
#         < <<`       ||
#          `\\\       ||
#            )\\      )\
#    ^^^jgs^^"""^^^^^^""^^^^^^^^^^
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
# Erstelle eine Basisklasse `Instrument` mit einer Methode `play()`, die nichts
# ausgibt. Erstelle zwei abgeleitete Klassen `Guitar` und `Piano`, die jeweils die
# Methode `play()` so implementieren, dass sie entweder „Die Gitarre wird gespielt.“
# oder „Das Klavier wird gespielt.“ ausgibt. Erzeuge ein Objekt von jeder Klasse und
# rufe die Methode `play()` auf.

'''
# Basisklasse `Instrument` mit der Methode `play()`
class Instrument:
    def play(self):
        pass  # Methode wird in den abgeleiteten Klassen implementiert

# Abgeleitete Klasse `Guitar` mit eigener Implementierung der Methode `play()`
class Guitar(Instrument):
    def play(self):
        print("Die Gitarre wird gespielt.")

# Abgeleitete Klasse `Piano` mit eigener Implementierung der Methode `play()`
class Piano(Instrument):
    def play(self):
        print("Das Klavier wird gespielt.")

# Objekte der Klassen erstellen und `play()` aufrufen
guitar = Guitar()
piano = Piano()

guitar.play()  # Ausgabe: Die Gitarre wird gespielt.
piano.play()   # Ausgabe: Das Klavier wird gespielt.
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Basisklasse `Animal` mit der Methode `sound()`. Erstelle abgeleitete
# Klassen `Cow` und `Sheep`, die jeweils „Muuu!“ und „Bäää!“ ausgeben. Schreibe ein
# Programm, das Objekte dieser Klassen in einer Liste speichert und für jedes Tier
# die Methode `sound()` aufruft.

'''
# Basisklasse `Animal` mit der Methode `sound()`
class Animal:
    def sound(self):
        pass  # Methode wird in den abgeleiteten Klassen implementiert

# Abgeleitete Klasse `Cow` mit eigener Implementierung der Methode `sound()`
class Cow(Animal):
    def sound(self):
        print("Muuu!")

# Abgeleitete Klasse `Sheep` mit eigener Implementierung der Methode `sound()`
class Sheep(Animal):
    def sound(self):
        print("Bäää!")

# Objekte der Klassen erstellen und in einer Liste speichern
animals = [Cow(), Sheep()]

# `sound()` für jedes Tier in der Liste aufrufen
for animal in animals:
    animal.sound()  # Ausgabe: Muuu! und Bäää!
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe eine Basisklasse `Sport` mit einer Methode `train()`, die nichts tut.
# Erstelle die abgeleiteten Klassen `Soccer` und `Tennis`, die `train()` so
# überschreiben, dass sie „Trainiere Fussball!“ oder „Trainiere Tennis!“ ausgeben.
# Erstelle Objekte der beiden Klassen und rufe `train()` auf.

'''
# Basisklasse `Sport` mit der Methode `train()`
class Sport:
    def train(self):
        pass  # Methode wird in den abgeleiteten Klassen implementiert

# Abgeleitete Klasse `Soccer` mit eigener Implementierung der Methode `train()`
class Soccer(Sport):
    def train(self):
        print("Trainiere Fussball!")

# Abgeleitete Klasse `Tennis` mit eigener Implementierung der Methode `train()`
class Tennis(Sport):
    def train(self):
        print("Trainiere Tennis!")

# Objekte der Klassen erstellen und `train()` aufrufen
soccer = Soccer()
tennis = Tennis()

soccer.train()  # Ausgabe: Trainiere Fussball!
tennis.train()  # Ausgabe: Trainiere Tennis!
'''



# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><



