#              ___________________________________
#       ______|                                   |_____
#       \     |   8.2 KAPSELUNG (ENCAPSULATION)   |    /
#        )    |___________________________________|   (
#       /________)                            (________\       30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Die Kapselung (Encapsulation) ist ein wichtiges Prinzip der
# Objektorientierten Programmierung (OOP). Sie dient dazu, Daten in einer
# Klasse zu verbergen und so zu schützen, dass nur bestimmte Teile des Codes
# auf diese Daten zugreifen können. Dies erhöht die Sicherheit und erleichtert
# die Wartung des Codes.


# ___________________________
#                           /
# Private Attribute        (
# __________________________\

# In Python werden Attribute durch den Unterstrich `_` oder zwei Unterstriche `__`
# als privat gekennzeichnet.
#
# - Ein Unterstrich (`_attribut`) wird verwendet, um darauf hinzuweisen,
#   dass das Attribut oder die Methode als "intern" betrachtet wird.
#
# - Zwei Unterstriche (`__attribut`) machen das Attribut oder die Methode vollständig
#   privat und schwerer zugänglich von außerhalb der Klasse.

# Beispiel: Ein Bankkonto mit privatem Kontostand

class Account:
    def __init__(self, owner, start_balance):
        self.owner = owner
        self.__balance = start_balance  # Privates Attribut
    
    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
            print(f"{amount} wurde eingezahlt. Neuer Kontostand: {self.__balance}")
    
    def __check_balance(self):  # Private Methode
        return self.__balance > 0

account = Account("Max", 100)
account.deposit(50)  # Ausgabe: "50 wurde eingezahlt. Neuer Kontostand: 150"

# Hier sehen wir, dass das Attribut `__balance` privat ist und nur innerhalb der
# Klasse `Account` direkt verwendet wird.




# ___________________________
#                           /
# Getter und Setter        (
# __________________________\

# Um auf private Attribute zuzugreifen und sie zu ändern, verwenden wir sogenannte
# "Getter" und "Setter". Diese Methoden kontrollieren, wie und wann auf ein Attribut
# zugegriffen wird.

# Beispiel: Getter und Setter für das private Attribut `__balance`

class BankAccount:
    def __init__(self, owner, start_balance):
        self.owner = owner
        self.__balance = start_balance  # Privates Attribut
    
    # Getter für das Guthaben
    def get_balance(self):
        return self.__balance
    
    # Setter für das Guthaben
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
            print(f"Neuer Kontostand: {self.__balance}")
        else:
            print("Der Betrag muss positiv sein.")


account = BankAccount("Anna", 200)
print("Aktueller Kontostand:", account.get_balance())  # Ausgabe: "Aktueller Kontostand: 200"
account.set_balance(300)  # Ausgabe: "Neuer Kontostand: 300"




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Verwende einen oder zwei Unterstriche, um Attribute und Methoden privat zu machen.
#
# - Getter und Setter ermöglichen den Zugriff auf private Attribute, ohne dass sie
#   direkt verändert werden können.
#
# - Kapselung hilft, Daten vor unbefugtem Zugriff zu schützen und den Code zu strukturieren.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine Klasse `Person` mit den Attributen `name` und `age`. Mache das
# Attribut `age` privat. Füge einen Getter und Setter für `age` hinzu, wobei
# der Setter sicherstellt, dass das Alter nur auf einen Wert über 0 gesetzt werden kann.
# Erzeuge ein Objekt und teste die Getter- und Setter-Methoden.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Klasse `Product` mit einem privaten Attribut `price`. Füge eine Methode
# hinzu, die den Preis um einen Prozentsatz (z.B. 10%) erhöht. Verwende einen Getter,
# um den aktuellen Preis anzuzeigen, und teste die Methoden, indem du ein Produkt-Objekt
# erstellst und den Preis erhöhst.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe eine Klasse `Temperature` mit einem privaten Attribut `celsius`. Füge einen
# Getter hinzu, der den Temperaturwert in Fahrenheit zurückgibt, und einen Setter,
# der den Temperaturwert in Celsius festlegt. Erstelle ein Temperatur-Objekt und
# teste die Getter- und Setter-Methoden.


