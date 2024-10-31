#              _________________________
#       ______|                         |_____
#       \     |    2.4 TEXTABENTEUER    |    /
#        )    |_________________________|   (
#       /________)                  (________\       27.10.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# In diesem Kapitel wirst du ein kleines Textabenteuer programmieren!
# Ein Textabenteuer ist ein interaktives Spiel, in dem der Spieler Entscheidungen
# trifft und die Geschichte dadurch beeinflusst. Du kannst dazu alle bisherigen
# Kenntnisse in Python einsetzen – Variablen, Verzweigungen und logische Operatoren.

# ______________________________
#                              /
# Aufbau eines Textabenteuers (
# _____________________________\

# In einem Textabenteuer gibt es eine Reihe von Szenen, bei denen der Spieler
# zwischen verschiedenen Optionen wählen kann. Je nach Entscheidung geht die
# Geschichte anders weiter. Ein solches Spiel kann komplett mit Variablen und
# Verzweigungen geschrieben werden, ohne Schleifen oder komplexere Konzepte.

# Schritte zur Erstellung eines Textabenteuers:
#
# 1. Einführung: Beginne mit einem Begrüßungstext, um den Spieler in die
#    Geschichte einzuführen.
#
# 2. Szenen und Entscheidungen: Baue Szenen auf, in denen der Spieler durch
#    Eingaben Optionen wählt (z. B. eine Zahl oder ein Wort für jede Entscheidung).
#    Verwende Variablen, um wichtige Entscheidungen oder Zustände festzuhalten.
#
# 3. Verzweigungen und Konsequenzen: Nutze `if`, `elif`, und `else`, um die
#    Entscheidungen des Spielers zu verarbeiten und entsprechende Ergebnisse anzuzeigen.
#
# 4. Ende der Geschichte: Beende die Geschichte je nach Verlauf auf unterschiedliche
#    Weise, damit das Abenteuer ein Ziel hat und nicht endlos weitergeht.


# ___________________________
#                           /
# Beispielstruktur         (
# __________________________\

# Ein einfaches Textabenteuer könnte so aussehen:

print("Willkommen zu deinem Textabenteuer!")
print("Du befindest dich vor einem alten Schloss. Die Tür ist angelehnt.")

# Entscheidung 1
decision1 = input("Willst du die Tür öffnen? (ja/nein): ")

if decision1 == "ja":
    print("Du betrittst das Schloss und siehst zwei Gänge.")
    
    # Entscheidung 2
    decision2 = input("Gehst du den linken Gang oder den rechten? (links/rechts): ")
    
    if decision2 == "links":
        print("Du gehst den linken Gang und findest einen Schatz!")
    elif decision2 == "rechts":
        print("Der rechte Gang führt zu einer Falle. Du bist gefangen!")
    else:
        print("Unentschlossen bleibst du stehen. Das Abenteuer endet hier.")
        
else:
    print("Du entscheidest dich, das Schloss nicht zu betreten und gehst nach Hause.")
    print("Vielleicht ein anderes Mal.")

# In diesem Beispiel gibt es mehrere Entscheidungspunkte. Je nach Eingabe
# führt der Weg des Spielers zu verschiedenen Szenen und Enden.


# ________________________________
#                                /
# Vorschlag für eine Geschichte (
# _______________________________\

# Hier ist ein Vorschlag für eine mögliche Geschichte, die du für dein eigenes
# Textabenteuer verwenden kannst. Füge deine eigenen Ideen hinzu und erweitere
# sie, wenn du möchtest.

# Abenteuergeschichte:
#
# - Du wachst in einem dunklen Wald auf und erinnerst dich nicht, wie du dorthin
#   gekommen bist.
#
# - Plötzlich siehst du einen Pfad, der in zwei Richtungen führt: einen dunklen
#   Weg und einen helleren Weg.
#
# - Du musst entscheiden, welchen Weg du gehst.


# Struktur der Entscheidungen:
#
# 1. Wegwahl: Gehst du den dunklen oder den hellen Weg?
#    - Dunkler Weg: Du triffst eine geheimnisvolle Kreatur, die dir ein 
#      Zahlenrätsel stellt.
#
#    - Heller Weg: Du findest ein verlassenes Lager und einige Vorräte.
#
# 2. Interaktion mit der Kreatur (wenn der dunkle Weg gewählt wurde):
#    - Die Kreatur stellt dir eine Aufgabe: "Ich denke an eine Zahl zwischen 
#      1 und 10. Wenn du sie errätst, lasse ich dich weiterziehen. Wenn du 
#      falsch liegst, bleibt dir der Weg verschlossen."
#
#    - Lass den Spieler die Zahl eingeben. Wenn die Zahl korrekt ist, darf er 
#      weitergehen. Beispiel: Wenn die Kreatur an die Zahl 7 denkt, muss der 
#      Spieler genau diese Zahl eingeben.
#
# 3. Lager durchsuchen (wenn der helle Weg gewählt wurde):
#    - Du findest eine Karte mit einem markierten Punkt und musst entscheiden, 
#      ob du dem Hinweis folgst oder im Lager bleibst.
#
# 4. Ende des Abenteuers:
#    - Je nach deinen Entscheidungen entkommst du dem Wald oder bleibst für 
#      immer gefangen.

# Lass deiner Kreativität freien Lauf und entwickle dein eigenes Abenteuer!

# Tipps:
# - Achte darauf, dass der Spieler bei jeder Entscheidung eine Auswahl hat.
# - Beschreibe die Szenen so, dass der Spieler sich in die Geschichte hineinversetzen kann.
# - Verwende Variablen, um bestimmte Informationen zu speichern, die später wichtig sein könnten.
# - Nutze Verzweigungen für unterschiedliche Enden, damit das Spiel mehrere Ausgänge hat.


# _________
#          \
# Aufgabe  /
# ________/
#
# Erstelle dein eigenes kleines Textabenteuer. Du kannst dich an der oben
# beschriebenen Geschichte orientieren oder eine eigene erfinden.
# Viel Spass beim Programmieren deines Abenteuers!


# Füge hier deine Lösung ein.




#                 \||/
#                 |  @___oo
#       /\  /\   / (__,,,,|      GROOAR
#      ) /^\) ^\/ _)               GUT GEMACHT !
#      )   /^\/   _)
#      )   _ /  / _)
#  /\  )/\/ ||  | )_)
# <  >      |(,,) )__)
#  ||      /    \)___)\
#  | \____(      )___) )___
#   \______(_______;;; __;;;
#  ___ _  _ ___  ___ 
# | __| \| |   \| __|
# | _|| .` | |) | _| 
# |___|_|\_|___/|___|
#                
# -=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x




