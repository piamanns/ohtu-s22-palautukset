class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo


class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._logiikka = sovelluslogiikka
        self._lue_syote = lue_syote
    
    def suorita(self):
        self._logiikka.plus(self._lue_syote())

class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._logiikka = sovelluslogiikka
        self._lue_syote = lue_syote
    
    def suorita(self):
        self._logiikka.miinus(self._lue_syote())

class Nollaus:
    def __init__(self, sovelluslogiikka):
        self._logiikka = sovelluslogiikka

    def suorita(self):
        self._logiikka.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka):
        self._logiikka = sovelluslogiikka
    
    def suorita(self):
        pass
