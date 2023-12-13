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
for element in dane_prz1:
    e1, e2 = element.strip().split(",")
    lista = parsuj(e1,e2)
    lista_przedzialow.append(lista)

# print(lista_przedzialow)

max_odd = 0
max_line = 0
for idx, value in enumerate(lista_przedzialow):
    max_odd_l = len([ x for x in value if odd(x) == 1 ])
    print(f"{idx=} {max_odd_l=} {value=}")
    if max_odd_l > max_odd:
        max_odd = max_odd_l
        max_line = idx + 1

print(f"Najwięcej liczb nieparzystych {max_odd} w wierszu {max_line} = {lista_przedzialow[max_line -1]}")

