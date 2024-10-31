#              ____________________________
#       ______|                            |_____
#       \     |    3.2 WHILE-SCHLEIFE      |    /
#        )    |____________________________|   (
#       /________)                     (________\       28.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Die `while`-Schleife ist eine Schleifenart, die so lange läuft, wie eine 
# bestimmte Bedingung erfüllt ist. Das bedeutet, dass der enthaltene 
# Codeblock sich wiederholt, solange die Bedingung `True` (wahr) ist.
# Erst wenn die Bedingung `False` (falsch) wird, endet die Schleife.

# Die `while`-Schleife wird häufig verwendet, wenn wir nicht genau wissen, wie 
# oft eine Schleife ausgeführt werden muss. Hier ist die allgemeine Syntax 
# einer `while`-Schleife:

# Syntax:
# while Bedingung:
#     Codeblock (wird wiederholt, solange die Bedingung True ist)




# ____________________________________
#                                    /
# Beispiel für eine while-Schleife  (
# ___________________________________\

# In diesem Beispiel gibt die `while`-Schleife die Zahlen von 1 bis 5 aus.
# Die Bedingung lautet `counter <= 5`, und die Schleife wird beendet, sobald
# der Wert von `counter` größer als 5 ist.

counter = 1
while counter <= 5:
    print("Durchlauf Nummer:", counter)
    counter += 1

# In diesem Beispiel:
# - `counter` wird zu Beginn auf 1 gesetzt.
# - Die Schleife läuft, solange `counter` kleiner oder gleich 5 ist.
# - Bei jedem Durchlauf wird `counter` um 1 erhöht.




# ____________________________
#                            /
# Die Endlosschleife        (
# ___________________________\

# Es ist wichtig sicherzustellen, dass die Bedingung der `while`-Schleife
# irgendwann `False` wird, damit die Schleife endet. Andernfalls läuft die
# Schleife unendlich weiter und das Programm wird nicht beendet.

# Beispiel für eine Endlosschleife:

# while True:
#     print("Das läuft unendlich!")

# Ein häufiger Anwendungsfall ist eine Schleife, die eine bestimmte Bedingung
# so lange abfragt, bis sie erfüllt ist. Beispiel: Das Programm fragt so lange
# nach einem Passwort, bis das richtige eingegeben wird.




# ______________________________
#                              /
# Schleifen beenden mit break (
# _____________________________\

# Manchmal möchtest du eine `while`-Schleife gezielt beenden, obwohl die
# Bedingung noch wahr ist. Der `break`-Befehl beendet die Schleife sofort.

# Beispiel:
password = ""
while True:
    password = input("Gib das Passwort ein: ")

    if password == "geheim":
        print("Zugriff gewährt.")
        break
    else:
        print("Falsches Passwort. Versuch es noch einmal.")

# In diesem Beispiel:
# - Die Schleife fragt immer wieder nach dem Passwort.
# - Wenn das Passwort korrekt ist, beendet `break` die Schleife.




# _______________________________________________
#                                               /
# Schleifendurchlauf überspringen mit continue (
# ______________________________________________\

# Mit dem `continue`-Befehl kannst du den aktuellen Schleifendurchlauf
# überspringen und direkt zum nächsten übergehen. Der Code unter `continue`
# wird für diesen Durchlauf nicht ausgeführt.

# Beispiel:
zahl = 0
while zahl < 10:
    zahl += 1
    if zahl % 2 == 0:
        continue

    print("Ungerade Zahl:", zahl)

# In diesem Beispiel:
# - Die Schleife erhöht `zahl` bei jedem Durchlauf um 1.
# - Wenn `zahl` gerade ist, überspringt `continue` die Ausgabe.
# - Nur ungerade Zahlen werden ausgegeben.




# _______________________________________
#                                       /
# while-Schleifen für Benutzereingaben (
# ______________________________________\

# `while`-Schleifen sind nützlich, um den Benutzer wiederholt nach Eingaben zu fragen,
# bis eine gültige Antwort gegeben wird. Ein einfaches Beispiel wäre das Abfragen
# einer Zahl innerhalb eines bestimmten Bereichs.

# Beispiel: Zahl zwischen 1 und 10 abfragen
number = None

while True:
    number = int(input("Gib eine Zahl zwischen 1 und 10 ein: "))

    if number >= 1 or number <= 10:
        break
    
    print("Ungültige Eingabe. Versuch es erneut.")


print(f"Die gültige Zahl ist: {number}")

