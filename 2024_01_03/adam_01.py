def parsuj(od, do):
    a, b = od[0], int(od[1:])
    c, d = int(do[:-1]), do[-1]
    if a == "(":
        b += 1
    if d == ">":
        c += 1
    return [x for x in range(b,c)]


with open("przedzialy.txt", "r") as fl:
    dane_prz1 = fl.readlines()

lista_przedzialow = []
suma_zbiorow = set()
for element in dane_prz1:
    e1, e2 = element.strip().split(",")
    lista = parsuj(e1,e2)
    suma_zbiorow = suma_zbiorow.union(set(lista))
    lista_przedzialow.append(lista)

print(suma_zbiorow)
posortowane = sorted(suma_zbiorow)
print("---")
print(posortowane)