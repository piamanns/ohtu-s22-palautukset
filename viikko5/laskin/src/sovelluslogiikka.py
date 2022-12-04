class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen_komento = None

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo


class KomentoBase:
    def __init__(self, sovelluslogiikka, lue_syote=None):
        self._logiikka = sovelluslogiikka
        self._lue_syote = lue_syote
        self._edellinen_tulos = 0

    def suorita(self):
        self._edellinen_tulos = self._logiikka.tulos
        self._logiikka.edellinen_komento = self

    def kumoa(self):
        self._logiikka.aseta_arvo(self._edellinen_tulos)


class Summa(KomentoBase):
    def suorita(self):
        syote = self._lue_syote()
        if syote:
            super().suorita()
            self._logiikka.plus(syote)

class Erotus(KomentoBase):    
    def suorita(self):
        syote = self._lue_syote()
        if syote:
            super().suorita()
            self._logiikka.miinus(syote)

class Nollaus(KomentoBase):
    def suorita(self):
        super().suorita()
        self._logiikka.nollaa()


class Kumoa():
    def __init__(self, sovelluslogiikka):
        self._logiikka = sovelluslogiikka

    def suorita(self):
        self._logiikka.edellinen_komento.kumoa()
