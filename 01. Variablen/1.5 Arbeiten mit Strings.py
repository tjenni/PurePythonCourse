#              ____________________________
#       ______|                            |_____
#       \     |  1.5 ARBEITEN MIT STRINGS  |    /
#        )    |____________________________|   (
#       /________)                     (________\       27.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
#  

# Ein String ist jede Art von Text, der zwischen Anführungszeichen steht.
# In diesem Kapitel lernst du, wie du Strings verbinden, verändern und 
# analysieren kannst.

# __________________________
#                           /
#  String-Operationen      (
# __________________________\

# Mit Strings kannst du verschiedene grundlegende Operationen durchführen,
# wie z. B. das Verbinden (Verkettung) oder Wiederholen.

# Verbinden (Verkettung) von Strings:
first_name = "Max"
last_name = "Mustermann"

full_name = first_name + " " + last_name  # Der Operator + verbindet Strings

print("Vollständiger Name:", full_name)


# Wiederholung eines Strings:
laugh = "Ha" * 3
print("Lachen:", laugh)  # Ausgabe: HaHaHa



# ________________________________
#                                /
# Länge eines Strings bestimmen (
# ______________________________\

# Die Funktion `len()` gibt die Länge eines Strings zurück, also die Anzahl
# der Zeichen im Text.
text = "Python"
print("Anzahl der Zeichen:", len(text))  # Ausgabe: 6



# _______________________________
#                               /
# Einzelne Zeichen und Slicing (
# ______________________________\

# Auf einzelne Zeichen eines Strings kannst du mit eckigen Klammern [] zugreifen.
# In Python beginnt die Zählung bei 0, also ist das erste Zeichen an der Position 0.

word = "Python"
print("Erstes Zeichen:", word[0])  # Ausgabe: P
print("Letztes Zeichen:", word[-1])  # Ausgabe: n

# Mit Slicing kannst du Teile eines Strings extrahieren, indem du die Start- 
# und Endposition angibst.
print("Erste drei Zeichen:", word[0:3])  # Ausgabe: Pyt
print("Zeichen 2 bis 4:", word[1:4])  # Ausgabe: yth



# _____________________________
#                              /
# Wichtige String-Methoden    (
# _____________________________\

# Strings haben viele eingebaute Methoden, die dir helfen, Text zu formatieren
# und zu bearbeiten. Hier sind einige wichtige Methoden:


# Grossbuchstaben und Kleinbuchstaben:
text = "Hallo Welt"
print("Grossbuchstaben:", text.upper())  # Ausgabe: HALLO WELT
print("Kleinbuchstaben:", text.lower())  # Ausgabe: hallo welt


# Leerzeichen entfernen:
text_with_spaces = "   Hallo   "
print("Ohne Leerzeichen:", text_with_spaces.strip())  # Ausgabe: Hallo


# Zeichen ersetzen:
greeting = "Hallo Welt"
print("Ersetzen:", greeting.replace("Welt", "Python"))  # Ausgabe: Hallo Python


# Position eines Wortes finden:
print("Position von 'Welt':", greeting.find("Welt"))  # Ausgabe: 6 (Index der Startposition)



# __________________________________
#                                  /
# Formatierte Strings (f-Strings) (
# _________________________________\

# Mit f-Strings kannst du Text und Variablen einfach kombinieren, indem du
# Variablen in geschweifte Klammern {} einfügst. Der f-String beginnt mit einem f.

name = "Max"
age = 20
print(f"Hallo, ich heisse {name} und bin {age} Jahre alt.")

# Ausgabe: Hallo, ich heisse Max und bin 20 Jahre alt.



# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Frage den Benutzer nach seinem Vor- und Nachnamen und gib eine formale
# Begrüssung aus, z. B.: "Hallo, Max Mustermann!"


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Lasse den Benutzer sein Lieblingswort eingeben und gib dieses fünfmal
# hintereinander wiederholt aus.
#
# Beispiel: Lieblingswort: Python
# Ausgabe: PythonPythonPythonPythonPython


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Frage den Benutzer nach einem Wort, wandle es in Grossbuchstaben um und
# ersetze alle Buchstaben "A" durch "@".
#
# Beispiel: Eingabe: "Apfel"
# Ausgabe: "@PFEL"


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 4  /
# __________/
#
# Frage den Benutzer nach Vor- und Nachnamen und gib die Initialen aus, z. B.:
# "M. M." für "Max Mustermann".
#
# Hinweis: Du kannst auf die ersten Buchstaben der Namen zugreifen und 
# sie mit "." kombinieren.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 5  /
# __________/
#
# Frage den Benutzer nach einem Passwort, entferne mögliche Leerzeichen am
# Anfang und Ende und gib die Länge des Passworts

# Füge hier deine Lösung ein.




# Gratuliere. Du bist nun ein/-e Text-Meister/-in.
#
# 
#        __...--~~~~~-._   _.-~~~~~--...__
#      //               `V'               \\ 
#     //                 |                 \\ 
#    //__...--~~~~~~-._  |  _.-~~~~~~--...__\\ 
#   //__.....----~~~~._\ | /_.~~~~----.....__\\
#  ====================\\|//====================
#                  dwb `---`
#
#  ___ _  _ ___  ___ 
# | __| \| |   \| __|
# | _|| .` | |) | _| 
# |___|_|\_|___/|___|
#                
# -=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-x=-=x=-=x=-=x=-x=



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

# Frage den Benutzer nach seinem Vor- und Nachnamen und gib eine formale Begrüssung aus.

'''
firstname = input("Wie ist dein Vorname? ")
name = input("Wie ist dein Nachname? ")

print(f"Hallo, {firstname} {name}!")
'''


# ___________
#            \
# Aufgabe 2  /
# __________/

# Lasse den Benutzer sein Lieblingswort eingeben und gib dieses fünfmal 
# hintereinander wiederholt aus.

'''
favourite_word = input("Was ist dein Lieblingswort? ")

print(favourite_word * 5)
'''


# ___________
#            \
# Aufgabe 3  /
# __________/

# Frage den Benutzer nach einem Wort, wandle es in Grossbuchstaben um und ersetze 
# alle "A"s durch "@".

'''
word = input("Gib ein Wort ein: ")
capital = word.upper().replace("A", "@")

print(capital)
'''


# ___________
#            \
# Aufgabe 4  /
# __________/

# Frage den Benutzer nach Vor- und Nachnamen und gib die Initialen aus.

'''
firstname = input("Wie ist dein Vorname? ")
name = input("Wie ist dein Nachname? ")

initials = f"{firstname[0].upper()}. {name[0].upper()}."
print(initials)
'''


# ___________
#            \
# Aufgabe 5  /
# __________/

# Frage den Benutzer nach einem Passwort, entferne mögliche Leerzeichen am Anfang 
# und Ende und gib die Länge des Passworts aus.

'''
password = input("Gib ein Passwort ein: ").strip()
length = len(password)

print(f"Die Länge des Passworts beträgt: {length}")
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><




