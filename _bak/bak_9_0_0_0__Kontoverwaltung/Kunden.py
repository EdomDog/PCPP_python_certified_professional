class Kunden:
    def __init__(self, kundennummer, vorname, nachname):
        self.kundennummer = kundennummer      # Kundennummer als Integer
        self.nachname = nachname              # Nachname als String
        self.vorname = vorname                # Vorname als String
        self.konten = []                      # Liste fuer Speicherung der Kunden-Konten 

    def ausgabe(self):
        # print Kundeninformationen
        print(f"Kundennummer: {self.kundennummer}")
        print(f"Name: {self.vorname} {self.nachname}")
        print("Konten:")
        for konto in self.konten:
            print(konto)

    def get_nachname(self):
        # get Nachname des Kunden
        return self.nachname

    def set_nachname(self, neuer_nachname):
        # set Nachname des Kunden
        self.nachname = neuer_nachname

    def get_vorname(self):
        # get Vorname des Kunden
        return self.vorname

    def set_vorname(self, neuer_vorname):
        # set Vorname des Kunden
        self.vorname = neuer_vorname

    @property
    def prop_vorname(self):
        # Property zum Abrufen des Vornamens
        return self.vorname

    @prop_vorname.setter
    def prop_vorname(self, neuer_vorname):
        # Property zum Setzen des Vornamens
        self.vorname = neuer_vorname

    @property
    def prop_nachname(self):
        # Property zum Abrufen des Nachnamens
        return self.nachname

    @prop_nachname.setter
    def prop_nachname(self, neuer_nachname):
        # Property zum Setzen des Nachnamens
        self.nachname = neuer_nachname

    def add_konto(self, konto):
        # add Konto für den Kunden
        self.konten.append(konto)

