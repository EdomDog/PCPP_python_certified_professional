class Kunden:
    def __init__(self, kundennummer, vorname, nachname):
        self.__kundennummer = kundennummer
        self.__vorname = vorname
        self.__nachname = nachname
        self.__konten = []

    def ausgabe(self):
        # print Kundeninformationen
        print(f"Kundennummer: {self.get_kundennummer()}")
        print(f"Name: {self.get_vorname()} {self.get_nachname()}")
        print("Konten:")
        for konto in self.get_konten():
            print(konto)

    def get_nachname(self):
        # get Nachname des Kunden
        return self.__nachname

    def set_nachname(self, neuer_nachname):
        # set Nachname des Kunden
        self.__nachname = neuer_nachname

    def get_vorname(self):
        # get Vorname des Kunden
        return self.__vorname

    def set_vorname(self, neuer_vorname):
        # set Vorname des Kunden
        self.__vorname = neuer_vorname

    def get_kundennummer(self):
        return self.__kundennummer

    def get_konten(self):
        return self.__konten

    @property
    def prop_vorname(self):
        # Property zum Abrufen des Vornamens
        return self.__vorname

    @prop_vorname.setter
    def prop_vorname(self, neuer_vorname):
        # Property zum Setzen des Vornamens
        self.__vorname = neuer_vorname

    @property
    def prop_nachname(self):
        # Property zum Abrufen des Nachnamens
        return self.__nachname

    @prop_nachname.setter
    def prop_nachname(self, neuer_nachname):
        # Property zum Setzen des Nachnamens
        self.__nachname = neuer_nachname

    def add_konto(self, konto):
        # add Konto für den Kunden
        self.__konten.append(konto)                 
