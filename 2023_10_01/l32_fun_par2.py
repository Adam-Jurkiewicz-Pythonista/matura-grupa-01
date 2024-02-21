def funkcja( x, y ):
    print("Podano:", x, "Typ to:", type(x))
    print("Podano:", y, "Typ to:", type(y))
    print(x*y)

funkcja(2,3)
funkcja(2.54,24)
funkcja("aaa", "bbb") # Tu bład, bo dane do x*y (wiersz 4) są złe.
