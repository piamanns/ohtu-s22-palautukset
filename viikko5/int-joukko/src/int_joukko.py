KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self._validoi_argumentit(kapasiteetti, kasvatuskoko)

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.taulukko = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def _validoi_argumentit(self, kapasiteetti, kasvatuskoko):
        self.validoi_kokonaisluku(kapasiteetti, "Anna kapasitetti kokonaislukuna")  
        self.validoi_kokonaisluku(kasvatuskoko, "Anna kasvatuskoko kokonaislukuna")
        self.validoi_arvo_vahintaan(kapasiteetti, 0, "Kapasiteetin on oltava positiivinen")
        self.validoi_arvo_vahintaan(kasvatuskoko, 0, "Kasvatuskoon on oltava positiivinen")

    def validoi_kokonaisluku(self, luku, viesti):
        if not isinstance(luku, int):
            raise TypeError(viesti)

    def validoi_arvo_vahintaan(self, luku, arvo, viesti):
        if luku < arvo:
            raise ValueError(viesti)  
  
    def kuuluu(self, luku):
        return luku in self.taulukko

    def lisaa(self, luku):
        if self.kuuluu(luku):
            return False

        if self.alkioiden_lkm == len(self.taulukko):
            self.taulukko = self.kasvata_taulukkoa(self.taulukko)
        
        self.taulukko[self.alkioiden_lkm] = luku
        self.alkioiden_lkm += 1

        return True

    def kasvata_taulukkoa(self, vanha_taulukko):
        uusi_taulukko = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_taulukko(vanha_taulukko, uusi_taulukko)
        return uusi_taulukko

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def poista(self, luku):
        if not self.kuuluu(luku):
            return False

        indeksi = self.taulukko.index(luku)
        self.taulukko = self.taulukko[:indeksi] + self.taulukko[indeksi+1:] + [0]
        self.alkioiden_lkm -= 1
        return True

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.taulukko[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        uusi_joukko = IntJoukko()
        joukko_a = a.to_int_list()
        joukko_b = b.to_int_list()

        for alkio in joukko_a:
            uusi_joukko.lisaa(alkio)

        for alkio in joukko_b:
            uusi_joukko.lisaa(alkio)

        return uusi_joukko

    @staticmethod
    def leikkaus(a, b):
        uusi_joukko = IntJoukko()
        joukko_a = a.to_int_list()
        joukko_b = b.to_int_list()

        for alkio in joukko_a:
            if alkio in joukko_b:
               uusi_joukko.lisaa(alkio)

        return uusi_joukko

    @staticmethod
    def erotus(a, b):
        uusi_joukko = IntJoukko()
        joukko_a = a.to_int_list()
        joukko_b = b.to_int_list()

        for alkio in joukko_a:
            uusi_joukko.lisaa(alkio)

        for alkio in joukko_b:
            uusi_joukko.poista(alkio)

        return uusi_joukko

    def __str__(self):
        alkiot = ", ".join([str(a) for a in self.taulukko[:self.alkioiden_lkm]])
        return "{" + alkiot + "}"
