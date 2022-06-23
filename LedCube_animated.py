import random

from address_dict import *
import pyglet
from math import pi

window = pyglet.window.Window(fullscreen=True, caption="LedCube")
window.set_exclusive_mouse(False)
batch = pyglet.graphics.Batch()
leds = cube_dimension + cube_dimension + cube_dimension
circle_size = 5
height_offset = window.height/(cube_dimension + 1)
width_offset = height_offset
angle = 30*pi/180
width_const = 2.5
height_const = 5
line_width = 1
color = (0, 255, 0)
opacity = 50
lvl1 = pyglet.graphics.OrderedGroup(0)
lvl2 = pyglet.graphics.OrderedGroup(1)
list_of_rain_leds = list()
list_of_white_leds = list()

class Led:
    def __init__(self, x , y):
        self.x = x
        self.y = y
        list_of_white_leds.append(pyglet.shapes.Circle(x = self.x, y = self.y, radius = circle_size, color=(200, 200, 200), batch=batch, group=lvl1))


class BasicLed:
    def __init__(self, x , y):
        self.x = x
        self.y = y


class RainLed:
    def __init__(self, x, y, z):
        self.x = x - 1
        self.y = y - 1
        self.z = z - 1
        self.life = 1
        a = window.width / 2 - (cube_dimension / 2) * width_offset + width_offset * self.x + height_offset / width_const * self.y
        b = height_offset * self.z + height_offset + height_offset / height_const * self.y - height_offset / height_const - 50
        self.image = pyglet.shapes.Circle(x = a, y = b, radius = 1.5*circle_size, color=(255, 0, 0), batch=batch, group=lvl2)

    def tick(self, dt):
        self.life -= dt
        if self.life < 0:
            self.image.delete()
            list_of_rain_leds.remove(self)



list_of_leds = list()
for z in range(cube_dimension):
    for y in range(cube_dimension):
        for x in range(cube_dimension):
            a = window.width / 2 - (cube_dimension/2) * width_offset + width_offset * x + height_offset / width_const * y
            b = height_offset*z+height_offset + height_offset/height_const*y - height_offset/height_const - 50
            list_of_leds.append(Led(a, b))

lines = list()
for x in range(cube_dimension * cube_dimension * cube_dimension):
    if x < cube_dimension * cube_dimension * cube_dimension-1:
        lines.append(pyglet.shapes.Line(list_of_leds[x].x, list_of_leds[x].y, list_of_leds[x+1].x, list_of_leds[x+1].y,width=line_width,color=color, batch=batch))
        lines[x].opacity = opacity

for x in range(cube_dimension * cube_dimension):
    if x > 0:
        lines.remove(lines[x * (cube_dimension - 1)])

#Zjednodušení
list_of_leds2 = list()
for x in range(cube_dimension):
    for y in range(cube_dimension):
        for z in range(cube_dimension):
            a = window.width / 2 - (cube_dimension/2) * width_offset + width_offset * x + height_offset / width_const * y
            b = height_offset*z+height_offset + height_offset/height_const*y - height_offset/height_const - 50
            list_of_leds2.append(BasicLed(a, b))
lines2 = list()
for x in range(cube_dimension * cube_dimension * cube_dimension):
    if x < cube_dimension * cube_dimension * cube_dimension-1:
        lines2.append(pyglet.shapes.Line(list_of_leds2[x].x, list_of_leds2[x].y, list_of_leds2[x+1].x, list_of_leds2[x+1].y,width=line_width,color=color, batch=batch))
        lines2[x].opacity = opacity

for x in range(cube_dimension * cube_dimension):
    if x > 0:
        lines2.remove(lines2[x * (cube_dimension - 1)])

list_of_leds3 = list()
for z in range(cube_dimension):
    for x in range(cube_dimension):
        for y in range(cube_dimension):
            a = window.width / 2 - (cube_dimension/2) * width_offset + width_offset * x + height_offset / width_const * y
            b = height_offset*z+height_offset + height_offset/height_const*y - height_offset/height_const - 50
            list_of_leds3.append(BasicLed(a, b))
lines3 = list()
for x in range(cube_dimension * cube_dimension * cube_dimension):
    if x < cube_dimension * cube_dimension * cube_dimension-1:
        lines3.append(pyglet.shapes.Line(list_of_leds3[x].x, list_of_leds3[x].y, list_of_leds3[x+1].x, list_of_leds3[x+1].y,width=line_width,color=color, batch=batch))
        lines3[x].opacity = opacity

for x in range(cube_dimension * cube_dimension):
    if x > 0:
        lines3.remove(lines3[x * (cube_dimension - 1)])


@window.event
def on_draw():
    window.clear()
    batch.draw()

def tick(dt):
    for item in list_of_rain_leds:
        item.tick(dt)

def spawn_led(dt):
    list_of_rain_leds.append(RainLed(random.randint(1, cube_dimension), random.randint(1, cube_dimension), random.randint(1, cube_dimension)))


pyglet.clock.schedule_interval(tick, 1 / 60)
pyglet.clock.schedule_interval(spawn_led, 0.2)
pyglet.app.run()