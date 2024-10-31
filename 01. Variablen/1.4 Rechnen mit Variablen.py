#              ______________________________
#       ______|                              |______
#       \     |  1.4 RECHNEN MIT VARIABLEN   |     /
#        )    |______________________________|    (
#       /________)                        (________\       27.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
#  


# In Python kannst du mit Variablen rechnen, indem du verschiedene Operatoren
# wie Addition (+), Subtraktion (-), Multiplikation (*) und Division (/) verwendest.
# Lassen wir uns die Grundrechenarten genauer ansehen:


# _____________________
#                     /
# Grundrechenarten   (
# ____________________\

# Nehmen wir die Variablen a und b und rechnen damit:

a = 10
b = 3

# Addition
summe = a + b
print("Addition:", summe)

# Subtraktion
differenz = a - b
print("Subtraktion:", differenz)

# Multiplikation
produkt = a * b
print("Multiplikation:", produkt)

# Division
quotient = a / b
print("Division:", quotient)

# Hinweis: Bei der Division gibt Python das Ergebnis als Dezimalzahl (float) zurück.



# ____________________________
#                            /
# Ganzzahlige Division und  (
# Rest berechnen            (
# ___________________________\

# Manchmal willst du das Ergebnis einer Division als ganze Zahl haben. Dafür
# kannst du den Operator // (ganzzahlige Division) verwenden. Der Operator %
# gibt den Rest einer Division zurück und wird Modulo genannt.

# Ganzzahlige Division
ganzzahl_div = a // b
print("Ganzzahlige Division:", ganzzahl_div)

# Modulo (Rest)
rest = a % b
print("Rest:", rest)

# Beispiel: Du hast 10 Bonbons und möchtest sie gerecht auf 3 Kinder aufteilen.
# Wie viele bekommt jedes Kind (Ganzzahldivision) und wie viele bleiben übrig (Modulo)?






# __________________________________
#                                  /
# Unterschiedliche Variablentypen (
# _________________________________\

# Rechenoperationen funktionieren in Python nur mit numerischen Typen
# wie Integer und Float. Wenn du versuchst, mit Strings oder Boolean-Werten
# zu rechnen, kann Python eine Fehlermeldung geben.

# Beispiel:
# result = "Apfel" + 5  # Dieser Code würde eine Fehlermeldung erzeugen.

#    TypeError: can only concatenate str (not "int") to str




# ______________________________________
#                                      /
#  Die Zuweisungsoperatoren += und -= (
# _____________________________________\


# Die Operatoren `+=` und `-=` sind Abkürzungen, die häufig verwendet werden,
# um den Wert einer Variablen zu erhöhen oder zu verringern.

# `+=` ist eine Kurzform für "addiere und weise zu". Es erhöht den Wert 
# einer Variablen um den angegebenen Betrag.

# Beispiel:
counter = 0
counter += 1  # entspricht: counter = counter + 1
print(counter)  # Ausgabe: 1

# Hier wird `counter` um 1 erhöht. `+=` kann auch für größere Erhöhungen 
# verwendet werden:

counter += 5  # erhöht `counter` um 5
print(counter)  # Ausgabe: 6


# `-=` funktioniert genauso, verringert den Wert aber um den angegebenen Betrag.

# Beispiel:
counter -= 2  # entspricht: counter = counter - 2
print(counter)  # Ausgabe: 4

# Beide Operatoren helfen, den Code übersichtlicher und kürzer zu gestalten,
# was besonders in Schleifen nützlich sein wird, wenn wir Variablen 
# schrittweise ändern.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Frage den Benutzer nach zwei Zahlen und gib das Ergebnis ihrer Addition,
# Subtraktion, Multiplikation und Division aus.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Lasse den Benutzer eine Zahl eingeben und gib aus, ob die Zahl gerade oder
# ungerade ist. Hinweis: Eine Zahl ist gerade, wenn zahl % 2 == 0.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Programm, das den Preis eines Artikels und die Anzahl der
# Artikel abfragt. Berechne den Gesamtpreis und gib ihn auf der Konsole aus.
#
# Beispiel:
# Preis eines Artikels: 3.50
# Anzahl Artikel: 4
# Gesamtpreis: 14.00


# Füge hier deine Lösung ein.


# Gratuliere. Du hast nun verstanden, wie man mit Python rechnen kann.
#
#   _____________________
#  |  _________________  |
#  | | JO           0. | |
#  | |_________________| |
#  |  ___ ___ ___   ___  |
#  | | 7 | 8 | 9 | | + | |
#  | |___|___|___| |___| |
#  | | 4 | 5 | 6 | | - | |
#  | |___|___|___| |___| |
#  | | 1 | 2 | 3 | | x | |
#  | |___|___|___| |___| |
#  | | . | 0 | = | | / | |
#  | |___|___|___| |___| |
#  |_____________________|
#
#  ___ _  _ ___  ___ 
# | __| \| |   \| __|
# | _|| .` | |) | _| 
# |___|_|\_|___/|___|
#                
# -=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-x=-=x=-=x=-=x=-=x




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

# Frage den Benutzer nach zwei Zahlen und gib das Ergebnis ihrer Addition,
# Subtraktion, Multiplikation und Division aus.

'''
number1 = float(input("Gib die erste Zahl ein: "))
number2 = float(input("Gib die zweite Zahl ein: "))

print("Addition:", number1 + number2)
print("Subtraktion:", number1 - number2)
print("Multiplikation:", number1 * number2)
print("Division:", number1 / number2)
'''


# ___________
#            \
# Aufgabe 2  /
# __________/

# Lasse den Benutzer eine Zahl eingeben und gib aus, ob die Zahl gerade oder
# ungerade ist.

'''
number = int(input("Gib eine Zahl ein: "))

if number % 2 == 0:
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")
'''

# ___________
#            \
# Aufgabe 3  /
# __________/

# Erstelle ein Programm, das den Preis eines Artikels und die Anzahl der
# Artikel abfragt und den Gesamtpreis berechnet und ausgibt.

'''
price = float(input("Preis eines Artikels: "))
amount = int(input("Anzahl Artikel: "))

total = price * amount
print("Gesamtpreis:", total)
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

