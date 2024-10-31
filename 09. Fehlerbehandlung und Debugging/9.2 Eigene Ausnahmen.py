#              ______________________________
#       ______|                              |_____
#       \     |     9.2 EIGENE AUSNAHMEN     |    /
#        )    |______________________________|   (
#       /________)                       (________\       30.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# In Python kannst du eigene Fehler oder Ausnahmen definieren, die auf spezielle
# Situationen in deinem Programm hinweisen. Eigene Ausnahmen helfen, den Code
# klarer und besser nachvollziehbar zu gestalten, da sie gezielt auf die Bedürfnisse
# des Programms zugeschnitten sind.

# Um eine eigene Ausnahme zu erstellen, erstellst du eine Klasse, die von der
# eingebauten Klasse `Exception` erbt.


# ____________________________
#                            /
# Eigene Ausnahme erstellen (
# ___________________________\

# Um eine eigene Ausnahme zu erstellen, definierst du eine Klasse, die von `Exception`
# abgeleitet wird. Dabei kannst du zusätzliche Informationen und Funktionen hinzufügen,
# die für deine Ausnahme nützlich sind.

# Beispiel:
class NegativeNumberError(Exception):
    """Diese Ausnahme wird ausgelöst, wenn eine Zahl negativ ist."""
    def __init__(self, number):
        super().__init__(f"Unerlaubte Eingabe: {number} ist eine negative Zahl.")
        self.number = number

# Funktion zur Verwendung der Ausnahme
def berechne_wurzel(number):
    if number < 0:
        raise NegativeNumberError(number)
    return number ** 0.5

try:
    result = berechne_wurzel(-5)

except NegativeNumberError as e:
    print(e)

# **Erläuterung**:
# - `NegativeNumberError` erbt von `Exception`.
# - Bei einer negativen Zahl wird `NegativeNumberError` ausgelöst, und es
#   erscheint eine benutzerdefinierte Fehlermeldung.




# _______________________________
#                               /
# Weitere angepasste Ausnahmen (
# ______________________________\

# Du kannst beliebig viele angepasste Ausnahmen definieren. Jede Ausnahme
# kann sich auf ein spezielles Problem oder eine bestimmte Bedingung beziehen.

class ScoreOutOfRangeError(Exception):
    """Diese Ausnahme wird ausgelöst, wenn ein Punktestand außerhalb des Bereichs liegt."""
    def __init__(self, score):
        super().__init__(f"Punktestand {score} liegt außerhalb des zulässigen Bereichs (0-100).")
        self.score = score

# Beispiel für eine Funktion, die nur Punktestände zwischen 0 und 100 akzeptiert
def punkte_pruefen(score):
    if not (0 <= score <= 100):
        raise ScoreOutOfRangeError(score)
    print(f"Punktestand {score} ist gültig.")

try:
    punkte_pruefen(120)
except ScoreOutOfRangeError as e:
    print(e)

# **Erläuterung**:
# - `ScoreOutOfRangeError` wird ausgelöst, wenn der Punktestand nicht zwischen 0 und 100 liegt.




# ____________________________
#                            /
# Fehler weiterleiten       (
# ___________________________\

# Manchmal möchte man eine eigene Ausnahme definieren, um den Fehler genauer
# zu spezifizieren, aber auch eine Standard-Ausnahme beibehalten.
# Beispiel: Wenn die Eingabe keine Zahl ist, wird `ValueError` ausgelöst und
# dann von der eigenen Ausnahme `NotANumberError` weitergeleitet.

class NotANumberError(Exception):
    """Diese Ausnahme wird ausgelöst, wenn die Eingabe keine Zahl ist."""
    def __init__(self, input_value):
        super().__init__(f"Die Eingabe '{input_value}' ist keine gültige Zahl.")

def eingabe_als_zahl(input_value):
    try:
        return int(input_value)
    except ValueError:
        raise NotANumberError(input_value)

try:
    eingabe_als_zahl("abc")
except NotANumberError as e:
    print(e)

# **Erläuterung**:
# - `NotANumberError` wird durch eine fehlerhafte Eingabe ausgelöst und
#   übergibt die Details des Fehlers an die benutzerdefinierte Ausnahme.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Eigene Ausnahmen erstellst du, indem du eine Klasse schreibst, die 
#   von `Exception` erbt.
#
# - Benenne deine eigenen Ausnahmen aussagekräftig und präzise, damit die Fehler
#   im Programm leichter zu verstehen sind.
#
# - Verwende den `raise`-Befehl, um eigene Ausnahmen auszulösen, wenn bestimmte
#   Bedingungen nicht erfüllt sind.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\

# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Schreibe eine Klasse `EvenNumberError`, die ausgelöst wird, wenn eine Zahl
# gerade ist. Erstelle eine Funktion, die eine Zahl akzeptiert und die Ausnahme
# auslöst, wenn die Zahl gerade ist. Teste die Funktion, indem du sie mit einer
# geraden Zahl aufrufst.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Klasse `TemperatureTooHighError`, die ausgelöst wird, wenn eine
# Temperatur den Wert von 100°C überschreitet. Erstelle eine Funktion, die
# eine Temperatur akzeptiert und die Ausnahme auslöst, wenn der Wert zu hoch ist.
# Teste die Funktion, indem du eine Temperatur über 100°C eingibst.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Entwickle eine Klasse `PasswordTooShortError`, die ausgelöst wird, wenn ein Passwort
# weniger als 8 Zeichen hat. Schreibe eine Funktion, die ein Passwort überprüft
# und die Ausnahme auslöst, wenn es zu kurz ist. Teste die Funktion, indem du
# ein zu kurzes Passwort eingibst.


# Füge hier deine Lösung ein.




#     ____________________
#    /                    \
#    !  Meine persönliche !
#    !      Ausnahme      !
#    \____________________/
#             !  !
#             !  !
#             L_ !
#            / _)!
#           / /__L
#     _____/ (____)
#            (____)
#     _____  (____)
#          \_(____)
#             !  !
#             !  !
#             \__/ 
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
# Schreibe eine Klasse `EvenNumberError`, die ausgelöst wird, wenn eine Zahl
# gerade ist. Erstelle eine Funktion, die eine Zahl akzeptiert und die Ausnahme
# auslöst, wenn die Zahl gerade ist. Teste die Funktion, indem du sie mit einer
# geraden Zahl aufrufst.

'''
class EvenNumberError(Exception):
    """Diese Ausnahme wird ausgelöst, wenn eine Zahl gerade ist."""
    def __init__(self, number):
        super().__init__(f"Die Zahl {number} ist gerade, eine ungerade Zahl wird erwartet.")
        self.number = number

def check_odd_number(number):
    if number % 2 == 0:
        raise EvenNumberError(number)
    print(f"Die Zahl {number} ist ungerade.")

# Testaufruf
try:
    check_odd_number(4)  # Diese Zahl ist gerade und löst die Ausnahme aus.
except EvenNumberError as e:
    print(e)
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle eine Klasse `TemperatureTooHighError`, die ausgelöst wird, wenn eine
# Temperatur den Wert von 100°C überschreitet. Erstelle eine Funktion, die
# eine Temperatur akzeptiert und die Ausnahme auslöst, wenn der Wert zu hoch ist.
# Teste die Funktion, indem du eine Temperatur über 100°C eingibst.

'''
class TemperatureTooHighError(Exception):
    """Diese Ausnahme wird ausgelöst, wenn die Temperatur über 100°C liegt."""
    def __init__(self, temperature):
        super().__init__(f"Die Temperatur {temperature}°C ist zu hoch! Maximal 100°C erlaubt.")
        self.temperature = temperature

def check_temperature(temp):
    if temp > 100:
        raise TemperatureTooHighError(temp)
    print(f"Die Temperatur {temp}°C ist im akzeptablen Bereich.")

# Testaufruf
try:
    check_temperature(105)  # Temperatur über 100°C, löst die Ausnahme aus.
except TemperatureTooHighError as e:
    print(e)
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Entwickle eine Klasse `PasswordTooShortError`, die ausgelöst wird, wenn ein Passwort
# weniger als 8 Zeichen hat. Schreibe eine Funktion, die ein Passwort überprüft
# und die Ausnahme auslöst, wenn es zu kurz ist. Teste die Funktion, indem du
# ein zu kurzes Passwort eingibst.

'''
class PasswordTooShortError(Exception):
    """Diese Ausnahme wird ausgelöst, wenn das Passwort zu kurz ist."""
    def __init__(self, password):
        super().__init__("Das Passwort ist zu kurz! Mindestens 8 Zeichen sind erforderlich.")
        self.password = password

def check_password(password):
    if len(password) < 8:
        raise PasswordTooShortError(password)
    print("Das Passwort ist ausreichend lang.")

# Testaufruf
try:
    check_password("abc123")  # Zu kurzes Passwort, löst die Ausnahme aus.
except PasswordTooShortError as e:
    print(e)
'''




# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

