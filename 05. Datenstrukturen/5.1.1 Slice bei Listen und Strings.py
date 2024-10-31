#              _______________________________________
#       ______|                                       |_____
#       \     |   5.1.1 SLICE BEI LISTEN UND STRINGS  |    /
#        )    |_______________________________________|   (
#       /________)                                (________\       28.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Der Slice-Befehl erlaubt es uns, einen bestimmten Abschnitt einer Liste oder 
# einer Zeichenkette auszuwählen. Dabei verwenden wir Start- und Endindexe, 
# um genau festzulegen, welche Teile eines Objekts wir extrahieren wollen.

# Die allgemeine Syntax des Slice-Befehls sieht so aus:
# liste[start:end]  # Gibt die Elemente von `start` bis `end-1` zurück

# Das Start- und Endindex wird in eckigen Klammern `[ ]` angegeben und 
# durch einen Doppelpunkt `:` getrennt.


# ____________________________
#                            /
# Slice bei Listen          (
# ___________________________\

# Beispiel: Wir nehmen bestimmte Teile einer Liste.

colors = ["Rot", "Blau", "Grün", "Gelb", "Lila"]
print("Originale Liste:", colors)

# Elemente von Index 1 bis 3 (Blau, Grün, Gelb)
print("Farben von Index 1 bis 3:", colors[1:4])

# Alle Elemente bis zum Index 2 (Rot, Blau, Grün)
print("Farben bis Index 2:", colors[:3])

# Alle Elemente ab Index 2 (Grün, Gelb, Lila)
print("Farben ab Index 2:", colors[2:])




# ____________________________
#                            /
# Slice bei Strings         (
# ___________________________\

# Wir können den Slice-Befehl auch auf Zeichenketten anwenden, um bestimmte Teile eines Textes
# zu extrahieren. Zum Beispiel können wir die ersten paar Buchstaben eines Wortes auswählen.

word = "Programmieren"
print("Originales Wort:", word)

# Die ersten 6 Buchstaben (Progra)
print("Ersten 6 Buchstaben:", word[:6])

# Buchstaben von Index 3 bis 8 (gramm)
print("Buchstaben von Index 3 bis 8:", word[3:9])

# Letzte 4 Buchstaben (eren)
print("Letzte 4 Buchstaben:", word[-4:])




# ____________________________
#                            /
# Schritte im Slice         (
# ___________________________\

# Ein optionaler dritter Parameter im Slice gibt die Schrittweite an. Dies ist besonders
# nützlich, um z. B. jedes zweite Element auszuwählen oder eine Liste umzudrehen.

# Beispiel: Jeder zweite Buchstabe des Wortes
print("Jeder zweite Buchstabe:", word[::2])

# Die Liste `farben` in umgekehrter Reihenfolge
print("Liste in umgekehrter Reihenfolge:", colors[::-1])




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Der Slice-Befehl verwendet die Syntax `[start:end:schritte]`.
#
# - Der Endindex wird nicht eingeschlossen, d. h., `liste[1:3]` gibt die 
#   Elemente bei Index 1 und 2 zurück.
# 
# - Negative Indizes beginnen von hinten, z. B., -1 ist das letzte Element.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine Liste namens `daynames` mit den Elementen „Montag“ bis „Sonntag“.
# Erstelle mit Slice eine neue Liste, die nur das Wochenende enthält, und gib sie aus.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Zeichenkette `alphabeth` mit den Buchstaben "abcdefghijklmnopqrstuvwxyz".
# Verwende Slice, um die Buchstaben von "d" bis "j" auszuwählen und gib das Ergebnis aus.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Liste `numbers` mit den Zahlen 1 bis 10. Verwende Slice, um alle
# geraden Zahlen in einer neuen Liste auszugeben.


# Füge hier deine Lösung ein.




#                                        .:^
#                 ^                     /   :
#    '`.        /;/                    /    /
#    \  \      /;/                    /    /
#     \\ \    /;/                    /  ///
#      \\ \  /;/                    /  ///
#       \  \/_/____________________/    /
#        `/                         \  /
#    HZ  {  o                     o  }'     Du kannst nun Listen schneiden.    
#         \_________________________/
#         
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
# Erstelle eine Liste namens `daynames` mit den Elementen „Montag“ bis „Sonntag“.
# Erstelle mit Slice eine neue Liste, die nur das Wochenende enthält, und gib sie aus.

'''
daynames = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
weekend = daynames[5:]  # Extrahiert "Samstag" und "Sonntag"
print("Wochenende:", weekend)
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Zeichenkette `alphabet` mit den Buchstaben "abcdefghijklmnopqrstuvwxyz".
# Verwende Slice, um die Buchstaben von "d" bis "j" auszuwählen und gib das Ergebnis aus.

'''
alphabet = "abcdefghijklmnopqrstuvwxyz"
sub_alphabet = alphabet[3:10]  # Extrahiert die Buchstaben von Index 3 bis 9 (d bis j)
print("Buchstaben von d bis j:", sub_alphabet)
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine Liste `numbers` mit den Zahlen 1 bis 10. Verwende Slice, um alle
# geraden Zahlen in einer neuen Liste auszugeben.

'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = numbers[1::2]  # Wählt jedes zweite Element ab Index 1 (gerade Zahlen)
print("Gerade Zahlen:", even_numbers)
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><




