#              ___________________________
#       ______|                           |_____
#       \     |      5.3 DICTIONARIES     |    /
#        )    |___________________________|   (
#       /________)                    (________\       28.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Dictionaries (Wörterbücher) sind eine spezielle Datenstruktur in Python, die
# es uns ermöglicht, Daten in Schlüssel-Wert-Paaren zu speichern. Damit sind 
# Dictionaries besonders nützlich, wenn man jedem Wert eine eindeutige 
# Bezeichnung (Schlüssel) zuweisen möchte.

# Beispiel: Ein Dictionary, das Informationen über ein Auto speichert.

auto = {
    "Marke": "Toyota",
    "Modell": "Corolla",
    "Baujahr": 2020
}
print("Auto-Dictionary:", auto)




# ____________________________
#                            /
# Zugriff auf Werte         (
# ___________________________\

# Auf einen Wert im Dictionary greifen wir zu, indem wir den zugehörigen Schlüssel
# in eckigen Klammern angeben. Falls der Schlüssel nicht vorhanden ist, führt dies
# zu einem Fehler. 

# Beispiel:
print("Marke:", auto["Marke"])  # Gibt "Toyota" aus

# Ein sicherer Zugriff auf Werte kann mit der Methode `get()` erfolgen, die `None`
# zurückgibt, wenn der Schlüssel nicht vorhanden ist.

color = auto.get("Farbe")  # Gibt `None` zurück, da "Farbe" nicht existiert
print("Farbe:", color)




# ______________________________
#                              /
# Werte hinzufügen und ändern (
# _____________________________\

# Ein Dictionary kann Werte mit neuen Schlüsseln ergänzen oder vorhandene Werte ändern.

auto["Farbe"] = "Blau"  # Fügt den Schlüssel "Farbe" hinzu
auto["Modell"] = "Yaris"  # Ändert den Wert für "Modell"
print("Aktualisiertes Auto:", auto)




# ________________________________
#                                /
# Schlüssel und Werte entfernen (
# _______________________________\

# Mit der Methode `pop()` entfernen wir ein Schlüssel-Wert-Paar aus dem Dictionary.
# Der entfernte Wert wird zurückgegeben. Falls der Schlüssel nicht existiert, führt dies
# zu einem Fehler.

modell = auto.pop("Modell")  # Entfernt "Modell" und gibt den Wert zurück
print("Entferntes Modell:", modell)
print("Auto nach Entfernen des Modells:", auto)




# _____________________________
#                             /
# Schleifen und Dictionaries (
# ____________________________\

# Wir können ein Dictionary mit einer Schleife durchlaufen. Die Methode `items()`
# gibt uns jedes Schlüssel-Wert-Paar in einer Schleife zurück.

for schluessel, wert in auto.items():
    print(f"{schluessel}: {wert}")

# Es gibt auch `keys()` und `values()` für Schleifen nur über die Schlüssel oder Werte.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Ein Dictionary speichert Daten in Schlüssel-Wert-Paaren.
#
# - Der Zugriff erfolgt über den Schlüssel. `get()` bietet eine sichere Alternative.
#
# - Mit `pop()` kann ein Schlüssel-Wert-Paar entfernt werden.
#
# - `items()`, `keys()` und `values()` ermöglichen den Zugriff auf Paare, Schlüssel oder Werte.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle ein Dictionary namens `students` mit den Schlüsseln "Name", "Alter" und "Klasse".
# Füge die entsprechenden Informationen zu einem Schüler hinzu und gib das Dictionary aus.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Dictionary namens `grades` mit den Schlüsseln "Mathe", "Deutsch" und "Physik".
# Weise den Schlüsseln Noten zu. Verwende `pop()`, um die Note in "Deutsch" zu entfernen,
# und gib das aktualisierte Dictionary aus.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Dictionary `countries` mit den Ländernamen als Schlüssel und deren Hauptstädte als Wert.
# Durchlaufe das Dictionary mit einer Schleife und gib jedes Land mit seiner Hauptstadt aus.


# Füge hier deine Lösung ein.



#          ______ ______
#        _/      Y      \_
#       // ~~ ~~ | ~~ ~  \\        Dicionaries hast du nun im Griff. :-)
#      // ~ ~ ~~ | ~~~ ~~ \\      
#     //________.|.________\\     
#    `----------`-'----------'DI
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
# Erstelle ein Dictionary namens `students` mit den Schlüsseln "Name", "Alter" und "Klasse".
# Füge die entsprechenden Informationen zu einem Schüler hinzu und gib das Dictionary aus.

'''
students = {
    "Name": "Lena",
    "Alter": 15,
    "Klasse": "9a"
}
print("Student-Informationen:", students)
'''





# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle ein Dictionary namens `grades` mit den Schlüsseln "Mathe", "Deutsch" und "Physik".
# Weise den Schlüsseln Noten zu. Verwende `pop()`, um die Note in "Deutsch" zu entfernen,
# und gib das aktualisierte Dictionary aus.

'''
grades = {
    "Mathe": 5,
    "Deutsch": 4,
    "Physik": 6
}
grades.pop("Deutsch")  # Entfernt den Eintrag für "Deutsch"
print("Notenspiegel nach Entfernen von Deutsch:", grades)
'''



# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle ein Dictionary `countries` mit den Ländernamen als Schlüssel und deren Hauptstädte als Wert.
# Durchlaufe das Dictionary mit einer Schleife und gib jedes Land mit seiner Hauptstadt aus.

'''
countries = {
    "Schweiz": "Bern",
    "Deutschland": "Berlin",
    "Österreich": "Wien"
}

for country, capital in countries.items():
    print(f"Die Hauptstadt von {country} ist {capital}.")
'''



# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

