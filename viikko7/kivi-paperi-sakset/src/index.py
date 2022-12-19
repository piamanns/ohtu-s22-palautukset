from kps_tehdas import KPSTehdas

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        pelityyppi = {
            "a": KPSTehdas.luo_peli_pelaaja_vs_pelaaja,
            "b": KPSTehdas.luo_peli_pelaaja_vs_tekoaly,
            "c": KPSTehdas.luo_peli_pelaaja_vs_parempi_tekoaly
        }

        valinta = input()

        if valinta in pelityyppi:
            print("Peli loppuu kun pelaaja antaa virheellisen siirron,\n"
                  + "eli jonkun muun kuin k, p tai s.")
            peli = pelityyppi[valinta]()
            peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
