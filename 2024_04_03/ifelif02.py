def setPower( pm25, pm10 ):
    power = -1
    if pm25 > 120 or pm10 > 200:
        power = 5
    elif 85 <= pm25 <= 120 or 141 <= pm10 <= 200:
        power = 4
    elif 61 <= pm25 <= 84 or 101 <= pm10 <= 140:
        power = 3
    elif 37 <= pm25 <= 60 or 61 <= pm10 <= 100:
        power = 2
    elif 13 <= pm25 <= 36 or 21 <= pm10 <= 60:
        power = 1
    # elif 0 <= pm25 <= 12 or 0 <= pm10 <= 20:
    else:
        power = 0

    return power

print(setPower(-3,19)) # 0, 1