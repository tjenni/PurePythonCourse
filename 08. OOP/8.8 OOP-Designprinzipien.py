#              _______________________________
#       ______|                               |_____
#       \     |    8.8 OOP-DESIGNPRINZIPIEN   |    /
#        )    |_______________________________|   (
#       /________)                        (________\       30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Objektorientierte Programmierung (OOP) ist nicht nur das Erstellen von Klassen und Objekten,
# sondern folgt auch einer Reihe von Designprinzipien, um den Code flexibel, verständlich und
# wiederverwendbar zu gestalten. Diese Prinzipien sind nützlich für eine klare Struktur und
# ein einfaches Refactoring des Codes.


# ___________________________
#                           /
# SOLID-Prinzipien         (
# __________________________\

# Die SOLID-Prinzipien umfassen fünf grundlegende Regeln für die OOP-Entwicklung:
#
# - **S**: Single Responsibility Principle (SRP)
# - **O**: Open/Closed Principle (OCP)
# - **L**: Liskov Substitution Principle (LSP)
# - **I**: Interface Segregation Principle (ISP)
# - **D**: Dependency Inversion Principle (DIP)




# ____________________________
#                            /
# 1. Single Responsibility  (
# ___________________________\

# Das **Single Responsibility Principle** (SRP) besagt, dass eine Klasse nur eine einzige
# Verantwortung haben soll. Das bedeutet, eine Klasse sollte nur eine bestimmte Aufgabe
# ausführen und keine zusätzlichen Aufgaben übernehmen.

class Report:
    def __init__(self, data):
        self.data = data
    
    def generate(self):
        print("Report generated.")

# Hier ist die Klasse `Report` nur für die Berichterstellung zuständig und sollte nicht
# zusätzlich für das Speichern des Berichts verantwortlich sein.




# ___________________________
#                           /
# 2. Open/Closed Principle  (
# ___________________________\

# Das **Open/Closed Principle** (OCP) besagt, dass Klassen offen für Erweiterungen,
# aber geschlossen für Änderungen sein sollten. Eine Klasse sollte durch Vererbung
# oder Zusammensetzung erweitert werden, ohne den bestehenden Code zu verändern.

class PaymentProcessor:
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}.")

# Hier kann `PaymentProcessor` durch `CreditCardPayment` erweitert werden, ohne die
# `PaymentProcessor`-Klasse selbst zu ändern.




# ____________________________
#                            /
# 3. Liskov Substitution    (
# ___________________________\

# Das **Liskov Substitution Principle** (LSP) besagt, dass Objekte von Unterklassen
# durch Objekte der Basisklasse ersetzt werden können, ohne das Programm zu verändern.
# Das bedeutet, die Unterklasse sollte die Funktionalität der Basisklasse nicht brechen.

class Bird:
    def fly(self):
        print("Flying!")

class Sparrow(Bird):
    pass

# Hier können wir `Sparrow` anstelle von `Bird` verwenden, ohne den Code zu ändern.




# ___________________________
#                           /
# 4. Interface Segregation  (
# ___________________________\

# Das **Interface Segregation Principle** (ISP) besagt, dass eine Klasse nur die
# Methoden implementieren sollte, die sie tatsächlich benötigt. Große Schnittstellen
# sollten in kleinere, spezifischere Schnittstellen aufgeteilt werden.

class Printer:
    def print_document(self):
        pass

class Scanner:
    def scan_document(self):
        pass

# Eine Klasse, die nur druckt, sollte keine Methoden zum Scannen haben und umgekehrt.




# ___________________________
#                           /
# 5. Dependency Inversion   (
# ___________________________\

# Das **Dependency Inversion Principle** (DIP) besagt, dass die Abhängigkeiten
# zwischen den Modulen so gestaltet werden sollten, dass Details von Abstraktionen
# abhängen und nicht umgekehrt.

class Database:
    def connect(self):
        pass

class App:
    def __init__(self, database: Database):
        self.database = database

# Hier hängt die App von der Abstraktion `Database`, wodurch Änderungen am Datenbanktyp
# einfacher zu handhaben sind.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\


