#              ____________________________
#       ______|                            |_____
#       \     |  4.5 REKURSIVE FUNKTIONEN  |    /
#        )    |____________________________|   (
#       /________)                     (________\       2.12.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Eine rekursive Funktion ist eine Funktion, die sich selbst aufruft, um eine 
# Aufgabe zu lösen. Rekursion ist besonders nützlich, wenn ein Problem in 
# kleinere, ähnliche Teilprobleme zerlegt werden kann.

# Rekursion besteht aus zwei Hauptbestandteilen:
# 1. Basisfall: Der Punkt, an dem die Rekursion stoppt, um eine unendliche
#    Schleife zu vermeiden.
#
# 2. Rekursiver Schritt: Der Teil der Funktion, in dem sie sich selbst aufruft,
#    um das Problem schrittweise zu lösen.

# Mit rekursiven Funktionen können wir Probleme lösen, die auf natürliche Weise 
# eine hierarchische oder sich wiederholende Struktur aufweisen, wie z. B. das Berechnen 
# der Fakultät, die Fibonacci-Folge oder das Durchlaufen eines Baums.


# ______________________________________
#                                      /
# Beispiel einer rekursiven Funktion  (
# _____________________________________\

# Fakultät einer Zahl:
# Die Fakultät einer Zahl ist das Produkt aller positiven ganzen Zahlen, die 
# kleiner oder gleich dieser Zahl sind.
# Beispiel: 5! = 5 * 4 * 3 * 2 * 1 = 120

# Die Fakultät kann rekursiv definiert werden:
#
# - Basisfall: 0! = 1
# - Rekursiver Schritt: n! = n * (n - 1)!

def factorial(n):
    if n == 0:
        return 1  # Basisfall: 0! = 1
    else:
        return n * factorial(n - 1)  # Rekursiver Schritt

# Test der Funktion
print("Die Fakultät von 5 ist:", factorial(5))  # Ausgabe: 120




# ____________________________
#                            /
# Warum Rekursion nutzen?   (
# ___________________________\

# Rekursive Funktionen sind besonders nützlich, wenn:
#
# - Ein Problem in kleinere Teilprobleme zerlegt werden kann.
#
# - Die genaue Anzahl der Iterationen im Voraus nicht bekannt ist.
#
# - Eine hierarchische oder verschachtelte Struktur vorliegt (z. B. Bäume, Graphen).


# Beispiel: Fibonacci-Folge
# Die Fibonacci-Folge ist eine Reihe von Zahlen, bei der jede Zahl die Summe
# der beiden vorherigen Zahlen ist.
#
# - Basisfälle: fib(0) = 0, fib(1) = 1
# - Rekursiver Schritt: fib(n) = fib(n-1) + fib(n-2)

def fibonacci(n):
    if n <= 1:
        return n  # Basisfälle: fib(0) = 0, fib(1) = 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Rekursiver Schritt

# Test der Funktion
print("Die 6. Fibonacci-Zahl ist:", fibonacci(6))  # Ausgabe: 8




# ____________________________
#                            /
# Rekursion vs. Iteration    (
# ___________________________\

# Rekursion ist nicht immer die effizienteste Methode. Eine rekursive Lösung 
# kann in manchen Fällen durch eine iterative Lösung ersetzt werden, die weniger 
# Speicher benötigt. Zum Beispiel: Fibonacci-Folge mit einer Schleife

def fibonacci_iteratively(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print("Die 6. Fibonacci-Zahl (iterativ) ist:", fibonacci_iteratively(6))  # Ausgabe: 8




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# Rekursive Funktionen sind mächtig, aber sie sollten mit Bedacht eingesetzt werden.
# - Wann Rekursion verwenden: Wenn ein Problem natürliche Teilprobleme hat.
#
# - Wann Iteration bevorzugen: Wenn Effizienz und Speicher eine wichtige Rolle spielen.
#
# - Wichtig: Immer einen Basisfall definieren, um unendliche Rekursion zu vermeiden.

# Beispiele für rekursive Probleme:
# - Fakultät
# - Fibonacci-Folge
# - Türme von Hanoi
# - Durchlaufen von Datenstrukturen (z. B. Bäume, Graphen)




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Schreibe eine Funktion `sum_to_n`, die die Summe aller Zahlen von 1 bis n 
# rekursiv berechnet. Beispiel: sum_n(5) = 1 + 2 + 3 + 4 + 5 = 15.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe eine Funktion `anzahl_ziffern`, die die Anzahl der Ziffern einer Zahl 
# rekursiv berechnet. Beispiel: count_digits(1234) = 4.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe eine rekursive Funktion, um die größte Zahl in einer Liste zu finden.
# Beispiel: max_in_list([3, 7, 1, 9, 2]) = 9.

# Füge hier deine Lösung ein.



#         __/\__ 
#         \    /   
#   __/\__/    \__/\__
#   \                /
#   /_              _\        Die Koch-Flocke ist ein Beispiel für
#     \            /          eine Grafik, welche mit einer rekursiven
#   __/            \__        Funktion gezeichnet werden kann.
#   \                /
#   /_  __      __  _\
#     \/  \    /  \/
#         /_  _\
#           \/
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
#                             |___/            

# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Schreibe eine Funktion `sum_to_n`, die die Summe aller Zahlen von 1 bis n 
# rekursiv berechnet. Beispiel: sum_to_n(5) = 1 + 2 + 3 + 4 + 5 = 15.

'''
def sum_to_n(n):
    if n == 0:  # Basisfall: Die Summe von 0 ist 0.
        return 0
    else:
        return n + sum_to_n(n - 1)  # Rekursiver Schritt: n + Summe von (n-1)

# Test der Funktion
print("Summe von 1 bis 5 ist:", sum_to_n(5))  # Ausgabe: 15
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe eine Funktion `anzahl_ziffern`, die die Anzahl der Ziffern einer Zahl 
# rekursiv berechnet. Beispiel: anzahl_ziffern(1234) = 4.

'''
def anzahl_ziffern(n):
    if n < 10:  # Basisfall: Eine einstellige Zahl hat genau eine Ziffer.
        return 1
    else:
        return 1 + anzahl_ziffern(n // 10)  # Rekursiver Schritt: Entferne die letzte Ziffer

# Test der Funktion
print("Anzahl der Ziffern in 1234 ist:", anzahl_ziffern(1234))  # Ausgabe: 4
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe eine rekursive Funktion, um die größte Zahl in einer Liste zu finden.
# Beispiel: max_in_list([3, 7, 1, 9, 2]) = 9.

'''
def max_in_list(lst):
    if len(lst) == 1:  # Basisfall: Eine Liste mit einer Zahl hat diese als Maximum.
        return lst[0]
    else:
        max_of_rest = max_in_list(lst[1:])  # Rekursiver Schritt: Maximum der restlichen Liste
        return max(lst[0], max_of_rest)  # Vergleiche die erste Zahl mit dem Maximum der restlichen Liste

# Test der Funktion
print("Das Maximum in der Liste [3, 7, 1, 9, 2] ist:", max_in_list([3, 7, 1, 9, 2]))  # Ausgabe: 9
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

