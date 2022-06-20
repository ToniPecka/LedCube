import random
from address_dict import *

number_of_rains = 8
led_list.clear()

for rain in range(number_of_rains):
    x = random.randint(1, object_dimension[0])
    y = random.randint(1, object_dimension[1])
    rain_list.append(LedRain(x, y, 0))
for item in rain_list:
    item.step()

pattern = join_leds(led_list)
print(pattern)