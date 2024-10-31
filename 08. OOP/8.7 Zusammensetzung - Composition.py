#              ______________________________________
#       ______|                                      |_____
#       \     |  8.7 ZUSAMMENSETZUNG (COMPOSITION)   |    /
#        )    |______________________________________|   (
#       /________)                               (________\       30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Die Zusammensetzung (oder "Composition") ist ein Konzept in der objektorientierten
# Programmierung, das es ermöglicht, Objekte in anderen Objekten zu verwenden, um komplexere
# Strukturen zu schaffen. Anstatt zu vererben, erstellen wir eine Beziehung zwischen Klassen,
# indem wir eine Klasse als Attribut in einer anderen Klasse verwenden.

# Zusammensetzung wird oft als "hat-eine"-Beziehung beschrieben:
# - Ein Auto *hat* einen Motor.
#
# - Ein Computer *hat* eine Festplatte.

# Dies unterscheidet sich von der Vererbung ("ist-eine"-Beziehung), da eine Klasse
# hier keine Unterklasse einer anderen ist, sondern mit einer anderen Klasse zusammenarbeitet.


# ____________________________
#                            /
# Einfache Zusammensetzung  (
# ___________________________\

# Beispiel: Eine Klasse `Engine` und eine Klasse `Car`. Anstatt dass `Car` von `Engine`
# erbt, hat `Car` ein Attribut `engine`, das eine Instanz der Klasse `Engine` ist.

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        print("Engine is starting...")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # `engine` ist eine Instanz der Klasse Engine

    def drive(self):
        print(f"The {self.brand} is driving.")
        self.engine.start()  # Methode der Engine-Klasse wird aufgerufen

# Beispiel:
engine = Engine(150)
car = Car("Toyota", engine)
car.drive()  
# Ausgabe:
# The Toyota is driving.
# Engine is starting.




# ___________________________
#                           /
# Zusammengesetzte Klassen  (
# ___________________________\

# Mit Zusammensetzung können wir komplexere Strukturen bauen, indem wir Objekte
# mehrerer Klassen kombinieren. Hier ist ein Beispiel für eine Klasse `House`,
# die mehrere Zimmer hat.

class Room:
    def __init__(self, name):
        self.name = name

    def describe(self):
        print(f"This is the {self.name}.")

class House:
    def __init__(self, address):
        self.address = address
        self.rooms = []  # Liste, um mehrere Room-Objekte zu speichern

    def add_room(self, room):
        self.rooms.append(room)

    def describe(self):
        print(f"House located at {self.address} has the following rooms:")
        for room in self.rooms:
            room.describe()

# Beispiel:
living_room = Room("Living Room")
kitchen = Room("Kitchen")
house = House("123 Maple Street")
house.add_room(living_room)
house.add_room(kitchen)
house.describe()
# Ausgabe:
# House located at 123 Maple Street has the following rooms:
# This is the Living Room.
# This is the Kitchen.


# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Zusammensetzung (Composition) ermöglicht die Kombination von Objekten,
#   um komplexere Strukturen zu schaffen.
#
# - Anstatt von einer Klasse zu erben, erstellt man eine "hat-eine"-Beziehung.
#
# - Die Verwendung von Zusammensetzung kann flexibler sein als Vererbung und
#   wird oft bevorzugt, wenn eine Klasse auf die Funktionalität einer anderen
#   Klasse zugreifen soll.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine Klasse `Battery` mit einem Attribut `capacity`, das die Kapazität
# der Batterie speichert. Erstelle eine Klasse `Laptop`, die eine Instanz der
# Klasse `Battery` als Attribut hat. Schreibe eine Methode, die die Kapazität der
# Batterie im Laptop ausgibt.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Klasse `Address` mit den Attributen `street` und `city`. Erstelle
# eine Klasse `Person`, die eine Instanz von `Address` als Attribut besitzt.
# Schreibe eine Methode, die den Namen und die vollständige Adresse der Person ausgibt.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Klasse `Screen` mit einem Attribut `size`. Erstelle eine Klasse
# `Smartphone`, die eine Instanz der Klasse `Screen` als Attribut hat. Füge eine
# Methode hinzu, die die Größe des Bildschirms ausgibt.


# Füge hier deine Lösung ein.




#               .------.____
#            .-'       \ ___)
#         .-'         \\\
#      .-'        ___  \\)
#   .-'          /  (\  |)
#            __  \  ( | |              Jetzt weisst du, wie man 
#           /  \  \__'| |              Objekte in anderen Objekten
#          /    \____).-'              verwendet.
#        .'       /   |
#       /     .  /    |
#     .'     / \/     |
#    /      /   \     |
#          /    /    _|_
#          \   /    /\ /\
#           \ /    /__v__\
#            '    |       |
#                 |     .#|
#                 |#.  .##|
#                 |#######|
#                 |#######|
#
#            (  )   (   )  )
#             ) (   )  (  (
#             ( )  (    ) )
#             _____________
#            <_____________> ___
#            |             |/ _ \
#            |               | | |
#            |               |_| |
#         ___|             |\___/
#        /    \___________/    \
#        \_____________________/
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
# Erstelle eine Klasse `Battery` mit einem Attribut `capacity`, das die Kapazität
# der Batterie speichert. Erstelle eine Klasse `Laptop`, die eine Instanz der
# Klasse `Battery` als Attribut hat. Schreibe eine Methode, die die Kapazität der
# Batterie im Laptop ausgibt.

'''
class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

class Laptop:
    def __init__(self, battery):
        self.battery = battery

    def show_battery_capacity(self):
        print(f"Kapazität der Batterie: {self.battery.capacity} mAh")

# Beispiel: Erstellen einer Batterie und eines Laptops
battery = Battery(5000)
laptop = Laptop(battery)
laptop.show_battery_capacity()  # Erwartete Ausgabe: "Kapazität der Batterie: 5000 mAh"
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Klasse `Address` mit den Attributen `street` und `city`. Erstelle
# eine Klasse `Person`, die eine Instanz von `Address` als Attribut besitzt.
# Schreibe eine Methode, die den Namen und die vollständige Adresse der Person ausgibt.

'''
class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def show_person_info(self):
        print(f"Name: {self.name}")
        print(f"Adresse: {self.address.street}, {self.address.city}")

# Beispiel: Erstellen einer Adresse und einer Person
address = Address("Hauptstraße 10", "Musterstadt")
person = Person("Max Mustermann", address)
person.show_person_info()
# Erwartete Ausgabe:
# Name: Max Mustermann
# Adresse: Hauptstraße 10, Musterstadt
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Klasse `Screen` mit einem Attribut `size`. Erstelle eine Klasse
# `Smartphone`, die eine Instanz der Klasse `Screen` als Attribut hat. Füge eine
# Methode hinzu, die die Größe des Bildschirms ausgibt.

'''
class Screen:
    def __init__(self, size):
        self.size = size

class Smartphone:
    def __init__(self, screen):
        self.screen = screen

    def show_screen_size(self):
        print(f"Bildschirmgröße: {self.screen.size} Zoll")

# Beispiel: Erstellen eines Bildschirms und eines Smartphones
screen = Screen(6.5)
smartphone = Smartphone(screen)
smartphone.show_screen_size()  # Erwartete Ausgabe: "Bildschirmgröße: 6.5 Zoll"
'''



# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


