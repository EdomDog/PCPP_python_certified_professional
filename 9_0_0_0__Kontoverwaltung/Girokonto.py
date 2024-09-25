from Konto import Konto

class Girokonto(Konto):
    def __init__(self, kontonummer, kontoinhaber, kontostand, kreditlimit):
        super().__init__(kontonummer, kontoinhaber, kontostand)
        self.__kreditlimit = kreditlimit

    def buchen(self, betrag):
        if (self.get_kontostand() + betrag) >= -self.__kreditlimit:  # check Kreditlimit
            self.set_kontostand(self.get_kontostand() + betrag)  # Verwende set_kontostand
            print(f"{betrag} gebucht. Neuer Kontostand: {self.get_kontostand()}")
        else:
            print(f"Buchung von {betrag} nicht möglich. Kreditlimit von {self.__kreditlimit} überschritten.")

    def ausgabe(self):
        print(f"Girokonto - Kontonummer: {self.get_kontonummer()}, Kontoinhaber: {self.get_kontoinhaber()}, "
              f"Kontostand: {self.get_kontostand()}, Kreditlimit: {self.__kreditlimit}")

    def __str__(self):
        s = f"Girokonto - Kontonummer: {self.get_kontonummer()} Kontoinhaber: {self.get_kontoinhaber()} Kontostand: {self.get_kontostand()}"
        return s
