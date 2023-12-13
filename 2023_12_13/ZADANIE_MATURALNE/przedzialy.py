def parsuj(od, do):
    a, b = od[0], int(od[1:])
    c, d = int(do[:-1]), do[-1]
    if a == "(":
        b += 1
    if d == ">":
        c += 1
    return [ x for x in range(b,c)]

def odd(number):
    if number % 2 == 1:
        return True
    return False

with open("przedzialy.txt", "r") as fl:
    dane_prz1 = fl.readlines()

# print(dane_prz1)

lista_przedzialow = []
lista_odd = []
for element in dane_prz1:
    e1, e2 = element.strip().split(",")
    lista = parsuj(e1,e2)
    ile_odd = len([ x for x in lista if odd(x) == 1 ])
    # ile_odd = len([x for x in lista if x % 2 == 1])
    lista_przedzialow.append(lista)
    lista_odd.append(ile_odd)

# print(lista_przedzialow)

max_odd = max(lista_odd)
print(f"{max_odd=}")
max_line = []

for idx, value in enumerate(lista_odd):
    if value == max_odd:
        # print(f"{idx=} {value=}")
        max_line.append(str(idx+1))

lines = " ".join(max_line)
print(f"Najwięcej liczb nieparzystych {max_odd} w wierszach {lines}")

with open("wyniki1.txt", "a") as out:
    out.write(f"{max_odd} \n")
    out.write(f"{lines} \n")