# Hier wird die Eingabe so lange wiederholt, bis eine Zahl zwischen 1 und 10 
# eingegeben wird.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Schreibe eine `while`-Schleife, die den Benutzer auffordert, eine Zahl einzugeben,
# die größer als 100 ist. Sobald der Benutzer dies tut, endet die Schleife.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/

# Schreibe eine `while`-Schleife, die Ali Baba vor einer verschlossenen Tür stehen lässt.
# Die Schleife soll den Benutzer wiederholt nach dem geheimen Codewort fragen.
# Solange der Benutzer nicht „Sesam öffne dich“ eingibt, bleibt die Tür geschlossen,
# und die Schleife fordert ihn erneut zur Eingabe auf.
# Sobald „Sesam öffne dich“ eingegeben wird, endet die Schleife und gibt die 
# Nachricht „Die Tür öffnet sich!“ aus.

# Beispiel:
# Eingabe: Lass mich rein
# Ausgabe: Falsches Codewort. Versuch es noch einmal.

# Eingabe: Sesam öffne dich
# Ausgabe: Die Tür öffnet sich!

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe eine `while`-Schleife, die von 1 bis 20 zählt und nur die Zahlen
# ausgibt, die nicht durch 3 teilbar sind. Verwende dazu den `continue`-Befehl.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 4  /
# __________/

# Erstelle eine `for`-Schleife, die alle Buchstaben in einem vom Benutzer
# eingegebenen Wort einzeln ausgibt, jedoch ohne den Buchstaben "a".

# Füge hier deine Lösung ein.





#   .::::.
# .::::::::.
# |'      `|
# |\      /|
# | \    / |
# \  \  /  /
#  \  \/  /      Schleifen sind praktisch :-)
#   \  \ /
#    \  \
#   / \  \
#  /  /\  \
# /  /  \  \
# | /    \ |
# |/      \|
# `        '
#  ___ _  _ ___  ___ 
# | __| \| |   \| __|
# | _|| .` | |) | _| 
# |___|_|\_|___/|___|
#                
# -=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=-=x=-=x=-=x=-=x=




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
# Schreibe eine `while`-Schleife, die den Benutzer auffordert, eine Zahl einzugeben,
# die größer als 100 ist. Sobald der Benutzer dies tut, endet die Schleife.

'''
number = 0
while number <= 100:
    number = int(input("Gib eine Zahl ein, die größer als 100 ist: "))

print("Vielen Dank! Die Schleife ist beendet.")
'''




# ___________
#            \
# Aufgabe 2  /
# __________/

# Schreibe eine `while`-Schleife, die Ali Baba vor einer verschlossenen Tür stehen lässt.
# Die Schleife soll den Benutzer wiederholt nach dem geheimen Codewort fragen.
# Solange der Benutzer nicht „Sesam öffne dich“ eingibt, bleibt die Tür geschlossen,
# und die Schleife fordert ihn erneut zur Eingabe auf.
# Sobald „Sesam öffne dich“ eingegeben wird, endet die Schleife und gibt die 
# Nachricht „Die Tür öffnet sich!“ aus.

# Beispiel:
# Eingabe: Lass mich rein
# Ausgabe: Falsches Codewort. Versuch es noch einmal.

# Eingabe: Sesam öffne dich
# Ausgabe: Die Tür öffnet sich!

'''
codewort = ""
while codewort != "Sesam öffne dich":
    codewort = input("Ali Baba spricht: ")
    if codewort != "Sesam öffne dich":
        print("Falsches Codewort. Die Tür bleibt verschlossen.")

print("Die Tür öffnet sich!")
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe eine `while`-Schleife, die von 1 bis 20 zählt und nur die Zahlen
# ausgibt, die nicht durch 3 teilbar sind. Verwende dazu den `continue`-Befehl.

'''
number = 1
while number <= 20:
    if number % 3 == 0:
        number += 1
        continue  # Überspringt die Ausgabe, wenn die Zahl durch 3 teilbar ist
    
    print(number)
    number += 1
'''




# ___________
#            \
# Aufgabe 4  /
# __________/

# Erstelle eine `for`-Schleife, die alle Buchstaben in einem vom Benutzer
# eingegebenen Wort einzeln ausgibt, jedoch ohne den Buchstaben "a".

'''
word = input("Gib ein Wort ein: ")

for letter in word:
    if letter.lower() == "a":
        continue  # Überspringt diesen Durchlauf, wenn der Buchstabe "a" ist

    print(letter)
'''
# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><
