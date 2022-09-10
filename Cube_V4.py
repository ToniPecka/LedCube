# Kostka V4
# Levy predni dolni roh je souradnice CS0.
# Odpredu dozadu rada, Odspodu nahoru vrstvy, otoceno v inputu.
# pattern("vrstva"+"rada_8"+"rada_7"+"rada_6"+...+"rada_1")
# Vrstva = 87654321     # Rada_X = 87654321
# FULL LIGHT: pattern = ("11111111"+"11111111"+"11111111"+"11111111"+"11111111"+"11111111"+"11111111"+"11111111"+"11111111")
from time import sleep
from gpiozero import LED
from random import randrange

# GPIO Definition
serial = LED(14) # SER Data vstup                   -Orange---Serial-
enabler = LED(15) # OE| LowVolt = povoli vystupy    -Gray---Enabler-
store = LED(18)  # RCLK Storage clock show stored   -Violet---Store-
clock = LED(23) # SRCLK Shift reg clock             -Green---Clock- 
clear = LED(24) # SRCLR| Reset LowVolt = clear      -Brown---Clear-

# Basic Pattern
pattern = ("00000001"+"00000000"+"00000000"+"00000000"+"00000000"+"00000000"+"00000000"+"00000000"+"00000001")

# Miscellaneous
signal_gap = 0.00000000001      # vteriny pauza mezi signaly

# Definice fce pro zobrazeni
def show(pattern):
    sleep(signal_gap)
    clear.off()
    sleep(signal_gap)
    clear.on()
    for i in range(72):
        if pattern[i] == "1":
            serial.on()
            sleep(signal_gap)
        if pattern[i] == "0":
            serial.off()
            sleep(signal_gap)

        clock.on()
        sleep(signal_gap)
        clock.off()
        serial.off()
        sleep(signal_gap)
    store.on()
    sleep(signal_gap)
    store.off()

# Awake The Cube and set basic pattern
serial.off()
enabler.off()
store.off()
clock.off()
clear.on()
show(pattern)
print('I em Awake')

# Cube Modes
while(True):
    print('I can do: breathe, rain, ..., exit')
    mode = input('Type Mode Name = ')

    # Mode: breathe
    if mode == 'breathe':
        gap_breath = 0.0001   # Mezera pro dech, Vteriny
        gap_breath_dark = 0.0001
        for j in range(6):
            for i in range(149):
                enabler.on()
                sleep((1+i) * gap_breath_dark)
                enabler.off()
                sleep((150-i) * gap_breath)

            for i in range(149):
                enabler.on()
                sleep((150-i) * gap_breath)
                enabler.off()
                sleep((1+i) * gap_breath_dark)

    # Mode: rain
    if mode == 'rain':
        rady_seznam = ['0','0','0','0','0','0','0','0'] # Template seznam  pro nasledujici vrstvy deste
        vrstvy_seznam = ['0','0','0','0','0','0','0','0'] # Template seznam  pro nasledujici vrstvy deste
        for s in range(8):
            rady = ''
            for r in range(8):   # vytvori vrstvu deste a seznam vrstev
                rada = ['0','0','0','0','0','0','0','0']
                rada[randrange(0, 8)] = str(randrange(2))
                rada_str = "".join(rada)    # Spojeni seznamu rad
                rady = (rady + rada_str)

            vrstva = ['0','0','0','0','0','0','0','0']
            vrstva[s] = '1'
            vrstva_str = "".join(vrstva)
            vrstvy_seznam[s] = vrstva_str # vrstvy pro padajici dest
            rady_seznam[s] = rady # Naplni seznam s desti

        for i in range(8): # meni vrstvy odzhora nahoru
            sleep(0.05)
            pattern = (vrstvy_seznam[i] + rady_seznam[0])
            show(pattern)
            sleep(0.05)
            if i > 1:
                pattern = (vrstvy_seznam[i-1] + rady_seznam[1])
                show(pattern)
                sleep(0.05)
            if i > 3:
                pattern = (vrstvy_seznam[i-3] + rady_seznam[2])
                show(pattern)
                sleep(0.05)
            if i > 5:
                pattern = (vrstvy_seznam[i-5] + rady_seznam[3])
                show(pattern)
                sleep(0.05)
            if i > 7:
                pattern = (vrstvy_seznam[i-1] + rady_seznam[4])
                show(pattern)
                sleep(0.05)
           
           
    # Mode: exit
    if mode == 'exit':
        gap_exit = 0.0001
        for i in range(199):
            enabler.on()
            sleep((1+i) * gap_exit)
            enabler.off()
            sleep((200-i) * gap_exit)

        enabler.on()
        break
