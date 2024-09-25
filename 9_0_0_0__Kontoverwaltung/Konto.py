from abc import ABC, abstractmethod

class Konto(ABC):
    def __init__(self, kontonummer, kontoinhaber, kontostand):
        self.__kontonummer = kontonummer
        self.__kontoinhaber = kontoinhaber
        self.__kontostand = kontostand
    
    def get_kontonummer(self):
        return self.__kontonummer

    def get_kontoinhaber(self):
        return self.__kontoinhaber

    def get_kontostand(self):
        return self.__kontostand

    def set_kontostand(self, betrag):
        self.__kontostand = betrag

    @abstractmethod
    def buchen(self, betrag):
        pass

    def ausgabe(self):
        print(f"Konto - Kontonummer: {self.get_kontonummer()}, Kontoinhaber: {self.get_kontoinhaber()}, Kontostand: {self.get_kontostand()}")

    def __str__(self):
        return f"Konto - Kontonummer: {self.get_kontonummer()}, Kontoinhaber: {self.get_kontoinhaber()}, Kontostand: {self.get_kontostand()}"
