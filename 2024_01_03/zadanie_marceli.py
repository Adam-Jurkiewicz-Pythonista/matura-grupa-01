from random import choice, randint

lista_imion_m = ["Marek", "Jacek", "Jakub", "Maciej", "Zbigniew", "Dariusz", "Ignacy", "Robert", "Michał", "Marcin", "Artur", "Bogdan"]
lista_imion_z = ["Julia", "Natalia", "Maria", "Klementyna", "Anna", "Barbara", "Józefa", "Stefania", "Daria", "Mirosława", "Agata", "Marzena"]
lista_nazwisk_m = ["Kowalski", "Nowak", "Sochociński", "Pilc", "Michalczyk", "Wiśniewski", "Karolak", "Borowicz", "Kurzyczak", "Miechacz"]
lista_nazwisk_z = ["Kowalska", "Nowak", "Sochocińska", "Pilc", "Michalczyk", "Wiśniewska", "Karolak", "Borowicz", "Kurzyczak", "Miechacz"]
ulice = ["Dworcowa", "Mysia", "Kościuszki", "Moniuszki", "Wojska Polskiego", "Prosta", "Mokra", "Klonowa", "Dębowa", "Batorego"]

ksiazka_tel = {}

def generuj_kontakt():
    plec = randint(0,1)
    if plec == 0:
        imie = choice(lista_imion_m)
        nazwisko = choice(lista_nazwisk_m)
        nr_tel = randint(100000000,999999999)
        adres = f"{choice(ulice)} {str(randint(1,150))}"
    else:
        imie = choice(lista_imion_z)
        nazwisko = choice(lista_nazwisk_z)
        nr_tel = randint(100000000,999999999)
        adres = f"{choice(ulice)} {str(randint(1,150))}"
    #print([imie, nazwisko, adres])
    ksiazka_tel[nr_tel] = [imie, nazwisko, adres]

def generuj_ksiazke(dlugosc):
    for n in range(0,dlugosc):
        generuj_kontakt()

def pokaz_ksiazke():
    idx = 0
    for n in ksiazka_tel:
        print(f"+48 {list(ksiazka_tel.keys())[idx]} - {ksiazka_tel[n][0]} {ksiazka_tel[n][1]} zamieszkały/a pod adresem {ksiazka_tel[n][2]}")
        idx += 1

generuj_ksiazke(20)
pokaz_ksiazke()