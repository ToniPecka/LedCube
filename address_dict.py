import random

cube_dimension = 8 # width, length, height

led_address = dict()
led_list = list()
rain_list = list()

for i in range(cube_dimension):
    for j in range(cube_dimension):
        for k in range(cube_dimension):
            height = ["0"] * cube_dimension
            height[-(k+1)] = "1"
            address = list()
            address.append(height)
            for x in range(cube_dimension):
                address.append(["0"] * cube_dimension)
            address[-(j+1)][-(i+1)] = "1"
            address_str = []
            for z in range(len(address)):
                first_join = "".join(address[z])
                address_str.append(first_join)
            address_str = "".join(address_str)
            led_address[int(str(i+1)+str(j+1)+str(k+1))] = address_str


class LedRain:
    def __init__(self, x, y, offset):
        self.x = x
        self.y = y
        self.offset = offset
        self.z = cube_dimension

    def step(self):
        if self.offset > 0:
            self.offset -= 1
        else:
            if self.z >= 1:
                led_list.append(led_address[int(str(self.x)+str(self.y)+str(self.z))])
                list_of_rain_leds.append(RainLed(self.x, self.y, self.z))

            self.z -= 1
            if self.z == 0:
                self.delete()
                x = random.randint(1, cube_dimension)
                y = random.randint(1, cube_dimension)
                rain_list.append(LedRain(x, y, 1))

    def delete(self):
        rain_list.remove(self)