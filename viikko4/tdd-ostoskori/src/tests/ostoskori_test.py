import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        kahvi = Tuote("Kahvi", 5)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kahvi)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        kahvi = Tuote("Kahvi", 5)
        
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kahvi)

        self.assertEqual(self.kori.hinta(), 8)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 6)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        # testaa ett?? metodin palauttaman listan pituus 1
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        # testaa t????ll??, ett?? palautetun listan ensimm??inen ostos on halutunkaltainen.
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosoliota(self):
        maito = Tuote("Maito", 3)
        kahvi = Tuote("Kahvi", 5)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kahvi)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)
    
    def test_kahden_saman_tuotteen_lis????misen_j??lkeen_ostoskori_sis??lt????_ostoksen_jolla_sama_nimi_kuin_tuotteella_ja_lkm_2(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()

        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 2)

    def test_jos_korissa_kaksi_samaa_tuotetta_ja_toisen_poistaa_koriin_jaa_ostos_jossa_tuotteen_lkm_1(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.kori.poista_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 1)
    
    def test_jos_koriin_lisatty_tuote_ja_tama_tuote_poistetaan_ostoskori_on_tyhja(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        ostokset = self.kori.ostokset()
        
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(ostokset), 0)

    def test_metodi_tyhjenna_tyhjentaa_ostoskorin(self):
        maito = Tuote("Maito", 3)
        kahvi = Tuote("Kahvi", 5)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kahvi)

        self.kori.tyhjenna()

        ostokset = self.kori.ostokset()
        
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(ostokset), 0)
