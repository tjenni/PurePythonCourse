#              ___________________________________
#       ______|                                  |_____
#       \     | 4.3 PARAMETER UND STANDARDWERTE  |    /
#        )    |__________________________________|   (
#       /________)                           (________\       28.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Parameter machen Funktionen flexibel, da sie es ermöglichen, dass Werte
# von aussen an eine Funktion übergeben werden. Doch manchmal ist es praktisch,
# wenn eine Funktion auch dann funktioniert, wenn nicht alle Werte übergeben werden.
# In solchen Fällen können Standardwerte für Parameter definiert werden.

# Ein Standardwert wird in der Funktionsdefinition angegeben und verwendet, falls
# beim Aufruf kein Argument übergeben wird. Dies hilft, die Funktion vielseitig
# und anpassungsfähig zu gestalten.

# Die Syntax für Standardwerte sieht so aus:

# def funktionsname(parameter=standardwert):
#     Codeblock (wird ausgeführt, wenn die Funktion aufgerufen wird)


# _______________________________________
#                                       /
# Beispiel: Parameter mit Standardwert (
# ______________________________________\

# Im folgenden Beispiel definieren wir eine Funktion `begruesse`, die eine Begrüssung
# ausgibt. Wenn kein Name übergeben wird, begrüsst sie „Gast“ als Standardwert.

def greet(name="Gast"):
    print(f"Hallo, {name}!")

# Aufruf der Funktion ohne Argument
greet()

# Aufruf der Funktion mit einem Argument
greet("Max")




# _____________________________
#                             /
# Vorteil von Standardwerten (
# ____________________________\

# Standardwerte sind nützlich, wenn ein Parameter nur selten einen anderen Wert
# benötigt oder eine sinnvolle Voreinstellung haben soll. So kann man unnötige
# Angaben beim Funktionsaufruf vermeiden.

# Beispiel: Eine Funktion, die das Doppelte einer Zahl berechnet, aber als
# Standardwert 1 verwendet.

def double(number=1):
    return number * 2

# Aufruf ohne Argumente: der Standardwert 1 wird verwendet
print("Das Doppelte von 1 ist:", double())

# Aufruf mit Argument
print("Das Doppelte von 5 ist:", double(5))




# ___________________________________
#                                   /
# Überschreiben von Standardwerten (
# __________________________________\

# Wenn ein Argument beim Funktionsaufruf übergeben wird, überschreibt es den Standardwert.

# Beispiel: Berechne den Gesamtpreis für ein Ticket, mit optionalem Rabatt.

def ticket_price(age, discount=0):
    base_price = 20  # Grundpreis in Fr. 

    if age < 18 or age > 65:
        discount = 0.5  # 50 % Rabatt für unter 18 und über 65

    price = base_price * (1 - discount)
    return price


# Aufruf mit Standardrabatt für einen Erwachsenen
print("Ticketpreis für 30 Jahre:", ticket_price(30))

# Aufruf mit Altersrabatt für eine Person unter 18
print("Ticketpreis für 15 Jahre:", ticket_price(15))

# Aufruf mit benutzerdefiniertem Rabatt
print("Ticketpreis für 40 Jahre mit 20% Rabatt:", ticket_price(40, 0.2))

# Man kann beim Funktionsaufruf auch den Parameternamen angeben. 
print("Ticketpreis für 40 Jahre mit 30% Rabatt:", ticket_price(40, discount=0.3))



# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# Standardwerte eignen sich gut für Parameter, die nur selten geändert werden,
# oder um bestimmte Voreinstellungen zu treffen, die flexibel überschrieben werden können.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Schreibe eine Funktion `greet`, die den Namen, die Lieblingsfarbe und 
# eine Uhrzeit als Parameter erhält. Standardfarbe ist "blau", 
# Standarduhrzeit ist "Tag".

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe eine Funktion `gaming_time`, die die Anzahl der Stunden und den 
# Wochentag als Parameter erhält.
# Die Standard-Gaming-Zeit ist 2 Stunden, am Wochenende erhöht sich die Zeit um 2 Stunden.

# Füge hier deine Lösung ein.



#                .-.
#               [.-''-.,
#               |  //`~\)
#               (<| 0\0|>_
#               ";\  _"/ \\_ _,
#              __\|'._/_  \ '='-,
#             /\ \    || )_///_\>>        Alladin hat den Flaschen-
#            (  '._ T |\ | _/),-'         geist aufgerufen. 
#             '.   '._.-' /'/ |
#             | '._   _.'`-.._/
#       snd   ,\ / '-' |/
#             [_/\-----j
#        _.--.__[_.--'_\__
#       /         `--'    '---._
#      /  '---.  -'. .'  _.--   '.
#      \_      '--.___ _;.-o     /
#        '.__ ___/______.__8----'
#    
#
#  ___ _  _ ___  ___ 
# | __| \| |   \| __|
# | _|| .` | |) | _| 
# |___|_|\_|___/|___|
#                
# -=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-x=-=x=-=x=-=x=-=x=




# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><
#  _    _   _                                  
# | |  (_)_(_)___ _   _ _ __   __ _  ___ _ __  
# | |   / _ \/ __| | | | '_ \ / _` |/ _ \ '_ \ 
# | |__| (_) \__ \ |_| | | | | (_| |  __/ | | |
# |_____\___/|___/\__,_|_| |_|\__, |\___|_| |_|
#                             |___/            


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Schreibe eine Funktion `greet`, die den Namen, die Lieblingsfarbe und 
# eine Uhrzeit als Parameter erhält. Standardfarbe ist "blau", 
# Standarduhrzeit ist "Tag".

'''
def greet(name, color="blau", time="Tag"):
    if time == "Morgen":
        print(f"Guten Morgen, {name}! Deine Lieblingsfarbe ist {color}.")
    elif time == "Abend":
        print(f"Guten Abend, {name}! Deine Lieblingsfarbe ist {color}.")
    else:
        print(f"Hallo, {name}! Deine Lieblingsfarbe ist {color}.")

# Aufruf mit allen drei Parametern
greet("Anna", "grün", "Abend")

# Aufruf mit nur Name und Uhrzeit (Standardfarbe "blau" wird verwendet)
greet("Tom", uhrzeit="Morgen")
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe eine Funktion `gaming_time`, die die Anzahl der Stunden und den 
# Wochentag als Parameter erhält.
# Die Standard-Gaming-Zeit ist 2 Stunden, am Wochenende erhöht sich die Zeit um 2 Stunden.

'''
def gaming_time(hours=2, weekday="Wochentag"):
    if weekday.lower() == "samstag" or weekday.lower() == "sonntag":
        hours += 2
        
    print(f"Du darfst heute {hours} Stunden gamen.")

# Aufruf mit Anzahl der Stunden und Wochentag "Samstag" (Gaming-Zeit wird um 2 Stunden erhöht)
gaming_time(3, "Samstag")

# Aufruf ohne Angabe der Stunden und Wochentag (Standardzeiten werden verwendet)
gaming_time()
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><



