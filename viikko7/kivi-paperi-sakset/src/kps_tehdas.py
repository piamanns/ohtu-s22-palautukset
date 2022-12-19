from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from tuomari import Tuomari


class KPSTehdas:
    @staticmethod
    def luo_peli_pelaaja_vs_pelaaja():
        return KPSPelaajaVsPelaaja(Tuomari())
    
    @staticmethod
    def luo_peli_pelaaja_vs_tekoaly():
        return KPSTekoaly(Tuomari(), Tekoaly())

    @staticmethod
    def luo_peli_pelaaja_vs_parempi_tekoaly():
        return KPSTekoaly(Tuomari(), TekoalyParannettu(10))
