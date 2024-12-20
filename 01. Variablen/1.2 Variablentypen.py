#              ______________________
#       ______|                      |_____
#       \     |  1.2 VARIABLENTYPEN  |    /
#        )    |______________________|   (
#       /________)               (________\       20.12.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
#


# Python kennt fünf grundlegende Typen, die in Variablen gespeichert
# werden können:
#
# - Integer    (Ganze Zahlen)
# - Float      (Dezimalzahlen)
# - String     (Text)
# - Boolean    (Wahr oder Falsch)
# - None       (Undefiniert)
#
# Jeder dieser Typen hat bestimmte Eigenschaften und wird für
# unterschiedliche Aufgaben verwendet. Schauen wir uns diese genauer an.



# ___________
#           /
# INTEGER  (
# __________\

# Integervariablen repräsentieren ganze Zahlen, das heisst
# Zahlen ohne Nachkommastellen. Sie umfassen sowohl positive
# als auch negative Zahlen, z.B. -20, 0 oder 7.
# Beispiele für Integer-Variabeln.

age = 27
points = -20
money = 1000



# ___________
#           /
# FLOAT    (
# __________\

# Ein Float ist eine Zahl mit Nachkommastellen (Dezimalstellen).
# In Python können Fliesskommazahlen auch sehr grosse oder sehr
# kleine Werte darstellen. Manchmal kann es bei diesen Zahlen
# zu kleinen Rundungsfehlern kommen, was bei normalen Berechnungen
# aber meist keine grosse Rolle spielt.
# Beispiele für Float-Variablen:

grade = 4.5
temperature = -1.4
mass = 5.972e24  # das e24 bedeutet "mal 10 hoch 24"



# ___________
#           /
# STRING   (
# __________\

# Der Computer kann auch mit Text umgehen. Eine Variable, die Text
# speichert, nennt man "String" oder auch "Zeichenkette".
# Ein String ist jede Art von Text, der zwischen Anführungszeichen
# steht. Beispiele:

name = 'Guido'
greeting = "Hallo, wie geht's?"

# Wichtig ist, dass du bei einem String immer Anführungszeichen verwendest,
# entweder doppelte (" ") oder einfache (' '). Andernfalls erkennt
# Python den Text nicht als String und zeigt die Fehlermeldung:
#
#     SyntaxError: unterminated string literal



# ___________
#           /
# BOOLEAN  (
# __________\

# Eine Boolesche Variable (Boolean) hat nur zwei mögliche Werte: Wahr (True)
# oder Falsch (False).
# Diese Variablen werden oft verwendet, um Zustände oder Bedingungen zu speichern.
# Achte auf die Gross- und Kleinschreibung der Werte True und False.

has_sisters = False
is_rich = True



# ___________
#           /
# NONE     (
# __________\

# Der Variablentyp None zeigt an, dass eine Variable keinen Wert hat.
# Dies kann hilfreich sein, wenn der Wert einer Variablen noch nicht
# feststeht oder wenn die Variable einen Wert im Laufe des Programms
# bekommen soll. Beispiel:

something = None



# ______________________________________________
#                                              /
#  Mehrere Variabeln auf der Konsole ausgeben (
# _____________________________________________\

# Mit dem `print`-Befehl kannst du mehrere Variablen oder Textstücke
# in einer Zeile ausgeben, indem du sie durch Kommas trennst.

print("Alter:", age)

# Der Text "Alter:" wird direkt so ausgegeben, wie du ihn geschrieben hast.
# Danach erscheint der Inhalt der Variablen `age`, also in diesem Fall die Zahl 7.

# Du kannst noch mehr Informationen auf einmal ausgeben, indem du sie einfach
# durch Kommas trennst. Zum Beispiel:

print("Name:", name, "Alter:", age, "Punkte:", points)

# Das Ergebnis wird dann so aussehen:

'''
Name: Guido Alter: 27 Punkte: -20
'''

# Python fügt automatisch Leerzeichen zwischen den Ausgaben ein,
# damit der Text lesbar bleibt.



# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#

# Erstelle die Variablen `name` mit deinem Vornamen, `height`
# mit deiner Körpergrösse und `likes_candy`, die True ist, wenn du
# Süssigkeiten magst. Gib diese Variablen dann mit print() auf der
# Konsole aus. Die Ausgabe sollte dann wie folgt ausschauen:

'''
Hallo ich heisse, Hans und bin 1.83 Meter gross. Ich mag Süssigkeiten: True
'''

# Füge hier deine Lösung ein.



# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Erstelle die Variabeln `firstname`, `name`, `street`, `nr`, `plz`, `city`
# und fülle sie mit deinen Angaben. Gib anschliessend auf der Konsole
# deine formatierte Adresse aus.
#

'''
Hans Mustermann
Beispielstrasse 4
5366 Modellhausen
'''

# Füge hier deine Lösung ein.



#
#                        GUT GEMACHT!
#               __
#   (\,--------'()'--o
#    (_    ___    /~"
#     (_)_)  (_)_)
#
#
#  ___ _  _ ___  ___
# | __| \| |   \| __|
# | _|| .` | |) | _|
# |___|_|\_|___/|___|
#
# -=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-



# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><
#  _    _   _
# | |  (_)_(_)___ _   _ _ __   __ _  ___ _ __
# | |   / _ \/ __| | | | '_ \ / _` |/ _ \ '_ \
# | |__| (_) \__ \ |_| | | | | (_| |  __/ | | |
# |_____\___/|___/\__,_|_| |_|\__, |\___|_| |_|
#                             |___/


# ___________
#            \
# Aufgabe 1  /
# __________/

# Erstelle die Variablen `name`, `height` und `likes_candy` und gib sie aus.

'''
name = "Hans"          # Ersetze "Hans" mit deinem Vornamen
height = 1.83          # Ersetze 1.83 mit deiner Körpergrösse
likes_candy = True     # Setze auf True oder False, je nachdem ob du Süssigkeiten magst

# Ausgabe
print("Hallo, ich heisse", name , "und bin" , height , "Meter gross. Ich mag Süssigkeiten:", likes_candy)
'''

# ___________
#            \
# Aufgabe 2  /
# __________/

# Erstelle die Variablen mit deinen Adressdaten und gib sie formatiert aus.

'''
firstname = "Hans"           # Ersetze "Hans" mit deinem Vornamen
name = "Mustermann"          # Ersetze "Mustermann" mit deinem Nachnamen
street = "Beispielstrasse"   # Ersetze mit deiner Strasse
nr = "4"                     # Ersetze mit deiner Hausnummer
plz = "5366"                 # Ersetze mit deiner PLZ
city = "Modellhausen"        # Ersetze mit deinem Wohnort

# Ausgabe der formatierten Adresse
print(firstname, name)
print(street, nr)
print(plz, city)
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><
