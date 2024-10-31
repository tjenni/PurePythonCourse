#              __________________________________
#       ______|                                 |_____
#       \     |   5.1.3 SCHLEIFEN UND LISTEN    |    /
#        )    |_________________________________|   (
#       /________)                          (________\       28.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Schleifen sind besonders nützlich, um Listen zu durchlaufen und auf jedes 
# Element einzeln zuzugreifen. Mit Schleifen können wir Informationen ausgeben, 
# Werte ändern, Berechnungen durchführen und vieles mehr.

# Python bietet uns verschiedene Möglichkeiten, eine Liste mit einer Schleife zu 
# durchlaufen. Die gebräuchlichste Methode ist die `for`-Schleife.


# ____________________________
#                            /
# For-Schleife für Listen   (
# ___________________________\

# Die einfachste Art, eine Liste zu durchlaufen, ist die `for`-Schleife.
# Dabei wird jedes Element in der Liste nacheinander bearbeitet.

fruits = ["Apfel", "Banane", "Kirsche"]

for fruit in fruits:
    print("Frucht:", fruit)

# In diesem Beispiel wird jedes Element der Liste `fruechte` ausgegeben.




# ____________________________
#                            /
# For-Schleife mit Index    (
# ___________________________\

# Wenn wir sowohl den Wert als auch den Index eines Elements benötigen, können wir
# `enumerate()` verwenden. So haben wir Zugriff auf den Index und das Element.

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Mit `enumerate()` erhalten wir eine Nummerierung, was besonders nützlich ist,
# wenn die Position in der Liste wichtig ist.




# ____________________________
#                            /
# While-Schleife für Listen (
# ___________________________\

# Listen lassen sich auch mit der `while`-Schleife durchlaufen. Dazu benötigen
# wir einen Zähler, um den Index jedes Elements zu kontrollieren.

index = 0
while index < len(fruechte):
    print(f"Element bei Index {index}:", fruechte[index])
    index += 1




# ___________________________
#                           /
# Liste verändern           (
# ___________________________\

# Wir können Elemente in einer Liste durchlaufen und je nach Bedarf verändern.
# Zum Beispiel können wir Zahlen in einer Liste verdoppeln.

numbers = [1, 2, 3, 4]
for i in range(len(numbers)):
    numbers[i] *= 2  # Jedes Element wird verdoppelt

print("Verdoppelte Zahlen:", numbers)




# ___________________
#                   /
# Zusammenfassung  (
# __________________\


# - Die `for`-Schleife ist ideal zum Durchlaufen von Listen.
#
# - Mit `enumerate()` haben wir zusätzlich Zugriff auf den Index jedes Elements.
#
# - Eine `while`-Schleife kann nützlich sein, wenn man den Index explizit 
#   kontrollieren möchte.



# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine Liste namens `colors` mit den Elementen "Rot", "Blau", "Grün" und "Gelb".
# Durchlaufe die Liste mit einer `for`-Schleife und gib jede Farbe auf der Konsole aus.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Liste `numbers` mit den Werten 2, 4, 6, 8.
# Quadriere jeden Wert in der Liste mit einer Schleife und gib die aktualisierte 
# Liste aus.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Liste namens `cities` mit den Elementen "Berlin", "Paris", "Rom".
# Durchlaufe die Liste mit einer `for`-Schleife und gib den Index und den Städtenamen aus,
# zum Beispiel „Index 0: Berlin“.


# Füge hier deine Lösung ein.



#                                  /\
#                                 /  \
#                                |    |
#                              --:'''':--
#                                :'_' :
#                                _:"":\___
#                 ' '      ____.' :::     '._
#                . *=====<<=)           \    :
#                 .  '      '-'-'\_      /'._.'
#                                  \====:_ ""
#                                 .'     \\    Du bist ein/-e Listenmagier/-in.
#                                :       :
#                               /   :    \
#                              :   .      '.
#              ,. _        snd :  : :      :
#           '-'    ).          :__:-:__.;--'
#        (        '  )        '-'   '-'
#      ( -   .00.   - _
#     (    .'  _ )     )
#     '-  ()_.\,\,   -
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
# Erstelle eine Liste namens `colors` mit den Elementen "Rot", "Blau", "Grün" und "Gelb".
# Durchlaufe die Liste mit einer `for`-Schleife und gib jede Farbe auf der Konsole aus.

'''
colors = ["Rot", "Blau", "Grün", "Gelb"]

for color in colors:
    print("Farbe:", color)
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Liste `numbers` mit den Werten 2, 4, 6, 8.
# Quadriere jeden Wert in der Liste mit einer Schleife und gib die aktualisierte 
# Liste aus.

'''
numbers = [2, 4, 6, 8]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * numbers[i]  # Quadriert jeden Wert
print("Quadrierte Zahlen:", numbers)
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Liste namens `cities` mit den Elementen "Berlin", "Paris", "Rom".
# Durchlaufe die Liste mit einer `for`-Schleife und gib den Index und den Städtenamen aus,
# zum Beispiel „Index 0: Berlin“.

'''
cities = ["Berlin", "Paris", "Rom"]

for index, city in enumerate(cities):
    print(f"Index {index}: {city}")
'''



# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><




