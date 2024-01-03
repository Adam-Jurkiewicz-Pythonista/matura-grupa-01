lista = [1, "A", 3.14]
wart_num = 5

def aktual1():
    lista[1] = 333333

def aktual2():
    wart_num = 444444

def aktual3():
    global wart_num  # niezalecane!!!!!
    wart_num = 444444

print(lista)
print(wart_num)
aktual1()
aktual2()
print(lista)
print(wart_num)
aktual3()
print(wart_num)
