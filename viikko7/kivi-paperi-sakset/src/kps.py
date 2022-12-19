

class KiviPaperiSakset:
    def __init__(self, tuomari):
        self._tuomari = tuomari

    def pelaa(self):
        while True:
            ekan_siirto = self._ensimmaisen_siirto()
            if not self._onko_ok_siirto(ekan_siirto):
                break
            tokan_siirto = self._toisen_siirto(ekan_siirto)
            if not self._onko_ok_siirto(tokan_siirto):
                break
            self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self._tuomari)

        print("Kiitos!")
        print(self._tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto in ["k", "p", "s"]
