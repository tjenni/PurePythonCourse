#              ____________________________________________
#       ______|                                            |_____
#       \     |    11.1 DATENMANIPULATION MIT PANDAS       |    /
#        )    |____________________________________________|   (
#       /________)                                     (________\      4.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# `pandas` ist eine Python-Bibliothek, die speziell für die Arbeit mit Daten 
# entwickelt wurde. Sie bietet effiziente Datenstrukturen und Funktionen 
# für die Datenanalyse. In diesem Kapitel lernst du, wie du Daten laden, 
# anzeigen, manipulieren und filtern kannst.

# Pandas wird oft unter dem Kürzel "pd" importiert

import pandas as pd  


# _________________________________
#                                 /
# Was ist ein DataFrame?         (
# ________________________________\

# Ein `DataFrame` ist die Hauptstruktur von `pandas`. Es ist eine Tabelle, die 
# Zeilen und Spalten enthält. Hier ein einfaches Beispiel für einen DataFrame.

data = {
    "Name": ["Anna", "Ben", "Chris", "Dani"],
    "Alter": [23, 35, 29, 41],
    "Stadt": ["Berlin", "München", "Hamburg", "Köln"]
}
df = pd.DataFrame(data)
print("DataFrame-Beispiel:\n", df)




# _________________________________
#                                 /
# Daten aus einer Datei laden    (
# ________________________________\

# Oft liegen Daten in CSV-Dateien vor, die sich mit `pandas` einfach laden lassen.
# (Für diesen Code benötigst du eine Datei „data.csv“ im selben Ordner)

# Lädt eine CSV-Datei in einen DataFrame
df = pd.read_csv("data.csv")  

# Zeigt die ersten 5 Zeilen an
print(df.head())




# _________________________________
#                                 /
# Erste Erkundung von Daten      (
# ________________________________\

# 1. Datenstruktur ansehen
print("\nErste Zeilen:\n", df.head())
print("\nDaten-Info:\n", df.info())
print("\nStatistische Beschreibung:\n", df.describe())


# 2. Spalten auswählen
alter = df["Alter"]
print("\nSpalte 'Alter':\n", alter)




# _________________________________
#                                 /
#  Daten filtern und sortieren   (
# ________________________________\

# 1. Daten filtern
df_ueber_30 = df[df["Alter"] > 30]
print("\nPersonen über 30 Jahre:\n", df_ueber_30)

# 2. Daten sortieren
df_sorted = df.sort_values(by="Alter", ascending=False)
print("\nDataFrame nach Alter sortiert:\n", df_sorted)




# _________________________________
#                                 /
#  Daten manipulieren            (
# ________________________________\

# 1. Neue Spalten hinzufügen
df["Geburtsjahr"] = 2024 - df["Alter"]
print("\nDataFrame mit Geburtsjahr:\n", df)


# 2. Spalten umbenennen
df = df.rename(columns={"Name": "Vorname"})
print("\nUmbenannter DataFrame:\n", df)


# 3. Fehlende Werte behandeln

# (Für dieses Beispiel sollte eine CSV-Datei mit fehlenden Werten vorhanden sein)

df = pd.read_csv("students_with_missing.csv")
df["Alter"].fillna(df["Alter"].mean(), inplace=True)
print("\nDataFrame mit gefüllten fehlenden Werten:\n", df)





# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# - Ein `DataFrame` ist eine tabellarische Datenstruktur in `pandas`.
#
# - Mit `.read_csv()` lassen sich Daten aus CSV-Dateien laden.
#
# - Die Methoden `.head()`, `.info()`, und `.describe()` helfen, Daten zu erkunden.
#
# - Filtere Daten mit Bedingungen und sortiere sie mit `sort_values()`.
#
# - Füge neue Spalten hinzu, benenne Spalten um und gehe mit fehlenden Werten um.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Lade eine CSV-Datei namens „students.csv“ mit den Spalten „Name“, „Alter“ und „Klasse“.
# Zeige die ersten fünf Zeilen sowie die Struktur und statistischen Informationen der Daten an.


# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle einen DataFrame, der Informationen über fünf Städte enthält:
# Name der Stadt, Einwohnerzahl, und Durchschnittstemperatur.
# Filtere die Städte, die mehr als 1 Million Einwohner haben, und zeige das Ergebnis an.

# Füge hier deine Lösung ein.




# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle einen DataFrame mit einer Liste von Produkten und ihren Preisen.
# Berechne und füge eine neue Spalte mit einem 10% Rabatt auf jeden Preis hinzu.


# Füge hier deine Lösung ein.




#       ,mMm.,------.,mMm.
#       (GNP'        `?ND)
#        P  dMm.  ,mMb  ?
#        (  ?X_O  O_XP  )               Mit Pandas kann man Daten
#        (      qp      )   bdsm        manipulieren.
#         \  `--'`--'  /
#
#      _____         ,__)
#     (--|__) _.._  _| _,
#       _|   (_|| |(_|(_|
#      (
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
# Lade eine CSV-Datei namens „students.csv“ mit den Spalten „Name“, „Alter“ und „Klasse“.
# Zeige die ersten fünf Zeilen sowie die Struktur und statistischen Informationen der Daten an.

'''
df = pd.read_csv("students.csv")
print(df.head())
print(df.info())
print(df.describe())
'''


# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle einen DataFrame, der Informationen über fünf Städte enthält:
# Name der Stadt, Einwohnerzahl, und Durchschnittstemperatur.
# Filtere die Städte, die mehr als 1 Million Einwohner haben, und zeige das Ergebnis an.

'''
cities_data = {
    "Stadt": ["Berlin", "München", "Hamburg", "Köln", "Frankfurt"],
    "Einwohner": [3669491, 1471508, 1841179, 1085664, 753056],
    "Temperatur": [10.0, 9.0, 9.5, 10.5, 9.8]
}
cities_df = pd.DataFrame(cities_data)
print("\nStädte mit mehr als 1 Million Einwohner:\n", cities_df[cities_df["Einwohner"] > 1000000])
'''


# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle einen DataFrame mit einer Liste von Produkten und ihren Preisen.
# Berechne und füge eine neue Spalte mit einem 10% Rabatt auf jeden Preis hinzu.

'''
products_data = {
    "Produkt": ["Apfel", "Banane", "Orange", "Trauben", "Mango"],
    "Preis": [1.20, 0.50, 0.80, 2.50, 3.00]
}
products_df = pd.DataFrame(products_data)
products_df["Preis nach Rabatt"] = products_df["Preis"] * 0.9
print("\nProdukte mit 10% Rabatt:\n", products_df)
'''


# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><

