'''
Programming Task: Python
Date: 20.08.2025
Course: PPCP1

TASK:
    - A bank account management system is to be programmed.
    - Each class should be saved in its own Python file.
    - There are four classes: Kunden, Konto, Sparkonto, Girokonto.
    - The account balance can only be modified via the "buchen" method.
    - The Girokonto should consider a credit limit.
    - The Konto class should have an abstract method.
    - Variables and classes should be named in German.

'''

from Kunden import Kunden
from Sparkonto import Sparkonto
from Girokonto import Girokonto

if __name__ == "__main__":
    # Kunde kunde1 - Max Mustermann erstellen
    kunde1 = Kunden(101, "Max", "Mustermann")
    
    # Sparkonto kunde1 für Max Mustermann erstellen
    sparkonto_kunde1 = Sparkonto(2001, "Max Mustermann", 5000)
    
    # Buchen: 1000 Euro einzahlen
    sparkonto_kunde1.buchen(1000)
    
    # Buchen: 2000 Euro abheben
    sparkonto_kunde1.buchen(-2000)
    
    # Sparkonto zu kunde1 Kunden hinzufügen
    kunde1.add_konto(sparkonto_kunde1)

    # Girokonto kunde1: Max Mustermann erstellen
    girokonto_kunde1 = Girokonto(3001, "Max Mustermann", 2000, 500)
    
    # Buchen: 500 Euro einzahlen
    girokonto_kunde1.buchen(500)
    
    # Buchen: 2500 Euro abheben (test ob Kreditlimit erreicht wird)
    girokonto_kunde1.buchen(-2500)
    
    # Girokonto: - kunde1
    kunde1.add_konto(girokonto_kunde1)

    # Kunde kunde2 "Elise Schmidt" erstellen
    kunde2 = Kunden(102,  "Elise", "Schmidt")
    
    # Sparkonto kunde2 - "Elise Schmidt"
    sparkonto_kunde2 = Sparkonto(2002, "Elise Schmidt", 3000)
    
    # Sparkonto zu kunde2 hinzufuegen
    kunde2.add_konto(sparkonto_kunde2)

    # Ausgabe für kunde1: "Max Mustermanns" alle Konten
    print("\nKonten für ", (kunde1.get_vorname(), kunde1.get_nachname()))
    kunde1.ausgabe()

    # Ausgabe für kunde2: "Elise Schmidts" alle Konten
    print("\nKonten für ", (kunde2.get_vorname(), kunde2.get_nachname()))
    kunde2.ausgabe()

    

