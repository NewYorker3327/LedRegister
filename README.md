# LedRegister

Library created for tennis scoreboards.

In this repository, there are also three general-purpose libraries:

## ```button_hub.py```

### A library designed to simplify the production of boards with inverted buttons. This means that during the production of a product, you can install a normal or inverted button, and the program will function correctly with both configurations. To achieve this, use the ```Button``` class.

Example ```Button```:
```
from button_hub import Button

pin = 5
b_1 = Button(pin)

if b_1.Value():
  print("Botton is ON")
else:
  print("Botton is OFF")
```

## ```register.py```

### This library is intended for working with registers; however, it has not been validated yet.

## ```ws2812b_hub.py```

### This library allows for easier handling of LED strips using the ```Leds``` class, adding predefined colors and some effects. Additionally, it is possible to assemble an LED display using this library, utilizing the ```Matrix_Leds``` class.

Example ```Leds```:
```
from ws2812b_hub import color, numbers, Leds
 
pin = 5
width = 7*3*5 #7 is the number of 'blocks,' 3 is the number of LEDs per block, and 5 is the number of digits on a board with this strip
my_tape_led = Leds(pin, width)

my_tap_led.add_numbers(numbers, values = "57281") #If the strip is allocated correctly, it will display '57281' on the LEDs
```

Example ```Matrix_Leds```:
```
from ws2812b_hub import color, numbers, Matrix_Leds

If you assemble a matrix of LEDs from top to bottom like this:
    >>>>>>>>>>>>>>v
    v<<<<<<<<<<<<<<
    >>>>>>>>>>>>>>v
    v<<<<<<<<<<<<<<
 
pin = 5
width = 30*10 #Width and height of LEDs, Note that in reality, this is a strip with 300 LEDs:
lines = 10
my_led_tv = Matrix_Leds(pin, width, lines)

you_dict = {"C":[[1,1,1,1,1],
                  [0,0,0,0,1],
                  [1,0,0,0,0],
                  [0,0,0,0,1],
                  [1,1,1,1,1]]}

my_led_tv.strings = you_dict #Your dict of characters

my_led_tv.write("ABCDEFGHIJ")
```
