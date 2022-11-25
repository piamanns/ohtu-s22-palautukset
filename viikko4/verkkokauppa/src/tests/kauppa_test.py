import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        
        self.viitegeneraattori_mock = Mock()
        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 12
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "korvapuusti", 7)
            if tuote_id == 3:
                return Tuote(3, "pillimehu", 3)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla arvoilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_kahden_eri_tuotteen_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 12)

    def test_kahden_saman_tuotteen_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)

    def test_loytyvan_ja_loppuneen_tuotteen_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_metodi_aloita_asiointi_nollaa_edellisen_maksetun_ostoksen_tiedot(self):
        # tehdään ensimmäinen ostos
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # tehdään toinen ostos
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("ville", "54321")

        # varmistetaan, että metodia tilisiirto on kutsuttu uuden ostoksen tiedoilla
        # (edellisen ostoksen hinta ei vaikuta uuden ostoksen hintaan)
        self.pankki_mock.tilisiirto.assert_called_with("ville", 42, "54321", "33333-44455", 7)

    def test_jokainen_maksutapahtuma_saa_uuden_viitenumeron(self):
        self.viitegeneraattori_mock.uusi.side_effect = [1, 2, 3]

        # tehdään ensimmäinen ostos
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(ANY, 1, ANY, ANY, ANY)

        # tehdään toinen ostos
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("ville", "54321")

        self.pankki_mock.tilisiirto.assert_called_with(ANY, 2, ANY, ANY, ANY)

        # tehdään kolmas ostos
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("tiina", "98765")

        self.pankki_mock.tilisiirto.assert_called_with(ANY, 3, ANY, ANY, ANY)

    def test_kun_tuote_poistetaan_ostoskorista_varaston_metodia_palauta_varastoon_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)

        # poistetaan tuote korista
        self.kauppa.poista_korista(1)

        # varmistetaan, että metodia palauta_varastoon kutsutaan oikeilla arvoilla
        self.varasto_mock.palauta_varastoon.assert_called_with(Tuote(1, "maito", 5))

    def test_kun_tuote_poistetaan_ostoskorista_sen_hinta_poistuu_ostoskorin_arvosta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)

        # poistetaan tuote korista
        self.kauppa.poista_korista(1)

        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että tuotteen hinta ei enää vaikuta ostoskorin hintaan
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 7)
