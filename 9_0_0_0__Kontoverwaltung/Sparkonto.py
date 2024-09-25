from Konto import Konto

class Sparkonto(Konto):
    def __init__(self, kontonummer, kontoinhaber, kontostand):
        super().__init__(kontonummer, kontoinhaber, kontostand)

    def buchen(self, betrag):
        if (self.get_kontostand() + betrag) >= 0:    # check ob Kontostand nach Abbuchung negativ
            self._Konto__kontostand += betrag        # Zugriff auf die private Variable von der Superclass
            print(f"{betrag} gebucht. Neuer Kontostand: {self.get_kontostand()}")
        else:
            print(f"Buchung von {betrag} nicht möglich. Zu wenig Guthaben.")

    def ausgabe(self):
        # Zugriff auf private Variablen via Getter
        print(f"Sparkonto - Kontonummer: {self.get_kontonummer()}, Kontoinhaber: {self.get_kontoinhaber()}, Kontostand: {self.get_kontostand()}")

    def __str__(self):
        # Zugriff auf private Variablen via Getter
        s = "Sparkonto - Kontonummer: " + str(self.get_kontonummer()) + " Kontoinhaber: " + str(self.get_kontoinhaber()) + " Kontostand: " + str(self.get_kontostand())
        return s
