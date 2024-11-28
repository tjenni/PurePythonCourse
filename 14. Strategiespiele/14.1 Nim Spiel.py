#              ____________________________
#       ______|                            |_____
#       \     |       14.1 NIM SPIEL       |    /
#        )    |____________________________|   (
#       /________)                      (________\     22.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Nim ist ein einfaches Strategiespiel, bei dem zwei Spieler abwechselnd Objekte
# von einem oder mehreren Stapeln entfernen. Das Ziel ist es, entweder das letzte
# Objekt zu vermeiden (Standardvariante) oder es zu nehmen (alternative Variante).

# Dieses Kapitel führt in die Regeln von Nim ein und zeigt, wie das Spiel
# mit Python und Arcade implementiert werden kann. Am Ende kannst du das Spiel
# Schritt für Schritt erweitern, z. B. um eine künstliche Intelligenz (KI) mit
# Strategien zur optimalen Spielweise zu integrieren.


# _____________________________
#                             /
# Regeln von Nim             (
# ____________________________\

# - Zu Beginn gibt es einen oder mehrere Stapel mit einer bestimmten Anzahl von Objekten.
# - Zwei Spieler ziehen abwechselnd 1 bis 3 Objekte (oder mehr, abhängig von den Regeln)
#   von einem der Stapel.
# - Der Spieler, der das letzte Objekt nimmt, verliert (Standardvariante).
# - Das Spiel endet, wenn alle Objekte genommen wurden.


# ____________________________
#                             /
# Implementierung eines Spiels
# ____________________________\

# Der folgende Code zeigt die grundlegende Implementierung eines einfachen Nim-Spiels
# mit einem Stapel. Das Spiel wird in der Konsole gespielt. In späteren Kapiteln
# kannst du dies mit einer grafischen Oberfläche und einer KI erweitern.

import random

def nim_game():
    """
    Ein einfaches Nim-Spiel mit einem Stapel, bei dem zwei Spieler abwechselnd
    1 bis 3 Objekte ziehen. Der Spieler, der das letzte Objekt nimmt, verliert.
    """
    print("Willkommen zu Nim!")
    print("Regeln: Nehme 1, 2 oder 3 Objekte vom Stapel. Der Spieler, der das letzte Objekt nimmt, verliert.")

    # Anzahl der Objekte auf dem Stapel
    pile = random.randint(10, 20)
    print(f"Zu Beginn befinden sich {pile} Objekte im Stapel.")

    # Spielschleife
    while pile > 0:
        # Spielerzug
        player_move = player_turn(pile)
        pile -= player_move
        print(f"Du hast {player_move} Objekte genommen. Es bleiben {pile} Objekte.")
        if pile == 0:
            print("Du hast das letzte Objekt genommen. Du verlierst!")
            break

        # KI-Zug
        ai_move = ai_turn(pile)
        pile -= ai_move
        print(f"Die KI nimmt {ai_move} Objekte. Es bleiben {pile} Objekte.")
        if pile == 0:
            print("Die KI hat das letzte Objekt genommen. Du gewinnst!")
            break


def player_turn(pile):
    """
    Führt den Zug des Spielers aus. Der Spieler wählt, wie viele Objekte er nehmen möchte.
    """
    while True:
        try:
            move = int(input("Wie viele Objekte möchtest du nehmen (1-3)? "))
            if move < 1 or move > 3 or move > pile:
                print("Ungültige Eingabe. Wähle eine Zahl zwischen 1 und 3, die im Stapel verfügbar ist.")
            else:
                return move
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")


def ai_turn(pile):
    """
    Führt den Zug der KI aus. In dieser einfachen Version wählt die KI zufällig
    eine Anzahl von Objekten (1-3), die im Stapel verfügbar sind.
    """
    move = random.randint(1, min(3, pile))
    return move


# Hauptprogramm starten
if __name__ == "__main__":
    nim_game()




# ____________________________
#                             /
# Erweiterungsmöglichkeiten  (
# ____________________________\

# Sobald du das grundlegende Nim-Spiel verstehst, kannst du es erweitern:
#
# 1. **Einführung mehrerer Stapel:**
#    - Der Spieler kann aus mehreren Stapeln wählen.
#    - Erweitere die KI, um mit mehreren Stapeln umzugehen.
#
# 2. **Optimale Strategie für die KI:**
#    - Implementiere den Minimax-Algorithmus, um der KI eine optimale Spielstrategie zu geben.
#
# 3. **Grafische Oberfläche:**
#    - Nutze `arcade`, um das Spiel mit visuellen Elementen wie Stapeln und Animationen darzustellen.
#
# 4. **Regelvarianten:**
#    - Ändere die Siegbedingungen, z. B., dass der Spieler, der das letzte Objekt nimmt, gewinnt.
#
# 5. **Power-Ups oder Spezialzüge:**
#    - Erlaube den Spielern, bestimmte Power-Ups zu nutzen, z. B. "nimm alle Objekte aus einem Stapel".
#
# 6. **Mehrere Spieler oder Netzwerkspiel:**
#    - Erweitere das Spiel um einen Mehrspielermodus mit Netzwerkunterstützung.

# Diese Erweiterungen helfen dir, komplexere Logiken und Strategien zu implementieren, und bereiten
# dich auf anspruchsvollere Spiele wie Tic-Tac-Toe oder Schach vor.




# ___________________
#                   /
# Zusammenfassung  (
# __________________\

# In diesem Kapitel hast du die Grundlagen von Nim gelernt:
# 
# 1. **Regeln des Spiels**: Spieler nehmen abwechselnd 1 bis 3 Objekte, und derjenige, der das
#    letzte nimmt, verliert.
#
# 2. **Konsolenbasiertes Spiel**: Ein einfaches Spiel, bei dem der Spieler gegen eine KI
#    antritt, die zufällige Züge macht.
#
# 3. **Grundlage für Strategien**: Nim ist ein ideales Spiel, um grundlegende KI-Techniken
#    wie den Minimax-Algorithmus zu erlernen.
#
# Mit diesen Grundlagen kannst du das Spiel erweitern und anspruchsvollere Mechaniken
# wie mehrere Stapel, strategische KI und eine grafische Oberfläche hinzufügen.




# ____________________________
#                            /
# Übungsaufgaben            (
# ___________________________\


# ___________
#            \
# Aufgabe 1  /
# __________/
#
# Füge eine Regelvariante hinzu, bei der der Spieler, der das letzte Objekt nimmt, gewinnt.
# Erstelle eine neue Funktion `nim_game_variant()`, die diese Regel umsetzt.


# ___________
#            \
# Aufgabe 2  /
# __________/
#
# Implementiere mehrere Stapel im Nim-Spiel. Spieler und KI sollen auswählen können,
# von welchem Stapel sie Objekte nehmen möchten.


# ___________
#            \
# Aufgabe 3  /
# __________/
#
# Erstelle eine einfache grafische Darstellung des Nim-Spiels mit Arcade. Zeichne
# Stapel als Rechtecke, die kleiner werden, wenn Objekte entfernt werden. Nutze die
# Tastatur oder Maus, um Züge zu machen.