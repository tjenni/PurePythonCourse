#              _____________________________________
#       ______|                                     |_____
#       \     |   2.3 VERSCHACHTELTE VERZWEIGUNGEN  |    /
#        )    |_____________________________________|   (
#       /________)                              (________\       27.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Bisher haben wir einfache Verzweigungen kennengelernt, bei denen nur eine
# Bedingung geprüft wird. Manchmal ist es aber nötig, mehrere Bedingungen
# nacheinander zu prüfen, um eine Entscheidung zu treffen.
# Verschachtelte Bedingungen (oder „geschachtelte Verzweigungen“) erlauben es uns,
# innerhalb einer Bedingung weitere Prüfungen durchzuführen.


# _________________________________
#                                 /
# Beispiel einer Verschachtelung (
# ________________________________\

# Stellen wir uns eine Entscheidung vor, ob jemand einen bestimmten Park betreten
# darf. Der Zugang zum Park ist nur Personen erlaubt, die über 18 Jahre alt sind
# und eine Mitgliedskarte besitzen.

age = 20
has_membership = True

if age >= 18:
    if has_membership:
        print("Willkommen im Park!")
    else:
        print("Leider ist der Zugang nur mit Mitgliedskarte erlaubt.")
else:
    print("Zugang nur für Erwachsene ab 18 Jahren.")

# Hier prüfen wir zuerst, ob die Person mindestens 18 Jahre alt ist. Wenn das
# zutrifft, wird innerhalb dieser Bedingung eine zweite Bedingung geprüft, ob
# die Person eine Mitgliedskarte hat. Nur wenn beide Bedingungen erfüllt sind,
# wird die Begrüßung ausgegeben.


# _____________________________
#                             /
# Struktur und Einrückungen  (
# ____________________________\

# Die Einrückung ist besonders wichtig bei verschachtelten Bedingungen.
# Jede neue Ebene wird weiter eingerückt, damit Python die Struktur richtig
# erkennt und damit der Code für uns besser lesbar ist.

# Syntax:
# if Bedingung1:
#     if Bedingung2:
#         Codeblock (wird ausgeführt, wenn beide Bedingungen wahr sind)
#     else:
#         Codeblock (wird ausgeführt, wenn Bedingung1 wahr, aber Bedingung2 falsch ist)
# else:
#     Codeblock (wird ausgeführt, wenn Bedingung1 falsch ist)

# ___________________________
#                           /
# Beispiele zur Anwendung  (
# __________________________\


# Beispiel 1: Wetterentscheidung

weather = "regnerisch"
temperature = 10

if weather == "regnerisch":
    if temperature < 15:
        print("Es ist kalt und regnerisch. Nimm einen Mantel und einen Regenschirm.")
    else:
        print("Es ist regnerisch, aber warm. Ein Regenschirm reicht aus.")
else:
    if temperature > 20:
        print("Es ist sonnig und warm. Eine Sonnenbrille wäre gut.")
    else:
        print("Es ist sonnig, aber nicht zu warm. Genieße das Wetter!")

# Hier werden zwei Bedingungen verschachtelt: Zuerst prüfen wir das Wetter.
# Ist es regnerisch, entscheiden wir weiter anhand der Temperatur.



# Beispiel 2: Prüfung im Schulalltag

is_present = True
has_done_homework = False

if is_present:
    if has_done_homework:
        print("Super, du bist gut vorbereitet!")
    else:
        print("Du bist anwesend, aber die Hausaufgaben fehlen.")
else:
    print("Du bist heute nicht anwesend.")

# In diesem Beispiel wird zuerst geprüft, ob der Schüler anwesend ist.
# Nur wenn er anwesend ist, prüfen wir, ob die Hausaufgaben erledigt wurden.



# ____________________________
#                             /
# Übungsaufgaben             (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Frage den Benutzer nach dem Wetter und der Temperatur.
# Gib passende Hinweise aus, ob ein Regenschirm, ein Mantel oder eine Sonnenbrille
# benötigt wird.


# Füge hier deine Lösung ein.



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Frage den Benutzer nach seinem Alter und ob er eine Mitgliedskarte besitzt.
# Entscheide je nach Eingabe, ob er freien Eintritt, ermäßigten Eintritt oder
# den vollen Preis zahlen muss:
# - Unter 18 Jahre mit Mitgliedskarte: freier Eintritt.
# - Unter 18 Jahre ohne Mitgliedskarte: ermäßigter Eintritt.
# - Über 18 Jahre mit Mitgliedskarte: ermäßigter Eintritt.
# - Über 18 Jahre ohne Mitgliedskarte: voller Eintritt.


