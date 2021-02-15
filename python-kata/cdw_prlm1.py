upSpeed, downSpeed, desiredHeight = 100, 10, 910


def growing_plant(upSpeed, downSpeed, desiredHeight):
    plantHeight = 0
    day = 0
    while True:
        plantHeight += upSpeed
        day += 1
        if plantHeight >= desiredHeight: break
        if plantHeight < desiredHeight: plantHeight -= downSpeed
    return day


print(growing_plant(upSpeed, downSpeed, desiredHeight))
