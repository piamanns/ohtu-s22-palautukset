# "Muistava tekoäly"
class TekoalyParannettu:
    def __init__(self, muistin_koko):
        self._muisti = [None] * muistin_koko
        self._vapaa_muisti_indeksi = 0

    def aseta_siirto(self, siirto):
        # jos muisti täyttyy, unohdetaan vanhin alkio
        if self._vapaa_muisti_indeksi == len(self._muisti):
            self._vapauta_muistia()
            self._vapaa_muisti_indeksi -= 1

        self._muisti[self._vapaa_muisti_indeksi] = siirto
        self._vapaa_muisti_indeksi += 1

    def _vapauta_muistia(self):
        for i in range(1, len(self._muisti)):
            self._muisti[i - 1] = self._muisti[i]

    def anna_siirto(self):
        k, p, s = self._laske_aiemmat()
        print("k,p,s", k,p,s)

        # Tehdään siirron valinta esimerkiksi seuraavasti;
        # - jos kiviä eniten, annetaan aina paperi
        # - jos papereita eniten, annetaan aina sakset
        # muulloin annetaan aina kivi
        # print("k,p,s", k, p, s)
        if k > p and k > s:
            return "p"
        elif p > s:
            return "s"
        else:
            return "k"

        # Tehokkaampiakin tapoja löytyy, mutta niistä lisää
        # Johdatus Tekoälyyn kurssilla!

    def _laske_aiemmat(self):
        k = 0
        p = 0
        s = 0

        for i in range(0, self._vapaa_muisti_indeksi):
            seuraava = self._muisti[i]
            if seuraava == "k":
                k += 1
            elif seuraava == "p":
                p += 1
            else:
                s += 1

        return (k,p,s)
