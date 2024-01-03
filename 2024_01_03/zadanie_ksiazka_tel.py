ksiazka = {
 662144425: ["Adam Jurkiewicz", "Kaden-Bandrowskiego", "Warszawa"],
 "+48 662.144.425": ["Adam Jurkiewicz", "Kaden-Bandrowskiego", "Warszawa"],
}

for telefon in ksiazka:
    adres = ksiazka[telefon]
    print(f"Kolega {adres[0]}, mieszka w {adres[2]}, ul {adres[1]} i ma nr tel. {telefon}")