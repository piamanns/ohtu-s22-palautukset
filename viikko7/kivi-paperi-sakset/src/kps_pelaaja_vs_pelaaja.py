from kps import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def __init__(self, tuomari):
        super().__init__(tuomari)

    def _toisen_siirto(self, ensimmaisen_siirto):
        return input("Toisen pelaajan siirto: ")
