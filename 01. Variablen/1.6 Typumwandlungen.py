#              ________________________
#       ______|                        |_____
#       \     |  1.6 TYPUMWANDLUNGEN   |    /
#        )    |________________________|   (
#       /________)                 (________\       27.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
#  


# In Python können Variablen verschiedene Datentypen haben, z. B. Integer,
# Float oder String. Manchmal ist es notwendig, den Typ einer Variable
# zu ändern, damit Berechnungen oder Ausgaben korrekt funktionieren.
# Dieses Kapitel erklärt, wie man Typumwandlungen in Python durchführt.


# __________________________
#                           /
# Häufige Typumwandlungen  (
# __________________________\

# Hier sind die häufigsten Typumwandlungen in Python:

# String zu Integer:
zahl_str = "25"       # "25" ist ein String
zahl_int = int(zahl_str)   # Mit int() wird der String in eine Zahl umgewandelt
print("String zu Integer:", zahl_int)  # Ausgabe: 25


# String zu Float:
zahl_str = "3.14"
zahl_float = float(zahl_str)  # Mit float() wird der String in eine Dezimalzahl umgewandelt
print("String zu Float:", zahl_float)  # Ausgabe: 3.14


# Integer oder Float zu String:
zahl = 42
zahl_str = str(zahl)  # Mit str() wird die Zahl in einen String umgewandelt
print("Integer zu String:", zahl_str)  # Ausgabe: "42"



# __________________________
#                           /
# Typumwandlungen für      /
# die Benutzereingabe      \
# __________________________\

# Da der Befehl input() immer einen String zurückgibt, ist es oft notwendig,
# die Eingabe direkt in eine Zahl umzuwandeln, wenn man damit rechnen möchte.

# Beispiel: Wir fragen nach einer Zahl und wandeln sie dann in einen Integer um.

eingabe = input("Gib eine Zahl ein: ")
zahl = int(eingabe)  # Umwandlung in Integer
print("Die Zahl + 5 ist:", zahl + 5)

# Hinweis: Wenn der Benutzer einen Text eingibt, der keine Zahl ist,
# gibt Python einen Fehler aus.



# ____________________________
#                             /
# Fehler bei Typumwandlungen (
# ____________________________\

# Versucht man einen Text, der keine Zahl ist, in einen Integer oder Float
# umzuwandeln, führt das zu einem Fehler. Beispiel:

# falsche_eingabe = "Hallo"
# print(int(falsche_eingabe))  # Das führt zu einer Fehlermeldung!

#   ValueError: invalid literal for int()

# Um Fehler zu vermeiden, kann man stattdessen eine Zahleneingabe abfragen
# oder (für Fortgeschrittene) mit Fehlerbehandlung arbeiten.


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Frage den Benutzer nach seinem Geburtsjahr und berechne anhand des
# aktuellen Jahres (z.B. 2023) sein Alter. Verwende dazu int() für die
# Umwandlung der Eingabe.
#
# Beispiel:
# Geburtsjahr: 2000
# Ausgabe: "Du bist 23 Jahre alt."


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Lasse den Benutzer zwei Dezimalzahlen eingeben (z. B. 3.5 und 2.7).
# Berechne die Summe und gib das Ergebnis als Text aus.
#
# Beispiel:
# Zahl 1: 3.5
# Zahl 2: 2.7
# Ausgabe: "Die Summe ist 6.2"


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Frage den Benutzer nach einer Zahl und einem Wort. Verwende die Zahl, um
# das Wort in der entsprechenden Anzahl zu wiederholen. Kombiniere beides
# zu einem Satz.
#
# Beispiel:
# Zahl: 3
# Wort: Katze
# Ausgabe: "KatzenKatzenKatzen"


# Füge hier deine Lösung ein.



# Gratuliere. Du hast die Kunst der Variablenverwandlung gemeistert. 
# Du bist nun ein/-e Variablenmagier/-in.
#                     .
#     
#                        .
#              /^\     .
#         /\   "V"
#        /__\   I      O  o
#       //..\\  I     .
#       \].`[/  I
#       /l\/j\  (]    .  O
#      /. ~~ ,\/I          .
#      \\L__j^\/I       o
#       \/--v}  I     o   .
#       |    |  I   _________
#       |    |  I c(`       ')o
#       |    l  I   \.     ,/
#     _/j  L l\_!  _//^---^\\_    -Row
# 
#  ___ _  _ ___  ___ 
# | __| \| |   \| __|
# | _|| .` | |) | _| 
# |___|_|\_|___/|___|
#                
# -=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x



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

# Frage den Benutzer nach seinem Geburtsjahr und berechne sein Alter.

'''
year = int(input("In welchem Jahr bist du geboren? "))
now = 2023
age = now - year

print(f"Du bist {age} Jahre alt.")
'''

# ___________
#            \
# Aufgabe 2  /
# __________/

# Lasse den Benutzer zwei Dezimalzahlen eingeben und berechne die Summe.

'''
number1 = float(input("Gib die erste Dezimalzahl ein: "))
number2 = float(input("Gib die zweite Dezimalzahl ein: "))
result = number1 + number2

print(f"Die Summe ist {result}")
'''

# ___________
#            \
# Aufgabe 3  /
# __________/

# Frage den Benutzer nach einer Zahl und einem Wort und wiederhole das Wort 
# entsprechend der Zahl.

'''
amount = int(input("Gib eine Zahl ein: "))
word = input("Gib ein Wort ein: ")

result = word * amount
print(f"{result}")
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


