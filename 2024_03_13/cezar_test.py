"""
5 13 18 8 19 20 22 2 18 25
"""
def cezar(tekst_jawny, klucz):
    szyfrowany = ""
    for znak in tekst_jawny:
        nowe_ascii = ord(znak) + klucz
        przesuniecie = (nowe_ascii - 65) % 26
        nowa_litera = chr(przesuniecie + 65)
        szyfrowany += nowa_litera
    return szyfrowany


klucze = []
with open("dane.txt", "r") as file:
    for line in file:
        jawny, szyfr = line.split()
        klucz = 0
        while klucz < 26:
            # print(f"Sprawdzam {jawny=} dla {klucz=}")
            if cezar(jawny, klucz) == szyfr:
                klucze.append(str(klucz))
                break
            klucz += 1

print(klucze)
print(" ".join(klucze))