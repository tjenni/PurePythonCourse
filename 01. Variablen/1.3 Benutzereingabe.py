#              ________________________
#       ______|                        |_____
#       \     |  1.3 BENUTZEREINGABEN  |    /
#        )    |________________________|   (
#       /________)                 (________\       27.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
#  


# Programme können nicht nur Informationen anzeigen, sondern auch
# vom Benutzer Eingaben erhalten. In Python verwenden wir dafür
# den `input()`-Befehl.

# Wenn du `input()` aufrufst, stoppt das Programm und wartet, bis der Benutzer
# etwas eingibt und die Eingabetaste drückt. Die Eingabe wird als Text (String)
# gespeichert und kann weiterverwendet werden. Hier ein Beispiel:

name = input("Wie heißt du? ")
print("Hallo", name)

# Wenn der Benutzer "Anna" eingibt, lautet die Ausgabe: Hallo Anna



# ______________________
#                      /
# Eine Zahl eingeben  (
# _____________________\
#

# Der `input()`-Befehl gibt immer einen String zurück. Möchtest du mit
# der Eingabe rechnen, musst du diesen in eine Zahl umwandeln.
# Hierfür verwenden wir `int()` für ganze Zahlen (Integer) und `float()`
# für Dezimalzahlen (Float).

# Beispiel: Frage den Benutzer nach seinem Alter und berechne, wie alt
# er in fünf Jahren sein wird.


age = input("Wie alt bist du? ")
age = int(age)  # Umwandeln der Eingabe in eine ganze Zahl (Integer)

print("In 5 Jahren wirst du", age + 5, "Jahre alt sein.")


# Wichtig: Wenn du versuchst, einen Text einzugeben, der keine Zahl ist
# (wie z. B. "Hallo"), wird das Programm eine Fehlermeldung ausgeben.

#     ValueError: invalid literal for int()



# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
# 
# Schreibe ein Programm, das den Benutzer nach seinem Namen und seinem
# Alter fragt und dann eine Nachricht ausgibt, z. B.:
#
# Hallo Max, du bist 15 Jahre alt.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein kleines Programm, das den Benutzer nach zwei Zahlen fragt.
# Gib die Summe dieser beiden Zahlen auf der Konsole aus.
# 
# Beispiel:
# Gib eine Zahl ein: 5
# Gib eine weitere Zahl ein: 3
# Ergebnis: 8


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Frage den Benutzer nach seiner Lieblingszahl und berechne das Doppelte
# dieser Zahl. Python hat den Stern * als Malzeichen. Gib das Ergebnis
# auf der Konsole aus.
# 
# Beispiel:
# Was ist deine Lieblingszahl? 4
# Das Doppelte deiner Lieblingszahl ist 8.


# Füge hier deine Lösung ein.


#
# Perfekt. Du kannst nun Benutzereingaben entgegennehmen und
# in Variablen abspeichern. 
#
#    o  \ o / _ o       __|   \ /    |__      o _ \ o /  o
#   /|\   |    /\  ___\o  \o   |   o/   o/__  /\    |   /|\
#   / \  / \  | \ /)  |   ( \ /o\ / )   |  (\ / |  / \  / \
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

# Frage den Benutzer nach seinem Namen und Alter und gib eine Nachricht aus.

'''
name = input("Wie heißt du? ")
age = input("Wie alt bist du? ")

print(f"Hallo {name}, du bist {age} Jahre alt.")
'''


# ___________
#            \
# Aufgabe 2  /
# __________/

# Frage den Benutzer nach zwei Zahlen und gib die Summe aus.

'''
number1 = int(input("Gib eine Zahl ein: "))
number2 = int(input("Gib eine weitere Zahl ein: "))

result = number1 + number2
print(f"Ergebnis: {result}")
'''


# ___________
#            \
# Aufgabe 3  /
# __________/

# Frage den Benutzer nach seiner Lieblingszahl und berechne das Doppelte.

'''
number = int(input("Was ist deine Lieblingszahl? "))
double = number * 2

print(f"Das Doppelte deiner Lieblingszahl ist {double}.")
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

