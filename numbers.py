len_number_1 = 3
len_number_2 = 3

color_1 = [200, 100, 100]
color_2 = [100, 100, 200]
color_3 = [100, 200, 100]

press_to_on = 1

from random import random
def animation_load(leds, num_leds:int, random = random):
    for i in range(num_leds - 1):
        if n[i + 1] != [0, 0, 0]:
            n[i] = [100, 120, 180]
        elif n[i] != [0, 0, 0]:
            mean = int((n[i][0] + n[i][1] + n[i][2])/3)
            n[i] = [mean, mean, n[i][2]]
 
def del_leds(leds, num_leds:int):
    for i in range(7):
        for i in range(len(num_leds)):
            leds[i] = [int(leds[i][0]*0.5),
                       int(leds[i][1]*0.5),
                       int(leds[i][2]*0.5)]
        sleep(0.01)
    for i in range(len(num_leds)):
        leds[i] = [0, 0, 0]

def new_number(len_:int):
    number = {"0":[*[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[0 for i in range(len_)]],
               "1":[*[0 for i in range(len_)],
                    *[0 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[0 for i in range(len_)],
                    *[0 for i in range(len_)],
                    *[0 for i in range(len_)]],
               "2":[*[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[0 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[0 for i in range(len_)],
                    *[1 for i in range(len_)]],
               "3":[*[0 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[0 for i in range(len_)],
                    *[1 for i in range(len_)]],
               "4":[*[0 for i in range(len_)],
                    *[0 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[0 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)]],
               "5":[*[0 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[0 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)]],
               "6":[*[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[0 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)]],
               "7":[*[0 for i in range(len_)],
                    *[0 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[0 for i in range(len_)],
                    *[0 for i in range(len_)]],
               "8":[*[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)]],
               "9":[*[0 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)],
                    *[1 for i in range(len_)]]}
    return number