# Füge hier deine Lösung ein.



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Lasse den Benutzer eine Spielfigur auswählen: „Ritter“ oder „Magier“.
# Danach lässt du ihn eine Waffe auswählen: „Schwert“, „Bogen“ oder „Zauberstab“.
# Gib basierend auf den beiden Entscheidungen eine kurze Beschreibung des Kampfstils aus.
# Beispiel:
# - Ritter + Schwert: „Du kämpfst mutig mit deinem Schwert.“
# - Magier + Zauberstab: „Du zauberst mächtige Sprüche mit deinem Stab.“
# - usw.


# Füge hier deine Lösung ein.




# Wenn du alle Aufgaben gelöst hast, bekommst du von mir
# die folgende Auszeichnung.
#
#               ____.----.
#     ____.----'          \
#     \                    \
#      \                    \
#       \                    \
#        \          ____.----'`--.__
#         \___.----'          |     `--.____
#        /`-._                |       __.-' \
#       /     `-._            ___.---'       \
#      /          `-.____.---'                \
#     /            / | \                       \
#    /            /  |  \                   _.--'
#    `-.         /   |   \            __.--'
#       `-._    /    |    \     __.--'     |
#         | `-./     |     \_.-'           |
#         |          |                     |
#         |          |  Verschachtelungs-  |
#         |          |     expert/-in      |
#         |          |                     |
#         |          |                     |   VK
#         |          |                     |
#  _______|          |                     |_______________
#         `-.        |                  _.-'
#            `-.     |           __..--'
#               `-.  |      __.-'
#                  `-|__.--'
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

# Frage den Benutzer nach dem Wetter und der Temperatur.
# Gib passende Hinweise aus, ob ein Regenschirm, ein Mantel oder eine Sonnenbrille
# benötigt wird.

'''
wetter = input("Wie ist das Wetter? (sonnig/regnerisch): ").lower()
temperatur = int(input("Wie ist die Temperatur? (in Grad Celsius): "))

if wetter == "regnerisch":
    if temperatur < 15:
        print("Es ist kalt und regnerisch. Nimm einen Mantel und einen Regenschirm.")
    else:
        print("Es ist regnerisch, aber warm. Ein Regenschirm reicht aus.")
elif wetter == "sonnig":
    if temperatur > 20:
        print("Es ist sonnig und warm. Eine Sonnenbrille wäre gut.")
    else:
        print("Es ist sonnig, aber nicht zu warm. Genieße das Wetter!")
else:
    print("Wettertyp unbekannt, bitte nur 'sonnig' oder 'regnerisch' eingeben.")
'''


# ___________
#            \
# Aufgabe 2  /
# __________/

# Frage den Benutzer nach seinem Alter und ob er eine Mitgliedskarte besitzt.
# Entscheide je nach Eingabe, ob er freien Eintritt, ermäßigten Eintritt oder
# den vollen Preis zahlen muss.

'''
alter = int(input("Wie alt bist du? "))
mitgliedskarte = input("Besitzt du eine Mitgliedskarte? (ja/nein): ").lower()

if alter < 18:
    if mitgliedskarte == "ja":
        print("Freier Eintritt.")
    else:
        print("Ermäßigter Eintritt.")
else:
    if mitgliedskarte == "ja":
        print("Ermäßigter Eintritt.")
    else:
        print("Voller Eintrittspreis.")
'''


# ___________
#            \
# Aufgabe 3  /
# __________/

# Lasse den Benutzer eine Spielfigur auswählen: „Ritter“ oder „Magier“.
# Danach lässt du ihn eine Waffe auswählen: „Schwert“, „Bogen“ oder „Zauberstab“.
# Gib basierend auf den beiden Entscheidungen eine kurze Beschreibung des Kampfstils aus.

'''
figur = input("Wähle deine Spielfigur (Ritter/Magier): ").capitalize()
waffe = input("Wähle deine Waffe (Schwert/Bogen/Zauberstab): ").capitalize()

if figur == "Ritter":
    if waffe == "Schwert":
        print("Du kämpfst mutig mit deinem Schwert.")
    elif waffe == "Bogen":
        print("Du zielst mit ruhiger Hand und schießt deinen Pfeil ab.")
    else:
        print("Diese Waffe passt nicht zu einem Ritter.")

elif figur == "Magier":
    if waffe == "Zauberstab":
        print("Du zauberst mächtige Sprüche mit deinem Stab.")
    elif waffe == "Bogen":
        print("Als Magier meisterst du auch den Bogen.")
    else:
        print("Diese Waffe passt nicht zu einem Magier.")
else:
    print("Unbekannte Spielfigur gewählt.")
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


