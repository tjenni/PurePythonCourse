#              _________________________
#       ______|                         |_____
#       \     |    2.1 VERZWEIGUNGEN    |    /
#        )    |_________________________|   (
#       /________)                  (________\       27.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# In Python können wir Programme so schreiben, dass sie Entscheidungen treffen.
# Das funktioniert mit Verzweigungen. Eine Verzweigung entscheidet,
# ob ein bestimmter Teil des Codes ausgeführt wird, abhängig davon, ob eine
# Bedingung wahr (True) oder falsch (False) ist.



# ___________________________
#                           /
# Der if-Befehl            (
# __________________________\

# Die einfachste Verzweigung ist der `if`-Befehl. Wenn die Bedingung nach `if`
# wahr `True` ist, führt Python den Codeblock darunter aus. Der Codeblock
# besteht aus allen Zeilen, die gleich eingerückt sind.
#
# Syntax:
# if `Bedingung`:
#     Codeblock (wird ausgeführt, wenn Bedingung True ist)

# Beispiel:

age = 18
if age >= 18
    print("Du bist volljährig.")
    print("Du kannst nun alleine Entscheidungen treffen.")

# In diesem Beispiel prüft Python, ob `age` (also das Alter) mindestens 18 ist.
# Da die Bedingung wahr ist, wird "Du bist volljährig." und "Wow." ausgegeben.

#  _ MERKE _________________________________________
# |                                                 |
# | 1. Setze immer einen Doppelpunkt (:) nach       |
# |    der Bedingung! Fehlt er, gibt Python         |
# |    folgenden Fehler aus:                        |
# |                                                 |
# |         SyntaxError: expected ':'               |
# |                                                 |
# | 2. Achte auf die Einrückung im Codeblock!       |
# |    Alle Zeilen eines Codeblocks müssen          |
# |    gleich eingerückt sein. Bei uneinheitlicher  |
# |    Einrückung erscheint dieser Fehler:          |
# |                                                 |
# |         IndentationError: unexpected indent     |
# |_________________________________________________|



# ___________________________
#                           /
# Der else-Befehl          (
# __________________________\

# Mit `else` kannst du einen zweiten Codeblock hinzufügen, der ausgeführt wird,
# wenn die Bedingung nicht wahr (`False`) ist.

# Syntax:
# if `Bedingung`:
#     Codeblock (wird ausgeführt, wenn Bedingung True ist)
# else:
#     Codeblock (wird ausgeführt, wenn Bedingung False ist)

# Beispiel:

age = 16
if age >= 18:
    print("Du bist volljährig.")
    print("Wow.")
else:
    print("Du bist minderjährig.")
    print("Geniesse deine Jugendzeit!")

# Da `age` hier 16 ist und die Bedingung `False` ergibt, führt Python den
# Code im `else`-Block aus.



# ___________________________
#                           /
# Der elif-Befehl          (
# __________________________\

# Mit `elif` (Kurzform für „else if“) kannst du mehrere Bedingungen nacheinander prüfen.
# Python sucht der Reihe nach die erste Bedingung, die wahr ist (`True`), und führt 
# den zugehörigen Codeblock aus. Sobald ein Codeblock ausgeführt wird, überspringt 
# Python die restlichen `elif`- und `else`-Blöcke.

# Syntax:
# if Bedingung1:
#     Codeblock (wird ausgeführt, wenn Bedingung1 True ist)
# elif Bedingung2:
#     Codeblock (wird nur ausgeführt, wenn Bedingung1 False und Bedingung2 True ist)
# else:
#     Codeblock (wird ausgeführt, wenn Bedingung1 und Bedingung2 False sind)

# Beispiel:

age = 15
if age >= 18:
    print("Du bist volljährig.")
elif age >= 16:
    print("Du darfst in manchen Ländern Auto fahren.")
else:
    print("Du bist minderjährig und darfst noch kein Auto fahren.")

# Hier ist `age` gleich 15, daher sind die `if`- und `elif`-Bedingungen `False`.
# Daher führt Python den `else`-Block aus.



# ___________________________
#                           /
# Vergleichsoperatoren     (
# __________________________\

# Vergleichsoperatoren sind zentral für Bedingungen, da sie zwei Werte
# miteinander vergleichen und entweder `True` (wahr) oder `False` (falsch) zurückgeben.
# Die wichtigsten Vergleichsoperatoren sind:

