#              _____________________________________
#       ______|                                     |_____
#       \     | 5.1.2 LISTEN DURCHSUCHEN UND PRÜFEN |    /
#        )    |_____________________________________|   (
#       /________)                              (________\       28.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# In Python gibt es viele Möglichkeiten, Listen zu durchsuchen und zu prüfen,
# ob bestimmte Elemente vorhanden sind. Diese Techniken helfen dabei, Informationen
# zu finden und Entscheidungen zu treffen, basierend auf dem Inhalt einer Liste.


# ____________________________
#                            /
# Prüfen, ob ein Element in  \
# einer Liste enthalten ist  /
# ___________________________\

# Wir können den `in`-Operator verwenden, um zu überprüfen, ob ein Element in
# einer Liste enthalten ist. Der `in`-Operator gibt `True` zurück, wenn das Element
# vorhanden ist, und `False`, wenn es nicht vorhanden ist.

# Beispiel:
fruits = ["Apfel", "Banane", "Kirsche"]
if "Banane" in fruits:
    print("Banane ist in der Liste!")

# Der `not in`-Operator prüft, ob ein Element nicht in der Liste enthalten ist.
if "Melone" not in fruits:
    print("Melone ist nicht in der Liste.")




# ___________________________
#                           /
# Elemente zählen          (
# __________________________\

# Mit der Methode `count()` können wir herausfinden, wie oft ein Element in
# einer Liste vorkommt. Diese Methode ist nützlich, wenn wir eine bestimmte
# Häufigkeit von Elementen prüfen möchten.

numbers = [1, 2, 2, 3, 4, 2, 5]
num_two = numbers.count(2)
print("Anzahl der Zweien:", num_two)




# ______________________________
#                              /
# Index eines Elements finden (
# _____________________________\

# Die Methode `index()` gibt den ersten Index eines Elements in der Liste zurück.
# Wenn das Element nicht vorhanden ist, gibt sie einen Fehler zurück. Diese Methode
# ist hilfreich, um die Position eines Elements herauszufinden.

animals = ["Hund", "Katze", "Vogel", "Katze"]
cat_index = animals.index("Katze")
print("Erste Katze ist bei Index:", cat_index)

# Hinweis: Falls ein Element mehrfach vorkommt, gibt `index()` nur die erste Position zurück.



# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - `in` und `not in` geben `True` oder `False` zurück, je nachdem, ob ein Element
#   in einer Liste enthalten ist oder nicht.
#
# - `count()` zählt, wie oft ein Element in der Liste vorkommt.
#
# - `index()` gibt den Index des ersten Vorkommens eines Elements zurück.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine Liste `subjects` mit den Fächern "Mathe", "Physik", "Chemie" und "Informatik".
# Überprüfe, ob das Fach "Geschichte" in der Liste enthalten ist und gib eine passende Nachricht aus.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Liste namens `grades` mit den Werten 5, 6, 5, 4, 5, 6.
# Zähle, wie oft die Note 5 vorkommt, und gib das Ergebnis aus.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Liste `participants` mit den Namen "Anna", "Ben", "Chris" und "Diana".
# Suche nach dem Index von "Chris" und gib den Index aus.


# Füge hier deine Lösung ein.




#           .-""-.
#   _______/      \  
#  |_______        ;        Listen zu durchsuchen ist nun ein
#          \      /         Kinderspiel für dich. 
#           '-..-'
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
# Erstelle eine Liste `subjects` mit den Fächern "Mathe", "Physik", "Chemie" und "Informatik".
# Überprüfe, ob das Fach "Geschichte" in der Liste enthalten ist und gib eine passende Nachricht aus.

'''
subjects = ["Mathe", "Physik", "Chemie", "Informatik"]
if "Geschichte" in subjects:
    print("Geschichte ist in der Liste enthalten.")
else:
    print("Geschichte ist nicht in der Liste.")
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Liste namens `grades` mit den Werten 5, 6, 5, 4, 5, 6.
# Zähle, wie oft die Note 5 vorkommt, und gib das Ergebnis aus.

'''
grades = [5, 6, 5, 4, 5, 6]
num_fives = grades.count(5)
print("Anzahl der 5er:", num_fives)
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Liste `participants` mit den Namen "Anna", "Ben", "Chris" und "Diana".
# Suche nach dem Index von "Chris" und gib den Index aus.

'''
participants = ["Anna", "Ben", "Chris", "Diana"]
chris_index = participants.index("Chris")
print("Chris ist bei Index:", chris_index)
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><



