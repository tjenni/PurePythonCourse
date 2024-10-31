#              _______________________________
#       ______|                               |_____
#       \     |    2.2 LOGISCHE OPERATORIEN   |    /
#        )    |_______________________________|   (
#       /________)                        (________\       27.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# Logische Operatoren helfen dir, mehrere Bedingungen miteinander zu kombinieren.
# So kannst du komplexe Entscheidungen in deinem Programm treffen.
# In Python gibt es drei grundlegende logische Operatoren: `and`, `or` und `not`.


# ______________________________
#                               /
# Der `and`-Operator           (
# ______________________________\

# Der `and`-Operator (UND) kombiniert zwei Bedingungen und gibt `True` (wahr) zurück,
# wenn beide Bedingungen wahr sind. Ist auch nur eine Bedingung falsch, ergibt `and` False.
# Beispiel:

age = 20
has_license = True

if age >= 18 and has_license:
    print("Du darfst Auto fahren.")
else:
    print("Du darfst kein Auto fahren.")

# Hier sind beide Bedingungen erfüllt (Alter mindestens 18 und Führerschein vorhanden),
# daher wird "Du darfst Auto fahren." ausgegeben.

# Hier ist die Wahrheitstabelle für den `and`-Operator:

# | Bedingung A | Bedingung B | A and B |
# |-------------|-------------|---------|
# |    False    |    False    |  False  |
# |    True     |    False    |  False  |
# |    False    |    True     |  False  |
# |    True     |    True     |  True   |



# ______________________________
#                               /
# Der `or`-Operator            (
# ______________________________\

# Der `or`-Operator (ODER) gibt `True` zurück, wenn mindestens eine der Bedingungen
# wahr ist. Nur wenn beide Bedingungen `False` sind, gibt `or` ebenfalls `False` zurück.
# Beispiel:

is_student = True
is_senior = False

if is_student or is_senior:
    print("Du bekommst einen Rabatt.")
else:
    print("Kein Rabatt für dich.")

# Hier ist `is_student` wahr, daher gibt der Code "Du bekommst einen Rabatt." aus,
# selbst wenn `is_senior` falsch ist.

# Hier ist die Wahrheitstabelle für den `or`-Operator:

# | Bedingung A | Bedingung B | A or B |
# |-------------|-------------|--------|
# |    False    |    False    |  False |
# |    True     |    False    |  True  |
# |    False    |    True     |  True  |
# |    True     |    True     |  True  |



# ______________________________
#                               /
# Der `not`-Operator           (
# ______________________________\

# Der `not`-Operator (NICHT) kehrt den Wert einer Bedingung um:
# `True` wird zu `False` und `False` wird zu `True`.
# Beispiel:

has_access = False

if not has_access:
    print("Zugriff verweigert.")
else:
    print("Zugriff gewährt.")

# Da `has_access` hier `False` ist, macht `not` daraus `True`, und die Ausgabe
# lautet "Zugriff verweigert."

# Hier ist die Wahrheitstabelle für den `not`-Operator:

# | Bedingung A | not A |
# |-------------|-------|
# |    False    | True  |
# |    True     | False |



# _______________________________
#                                /
# Beispiele für Kombinationen   (
# _______________________________\

# Mit den logischen Operatoren kannst du komplexe Bedingungen formulieren.
# Hier sind zusätzliche Beispiele zur Vertiefung.


# Beispiel 1: Überprüfe, ob das Alter zwischen 13 und 17 liegt.

age = 14

if age >= 13 and age <= 17:
    print("Du bist ein Teenager.")
else:
    print("Du bist kein Teenager.")

# Hier kombiniert `and` die beiden Bedingungen, um festzustellen, ob das Alter in
# dem gewünschten Bereich liegt.


# Beispiel 2: Überprüfung, ob eine Jahreszahl ein Schaltjahr ist.

jahr = 2024

if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
    print(f"{jahr} ist ein Schaltjahr.")
else:
    print(f"{jahr} ist kein Schaltjahr.")

# Diese Bedingung kombiniert `and` und `or`, um zu prüfen, ob eine 
# Jahreszahl die Kriterien für ein Schaltjahr erfüllt.



# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Frage den Benutzer, ob er Schüler oder Student ist („ja“ oder „nein“),
# und ob er unter 26 ist. Gib die Nachricht „Du bekommst einen Rabatt.“
# aus, wenn er mindestens eine der beiden Bedingungen erfüllt.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Frage den Benutzer nach einer Zahl. Gib die Nachricht „Die Zahl liegt
# zwischen 1 und 10“ nur dann aus, wenn die Zahl größer oder gleich 1 und
# kleiner oder gleich 10 ist.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Frage den Benutzer, ob er eine Mitgliedskarte besitzt („ja“ oder „nein“)
# und ob er heute Geburtstag hat („ja“ oder „nein“). Gib eine Nachricht aus,
# die die Kombination der Antworten berücksichtigt:
# - „Du bekommst einen Geburtstagsbonus und Mitgliedsrabatt!“
# - „Du bekommst einen Mitgliedsrabatt.“
# - „Du bekommst einen Geburtstagsbonus!“
# - „Kein Rabatt verfügbar.“


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 4  /
# __________/
#
# Frage den Benutzer nach einer Zahl und gib aus, ob sie „positiv und gerade“,
# „positiv und ungerade“, „negativ und gerade“ oder „negativ und ungerade“ ist.
# Hinweis: Eine Zahl ist gerade, wenn zahl % 2 == 0.


# Füge hier deine Lösung ein.




# Wenn du alle Aufgaben gelöst hast, bekommst du von mir
# die folgende Auszeichnung.
#
#    ,_       
#  ,'  `\,_   
#  |_,-'_)          Logik
#  /##c '\  (       Detektiv/-in
# ' |'  -{.  )
#   /\__-' \[]
#  /`-_`\     
#  '     \    
# hjm
#
#  ___ _  _ ___  ___ 
# | __| \| |   \| __|
# | _|| .` | |) | _| 
# |___|_|\_|___/|___|
#                
# -=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-




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

# Frage den Benutzer, ob er Schüler oder Student ist („ja“ oder „nein“),
# und ob er unter 26 ist. Gib die Nachricht „Du bekommst einen Rabatt.“
# aus, wenn er mindestens eine der beiden Bedingungen erfüllt.

'''
schueler_student = input("Bist du Schüler oder Student? (ja/nein): ").lower()
alter = int(input("Wie alt bist du? "))

if schueler_student == "ja" or alter < 26:
    print("Du bekommst einen Rabatt.")
else:
    print("Kein Rabatt verfügbar.")
'''

# ___________
#            \
# Aufgabe 2  /
# __________/

# Frage den Benutzer nach einer Zahl. Gib die Nachricht „Die Zahl liegt
# zwischen 1 und 10“ nur dann aus, wenn die Zahl größer oder gleich 1 und
# kleiner oder gleich 10 ist.

'''
zahl = int(input("Gib eine Zahl ein: "))

if zahl >= 1 and zahl <= 10:
    print("Die Zahl liegt zwischen 1 und 10.")
else:
    print("Die Zahl liegt nicht im Bereich von 1 bis 10.")
'''

# ___________
#            \
# Aufgabe 3  /
# __________/

# Frage den Benutzer, ob er eine Mitgliedskarte besitzt („ja“ oder „nein“)
# und ob er heute Geburtstag hat („ja“ oder „nein“). Gib eine Nachricht aus,
# die die Kombination der Antworten berücksichtigt.

'''
mitgliedskarte = input("Besitzt du eine Mitgliedskarte? (ja/nein): ").lower()
geburtstag = input("Hast du heute Geburtstag? (ja/nein): ").lower()

if mitgliedskarte == "ja" and geburtstag == "ja":
    print("Du bekommst einen Geburtstagsbonus und Mitgliedsrabatt!")
elif mitgliedskarte == "ja":
    print("Du bekommst einen Mitgliedsrabatt.")
elif geburtstag == "ja":
    print("Du bekommst einen Geburtstagsbonus!")
else:
    print("Kein Rabatt verfügbar.")
'''

# ___________
#            \
# Aufgabe 4  /
# __________/

# Frage den Benutzer nach einer Zahl und gib aus, ob sie „positiv und gerade“,
# „positiv und ungerade“, „negativ und gerade“ oder „negativ und ungerade“ ist.

'''
zahl = int(input("Gib eine Zahl ein: "))

if zahl > 0:
    if zahl % 2 == 0:
        print("Die Zahl ist positiv und gerade.")
    else:
        print("Die Zahl ist positiv und ungerade.")
elif zahl < 0:
    if zahl % 2 == 0:
        print("Die Zahl ist negativ und gerade.")
    else:
        print("Die Zahl ist negativ und ungerade.")
else:
    print("Die Zahl ist null.")
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><