#   ==    (gleich) Prüft, ob zwei Werte gleich sind.
#         Beispiel: 5 == 5 ergibt `True`, 5 == 3 ergibt `False`.

#   !=    (ungleich) Prüft, ob zwei Werte ungleich sind.
#         Beispiel: 5 != 3 ergibt `True`, 5 != 5 ergibt `False`.

#   >     (grösser als) Prüft, ob der linke Wert grösser ist als der rechte.
#         Beispiel: 7 > 5 ergibt `True`, 3 > 5 ergibt `False`.

#   <     (kleiner als) Prüft, ob der linke Wert kleiner ist als der rechte.
#         Beispiel: 3 < 5 ergibt `True`, 7 < 5 ergibt `False`.

#   >=    (grösser gleich) Prüft, ob der linke Wert grösser oder gleich dem rechten ist.
#         Beispiel: 5 >= 5 ergibt `True`, 3 >= 5 ergibt `False`.

#   <=    (kleiner gleich) Prüft, ob der linke Wert kleiner oder gleich dem rechten ist.
#         Beispiel: 3 <= 5 ergibt `True`, 7 <= 5 ergibt `False`.


#  _ MERKE _____________________________________________
# |                                                     |
# | Verwende zum Vergleichen von Werten immer zwei      |
# | Gleichheitszeichen `==`. Wird stattdessen nur ein   |
# | Gleichheitszeichen `=` geschrieben, interpretiert   |
# | Python dies als Zuweisung an eine Variable, und das |
# | Programm funktioniert nicht wie gewünscht.          |
# |_____________________________________________________|

# Hier sind zusätzliche Beispiele zur Vertiefung.



# Beispiel 1: Überprüfen, ob eine Zahl positiv, negativ oder null ist.

zahl = -7

if zahl > 0:
    print("Die Zahl ist positiv.")
elif zahl < 0:
    print("Die Zahl ist negativ.")
else:
    print("Die Zahl ist null.")



# Beispiel 2: Überprüfen, ob zwei Zeichenfolgen (Strings) gleich oder unterschiedlich sind.

wort1 = "Apfel"
wort2 = "apfel"

if wort1 == wort2:
    print("Die Wörter sind identisch.")
else:
    print("Die Wörter sind unterschiedlich.")

# Bei Zeichenfolgen unterscheidet Python zwischen Gross- und Kleinschreibung,
# daher ergibt der Vergleich hier `False`, weil "Apfel" nicht gleich "apfel" ist.



# Beispiel 3: Überprüfen, ob ein Preis unter oder über einem bestimmten Wert liegt.

preis = 120

if preis <= 100:
    print("Der Preis liegt im Budget.")
else:
    print("Der Preis liegt über dem Budget.")




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Frage den Benutzer nach zwei Zahlen und gib die grössere der beiden Zahlen aus.
# Falls beide gleich sind, gib aus: „Die beiden Zahlen sind gleich.“


# Füge hier deine Lösung ein.



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Frage den Benutzer nach einem Passwort. Wenn der Benutzer das Wort "Sesam"
# eingibt, erscheint auf der Konsole der Text „Das Tor öffnet sich.“
# Andernfalls erscheint der Text „Das Tor bleibt verschlossen.“


# Füge hier deine Lösung ein.



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Frage den Benutzer nach einer Zahl und überprüfe, ob die Zahl gerade
# oder ungerade ist. Gib das Ergebnis auf der Konsole aus.
#
# Hinweis: Eine Zahl ist gerade, wenn zahl % 2 == 0.


# Füge hier deine Lösung ein.



# ___________
#            \
# Aufgabe 4  /
# __________/
#
# Frage den Benutzer nach einer Zahl. Überprüfe, ob diese Zahl durch 7 teilbar ist.
# Gib das Ergebnis auf der Konsole aus.


# Füge hier deine Lösung ein.



# ___________
#            \
# Aufgabe 5  /
# __________/
#
# Frage den Benutzer nach einem Wort und überprüfe, ob es mit „A“ beginnt.
# Gib passend dazu aus, ob das Wort mit „A“ anfängt oder nicht.


# Füge hier deine Lösung ein.



