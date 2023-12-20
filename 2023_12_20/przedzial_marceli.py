def parsuj(od, do):
    a, b = od[0], int(od[1:])
    c, d = int(do[:-1]), do[-1]
    if a == "(":
        b += 1
    if d == ">":
        c += 1
    return [ x for x in range(b,c)]

def czypierwsza(num):
    if num == 2:
        return True
    if num % 2 == 0 or num <= 1:
        return False

    pierw = int(num ** 0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if num % dzielnik == 0:
            return False
    return True

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
max_line = []
for idx, value in enumerate(lista_przedzialow):
    max_odd_l = len([ x for x in value if czypierwsza(x) == 1 ])
    print(f"{idx=} {max_odd_l=} {value=}")
    if max_odd_l > max_odd:
        max_odd = max_odd_l
        max_line.clear()
        max_line.append(idx)
    elif max_odd_l == max_odd:
        max_line.append(idx)

print(f"Najwięcej liczb pierwszych ({max_odd}) jest w wierszu/ach")
#{lista_przedzialow[max_line -1]}
with open("wyniki1.txt", "a") as dane_out:
    for idx, val in enumerate(max_line):
        dane_out.write(f"{dane_prz1[max_line[idx]]}")