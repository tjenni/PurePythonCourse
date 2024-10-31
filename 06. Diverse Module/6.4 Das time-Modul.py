#              ___________________________
#       ______|                           |_____
#       \     |     6.4 DAS TIME-MODUL    |    /
#        )    |___________________________|   (
#       /________)                    (________\       29.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Das `time`-Modul in Python bietet Funktionen zur Arbeit mit Zeit und zur
# Messung von Zeitspannen. Es wird häufig genutzt, um Verzögerungen in
# Programmen einzubauen oder Laufzeiten zu messen.


# ___________________________
#                           /
# Modul importieren         (
# ___________________________\

# Um das `time`-Modul zu verwenden, muss es zuerst importiert werden:

import time


# ___________________________
#                           /
# Aktuelle Zeit             (
# ___________________________\

# 1. `time.time()`: Gibt die aktuelle Zeit in Sekunden seit dem "Unix-Zeitstempel"
#    (01.01.1970) zurück. Der Zeitstempel ist ein Zahlwert, der sich gut für die
#    Messung von Zeitdifferenzen eignet.
aktuelle_zeit = time.time()
print("Aktuelle Zeit in Sekunden seit 01.01.1970:", aktuelle_zeit)

# 2. `time.ctime()`: Konvertiert den Zeitstempel in ein lesbares Datum und eine Uhrzeit.
lesbare_zeit = time.ctime(aktuelle_zeit)
print("Lesbares Datum und Uhrzeit:", lesbare_zeit)


# ___________________________
#                           /
# Verzögerungen einbauen    (
# ___________________________\

# Mit `time.sleep(sekunden)` können wir eine Pause in unser Programm einbauen.
# Das Programm wird um die angegebene Anzahl von Sekunden verzögert.

print("Pause beginnt...")
time.sleep(2)  # 2 Sekunden Pause
print("Pause beendet.")


# ___________________________
#                           /
# Zeitmessung               (
# ___________________________\

# Das `time`-Modul kann verwendet werden, um die Ausführungszeit eines
# Programmabschnitts zu messen.

# Beispiel: Messung der Zeitspanne für einen Codeblock
startzeit = time.time()  # Startzeit
for i in range(1000000):  # Beispiel-Schleife
    pass
endzeit = time.time()  # Endzeit

# Berechnung der Zeitspanne
dauer = endzeit - startzeit
print("Dauer der Schleife:", dauer, "Sekunden")


# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - `time.time()` gibt den aktuellen Zeitstempel in Sekunden zurück, ideal zur
#   Zeitmessung.
#
# - `time.ctime()` konvertiert den Zeitstempel in ein lesbares Datum und Uhrzeit.
#
# - `time.sleep(sekunden)` erlaubt es, eine Verzögerung im Programm einzubauen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Schreibe ein Programm, das einen Countdown von 5 bis 1 anzeigt. Verwende `time.sleep()`,
# um eine Sekunde zwischen jeder Zahl zu warten. Sobald der Countdown endet,
# gib die Nachricht „Countdown beendet!“ aus.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Programm, das die Zeit in Sekunden misst, die der Benutzer benötigt,
# um auf die Eingabetaste zu drücken. Verwende dazu `time.time()` und gib die
# Zeitdifferenz aus.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe ein Programm, das den Benutzer nach einem Intervall in Sekunden fragt.
# Lasse das Programm dann in diesem Intervall eine Nachricht wie „Tick...“ anzeigen.
# Verwende dazu eine Schleife und `time.sleep()`.


# Füge hier deine Lösung ein.




#    +8-=-=-=-=-=-8+
#     | ,.-'"'-., |
#     |/         \|
#     |\:.     .:/|
#     | \:::::::/ |
#     |  \:::::/  |        Nun weisst du wie die Zeit vergeht. 
#     |   \:::/   |
#     |    ):(    |
#     |   / . \   |
#     |  /  .  \  |
#     | /   .   \ |
#     |/   .:.   \|
#     |\.:::::::./|
#     | '--___--' |
#    +8-=-=-=-=-=-8+
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
# Schreibe ein Programm, das einen Countdown von 5 bis 1 anzeigt. Verwende `time.sleep()`,
# um eine Sekunde zwischen jeder Zahl zu warten. Sobald der Countdown endet,
# gib die Nachricht „Countdown beendet!“ aus.

'''
print("Countdown beginnt:")
for second in range(5, 0, -1):
    print(second)
    time.sleep(1)  # Warten für eine Sekunde
print("Countdown beendet!")
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Programm, das die Zeit in Sekunden misst, die der Benutzer benötigt,
# um auf die Eingabetaste zu drücken. Verwende dazu `time.time()` und gib die
# Zeitdifferenz aus.

'''
input("Drücke die Eingabetaste, um zu starten...")
startzeit = time.time()  # Startzeit

input("Drücke die Eingabetaste, um zu stoppen...")
endzeit = time.time()  # Endzeit

reaktionszeit = endzeit - startzeit
print("Deine Reaktionszeit beträgt:", round(reaktionszeit, 2), "Sekunden.")
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe ein Programm, das den Benutzer nach einem Intervall in Sekunden fragt.
# Lasse das Programm dann in diesem Intervall eine Nachricht wie „Tick...“ anzeigen.
# Verwende dazu eine Schleife und `time.sleep()`.

'''
interval = int(input("Gib das Intervall in Sekunden ein: "))

print("Tick-Programm startet. Drücke Strg+C, um das Programm zu beenden.")
while True:
    print("Tick...")
    time.sleep(interval)
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