# ___________
#            \
# Aufgabe 6  /
# __________/
#
# Frage den Benutzer nach einer Eingabe und überprüfe, ob sie nur aus Ziffern besteht.
# Gib passend dazu aus, ob die Eingabe nur Ziffern enthält oder nicht.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 7  /
# __________/
#
# Frage den Benutzer nach einem Text, der nur aus Grossbuchstaben besteht.
# Gib passend dazu aus, ob der Text nur Grossbuchstaben enthält oder nicht.
#
# Hinweis: Verwende die Methode `.isupper()`, um zu prüfen, ob alle Zeichen
# im Text Grossbuchstaben sind.


# Füge hier deine Lösung ein.



# Wenn du alle Aufgaben gelöst hast, bekommst du von mir
# die folgende Auszeichnung.
#
#
#           |@@@@|     |####|
#           |@@@@|     |####|
#           |@@@@|     |####|
#           \@@@@|     |####/
#            \@@@|     |###/
#             `@@|_____|##'
#                  (O)
#               .-'''''-.
#             .'  * * *  `.
#            :  *       *  :
#           :   Verzweig-   :
#           :   ungsprofi   :
#            :  *       *  :
#       jgs   `.  * * *  .'
#               `-.....-'
#
#  ___ _  _ ___  ___ 
# | __| \| |   \| __|
# | _|| .` | |) | _| 
# |___|_|\_|___/|___|
#                
# -=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-





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

# Frage den Benutzer nach zwei Zahlen und gib die grössere der beiden Zahlen aus.
# Falls beide gleich sind, gib aus: „Die beiden Zahlen sind gleich.“

'''
number1 = float(input("Gib die erste Zahl ein: "))
number2 = float(input("Gib die zweite Zahl ein: "))

if number1 > number2:
    print("Die grössere Zahl ist:", zahl1)
elif number2 > number1:
    print("Die grössere Zahl ist:", zahl2)
else:
    print("Die beiden Zahlen sind gleich.")
'''


# ___________
#            \
# Aufgabe 2  /
# __________/

# Frage den Benutzer nach einem Passwort. Wenn der Benutzer das Wort "Sesam"
# eingibt, erscheint auf der Konsole der Text „Das Tor öffnet sich.“
# Andernfalls erscheint der Text „Das Tor bleibt verschlossen.“

'''
password = input("Gib das Passwort ein: ")

if password == "Sesam":
    print("Das Tor öffnet sich.")
else:
    print("Das Tor bleibt verschlossen.")
'''


# ___________
#            \
# Aufgabe 3  /
# __________/

# Frage den Benutzer nach einer Zahl und überprüfe, ob die Zahl gerade
# oder ungerade ist. Gib das Ergebnis auf der Konsole aus.

'''
number = int(input("Gib eine Zahl ein: "))

if number % 2 == 0:
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")
'''


# ___________
#            \
# Aufgabe 4  /
# __________/

# Frage den Benutzer nach einer Zahl. Überprüfe, ob diese Zahl durch 7 teilbar ist.

'''
number = int(input("Gib eine Zahl ein: "))

if number % 7 == 0:
    print("Die Zahl ist durch 7 teilbar.")
else:
    print("Die Zahl ist nicht durch 7 teilbar.")
'''


# ___________
#            \
# Aufgabe 5  /
# __________/

# Frage den Benutzer nach einem Wort und überprüfe, ob es mit „A“ beginnt.
# Gib passend dazu aus, ob das Wort mit „A“ anfängt oder nicht.


'''
word = input("Gib ein Wort ein: ")

if word[0] = "A":
    print("Das Wort beginnt mit A.")
else:
    print("Das Wort beginnt nicht mit A.")
'''


# ___________
#            \
# Aufgabe 6  /
# __________/

# Frage den Benutzer nach einer Eingabe und überprüfe, ob sie nur aus Ziffern besteht.
# Gib passend dazu aus, ob die Eingabe nur Ziffern enthält oder nicht.

'''
code = input("Gib eine Eingabe ein: ")

if code.isdigit():
    print("Die Eingabe enthält nur Ziffern.")
else:
    print("Die Eingabe enthält nicht nur Ziffern.")
'''


# ___________
#            \
# Aufgabe 7  /
# __________/

# Frage den Benutzer nach einem Text, der nur aus Grossbuchstaben besteht.
# Gib passend dazu aus, ob der Text nur Grossbuchstaben enthält oder nicht.

'''
text = input("Gib einen Text ein: ")

if text.isupper():
    print("Der Text besteht nur aus Grossbuchstaben.")
else:
    print("Der Text enthält auch andere Zeichen als Grossbuchstaben.")
''' 

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


