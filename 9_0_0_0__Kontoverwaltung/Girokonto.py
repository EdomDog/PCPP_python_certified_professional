from Konto import Konto

class Girokonto(Konto):
    def __init__(self, kontonummer, kontoinhaber, kontostand, kreditlimit):
        super().__init__(kontonummer, kontoinhaber, kontostand)
        self.kreditlimit = kreditlimit

    def buchen(self, betrag):
        if (self.kontostand + betrag) >= -self.kreditlimit:  # check Kreditlimit 
            self.kontostand += betrag
            print(f"{betrag} gebucht. Neuer Kontostand: {self.kontostand}")
        else:
            print(f"Buchung von {betrag} nicht möglich. Kreditlimit von {self.kreditlimit} überschritten.")
    
    def ausgabe(self):
        print(f"Girokonto - Kontonummer: {self.kontonummer}, Kontoinhaber: {self.kontoinhaber}, Kontostand: {self.kontostand}, Kreditlimit: {self.kreditlimit}")

    def __str__(self):
        s="Girokonto - Kontonummer: " + str(self.kontonummer) + " Kontoinhaber: " + str(self.kontoinhaber) + " Kontostand: " + str(self.kontostand)
        return(s)