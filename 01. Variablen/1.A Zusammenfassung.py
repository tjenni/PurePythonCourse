#              ________________________
#       ______|                        |_____
#       \     |   1 ZUSAMMENFASSUNG    |    /
#        )    |________________________|   (
#       /________)                 (________\       11.12.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
#  

# In diesem Kapitel hast du eine Einführung in die Grundlagen der Programmiersprache
#  Python erhalten. Wir begannen mit der Definition und Zuweisung
# von Variablen und untersuchten, wie unterschiedliche Datentypen verwendet
# werden können, um einfache Programme zu schreiben.
#
# Darüber hinaus hast du gelernt, wie du mit Benutzereingaben verwendest, 
# mathematische Berechnungen durchführst und Texte (Strings) verarbeitest.
# Ein weiterer Schwerpunkt lag auf der Umwandlung von Datentypen, was 
# eine wichtige Fähigkeit ist, um flexibel mit Daten zu arbeiten.
#
# Ziel dieses Kapitels war es, dir eine solide Grundlage zu geben, damit 
# du einfache Programme schreiben und grundlegende Programmierkonzepte 
# verstehen kannst.


# ___________________________
#                            /
#  Kapitelübersicht         (
# ___________________________\

# 1.1 Variablen erstellen
#     - Definition und Zuweisung von Variablen
#     - Datentypen: int, float, str, bool

# 1.2 Variablentypen
#     - Numerische Typen und Operatoren
#     - Beispiele für +, -, *, /, //, %

# 1.3 Benutzereingabe
#     - Verwendung des input()-Befehls
#     - Interaktive Programme

# 1.4 Rechnen mit Variablen
#     - Grundlegende mathematische Operationen
#     - Anwendungsbeispiele: Kostenberechnungen

# 1.5 Arbeiten mit Strings
#     - Verkettung und Wiederholung von Strings
#     - String-Methoden: upper(), lower(), replace(), len()
#     - Formatierte Strings (f-Strings)

# 1.6 Typumwandlungen
#     - Umwandlungen zwischen int, float, str
#     - Typüberprüfung mit type()
#     - Umgang mit Benutzereingaben




# ___________________________
#                            /
#  Befehlsreferenz          (
# ___________________________\


# Variablen
# ----------
# Zuweisung: variable = wert
# Zuweisungsoperatoren:
#    += : Erhöht den Wert einer Variablen
#    -= : Verringert den Wert einer Variablen


# Benutzereingabe
# ----------------
# Eingabe eines Strings: input("Text")
# Umwandlung der Eingabe:
#    int(input("Text"))  # für ganze Zahlen
#    float(input("Text"))  # für Dezimalzahlen


# Mathematische Operationen
# --------------------------
# Addition: +
# Subtraktion: -
# Multiplikation: *
# Division: /
# Ganzzahldivision: //
# Modulo (Rest): %


# String-Operationen
# -------------------
# Verkettung: str1 + str2
# Wiederholung: str * n
# String-Methoden:
#    Großbuchstaben: text.upper()
#    Kleinbuchstaben: text.lower()
#    Zeichen ersetzen: text.replace("alt", "neu")
#    Länge: len(text)
#    Slicing: text[start:end]


# Typumwandlungen
# ----------------
# String zu Integer: int("Zahl")
# String zu Float: float("Zahl")
# Zahl zu String: str(zahl)
# Typüberprüfung: type(variable)


# Formatierte Strings
# --------------------
# f"Text {variable}"  # Fügt Variablen in einen String ein







