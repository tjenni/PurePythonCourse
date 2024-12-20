#              ___________________________
#       ______|                           |_____
#       \     |  1.1 VARIABLEN ERSTELLEN  |    /
#        )    |___________________________|   (
#       /________)                    (________\       20.12.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
#

# Computer sind in der Lage Informationen zu speichern. In Python
# verwendet man dazu Variablen. Variablen sind "Behälter"
# zum Speichern von Daten. Sie haben einen Namen und können
# verschiedene Werte annehmen.
#
# Hier sind drei Beispiele:

name = "Anna"  # Speichert den Namen Anna in der Variable 'name'

age = 25       # Speichert das Alter 25 in der Variable 'age'

price = 19.99  # Speichert den Preis 19.99 in der Variable 'price'


# Das Gleichheitszeichen ist kein mathematisches Gleichheitszeichen,
# sondern der `Zuweisungsoperator`. Er macht, dass Python eine Variable erstellt
# und ihr einen Wert zuweist.

# Python unterscheidet zwischen Gross- und Kleinschreibung,
# daher sind `age` und `Age` zwei verschiedene Variablen.



# ______________________________
#                              /
#  Regeln für Variablennamen  (
# _____________________________\
#
# 1. Sie sollten mit einem Kleinbuchstaben beginnen.
#    Auf keinen Fall dürfen sie mit einer Zahl beginnen.
#
# 2. Sie sollten nur alphanumerische Zeichen und Unterstriche
#    enthalten (a-z, A-Z, 0-9, _). Umlaute ä,ö,ü oder Leerzeichen
#    dürfen sie nicht enthalten.
#
# 3. Sie sollten aus ganzen, sinnvollen englischen Wörtern bestehen.
#    Die Wörter können durch Unterstriche abgegrenzt werden. (Snake-Case)
#
# 4. Reservierte Wörter wie `print`, `if`, `else` dürfen nicht verwendet werden.



# Beispiele:

_name = "Guido"  # gültig, jedoch wurde 1. nicht beachtet.

Name1 = "Lisa"   # gültig, jedoch wurde 1. nicht beachtet.

höhe = 23        # gültig, jedoch wurde 2. nicht beachtet.

hausnummer = 4  # gültig, jedoch wurde 3. nicht beachtet.

akb_2 = 68       # gültig, jedoch wurde 3. nicht beachtet

# 1name = "Fehler"  # ungültig, da der Name mit einer Zahl beginnt

# street number = 23  # ungültig, da der Name ein Leerzeichen enthält.




# ____________________
#                    /
# Der print-Befehl  (
# ___________________\
#

# Man kann den Wert einer Variabel auf der Kommandozeile (auch Konsole genannt)
# ausgeben lassen – das ist der Bereich, in dem du die Ausgaben deines
# Programms siehst. Dazu verwendet man den Befehl print().

print(age)

# Die Klammern sind wichtig und müssen unbedingt geschrieben werden.
# Wenn du dieses Programm ausführst, d.h. in Thonny oben auf den grünen
# Pfeil klickst, erscheint auf der Kommandozeile (Konsole) der Wert 25.



# ______________
#              /
# Kommentare  (
# _____________\
#

# Wenn eine Zeile mit dem Hashtag # beginnt, wird Python diese Zeile einfach
# ignorieren. Man kann auf diese Weise ein Programm mit Kommentaren versehen.

# Es gibt auch die Möglichkeit mehrere Zeilen als Kommentar zu schreiben.
# Verwende dazu drei ' oder drei """ am Anfang und am Ende des Kommentarblocks.
# Hier sind Beispiele.

"""
Das ist ein mehrzeiliger
Kommentar. Verwende dazu
drei Anführungszeichen.
"""

'''
Man kann zur Kennzeichnung von
mehrzeiligen Kommentaren auch
drei Apostroph (Hochkomma)
verwenden.
'''


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Erstelle eine Variable mit dem Namen "zip_code" und weise ihr den Wert 6300 zu.
# Gib dann die Variable auf der Konsole aus.


# Füge hier deine Lösung ein.



#        /\_/\  (
#       ( ^.^ ) _)      Gut gemacht. Miauu.
#        \\"/  (
#       ( | | )
#      (__d b__)
#
#  ___ _  _ ___  ___
# | __| \| |   \| __|
# | _|| .` | |) | _|
# |___|_|\_|___/|___|
#
# -=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x



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
#
# Erstelle eine Variable mit dem Namen "zip_code" und weise ihr den Wert 6300 zu.
# Schreibe deine Lösung in die Zeile unten und führe dann das Programm aus,
# indem du auf den grünen Pfeil klickst.

'''
zip_code = 6300
print(zip_code)
'''

# >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< ><
