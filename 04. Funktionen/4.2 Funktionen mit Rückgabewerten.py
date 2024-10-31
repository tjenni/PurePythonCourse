#              ___________________________________
#       ______|                                   |_____
#       \     | 4.2 FUNKTIONEN MIT RÜCKGABEWERTEN |    /
#        )    |___________________________________|   (
#       /________)                            (________\       28.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# In Python-Funktionen können wir Ergebnisse berechnen und mit dem `return`-Befehl
# zurückgeben. Ein Rückgabewert ist besonders nützlich, wenn wir das Ergebnis einer
# Funktion weiterverwenden oder verarbeiten möchten. Mit `return` endet die Ausführung
# der Funktion und gibt den Wert an die Stelle im Code zurück, wo die Funktion 
# aufgerufen wurde.

# Die allgemeine Syntax mit Rückgabewert sieht wie folgt aus:

# def funktionsname():
#     Codeblock (hier wird eine Berechnung durchgeführt)
#     return Ergebnis  # Das Ergebnis wird zurückgegeben

# Wenn wir die Funktion aufrufen, können wir den Rückgabewert einer Variablen zuweisen:
# ergebnis = funktionsname()


# ___________________________________
#                                   /
# Beispiel: Einfacher Rückgabewert (
# __________________________________\

# Hier ist ein Beispiel einer Funktion, die das Quadrat einer Zahl berechnet 
# und das Ergebnis zurückgibt.

def square(number):
    result = number * number
    return result  # Das Ergebnis wird an den Aufrufer zurückgegeben

# Wir können das Ergebnis einer Variablen zuweisen und es ausgeben:
result = square(5)
print("Das Quadrat von 5 ist:", result)




# __________________________________
#                                  /
# Beispiel: Mehrere Rückgabewerte (
# _________________________________\

# Funktionen können auch mehrere Werte zurückgeben, indem wir sie als Tupel zurückgeben.
# Dies ist nützlich, wenn wir mehr als nur ein Ergebnis berechnen und zurückgeben möchten.

# Beispiel: Berechne das Quadrat und die dritte Potenz einer Zahl

def powers(number):
    square = number * number
    third = number * number * number

    return quadrat, dritte_potenz  # Gibt beide Werte als Tupel zurück

# Wir können die Rückgabewerte direkt in zwei Variablen speichern:
result1, result2 = powers(4)
print("Das Quadrat von 4 ist:", result1 )
print("Die dritte Potenz von 4 ist:", result2 )




# ____________________________________________
#                                            /
# Beispiel: Rückgabewerte weiterverarbeiten (
# ___________________________________________\

# Mit Rückgabewerten können wir weiterarbeiten und sie in Berechnungen oder
# Bedingungen verwenden.

# Beispiel: Berechne den Durchschnitt von drei Zahlen und überprüfe, ob er über 10 liegt

def mean(a, b, c):
    result = (a + b + c) / 3
    return result

# Wir verwenden den Rückgabewert in einer Bedingung:
result = mean(12, 9, 15)

if result > 10:
    print("Der Durchschnitt liegt über 10:", result)
else:
    print("Der Durchschnitt liegt bei oder unter 10:", result)




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# Rückgabewerte machen Funktionen flexibler und ermöglichen es uns, Berechnungen
# durchzuführen, die wir direkt weiterverarbeiten können, ohne die Logik neu 
# schreiben zu müssen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Schreibe eine Funktion namens `berechne_summe`, die zwei Zahlen als Parameter erhält
# und deren Summe zurückgibt. Verwende die Funktion und gib das Ergebnis auf der Konsole aus.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Funktion namens `find_max`, die drei Zahlen als Parameter erhält und
# die größte dieser Zahlen zurückgibt. Gib das Ergebnis mit einem Funktionsaufruf aus.
# Die Funktion `max()` darf nicht verwendet werden. 


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe eine Funktion namens `convert_km_mile`, die eine Kilometerangabe
# als Parameter erhält und sie in Meilen umrechnet. Die Funktion soll 
# den Meilenwert zurückgeben.
#
# Hinweis: 1 Kilometer entspricht ca. 0.621371 Meilen.


# Füge hier deine Lösung ein.



#      ==================
#       |@@@@----@|--@@|
#       |@@@----@@|--@@|
#       |@@----@@@|--@@|      Mit Rückgabewerten werden Funktionen
#       |@----@@@@|--@@|      zu Rechenmaschinen. So wie dieser Abakus.
#       |@@@@@----|@--@|
# ejm97 |@@@@----@|@--@|
#      ==================
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
#
# Schreibe eine Funktion namens `calculate_sum`, die zwei Zahlen als Parameter erhält
# und deren Summe zurückgibt. Verwende die Funktion und gib das Ergebnis auf der Konsole aus.

'''
def calculate_sum(number1, number1):
    return number1 + number2

# Aufruf der Funktion und Ausgabe des Ergebnisses
result = calculate_sum(10, 15)
print("Die Summe von 10 und 15 ist:", result)
'''


# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Funktion namens `find_max`, die drei Zahlen als Parameter erhält und
# die größte dieser Zahlen zurückgibt. Gib das Ergebnis mit einem Funktionsaufruf aus.
# Die Funktion `max()` darf nicht verwendet werden. 

'''
def find_max(a, b, c):
    if a > b and a > c :
        return a

    elif b > c :
        return b

    else:
        return c

# Aufruf der Funktion und Ausgabe des Ergebnisses
max_number = find_max(12, 5, 23)
print("Die größte Zahl ist:", max_number)
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe eine Funktion namens `convert_km_mile`, die eine Kilometerangabe
# als Parameter erhält und sie in Meilen umrechnet. Die Funktion soll 
# den Meilenwert zurückgeben.
#
# Hinweis: 1 Kilometer entspricht ca. 0.621371 Meilen.

'''
def convert_km_mile(length_in_meter):
    length_in_miles = length_in_meter * 0.621371
    return length_in_miles

# Aufruf der Funktion und Ausgabe des Ergebnisses
l_in_km = 5
l_in_miles = convert_km_mile(l_in_km)
print(f"{l_in_km} Kilometer entsprechen {l_in_miles} Meilen.")
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><




