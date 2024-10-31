#              ____________________________
#       ______|                            |_____
#       \     |        9.4 LOGGING         |    /
#        )    |____________________________|   (
#       /________)                     (________\       30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Logging ist ein hilfreiches Werkzeug, um den Ablauf eines Programms zu überwachen
# und Fehler zu finden. Es ermöglicht die Aufzeichnung von Ereignissen und
# Fehlermeldungen in einem Programm, die dann zu Analysezwecken gespeichert und
# überprüft werden können.

# In Python gibt es das `logging`-Modul, das vielfältige Funktionen zur Verwaltung
# von Log-Nachrichten bietet. Diese Nachrichten können in der Konsole oder in einer
# Datei gespeichert werden und helfen Entwicklern, den Zustand und das Verhalten
# des Codes im Detail zu verstehen.


# ____________________________
#                            /
# Grundlagen des Logging    (
# ___________________________\

# Mit dem `logging`-Modul können verschiedene Log-Level für Nachrichten festgelegt
# werden. Hier sind die wichtigsten Level:

# - `DEBUG`: Detaillierte Informationen, hauptsächlich zur Diagnose.
#
# - `INFO`: Allgemeine Bestätigungen darüber, dass das Programm wie erwartet läuft.
#
# - `WARNING`: Ein Hinweis auf mögliche Probleme, die jedoch das Programm
#   nicht anhalten.
#
# - `ERROR`: Ein schwerwiegender Fehler, der eine Funktion oder einen Abschnitt
#   des Programms unterbrechen kann.
#
# - `CRITICAL`: Ein schwerwiegender Fehler, der das gesamte Programm stoppen könnte.

# Beispiel:
import logging

# Logging konfigurieren
logging.basicConfig(level=logging.DEBUG)

# Logging in Aktion
logging.debug("Dies ist eine Debug-Nachricht.")
logging.info("Dies ist eine Info-Nachricht.")
logging.warning("Dies ist eine Warnung.")
logging.error("Dies ist eine Fehlermeldung.")
logging.critical("Dies ist eine kritische Fehlermeldung.")

# **Erläuterung**:
# - Jede Nachricht wird mit ihrem entsprechenden Log-Level angezeigt, basierend
#   auf der eingestellten Stufe. Das `basicConfig()`-Setup legt fest, dass alle
#   Nachrichten ab `DEBUG` angezeigt werden.




# ____________________________
#                            /
# Log-Nachrichten in Datei  (
# ___________________________\

# Wir können Log-Nachrichten nicht nur in der Konsole anzeigen lassen, sondern auch
# in einer Datei speichern. Das ist besonders nützlich, um Log-Dateien nach Abschluss
# des Programms zu analysieren.

# Beispiel:
logging.basicConfig(filename="app.log", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("Programm gestartet.")
logging.warning("Dies ist eine Warnung!")
logging.error("Fehler im Programmablauf.")

# **Erläuterung**:
# - `filename="app.log"` speichert alle Log-Nachrichten in die Datei `app.log`.
# - Das `format`-Argument definiert das Format der Log-Ausgaben, hier mit Zeitstempel,
#   Log-Level und Nachricht.




# ____________________________
#                            /
# Log-Level konfigurieren   (
# ___________________________\

# Der Log-Level bestimmt, welche Nachrichten ausgegeben werden. Nachrichten unterhalb
# der festgelegten Stufe werden ignoriert.

logging.basicConfig(level=logging.WARNING)

# Beispiel mit verschiedenen Log-Leveln
logging.debug("Debug-Nachricht wird ignoriert.")
logging.info("Info-Nachricht wird ignoriert.")
logging.warning("Warnung wird angezeigt.")
logging.error("Fehler wird angezeigt.")
logging.critical("Kritischer Fehler wird angezeigt.")

# **Erläuterung**:
# - Da der Level auf `WARNING` gesetzt ist, werden nur Nachrichten ab `WARNING`
#   und höher angezeigt. Die `DEBUG`- und `INFO`-Nachrichten werden ignoriert.




# ____________________________
#                            /
# Log-Format anpassen       (
# ___________________________\

# Das Format von Log-Nachrichten kann angepasst werden, um spezifische Informationen
# wie Zeitstempel, Log-Level und die Nachricht selbst aufzunehmen.

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)
logging.info("Dies ist eine Info-Nachricht mit einem angepassten Format.")

# Beispiel eines erweiterten Formats:
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)
logging.warning("Warnung mit Zeitstempel und benutzerdefiniertem Format.")

# **Erläuterung**:
# - Das `format`-Argument legt fest, welche Details angezeigt werden.
# - `datefmt` definiert das Format des Zeitstempels.




# ____________________________
#                            /
# Erstellen von Loggern     (
# ___________________________\

