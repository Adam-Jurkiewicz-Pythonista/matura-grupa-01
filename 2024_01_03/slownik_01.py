slownik = {
    1: "Linux",
    "Adam": 222,
    3: "System",
    4: 1.05,
    4.05: 1,
    1.04: "Linux",
    "B": "cosik",
}
print(slownik)
print(slownik.keys())
print(slownik.values())

slownik[4] = 2222 # to jest aktualizacja wartości istniejącego klucza
slownik[44] = 2222333 # to jest zupełnie nowe, więc na końcu

for elem in slownik:
    print(f"{elem=} / {slownik[elem]=}")
