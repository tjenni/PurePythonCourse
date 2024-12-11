#              ___________________________
#       ______|                           |_____
#       \     |    2 ZUSAMMENFASSUNG      |    /
#        )    |___________________________|   (
#       /________)                    (________\       11.12.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
#  


# In diesem Kapitel dreht sich alles um Entscheidungen und deren Umsetzung
# in Python. Verzweigungen sind ein grundlegendes Konzept in der Programmierung,
# das es uns ermöglicht, unseren Code auf verschiedene Szenarien zu reagieren
# und unterschiedliche Abläufe zu steuern.
#
# Wir beginnen mit einfachen Verzweigungen und erweitern diese Schritt für
# Schritt, um komplexere Entscheidungen zu treffen, einschließlich der
# Verwendung logischer Operatoren und verschachtelter Bedingungen. Das
# Kapitel endet mit der Erstellung eines interaktiven Textabenteuers,
# das all diese Techniken kombiniert.
#
# Ziel dieses Kapitels ist es, dir zu zeigen, wie du mit Bedingungen und
# Verzweigungen realistische Entscheidungen programmieren kannst.


# ____________________________
#                            /
#  Kapitelübersicht         (
# ___________________________\

# 2.1 Verzweigungen
#    - Grundlagen der Verzweigungen (`if`, `elif`, `else`).
#    - Anwendung einfacher Bedingungen.

# 2.2 Logische Operatoren
#    - Verknüpfung mehrerer Bedingungen mit `and`, `or`, `not`.
#    - Verwendung für komplexere Entscheidungen.

# 2.3 Verschachtelte Verzweigungen
#    - Prüfungen von Bedingungen innerhalb anderer Bedingungen.
#    - Struktur und Einrückungen bei komplexen Verzweigungen.

# 2.4 Textabenteuer
#    - Anwendung von Verzweigungen zur Erstellung eines interaktiven Spiels.
#    - Kombination der bisherigen Konzepte in einem kreativen Projekt.




# ___________________________
#                            /
#  Befehlsreferenz          (
# ___________________________\


#  Verzweigungen
# --------------
# Eine Verzweigung erlaubt es, verschiedene Codepfade auszuführen,
# basierend auf einer Bedingung.

# Syntax:
# if Bedingung:
#     # Codeblock wird ausgeführt, wenn die Bedingung wahr ist
# elif weitere_Bedingung:
#     # Codeblock wird ausgeführt, wenn die erste Bedingung falsch ist,
#     # aber diese Bedingung wahr ist
# else:
#     # Codeblock wird ausgeführt, wenn keine der Bedingungen wahr ist

# Beispiel:
alter = 20
if alter < 18:
    print("Du bist minderjährig.")
elif alter == 18:
    print("Du bist gerade volljährig geworden.")
else:
    print("Du bist volljährig.")



#  Logische Operatoren
# --------------------

# Mit logischen Operatoren kannst du mehrere Bedingungen kombinieren.

# `and`: Alle Bedingungen müssen wahr sein.
# `or`: Mindestens eine Bedingung muss wahr sein.
# `not`: Kehrt den Wahrheitswert um.

# Beispiele:
note = 4
ist_anwesend = True

# AND: Beide Bedingungen müssen erfüllt sein
if note <= 4 and ist_anwesend:
    print("Du hast bestanden.")

# OR: Eine der Bedingungen reicht
if note > 4 or not ist_anwesend:
    print("Du hast nicht bestanden.")

# NOT: Negiert die Bedingung
if not ist_anwesend:
    print("Du bist nicht anwesend.")



#  Verschachtelte Bedingungen
# ---------------------------

# Verschachtelte Bedingungen ermöglichen weitere Prüfungen innerhalb
# eines `if`-Blocks.

# Syntax:
# if Bedingung1:
#     if Bedingung2:
#         # Codeblock, wenn beide Bedingungen wahr sind
#     else:
#         # Codeblock, wenn Bedingung1 wahr, aber Bedingung2 falsch ist
# else:
#     # Codeblock, wenn Bedingung1 falsch ist

# Beispiel:
alter = 20
mitglied = True

if alter >= 18:
    if mitglied:
        print("Du hast freien Eintritt.")
    else:
        print("Du erhältst ermäßigten Eintritt.")
else:
    print("Zugang nur für Erwachsene.")



#  Eingaben und Entscheidungen
# ----------------------------

# Entscheidungsbäume basieren oft auf Benutzereingaben.
# Eingaben können mit `input()` gesammelt und in Bedingungen verwendet werden.

# Beispiel:
antwort = input("Hast du eine Mitgliedskarte? (ja/nein): ").lower()

if antwort == "ja":
    print("Du erhältst einen Rabatt.")
else:
    print("Kein Rabatt verfügbar.")





