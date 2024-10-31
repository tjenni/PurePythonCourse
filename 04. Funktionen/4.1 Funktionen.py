#              _____________________
#       ______|                     |_____
#       \     |   4.1 FUNKTIONEN    |    /
#        )    |_____________________|   (
#       /________)              (________\       28.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Funktionen sind ein zentraler Bestandteil der Programmierung. Sie ermöglichen 
# es uns, bestimmte Abschnitte des Codes zu bündeln und ihnen einen Namen zu geben. 
# Auf diese Weise können wir Aufgaben oder Berechnungen in Funktionen auslagern 
# und bei Bedarf immer wieder verwenden, ohne den Code neu schreiben zu müssen.

# In Python definieren wir eine Funktion mit dem Schlüsselwort `def`, gefolgt vom 
# Namen der Funktion und runden Klammern. Der Codeblock, der die eigentliche 
# Funktion ausführt, wird eingerückt unterhalb der Funktionsdefinition geschrieben.

# Die Syntax einer Funktion sieht wie folgt aus:

# def funktionsname():
#     Codeblock    # wird ausgeführt, wenn die Funktion aufgerufen wird

# Die Funktion wird aufgerufen, indem wir ihren Namen gefolgt von Klammern schreiben:
# funktionsname()  # Funktionsaufruf



# ____________________________
#                            /
# Beispiel einer Funktion   (
# ___________________________\

# Hier erstellen wir eine einfache Funktion, die den Text "Hallo, Welt!" ausgibt.

def hallo():
    print("Hallo, Welt!")

# Die Funktion `hallo()` gibt eine Begrüssung aus. Sie muss jedoch erst aufgerufen
# werden, damit der Code in ihr ausgeführt wird.

# Aufruf der Funktion:
hallo()




# ____________________________
#                            /
# Warum Funktionen nutzen?  (
# ___________________________\

# Funktionen helfen uns, den Code übersichtlicher zu gestalten und wiederverwendbare
# Bausteine zu erstellen. Anstatt denselben Code mehrmals zu schreiben, legen wir
# ihn einfach in einer Funktion ab und rufen diese auf, wann immer wir die Aktion
# ausführen wollen.

# Beispiel: Eine Funktion zur Berechnung des Quadrats einer Zahl
def quadrat():
    zahl = int(input("Gib eine Zahl ein: "))
    ergebnis = zahl * zahl
    print(f"Das Quadrat der Zahl ist: {ergebnis}")

# Aufruf der Funktion
quadrat()




# ____________________________
#                            /
# Funktionen mit Parametern (
# ___________________________\

# Funktionen können auch Werte als Eingabe erhalten. Diese Eingabewerte nennt man
# Parameter. In der Funktion wird der Parameter wie eine Variable behandelt.

# Beispiel: Eine Funktion, die das Quadrat einer Zahl berechnet, die wir ihr übergeben.

def quadrat_mit_parameter(zahl):
    ergebnis = zahl * zahl
    print(f"Das Quadrat von {zahl} ist: {ergebnis}")

# Wir übergeben beim Aufruf eine Zahl als Argument:
quadrat_mit_parameter(5)
quadrat_mit_parameter(10)

# Hier sehen wir, dass die Funktion `quadrat_mit_parameter()` flexibel ist und 
# mit verschiedenen Werten arbeiten kann, ohne dass der Code geändert werden muss.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# Verwende Funktionen, wenn:
# - Eine bestimmte Aufgabe mehrfach im Programm ausgeführt wird.

# - Der Code übersichtlich und strukturiert sein soll.

# - Du Werte verarbeiten und Berechnungen kapseln möchtest, die später 
#   wiederverwendbar sind.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Schreibe eine Funktion namens `greeting`, die den Benutzer nach seinem Namen fragt
# und dann eine Begrüssung ausgibt, z. B.: „Hallo, Max!“
# Verwende die Funktion, um einen beliebigen Namen zu begrüssen.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Funktion namens `double`, die eine Zahl als Parameter erhält und 
# das Doppelte dieser Zahl auf der Konsole ausgibt. Rufe die Funktion mit verschiedenen 
# Werten auf, um das Ergebnis zu sehen.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe eine Funktion namens `addition`, die zwei Zahlen als Parameter erhält
# und deren Summe berechnet. Die Funktion soll das Ergebnis auf der Konsole ausgeben.


# Füge hier deine Lösung ein.



#    .----------------.
#   /    _H______H_    \@,
#   \____/        \____/ @,
#      /            \    `@
#      |  LI LI LI  |    ,@      Du hast es geschafft eine Funktion
#      |  LI LI LI  |   ,@'      anzurufen, ähh aufzurufen.
#      |  LI LI LI  |  ,@'
#      |  LI LI LI  |@@'
#  jgs \            /'
#       `----------'
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
# Schreibe eine Funktion namens `greeting`, die den Benutzer nach seinem Namen fragt
# und dann eine Begrüssung ausgibt, z. B.: „Hallo, Max!“
# Verwende die Funktion, um einen beliebigen Namen zu begrüssen.

'''
def greeting():
    name = input("Wie heisst du? ")
    print(f"Hallo, {name}!")

# Aufruf der Funktion
greeting()
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Funktion namens `double`, die eine Zahl als Parameter erhält und 
# das Doppelte dieser Zahl auf der Konsole ausgibt. Rufe die Funktion mit verschiedenen 
# Werten auf, um das Ergebnis zu sehen.

'''
def double(number):
    result = number * 2
    print(f"Das Doppelte von {number} ist {result}")

# Aufrufe der Funktion mit verschiedenen Werten
double(5)
double(10)
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe eine Funktion namens `addition`, die zwei Zahlen als Parameter erhält
# und deren Summe berechnet. Die Funktion soll das Ergebnis auf der Konsole ausgeben.

'''
def addition(number1, number1):
    result = number1 + number2
    print(f"Die Summe von {number1} und {number2} ist {result}")

# Aufruf der Funktion
addition(3, 7)
addition(15, 20)
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

