import random
from time import sleep
from LedCube_animated import *

number_of_rains = 1

while True:
    led_list.clear()
    if len(rain_list) == 0:
        for rain in range(number_of_rains):
            x = random.randint(1, cube_dimension)
            y = random.randint(1, cube_dimension)
            rain_list.append(LedRain(x, y, rain))
    for item in rain_list:
        item.step()
    for led in led_list:
        print(led_list)
    sleep(0.3)