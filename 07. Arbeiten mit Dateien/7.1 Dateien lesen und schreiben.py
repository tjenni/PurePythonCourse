#              _____________________________________
#       ______|                                     |_____
#       \     |   7.1 DATEIEN LESEN UND SCHREIBEN   |    /
#        )    |_____________________________________|   (
#       /________)                              (________\       29.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Python ermöglicht die Arbeit mit Dateien, was nützlich ist, um Daten dauerhaft
# zu speichern, z.B. Notizen, Benutzerinformationen oder Konfigurationen.
# In diesem Kapitel behandeln wir, wie Dateien geöffnet, gelesen, beschrieben
# und geschlossen werden.


# _____________________________
#                             /
# Datei öffnen und schließen (
# ____________________________\

# Mit der Funktion `open()` kann man eine Datei öffnen. 

# Die Syntax lautet:
#   open(dateiname, modus)
#
# Hierbei ist der `modus` entscheidend dafür, ob die Datei gelesen, beschrieben
# oder angehängt wird.

# Beispiele für Modi:
# - `"r"`: Lesen (Read) – öffnet die Datei nur zum Lesen
# - `"w"`: Schreiben (Write) – erstellt die Datei neu oder überschreibt sie
# - `"a"`: Anhängen (Append) – fügt neuen Inhalt am Ende der Datei hinzu
# - `"x"`: Erstellen (Create) – erstellt eine neue Datei und gibt einen Fehler zurück,
#   wenn die Datei bereits existiert

# Beispiel für das Erstellen und Schließen einer Datei
file = open("beispiel.txt", "w")  # Datei im Schreibmodus öffnen
file.write("Dies ist ein Testinhalt.")
file.close()  # Datei schließen




# ____________________________________
#                                    /
# Arbeiten mit dem `with`-Statement (
# ___________________________________\

# Um sicherzustellen, dass Dateien korrekt geschlossen werden, verwenden wir oft 
# das `with`-Statement. Dieses sorgt dafür, dass die Datei auch bei Fehlern 
# automatisch geschlossen wird.

# Beispiel: Eine Datei mit `with` öffnen und beschreiben
with open("beispiel.txt", "w") as file:
    file.write("Dies ist ein weiterer Testinhalt.\n")
    file.write("Mit dem with-Statement wird die Datei automatisch geschlossen.")




# ____________________________
#                            /
# Datei schreiben           (
# ___________________________\

# Der Schreibmodus `"w"` überschreibt den gesamten Inhalt der Datei. Um Text zu einer
# Datei hinzuzufügen, verwenden wir den Modus `"a"`.

# Beispiel: Text an eine Datei anhängen
with open("beispiel.txt", "a") as datei:
    datei.write("\nZusätzlicher Inhalt, der am Ende der Datei hinzugefügt wird.")




# ____________________________
#                            /
# Datei lesen               (
# ___________________________\

# Im Lesemodus `"r"` kann der Inhalt der Datei angezeigt werden.
# Methoden zur Anzeige von Inhalten:
# - `read()`: Gibt den gesamten Inhalt der Datei zurück
# - `readline()`: Liest eine Zeile aus der Datei
# - `readlines()`: Gibt alle Zeilen als Liste zurück

# Beispiel: Dateiinhalt mit `read()` anzeigen
with open("beispiel.txt", "r") as file:
    content = file.read()
    print("Dateiinhalt:", content)

# Beispiel: Zeilenweise mit `readlines()` lesen
with open("beispiel.txt", "r") as file:
    rows = file.readlines()
    print("Dateiinhalt als Liste von Zeilen:", rows)




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Verwende das `with`-Statement, um sicherzustellen, dass Dateien ordnungsgemäß
#   geschlossen werden.
#
# - Der Modus `"w"` überschreibt die Datei, während `"a"` neuen Inhalt anhängt.
#
# - `read()` liest die gesamte Datei, während `readline()` und `readlines()`
#   einzelne Zeilen lesen.





# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Programm, das eine neue Datei namens „notizen.txt“ erstellt und
# drei Zeilen Text speichert. Verwende dann ein zweites Programm, um den Inhalt
# der Datei anzuzeigen.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe ein Programm, das eine Datei „aufgaben.txt“ erstellt und fünf
# Aufgaben speichert. Nutze den Modus „a“, um zwei weitere Aufgaben anzuhängen.
# Zeige den gesamten Inhalt der Datei auf der Konsole an.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Programm, das eine Datei „log.txt“ erstellt und in einer
# Schleife jede Sekunde eine neue Zeile mit der aktuellen Uhrzeit hinzufügt.
# Das Programm soll nach fünf Einträgen enden.


# Füge hier deine Lösung ein.



#   .-------.
#   | -----.-----.
#   | -----| ----|\       Nun kannst du deine Daten 
#   | -----| ----- |      permanent in Dateien speichern. 
#   | -----| ----- |
#   '------| ----- |
#   mga    '-------'
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
# Erstelle ein Programm, das eine neue Datei namens „notizen.txt“ erstellt und
# drei Zeilen Text speichert. Verwende dann ein zweites Programm, um den Inhalt
# der Datei anzuzeigen.

'''
with open("notizen.txt", "w") as file:
    file.write("Erste Notiz.\n")
    file.write("Zweite Notiz.\n")
    file.write("Dritte Notiz.\n")

# Zweites Programm, um den Inhalt der Datei anzuzeigen
with open("notizen.txt", "r") as file:
    content = file.read()
    print("Inhalt der Datei 'notizen.txt':\n", content)
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Schreibe ein Programm, das eine Datei „aufgaben.txt“ erstellt und fünf
# Aufgaben speichert. Nutze den Modus „a“, um zwei weitere Aufgaben anzuhängen.
# Zeige den gesamten Inhalt der Datei auf der Konsole an.

'''
with open("aufgaben.txt", "w") as file:
    file.write("Aufgabe 1: Einkaufen gehen\n")
    file.write("Aufgabe 2: Mathe lernen\n")
    file.write("Aufgabe 3: Hausaufgaben machen\n")
    file.write("Aufgabe 4: Zimmer aufräumen\n")
    file.write("Aufgabe 5: Freunde anrufen\n")

# Anhängen von zwei weiteren Aufgaben an die Datei
with open("aufgaben.txt", "a") as file:
    file.write("Aufgabe 6: Sport machen\n")
    file.write("Aufgabe 7: Gitarre üben\n")

# Anzeigen des gesamten Inhalts der Datei
with open("aufgaben.txt", "r") as file:
    content = file.read()
    print("Inhalt der Datei 'aufgaben.txt':\n", content)
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Programm, das eine Datei „log.txt“ erstellt und in einer
# Schleife jede Sekunde eine neue Zeile mit der aktuellen Uhrzeit hinzufügt.
# Das Programm soll nach fünf Einträgen enden.

'''
with open("log.txt", "w") as file:
    for i in range(5):  # Schleife für 5 Einträge
        now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        file.write(f"Eintrag {i + 1}: {now}\n")
        print(f"Eintrag {i + 1}: {now}")  # Ausgabe zur Bestätigung
        time.sleep(1)  # Warte eine Sekunde
'''



# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><