# Füge hier deine Lösung ein.




#          ...
#        /`   `\
#       /       \
#      |\~~~~~~~/|        Mit Hilfe der Kapselung, kann man 
#      | \=====/ |        komplexeren Code schreiben und die 
#      | /`...'\ |        Teile separat testen. 
#      |/_______\|ldb
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
# Erstelle eine Klasse `Person` mit den Attributen `name` und `age`. Mache das
# Attribut `age` privat. Füge einen Getter und Setter für `age` hinzu, wobei
# der Setter sicherstellt, dass das Alter nur auf einen Wert über 0 gesetzt werden kann.
# Erzeuge ein Objekt und teste die Getter- und Setter-Methoden.

'''
class Person:
    def __init__(self, name, age):
        self.name = name

        if age > 0:
            self.age = age
        else:
            self.age = 1

    # Getter für `__age`
    def get_age(self):
        return self.__age

    # Setter für `__age`, nur Werte über 0 werden akzeptiert
    def set_age(self, age):
        if alter > 0:
            self.__age = age
        else:
            print("Das Alter muss über 0 sein.")

# Testen der Klasse `Person`
person1 = Person("Max", 25)
print("Aktuelles Alter:", person1.get_age())  # Ausgabe: Aktuelles Alter: 25
person1.set_age(30)
print("Neues Alter:", person1.get_age())      # Ausgabe: Neues Alter: 30
person1.set_age(-5)                           # Ausgabe: Das Alter muss über 0 sein.
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Klasse `Product` mit einem privaten Attribut `price`. Füge eine Methode
# hinzu, die den Preis um einen Prozentsatz (z.B. 10%) erhöht. Verwende einen Getter,
# um den aktuellen Preis anzuzeigen, und teste die Methoden, indem du ein Produkt-Objekt
# erstellst und den Preis erhöhst.

'''
class Product:
    def __init__(self, price):
        self.__price = price  # Privates Attribut `price`

    # Methode zur Preiserhöhung um einen bestimmten Prozentsatz
    def increase_price(self, percentage):
        self.__price *= (1 + percentage / 100)
        print(f"Neuer Preis: {self.__price:.2f}")

    # Getter für den aktuellen Preis
    def get_price(self):
        return self.__price

# Testen der Klasse `Product`
product1 = Product(50.00)
print("Aktueller Preis:", product1.get_price())  # Ausgabe: Aktueller Preis: 50.0
product1.increase_price(10)                       # Ausgabe: Neuer Preis: 55.0
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe eine Klasse `Temperature` mit einem privaten Attribut `celsius`. Füge einen
# Getter hinzu, der den Temperaturwert in Fahrenheit zurückgibt, und einen Setter,
# der den Temperaturwert in Celsius festlegt. Erstelle ein Temperatur-Objekt und
# teste die Getter- und Setter-Methoden.


'''
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius  # Privates Attribut `celsius`

    # Getter, der die Temperatur in Fahrenheit zurückgibt
    def get_fahrenheit(self):
        return self.__celsius * 9/5 + 32

    # Setter für das Attribut `celsius`
    def set_celsius(self, celsius):
        self.__celsius = celsius

# Testen der Klasse `Temperature`
temp1 = Temperature(25)
print("Temperatur in Fahrenheit:", temp1.get_fahrenheit())  # Ausgabe: Temperatur in Fahrenheit: 77.0
temp1.set_celsius(30)
print("Neue Temperatur in Fahrenheit:", temp1.get_fahrenheit())  # Ausgabe: Neue Temperatur in Fahrenheit: 86.0
'''



# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

