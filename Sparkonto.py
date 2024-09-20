from Konto import Konto

class Sparkonto(Konto):
    def __init__(self, kontonummer, kontoinhaber, kontostand):
        super().__init__(kontonummer, kontoinhaber, kontostand)

    def buchen(self, betrag):
        if (self.kontostand + betrag) >= 0:  # check ob  Kontostand nach Abbuchung negativ
            self.kontostand += betrag
            print(f"{betrag} gebucht. Neuer Kontostand: {self.kontostand}")
        else:
            print(f"Buchung von {betrag} nicht möglich. Zu wenig Guthaben.")

    def ausgabe(self):
        print(f"Sparkonto - Kontonummer: {self.kontonummer}, Kontoinhaber: {self.kontoinhaber}, Kontostand: {self.kontostand}")

    def __str__(self):
        s="Sparkonto - Kontonummer: " + str(self.kontonummer) + " Kontoinhaber: " + str(self.kontoinhaber) + " Kontostand: " + str(self.kontostand)
        return(s)
