#              ___________________________
#       ______|                           |_____
#       \     |    4 ZUSAMMENFASSUNG      |    /
#        )    |___________________________|   (
#       /________)                    (________\       11.12.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
#  


# Dieses Kapitel widmet sich Funktionen – einem essenziellen Konzept in Python.
# Funktionen ermöglichen es, Code in logische Einheiten zu unterteilen und
# wiederverwendbar zu machen. Damit wird dein Code übersichtlicher, modularer
# und leichter zu pflegen.
#
# Wir starten mit den Grundlagen der Funktionsdefinition und -aufruf. Dann
# betrachten wir Rückgabewerte, Parameter mit Standardwerten und den Unterschied
# zwischen lokalen und globalen Variablen. Abschließend lernen wir, wie
# rekursive Funktionen genutzt werden können, um komplexe Probleme elegant zu lösen.

# Ziel ist es, dich mit Funktionen vertraut zu machen und dir zu zeigen, wie
# du sie effektiv einsetzen kannst, um deinen Code klarer und strukturierter
# zu gestalten.




# ___________________________
#                            /
#  Kapitelübersicht         (
# ___________________________\

# 4.1 Funktionen
#    - Grundlagen: Definition und Aufruf von Funktionen.
#    - Wichtige Syntax und erste Beispiele.

# 4.2 Funktionen mit Rückgabewerten
#    - Wie Rückgabewerte genutzt werden, um Ergebnisse aus Funktionen zu erhalten.
#    - Beispiele: Berechnungen und Datenverarbeitung.

# 4.3 Parameter und Standardwerte
#    - Übergabe von Parametern an Funktionen.
#    - Verwendung von Standardwerten für Parameter.

# 4.4 Lokale und globale Variablen
#    - Unterschied zwischen lokalen und globalen Variablen.
#    - Nutzung des `global`-Schlüsselworts.

# 4.5 Rekursive Funktionen
#    - Funktionen, die sich selbst aufrufen.
#    - Einsatzmöglichkeiten und Grenzen.
#    - Beispiele: Fakultät, Fibonacci-Folge, maximale Werte in Listen.




# ___________________________
#                            /
#  Befehlsreferenz          (
# ___________________________\


#  Funktionen
# ----------
# Funktionen sind benannte Codeblöcke, die spezifische Aufgaben ausführen.
# Sie helfen dabei, Code modular und wiederverwendbar zu gestalten.

# Syntax:
# def funktionsname(parameter1, parameter2, ...):
#     # Codeblock
#     return ergebnis  # (optional)

# Beispiel:
def addiere(a, b):
    return a + b

# Aufruf der Funktion:
ergebnis = addiere(5, 3)
print("Ergebnis:", ergebnis)  # Ausgabe: 8



#  Rückgabewerte
# --------------
# Funktionen können mit `return` Werte zurückgeben, die im Programm weiterverwendet
# werden können. Ohne `return` gibt die Funktion `None` zurück.

# Beispiel:
def quadrat(x):
    return x * x

print("Das Quadrat von 4 ist:", quadrat(4))  # Ausgabe: 16



#  Parameter und Standardwerte
# ----------------------------
# Funktionen können Parameter verwenden, um Daten zu empfangen.
# Standardwerte können definiert werden, die genutzt werden, wenn kein Wert übergeben wird.

# Syntax:
# def funktionsname(parameter1, parameter2=standardwert):
#     # Codeblock

# Beispiel:
def begrüßung(name, zeit="Tag"):
    print(f"Guten {zeit}, {name}!")

begrüßung("Anna", "Morgen")  # Ausgabe: Guten Morgen, Anna!
begrüßung("Tom")  # Ausgabe: Guten Tag, Tom!



#  Lokale und globale Variablen
# -----------------------------
# - **Lokale Variablen**: Innerhalb einer Funktion definiert und nur dort verfügbar.
# - **Globale Variablen**: Außerhalb einer Funktion definiert und im gesamten Programm verfügbar.

# Beispiel für lokale Variablen:
def lokale_beispiel():
    lokal = 5
    print("Lokale Variable:", lokal)

lokale_beispiel()
# print(lokal)  # Fehler: `lokal` ist außerhalb der Funktion nicht verfügbar.

# Beispiel für globale Variablen:
globale_var = 10

def globale_beispiel():
    global globale_var
    globale_var += 5

globale_beispiel()
print("Globale Variable:", globale_var)  # Ausgabe: 15



#  Rekursive Funktionen
# ---------------------
# Rekursive Funktionen rufen sich selbst auf, um iterative Probleme zu lösen.
# Sie benötigen einen Basisfall, um die Rekursion zu beenden.

# Beispiel: Fakultät einer Zahl:
def fakultaet(n):
    if n == 0:
        return 1
    return n * fakultaet(n - 1)

print("Fakultät von 5 ist:", fakultaet(5))  # Ausgabe: 120

# Hinweis: Rekursion kann ineffizient sein und sollte mit Bedacht eingesetzt werden.





