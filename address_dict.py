import random
object_dimension = [8, 8, 8]  # width, length, height

led_address = dict()
led_list = list()
rain_list = list()

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


class LedRain():
    def __init__(self, x, y, offset):
        self.x = x
        self.y = y
        self.offset = offset
        self.z = object_dimension[2]

    def step(self):
        if self.offset > 0:
            self.offset -= 1
        else:
            if self.z >= 1:
                led_list.append(led_address[int(str(self.x)+str(self.y)+str(self.z))])
            self.z -= 1
            if self.z == 0:
                self.delete()
                x = random.randint(1, object_dimension[0])
                y = random.randint(1, object_dimension[1])
                rain_list.append(LedRain(x, y, 1))

    def delete(self):
        rain_list.remove(self)