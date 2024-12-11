#              ___________________________
#       ______|                           |_____
#       \     |    3 ZUSAMMENFASSUNG      |    /
#        )    |___________________________|   (
#       /________)                    (________\       11.12.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
#  


# In diesem Kapitel lernst du die Grundlagen von Schleifen in Python kennen.
# Schleifen sind eine zentrale Struktur in der Programmierung, mit der
# Aktionen wiederholt ausgeführt werden können, solange eine Bedingung erfüllt
# ist oder für jedes Element in einer Sammlung.
#
# Wir behandeln die beiden wichtigsten Schleifentypen: die `while`- und die
# `for`-Schleife. Du lernst, wie du Schleifen effizient einsetzt und wie sie
# dir helfen können, wiederholte Aufgaben zu vereinfachen. Das Kapitel endet
# mit der praktischen Anwendung von Schleifen in interaktiven Spielen.

# Ziel ist es, dir die Grundlagen der Wiederholungsstrukturen zu vermitteln
# und dir Werkzeuge an die Hand zu geben, mit denen du wiederkehrende Abläufe
# programmieren kannst.




# ___________________________
#                            /
#  Kapitelübersicht         (
# ___________________________\

# 3.1 Schleifen
#    - Einführung in Schleifen und ihre Rolle in der Programmierung.
#    - Erklärung des Unterschieds zwischen `while`- und `for`-Schleifen.

# 3.2 while-Schleife
#    - Wiederholungen basierend auf einer Bedingung.
#    - Verwendung von Schleifensteuerungen wie `break` und `continue`.

# 3.3 for-Schleife
#    - Iteration über Sequenzen wie Listen oder Zahlenbereiche.
#    - Die `range()`-Funktion und ihre Anwendungen.

# 3.4 Schleifen und einfache Spiele
#    - Praktische Anwendungen von Schleifen in interaktiven Programmen.
#    - Programmierung von Spielen wie Zahlenraten und Schere, Stein, Papier.




# ___________________________
#                            /
#  Befehlsreferenz          (
# ___________________________\


#  Schleifen
# ---------
# Schleifen erlauben es, einen Codeblock wiederholt auszuführen,
# solange eine Bedingung erfüllt ist oder für jedes Element in einer Sammlung.

# Es gibt zwei Haupttypen von Schleifen in Python:
# - `while`-Schleifen: Wiederholungen basierend auf einer Bedingung.
# - `for`-Schleifen: Iterationen über Sequenzen wie Listen, Strings oder Zahlenbereichen.


#  while-Schleife
# ---------------
# Wiederholt den Codeblock, solange die Bedingung `True` ist.

# Syntax:
# while Bedingung:
#     # Codeblock wird ausgeführt, solange die Bedingung wahr ist

# Beispiel:
counter = 0
while counter < 5:
    print("Counter:", counter)
    counter += 1  # Erhöht den Zähler um 1

# Die Schleife endet, wenn die Bedingung `counter < 5` nicht mehr erfüllt ist.



#  for-Schleife
# -------------
# Iteriert über eine Sequenz (z. B. Liste, String, `range`).

# Syntax:
# for Element in Sequenz:
#     # Codeblock wird für jedes Element ausgeführt

# Beispiel:
for buchstabe in "Python":
    print("Buchstabe:", buchstabe)

# Die Schleife gibt jeden Buchstaben des Strings "Python" aus.



#  Schleifensteuerung
# -------------------
# Steuerbefehle für Schleifen:
# - `break`: Beendet die Schleife sofort.
# - `continue`: Überspringt den aktuellen Durchlauf und setzt mit dem nächsten fort.

# Beispiel:
for zahl in range(10):
    if zahl == 5:
        break  # Beendet die Schleife, sobald zahl 5 ist
    print("Zahl:", zahl)

# Beispiel:
for zahl in range(10):
    if zahl % 2 == 0:
        continue  # Überspringt gerade Zahlen
    print("Ungerade Zahl:", zahl)



#  Die range()-Funktion
# ---------------------
# Erzeugt Zahlenbereiche für die Verwendung in `for`-Schleifen.

# Syntax:
# range(stop): Erzeugt Zahlen von 0 bis `stop - 1`.
# range(start, stop): Erzeugt Zahlen von `start` bis `stop - 1`.
# range(start, stop, step): Erzeugt Zahlen von `start` bis `stop - 1`, mit Schritten `step`.

# Beispiel:
for i in range(1, 6):
    print("Zahl:", i)  # Gibt die Zahlen 1 bis 5 aus



#  Verschachtelte Schleifen
# -------------------------
# Schleifen können ineinander verschachtelt werden.

# Syntax:
# for Element1 in Sequenz1:
#     for Element2 in Sequenz2:
#         # Codeblock wird für jede Kombination von Elementen ausgeführt

# Beispiel:
for zeile in range(3):
    for spalte in range(3):
        print(f"({zeile}, {spalte})", end=" ")
    print()  # Zeilenumbruch nach jeder Zeile




