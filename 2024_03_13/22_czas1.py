"""
utwórz funkcję to_time() z trzema parametrami. Przez parametry zostaną przekazane do funkcji wskazania timera: przez pierwszy parametr liczba sekund, przez drugi - liczba minut, przez trzeci - liczba godzin. Przekazane wartości spełniają warunki:

0 <= sekundy <= 59
0 <= minuty <= 59
0 <= godziny <= 23

Funkcja ma zwrócić czas zapisany jako jedna liczba całkowita w formacie: HHMMSS.

Przykłady zwracanych wartości dla różnych argumentów:

to_time( 12, 5, 16 ) → 16 05 12
to_time( 0, 5, 0 ) → 500
to_time( 3, 0, 0 ) → 03 00 00
16 godzin 5 minut 12 sekund
to_time( 3, 17, 5 ) → 51703
5 godzin 17 minut 3 sekundy
to_time( 48, 0, 11 ) → 110048
"""

def to_time(s, m, g):
    return g*10000 + m*100 + s

print(to_time(12,5,16))