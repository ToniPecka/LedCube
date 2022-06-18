object_dimension = [8, 8, 8]  # width, length, height
import random
led_address = {
}

for i in range(object_dimension[0]):
    for j in range(object_dimension[1]):
        for k in range(object_dimension[2]):
            height = ["0"] * object_dimension[2]
            height[-(k+1)] = "1"
            address = list()
            address.append(height)
            for x in range(object_dimension[1]):
                address.append(["0"] * object_dimension[0])
            address[-(j+1)][-(i+1)] = "1"
            address_str = []
            for z in range(len(address)):
                first_join = "".join(address[z])
                address_str.append(first_join)
            address_str = "".join(address_str)
            led_address[int(str(i+1)+str(j+1)+str(k+1))] = address_str


def join_leds(led_list):
    joined_leds = list(led_list[0])
    for led in led_list:
        led = list(led)
        for i in range(len(led)):
            if led[i] == "1":
                joined_leds[i] = "1"
    joined_leds_str = "".join(joined_leds)
    return joined_leds_str


led_list = list()
number_of_rains = 4
for rain in range(number_of_rains):
    x, y = random.randrange(1, object_dimension[0] + 1), random.randrange(1, object_dimension[1] + 1)
    for i in range(object_dimension[2]):
        led = int(str(x) + str(y) + str(object_dimension[2] - i - rain))
        print(led)
        led_list.append(led_address[led])

pattern = join_leds(led_address)
print(pattern)