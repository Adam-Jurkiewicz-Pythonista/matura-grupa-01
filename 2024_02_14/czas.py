"""
utwórz funkcję to_time() z jednym parametrem.
Tym razem do funkcji zostanie przekazana liczba sekund,
mieszcząca się w przedziale od 0 do 86000.

Funkcja powinna przeliczyć czas podany w sekundach na godziny, minuty oraz sekundy,
i tak jak w poprzednim zadaniu zwrócić czas zapisany za pomocą jednej liczby całkowitej
w formacie:

HHMMSS,

przy czym wartości minut i godzin w zwracanej wartości pojawią się tylko wtedy,
kiedy liczba sekund przekazana przez parametr jest wystarczająco duża.

Przykłady zwracanych wartości dla różnych argumentów:

to_time( 56 ) → 56
56 sekund
to_time( 60 ) → 100
1 minuta

to_time( 612 ) → 1012
10 minut i 12 sekund

"""