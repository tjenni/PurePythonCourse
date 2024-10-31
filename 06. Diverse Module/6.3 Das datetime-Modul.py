#              ___________________________
#       ______|                           |_____
#       \     |   6.3 DAS DATETIME-MODUL  |    /
#        )    |___________________________|   (
#       /________)                    (________\       29.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Das `datetime`-Modul in Python ermöglicht uns, mit Daten und Zeiten zu arbeiten.
# Es bietet viele Funktionen zur Berechnung von Zeitdifferenzen, zum Formatieren von
# Datumsangaben und vielem mehr.


# ____________________________
#                            /
# Modul importieren         (
# ___________________________\

# Um das `datetime`-Modul zu verwenden, muss es zuerst importiert werden:

import datetime


# ____________________________
#                            /
# Aktuelles Datum und Zeit  (
# ___________________________\

# 1. `datetime.datetime.now()`: Gibt das aktuelle Datum und die aktuelle Uhrzeit zurück.
now = datetime.datetime.now()
print("Aktuelles Datum und Uhrzeit:", now)

# 2. `datetime.date.today()`: Gibt nur das aktuelle Datum zurück, ohne Uhrzeit.
today = datetime.date.today()
print("Heutiges Datum:", today)


# ____________________________
#                            /
# Datums- und Zeitobjekte   (
# ___________________________\

# Wir können eigene Datums- und Zeitobjekte erstellen, indem wir `datetime.date()`
# und `datetime.time()` verwenden:

# Beispiel: Erstellen eines Datumsobjekts für den 1. Januar 2023.
date = datetime.date(2023, 1, 1)
print("Erstelltes Datum:", date)

# Beispiel: Erstellen eines Zeitobjekts für 14:30:00.
time = datetime.time(14, 30, 0)
print("Erstellte Uhrzeit:", time)

# Beispiel: Kombinieren von Datum und Uhrzeit.
combined = datetime.datetime(2023, 1, 1, 14, 30, 0)
print("Erstelltes Datum und Uhrzeit:", combined)




# ____________________________
#                            /
# Zeitdifferenzen berechnen (
# ___________________________\

# Mit `datetime.timedelta` können wir Zeitspannen erstellen und Berechnungen
# mit Datums- und Zeitangaben durchführen.

# Beispiel: Berechnung des Datums in 7 Tagen
in_seven_days = today + datetime.timedelta(days=7)
print("Datum in 7 Tagen:", in_seven_days)

# Beispiel: Berechnung der Zeitspanne zwischen zwei Daten
date1 = datetime.date(2023, 1, 1)
date2 = datetime.date(2023, 1, 10)
difference = date2 - date1
print("Zeitdifferenz zwischen Datum1 und Datum2:", difference.days, "Tage")


# ___________________________
#                           /
# Datumsformatierung        (
# ___________________________\

# Mit `strftime()` können wir das Format von Datum und Zeit ändern. `strftime`
# erlaubt es uns, ein Datum in verschiedenen Formaten anzuzeigen.

# Beispiel: Formatieren des aktuellen Datums
date_formated = today.strftime("%d.%m.%Y")  # Ausgabe als Tag.Monat.Jahr
print("Formatiertes Datum:", date_formated)

# Beispiel: Uhrzeit in einem benutzerdefinierten Format
time_formated = now.strftime("%H:%M:%S")  # Ausgabe als Stunde:Minute:Sekunde
print("Formatiertes Uhrzeit:", time_formated)




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - `datetime.now()` gibt das aktuelle Datum und die Uhrzeit zurück.
#
# - `datetime.date()` und `datetime.time()` erlauben die Erstellung von Datums-
#   und Zeitobjekten.
#
# - `timedelta` wird verwendet, um Zeitspannen zu berechnen, z. B. den Unterschied
#   zwischen zwei Daten.
#
# - Mit `strftime()` können wir das Datum und die Uhrzeit in einem benutzerdefinierten
#   Format darstellen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Programm, das das aktuelle Datum und die aktuelle Uhrzeit anzeigt
# und den Benutzer fragt, wie viele Tage in die Zukunft berechnet werden sollen.
# Zeige dann das Datum in der Zukunft an.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Frage den Benutzer nach seinem Geburtsdatum (Jahr, Monat, Tag) und berechne
# sein aktuelles Alter in Jahren. Gib das Alter auf der Konsole aus.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Programm, das den Benutzer nach einem Datum im Format TT.MM.JJJJ fragt.
# Berechne, wie viele Tage zwischen diesem Datum und dem heutigen Datum liegen.


# Füge hier deine Lösung ein.




#           .-.-.
#      ((  (__I__)  ))
#        .'_....._'.
#       / / .12 . \ \
#      | | '  |  ' | |        Die verstehst nun, wie Python mit
#      | | 9  /  3 | |        Zeit und Datum arbeiten kann. 
#       \ \ '.6.' / /
#        '.`-...-'.'
#    jgs  /'-- --'\
#        `"""""""""`    
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
# Erstelle ein Programm, das das aktuelle Datum und die aktuelle Uhrzeit anzeigt
# und den Benutzer fragt, wie viele Tage in die Zukunft berechnet werden sollen.
# Zeige dann das Datum in der Zukunft an.

'''
now = datetime.now()
print("Aktuelles Datum und Uhrzeit:", now.strftime("%d.%m.%Y %H:%M:%S"))

days_in_future = int(input("Gib die Anzahl der Tage in die Zukunft ein: "))
future_date = aktuelles_datum + timedelta(days=days_in_future)
print("Datum in", days_in_future, "Tagen:", future_date.strftime("%d.%m.%Y"))
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Frage den Benutzer nach seinem Geburtsdatum (Jahr, Monat, Tag) und berechne
# sein aktuelles Alter in Jahren. Gib das Alter auf der Konsole aus.

'''
year = int(input("Gib dein Geburtsjahr ein (z.B. 2000): "))
month = int(input("Gib deinen Geburtsmonat ein (z.B. 5 für Mai): "))
day = int(input("Gib deinen Geburtstag ein (z.B. 15): "))

birthday = datetime(jahr, monat, tag)
now = datetime.now()

age = now.year - birthday.year
if (now.month, now.day) < (birthday.month, birthday.day):
    alter -= 1  # Abziehen, wenn der Geburtstag noch nicht war in diesem Jahr

print("Du bist", age, "Jahre alt.")
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Programm, das den Benutzer nach einem Datum im Format TT.MM.JJJJ fragt.
# Berechne, wie viele Tage zwischen diesem Datum und dem heutigen Datum liegen.

'''
date_input = input("Gib ein Datum im Format TT.MM.JJJJ ein: ")
date = datetime.strptime(datum_input, "%d.%m.%Y")
now = datetime.now().date()

days_difference = abs((now - date.date()).days)
print("Es liegen", days_difference, "Tage zwischen", date_input, "und dem heutigen Datum.")
'''



# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

