from abc import ABC, abstractmethod 

class Konto:
    def __init__(self, kontonummer, kontoinhaber, kontostand):
        self.kontonummer = kontonummer
        self.kontoinhaber = kontoinhaber
        self.kontostand = kontostand
    
    @abstractmethod
    def buchen(self, betrag):
        pass

    def ausgabe(self):
        print(f"Konto - Kontonummer: {self.kontonummer}, Kontoinhaber: {self.kontoinhaber}, Kontostand: {self.kontostand}")

    def __str__(self):
        return f"Konto - Kontonummer: {self.kontonummer}, Kontoinhaber: {self.kontoinhaber}, Kontostand: {self.kontostand}"
