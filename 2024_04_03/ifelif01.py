def setPower( pm25, pm10 ):
    power = -1
    if 0 < pm25 <= 12 and 0 < pm10 <= 20:
        power = 0
    elif 13 < pm25 <= 36 and 21 < pm10 <= 60:
        power = 1
    elif 37 < pm25 <= 60 and 61 < pm10 <= 100:
        power = 2
    elif 61 < pm25 <= 84 and 101 < pm10 <= 140:
        power = 3
    elif 85 < pm25 <= 120 and 141 < pm10 <= 200:
        power = 4
    elif pm25 > 120 and pm10 > 200:
        power = 5
    # tu mamy 97,13, a power -1
    return power

print(setPower(97, 13))
print(setPower(17,58))