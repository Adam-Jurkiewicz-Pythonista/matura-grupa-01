"""
to_time( 56 ) → 56
56 sekund
to_time( 60 ) → 1 00
1 minuta
to_time( 61 ) → 101
1 minuta i jedna sekunda
to_time( 122 ) → 2 02
2 minuty i 2 sekundy
to_time( 612 ) → 1012
10 minut i 12 sekund
to_time( 3601 ) → 10001
to_time( 8417 ) ->
1 godzina i 1 sekunda
to_time( 3671 ) → 10111
1 godzina 1 minuta i 11 sekund
"""
def to_time(sek):
    sekundy = sek % 60
    minuty = sek // 60
    godz = minuty // 60
    minuty2 = minuty % 60
    return godz*10000 + minuty2*100+ sekundy

def to_time(sek):
    minuty, sekundy = divmod(sek, 60)
    godz, minuty = divmod(minuty, 60)
    return godz*10000 + minuty*100+ sekundy