# - SRP: Eine Klasse sollte nur eine Aufgabe haben.
#
# - OCP: Klassen sollten erweiterbar, aber nicht modifizierbar sein.
#
# - LSP: Unterklassen sollten sich wie Basisklassen verhalten.
#
# - ISP: Klassen sollten nur die Methoden implementieren, die sie benötigen.
#
# - DIP: Abhängigkeiten sollten auf Abstraktionen basieren.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine Klasse `Employee` mit einem `name`-Attribut und einer Methode `work()`,
# die eine Nachricht ausgibt. Erstelle eine Unterklasse `Manager`, die eine zusätzliche
# Methode `manage_team()` enthält. Verwende Vererbung und das Prinzip der Single
# Responsibility, um die Aufgaben zwischen den beiden Klassen aufzuteilen.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe eine Basisklasse `Notification` mit einer Methode `send()`, die eine Nachricht
# sendet. Erstelle zwei Unterklassen `EmailNotification` und `SMSNotification`, die
# das `send()`-Verhalten für jede Art von Benachrichtigung implementieren. Verwende das
# Open/Closed-Prinzip, um die Funktionalität zu erweitern, ohne die Basisklasse zu ändern.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Basisklasse `Appliance` und zwei abgeleitete Klassen `Washer` und `Dryer`,
# die jeweils eine Methode `operate()` besitzen. Jede Methode sollte eine Nachricht über
# den Betrieb des Geräts ausgeben. Verwende das Liskov Substitution Principle, um sicherzustellen,
# dass die abgeleiteten Klassen die Basisklasse korrekt ersetzen können.


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
# Erstelle eine Klasse `Employee` mit einem `name`-Attribut und einer Methode `work()`,
# die eine Nachricht ausgibt. Erstelle eine Unterklasse `Manager`, die eine zusätzliche
# Methode `manage_team()` enthält. Verwende Vererbung und das Prinzip der Single
# Responsibility, um die Aufgaben zwischen den beiden Klassen aufzuteilen.

'''
class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} arbeitet an den Aufgaben.")

class Manager(Employee):
    def manage_team(self):
        print(f"{self.name} verwaltet das Team.")

# Beispiel: Erstellen eines Managers und eines Mitarbeiters
employee = Employee("Max Mustermann")
manager = Manager("Sarah Schneider")

employee.work()        # Erwartet: "Max Mustermann arbeitet an den Aufgaben."
manager.work()         # Erwartet: "Sarah Schneider arbeitet an den Aufgaben."
manager.manage_team()  # Erwartet: "Sarah Schneider verwaltet das Team."
'''


# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe eine Basisklasse `Notification` mit einer Methode `send()`, die eine Nachricht
# sendet. Erstelle zwei Unterklassen `EmailNotification` und `SMSNotification`, die
# das `send()`-Verhalten für jede Art von Benachrichtigung implementieren. Verwende das
# Open/Closed-Prinzip, um die Funktionalität zu erweitern, ohne die Basisklasse zu ändern.

'''
class Notification:
    def send(self, message):
        raise NotImplementedError("Die send()-Methode muss von der Unterklasse implementiert werden")

class EmailNotification(Notification):
    def send(self, message):
        print(f"Email-Benachrichtigung gesendet: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS-Benachrichtigung gesendet: {message}")

# Beispiel: Senden von Benachrichtigungen
email_notif = EmailNotification()
sms_notif = SMSNotification()

email_notif.send("Willkommen zu unserem Service!")  # Erwartet: "Email-Benachrichtigung gesendet: Willkommen zu unserem Service!"
sms_notif.send("Ihre Bestellung ist unterwegs!")    # Erwartet: "SMS-Benachrichtigung gesendet: Ihre Bestellung ist unterwegs!"
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Basisklasse `Appliance` und zwei abgeleitete Klassen `Washer` und `Dryer`,
# die jeweils eine Methode `operate()` besitzen. Jede Methode sollte eine Nachricht über
# den Betrieb des Geräts ausgeben. Verwende das Liskov Substitution Principle, um sicherzustellen,
# dass die abgeleiteten Klassen die Basisklasse korrekt ersetzen können.

'''
class Appliance:
    def operate(self):
        raise NotImplementedError("Die operate()-Methode muss von der Unterklasse implementiert werden")

class Washer(Appliance):
    def operate(self):
        print("Die Waschmaschine wäscht die Kleidung.")

class Dryer(Appliance):
    def operate(self):
        print("Der Trockner trocknet die Kleidung.")

# Beispiel: Verwendung der Geräte
washer = Washer()
dryer = Dryer()

def start_appliance(appliance):
    appliance.operate()

start_appliance(washer)  # Erwartet: "Die Waschmaschine wäscht die Kleidung."
start_appliance(dryer)   # Erwartet: "Der Trockner trocknet die Kleidung."
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


