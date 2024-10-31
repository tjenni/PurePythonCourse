#              ___________________________
#       ______|                           |_____
#       \     |       3.1 SCHLEIFEN       |    /
#        )    |___________________________|   (
#       /________)                    (________\       27.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Schleifen sind zentrale Werkzeuge in der Programmierung, die uns erlauben,
# bestimmte Aktionen beliebig oft zu wiederholen. Mit Schleifen können wir
# Aufgaben automatisieren, die sonst viel mehr Code erfordern würden.

# In Python gibt es zwei Hauptarten von Schleifen: die `for`-Schleife und 
# die `while`-Schleife.
# Beide haben ihre spezifischen Einsatzbereiche und Vorteile. Die `for`-Schleife eignet
# sich ideal, wenn die Anzahl der Wiederholungen feststeht, während die `while`-Schleife
# genutzt wird, wenn eine Aktion solange wiederholt werden soll, wie eine bestimmte
# Bedingung erfüllt ist.

# In den nächsten Kapiteln werden wir beide Schleifenarten im Detail kennenlernen.
# Diese Einführung bietet zunächst einen Überblick – mach dir also keine Sorgen,
# wenn dir einige Punkte noch nicht ganz klar sind.




# ___________________________
#                           /
# Die for-Schleife         (
# __________________________\

# Die `for`-Schleife wird verwendet, wenn die Anzahl der Wiederholungen
# bereits feststeht oder wir durch eine Sammlung (z. B. Zeichenkette)
# iterieren möchten. Sie durchläuft jedes Element in einer Sammlung und führt den
# Code im Schleifenblock aus.

# Syntax:
# for variable in Sammlung:
#     Codeblock (wird für jedes Element in der Sammlung ausgeführt)

# Beispiel:
for letter in "Hallo wie gehts?":
    print(zahl)


# Die `range()`-Funktion ist besonders nützlich, wenn du die Anzahl der
# Schleifendurchläufe kontrollieren oder bestimmte Zahlenfolgen erzeugen möchtest.

# Beispiel:
for i in range(10): 
    print("i:", i)




# ___________________________
#                           /
# Die while-Schleife       (
# __________________________\

# Die `while`-Schleife wird verwendet, wenn wir nicht genau wissen, wie oft
# die Schleife wiederholt werden soll. Stattdessen wiederholt sich der Codeblock
# solange eine Bedingung wahr (`True`) ist. Wenn die Bedingung `False` wird,
# endet die Schleife.

# Syntax:
# while Bedingung:
#     Codeblock (wird wiederholt, solange die Bedingung True ist)

# Beispiel:
counter = 1
while counter < 5:
    print("Schleifendurchlauf:", counter)

    counter += 1

# Hier wiederholt sich der Codeblock solange `counter` kleiner als 5 ist.
# Bei jedem Durchlauf wird `counter` um 1 erhöht.

#  _ HINWEIS ______________________________________________
# |                                                        |
# |   Die Operatoren `+=` und `-=` sind Abkürzungen,       |
# |   die häufig in Schleifen verwendet werden, um den     |
# |   Wert einer Variablen zu erhöhen oder zu verringern,  |
# |   siehe Kapitel `1.4 Rechnen mit Variablen`            |
# |________________________________________________________|




# _____________________________________________
#                                             /
# Überblick: Wann welche Schleife verwenden? (
# ____________________________________________\

# - Verwende `for`-Schleifen, wenn du durch eine Sammlung wie eine Liste oder Zeichenkette
#   iterieren möchtest, oder wenn die Anzahl der Wiederholungen feststeht.

# - Verwende `while`-Schleifen, wenn du eine Bedingung hast, die sich während
#   der Schleifenwiederholungen ändern kann und du nicht genau weisst, wie oft die Schleife
#   ausgeführt wird.

# Merke: Achte darauf, dass die Bedingung in `while`-Schleifen irgendwann `False` wird.
# Ansonsten läuft die Schleife unendlich lange weiter und das Programm hört nicht auf!




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/

# Schreibe eine `for`-Schleife, die die Zahlen von 0 bis 100 der Reihe nach auf 
# der Konsole ausgibt. Nutze dazu die `range()`-Funktion.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/

# Schreibe eine `while`-Schleife, die einen Countdown von 9 bis 0 auf der 
# Konsole ausgibt.


# Füge hier deine Lösung ein.




#
#             __   ___  / /
#         ___( (\_( ) )/ /
#        |\___` \\_\/_/_/_\
#        | | ____/\_\`._._...^^^^^^^^^^^^^^^^^^^^^^^\
#        | ||\__/ '_\ \`_._\.;                       \
#         \|| | | | | |    | \    gut gemacht!        \
#          || | |^| | |    |  \     Deine ersten       \
#           \ |     | |    |   \   Schleifen sind toll! \
#            \|ejm__| |____|    \                        \
#                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
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

# Schreibe eine `for`-Schleife, die die Zahlen von 1 bis 10 der Reihe nach auf 
# der Konsole ausgibt. Nutze dazu die `range(start, stop, step)`-Funktion, 
# um den Zahlenbereich festzulegen.

'''
for zahl in range(101):
    print(zahl)
'''




# ___________
#            \
# Aufgabe 2  /
# __________/

# Schreibe eine `while`-Schleife, die einen Countdown von 9 bis 0 auf der 
# Konsole ausgibt.

'''
countdown = 9
while countdown >= 0:
    print(countdown)

    countdown -= 1  
'''




# ___________
#            \
# Aufgabe 3  /
# __________/

# Schreibe eine `for`-Schleife, die alle geraden Zahlen von 2 bis 20 auf der 
# Konsole ausgibt. Verwende dazu die `range(start, stop, step)`-Funktion, 
# um nur gerade Zahlen zu erzeugen.

'''
for zahl in range(2, 21,2):  # Start bei 2, Ende bei 20, Schrittweite von 2
    print(zahl)
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


