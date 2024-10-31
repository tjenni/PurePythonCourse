#              ___________________________
#       ______|                           |_____
#       \     |         5.4 SETS          |    /
#        )    |___________________________|   (
#       /________)                    (________\       28.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Ein Set (Menge) ist eine Datenstruktur in Python, die eine Sammlung von 
# einzigartigen, ungeordneten Elementen enthält. In einem Set gibt es keine 
# doppelten Werte, und die Reihenfolge der Elemente ist zufällig.

# Sets sind besonders nützlich, wenn wir nur eindeutige Werte speichern oder 
# Mengenoperationen wie Vereinigung, Schnittmenge und Differenz durchführen möchten.


# ____________________________
#                            /
# Ein Set erstellen         (
# ___________________________\

# Ein Set wird mit geschweiften Klammern `{}` erstellt oder mit der Funktion `set()`.
# Beispiel:

colors = {"Rot", "Blau", "Grün"}
print("Set der Farben:", colors)

# Hinweis: Ein leeres Set muss mit `set()` erstellt werden, da `{}` ein leeres Dictionary erzeugt.
empty_set = set()
print("Leeres Set:", empty_set)




# ____________________________________
#                                    /
# Elemente hinzufügen und entfernen (
# ___________________________________\

# Mit `add()` können wir ein Element zu einem Set hinzufügen, wenn es noch nicht vorhanden ist.
# Mit `remove()` oder `discard()` können wir ein Element entfernen.

colors.add("Gelb")  # Fügt "Gelb" hinzu
print("Nach Hinzufügen von Gelb:", colors)

colors.discard("Blau")  # Entfernt "Blau", falls es vorhanden ist
print("Nach Entfernen von Blau:", colors)

# Unterschied zwischen `remove()` und `discard()`:
# `remove()` gibt einen Fehler aus, wenn das Element nicht existiert, `discard()` nicht.




# ___________________________
#                           /
# Mengenoperationen        (
# __________________________\

# Sets unterstützen viele nützliche Mengenoperationen wie Vereinigung, Schnittmenge und Differenz.
# Diese Operationen sind nützlich, um Vergleiche und Analysen durchzuführen.

# Erstellen weiterer Sets
prime_colors = {"Rot", "Gelb", "Blau"}
secundary_colors = {"Grün", "Lila", "Orange", "Rot"}

# 1. Vereinigung (`union`): Alle Elemente aus beiden Sets
result = prime_colors | secundary_colors
print("Vereinigung:", result)

# 2. Schnittmenge (`intersection`): Nur die gemeinsamen Elemente
result = prime_colors & secundary_colors
print("Schnittmenge:", result)

# 3. Differenz (`difference`): Elemente, die nur im ersten Set vorkommen
result = prime_colors - secundary_colors
print("Differenz:", result)




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Sets enthalten nur eindeutige Elemente und sind ungeordnet.
#
# - Mit `add()` fügen wir Elemente hinzu, mit `discard()` oder `remove()` 
#   entfernen wir sie.
# 
# - Mengenoperationen wie Vereinigung (`|`), Schnittmenge (`&`) und Differenz 
#   (`-`) sind sehr nützlich.



# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Set `subjects` mit den Elementen "Mathe", "Physik" und "Chemie".
# Füge "Informatik" hinzu und entferne "Physik". Gib das Set auf der Konsole aus.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle zwei Sets: `sports1` mit "Fussball", "Tennis" und "Schwimmen" und
# `sports2` mit "Basketball", "Schwimmen" und "Volleyball".
# Führe eine Schnittmengenoperation durch, um die gemeinsamen Sportarten zu finden.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Set `leasure` mit den Aktivitäten "Lesen", "Schwimmen", "Wandern".
# Füge "Radfahren" hinzu und überprüfe, ob "Schwimmen" im Set enthalten ist. 
# Gib eine passende Nachricht aus.


# Füge hier deine Lösung ein.

#                    _....._
#                   ';-.--';'
#                     }===={       _.---.._
#                   .'      '.    ';-..--';
#                  /::        \    `}===={
#                 |::          :   '      '.
#    Mengen hast  \::.        _.---_        \
#    du im Griff.  '::_     _`---..-';       |
#                      `````  }====={        /
#                           .'       '.   _.'
#                          /::         \ `
#                         |::           |
#                         \::.          /
#                     jgs  '::_      _.'
#                              ``````
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
# Erstelle ein Set `subjects` mit den Elementen "Mathe", "Physik" und "Chemie".
# Füge "Informatik" hinzu und entferne "Physik". Gib das Set auf der Konsole aus.

'''
subjects = {"Mathe", "Physik", "Chemie"}
subjects.add("Informatik")  # Fügt "Informatik" hinzu
subjects.discard("Physik")  # Entfernt "Physik"
print("Aktuelle Fächer:", subjects)
'''



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle zwei Sets: `sports1` mit "Fussball", "Tennis" und "Schwimmen" und
# `sports2` mit "Basketball", "Schwimmen" und "Volleyball".
# Führe eine Schnittmengenoperation durch, um die gemeinsamen Sportarten zu finden.

'''
sports1 = {"Fussball", "Tennis", "Schwimmen"}
sports2 = {"Basketball", "Schwimmen", "Volleyball"}
common_sports = sports1 & sports2  # Schnittmenge der beiden Sets
print("Gemeinsame Sportarten:", common_sports)
'''




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Set `leasure` mit den Aktivitäten "Lesen", "Schwimmen", "Wandern".
# Füge "Radfahren" hinzu und überprüfe, ob "Schwimmen" im Set enthalten ist. 
# Gib eine passende Nachricht aus.

'''
leasure = {"Lesen", "Schwimmen", "Wandern"}
leasure.add("Radfahren")  # Fügt "Radfahren" hinzu

if "Schwimmen" in leasure:
    print("Schwimmen ist im Set enthalten.")
else:
    print("Schwimmen ist nicht im Set enthalten.")
'''




# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><



