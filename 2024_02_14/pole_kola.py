# napisz funkcję calcArea() z jednym parametrem,
# przez który zostanie przekazana do funkcji długość promienia koła.
# Funkcja powinna zwrócić pole koła.

# Na potrzeby zadania zakładamy
# Pi = 3.1416

#Pole = pi * (r ** 2)

def calcArea(x):
    return 3.1416 * (x**2)

print(calcArea(4))