# Wir können benannte Logger erstellen, um bestimmte Module oder Abschnitte des
# Codes gezielt zu überwachen.

# Beispiel:
logger = logging.getLogger("Sicherheits-Logger")
logger.setLevel(logging.ERROR)
logger.error("Dieser Fehler wurde von Sicherheits-Logger protokolliert.")

# **Erläuterung**:
# - Benannte Logger helfen, unterschiedliche Bereiche im Code zu trennen und zu verfolgen.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Verwende `logging.basicConfig()`, um das Standard-Logging zu konfigurieren.
#
# - Nutze verschiedene Log-Level (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`), 
#   um den Schweregrad anzugeben.
#
# - Speichere Logs in Dateien, um das Programmverhalten auch nach Beenden zu analysieren.
#
# - Passe das Log-Format an, um detaillierte Informationen zu erhalten.
#
# - Erstelle benannte Logger, um das Logging für verschiedene Module zu strukturieren.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Programm, das jede Sekunde eine zufällige Zahl generiert und in einer
# Log-Datei speichert. Verwende das `logging`-Modul und logge nur Zahlen über 50
# als `WARNING` und Zahlen über 80 als `ERROR`.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle ein Programm, das eine Datei öffnet und den Inhalt liest. Logge
# eine `INFO`-Nachricht bei erfolgreichem Öffnen, eine `ERROR`-Nachricht,
# wenn die Datei nicht existiert, und eine `CRITICAL`-Nachricht, wenn die
# Datei leer ist.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe eine Funktion `factorial_logger`, die die Fakultät einer Zahl berechnet
# und dabei das `logging`-Modul verwendet. Logge die Eingabe als `INFO`, die
# Berechnung bei jedem Schritt als `DEBUG` und einen `ERROR`, wenn die Eingabe
# negativ ist.


# Füge hier deine Lösung ein.



#                             ___.. _.-.
#                         _.-' ._.-' _.'
#                     _.-' ._.-'_..-'`.`.          Jetzt weisst du, wie man
#                  ,-',--.''_.-'_,_,     `.        Logfiles schreibt.
#                 '_,(._,'`-.._.-' \,_  `. \ 
#        _    \ _,'_,,`.  ,',  ``--'.       `-._
#   _   / `  ,'\     `._;,_ '        `      
#  / `  \   _   \  .     `-`-._       
#  \   _ `-' `.  `-'           `.__  
#   `-' `. __,'                    ``--.._
#     __,'
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
# Erstelle ein Programm, das jede Sekunde eine zufällige Zahl generiert und in einer
# Log-Datei speichert. Verwende das `logging`-Modul und logge nur Zahlen über 50
# als `WARNING` und Zahlen über 80 als `ERROR`.

'''
import logging
import random
import time

# Logging konfigurieren
logging.basicConfig(filename="random_numbers.log", level=logging.DEBUG, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def log_random_numbers():
    while True:
        number = random.randint(1, 100)
        if number > 80:
            logging.error(f"Generierte Zahl: {number}")
        elif number > 50:
            logging.warning(f"Generierte Zahl: {number}")
        else:
            logging.info(f"Generierte Zahl: {number}")
        time.sleep(1)

# Funktion starten
log_random_numbers()
'''




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Entwickle ein Programm, das eine Datei öffnet und den Inhalt liest. Logge
# eine `INFO`-Nachricht bei erfolgreichem Öffnen, eine `ERROR`-Nachricht,
# wenn die Datei nicht existiert, und eine `CRITICAL`-Nachricht, wenn die
# Datei leer ist.

'''
import logging

# Logging konfigurieren
logging.basicConfig(filename="file_access.log", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            if content:
                logging.info("Datei erfolgreich geöffnet.")
                print(content)
            else:
                logging.critical("Datei ist leer.")
    except FileNotFoundError:
        logging.error("Datei existiert nicht.")

# Datei lesen
read_file("example.txt")
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Schreibe eine Funktion `factorial_logger`, die die Fakultät einer Zahl berechnet
# und dabei das `logging`-Modul verwendet. Logge die Eingabe als `INFO`, die
# Berechnung bei jedem Schritt als `DEBUG` und einen `ERROR`, wenn die Eingabe
# negativ ist.

'''
import logging

# Logging konfigurieren
logging.basicConfig(filename="factorial.log", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def factorial_logger(n):
    if n < 0:
        logging.error("Negative Zahl eingegeben. Fakultät kann nicht berechnet werden.")
        return None
    result = 1
    logging.info(f"Berechnung der Fakultät von {n}")
    for i in range(1, n + 1):
        result *= i
        logging.debug(f"Zwischenergebnis für i={i}: {result}")
    return result

# Test der Funktion
print("Fakultät:", factorial_logger(5))  # Erwartete Ausgabe: 120
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

