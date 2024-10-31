#              __________________________________
#       ______|                                  |_____
#       \     | 4.4 LOKALE UND GLOBALE VARIABLEN |    /
#        )    |__________________________________|   (
#       /________)                           (________\       28.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# In Python gibt es verschiedene Arten von Variablen, die je nach Ort ihrer 
# Definition entweder nur in einer Funktion (lokale Variablen) oder im gesamten 
# Programm (globale Variablen) verfügbar sind. Es ist wichtig zu verstehen, 
# wie der Gültigkeitsbereich von Variablen funktioniert, um Fehler zu vermeiden 
# und den Code übersichtlich zu halten.

# ___________________________
#                           /
# Lokale Variablen         (
# __________________________\

# Lokale Variablen sind Variablen, die innerhalb einer Funktion definiert werden.
# Sie existieren nur innerhalb der Funktion und sind ausserhalb nicht zugänglich.

# Beispiel:
def foo():
    number = 5  # Das ist eine lokale Variable
    print("In der Funktion: Zahl =", number)

foo()

# Die folgende Zeile führt zu einem Fehler, weil `number` ausserhalb der 
# Funktion nicht existiert. 
#
#      NameError: name 'number' is not defined

print(number)

# Am besten kommentiest diese Zeile nun wieder aus.




# ___________________________
#                           /
# Globale Variablen        (
# __________________________\

# Globale Variablen werden ausserhalb einer Funktion definiert und sind im 
# gesamten Programm verfügbar. Sie können von verschiedenen Funktionen 
# genutzt werden.

# Beispiel:
number_global = 10  # Das ist eine globale Variable

def andere_funktion():
    print("In der Funktion: Globale Zahl =", number_global)

andere_funktion()
print("Ausserhalb der Funktion: Globale Zahl =", number_global)




# ___________________________
#                           /
# Globale Variablen ändern (
# __________________________\

# In Funktionen können wir mit dem `global`-Schlüsselwort auf eine globale 
# Variable zugreifen und sie ändern. Ohne das `global`-Schlüsselwort wird eine 
# neue, lokale Variable mit demselben Namen erstellt, und die globale Variable 
# bleibt unverändert.

# Beispiel:
points = 0  # Globale Variable

def increase_points():
    global points
    points += 1  # Erhöht die globale Variable um 1

increase_points()
print("Aktueller Punktestand:", points)




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Lokale Variablen existieren nur innerhalb der Funktion, in der sie 
#   definiert wurden.
#
# - Globale Variablen sind im gesamten Programm verfügbar und können mit dem 
#   `global`-Schlüsselwort in Funktionen geändert werden.
# 
# - Es ist ratsam, globale Variablen sparsam zu verwenden, da sie den Code 
#   schwieriger zu debuggen machen können.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Schreibe eine Funktion namens `write_text`, die eine lokale Variable `text`
# mit dem Inhalt „Hallo Welt!“ erstellt und ausgibt. Überprüfe, ob du die Variable
# `text` ausserhalb der Funktion aufrufen kannst.


# Füge hier deine Lösung ein.



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Definiere eine globale Variable namens `playername` mit dem Inhalt „Gast“.
# Schreibe eine Funktion namens `set_playername`, die den `playername` auf einen
# neuen Wert ändert. Verwende das `global`-Schlüsselwort und rufe die Funktion auf,
# um den neuen `playername` auszugeben.


# Füge hier deine Lösung ein.



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Funktion `calc_sum`, die zwei lokale Variablen `a` und `b`
# enthält, die jeweils Zahlen sind. Die Funktion soll die Summe der beiden Variablen
# berechnen und das Ergebnis zurückgeben. Verwende die Funktion, um eine Berechnung
# durchzuführen, und gib das Ergebnis ausserhalb der Funktion aus.


# Füge hier deine Lösung ein.




#             _____
#         ,-:` \;',`'-, 
#       .'-;_,;  ':-;_,'.
#      /;   '/    ,  _`.-\
#     | '`. (`     /` ` \`|
#     |:.  `\`-.   \_   / |      Globale Variablen gelten überall ;-)
#     |     (   `,  .`\ ;'|
#      \     | .'     `-'/
#       `.   ;/        .'
#     jgs `'-._____.
#  ___ _  _ ___  ___ 
# | __| \| |   \| __|
# | _|| .` | |) | _| 
# |___|_|\_|___/|___|
#                
# -=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=-=x=-





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
# Schreibe eine Funktion namens `write_text`, die eine lokale Variable `text`
# mit dem Inhalt „Hallo Welt!“ erstellt und ausgibt. Überprüfe, ob du die Variable
# `text` ausserhalb der Funktion aufrufen kannst.

'''
def write_text():
    text = "Hallo Welt!"  # Lokale Variable
    print(text)

# Aufruf der Funktion
write_text()
'''


# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Definiere eine globale Variable namens `playername` mit dem Inhalt „Gast“.
# Schreibe eine Funktion namens `set_playername`, die den `playername` auf einen
# neuen Wert ändert. Verwende das `global`-Schlüsselwort und rufe die Funktion auf,
# um den neuen `playername` auszugeben.

'''
playername = "Gast"  # Globale Variable

def set_playername(name):
    global playername
    playername = name  # Ändert die globale Variable

# Aufruf der Funktion und Ausgabe des neuen Spielernamens
set_playername("Alex")
print("Aktueller Spielername:", playername)
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Funktion `calc_sum`, die zwei lokale Variablen `a` und `b`
# enthält, die jeweils Zahlen sind. Die Funktion soll die Summe der beiden Variablen
# berechnen und das Ergebnis zurückgeben. Verwende die Funktion, um eine Berechnung
# durchzuführen, und gib das Ergebnis ausserhalb der Funktion aus.

'''
def calc_sum():
    a = 5  # Lokale Variable
    b = 10  # Lokale Variable
    return a + b  # Gibt die Summe zurück

# Aufruf der Funktion und Ausgabe des Ergebnisses außerhalb der Funktion
result = calc_sum()
print("Die Summe ist:", result)
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><





