from time import sleep

len_number_1 = 3
len_number_2 = 2

color_1 = [0, 250, 0] #Verde
color_2 = [250, 0, 0] #Vermelho
color_3 = [255, 255, 0] #Amarelo

press_to_on = 1

from random import random
def animation_load(leds, num_leds:int, random = random):
    for i in range(num_leds - 1):
        if leds[i + 1] != [0, 0, 0]:
            leds[i] = [100, 120, 180]
        elif leds[i] != [0, 0, 0]:
            mean = int((leds[i][0] + leds[i][1] + leds[i][2])/3)
            leds[i] = [mean, mean, leds[i][2]]
 
def del_leds(leds, num_leds:int):
    if type(num_leds) != int:
        num_leds = int(num_leds)
        
    for i in range(7):
        for i in range(num_leds):
            leds[i] = [int(leds[i][0]*0.5),
                       int(leds[i][1]*0.5),
                       int(leds[i][2]*0.5)]
        sleep(0.01)
    for i in range(num_leds):
        leds[i] = [0, 0, 0]

def new_number(len_:int):

    number_ = {"0":[1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    0],
               "1":[0,
                    0,
                    1,
                    1,
                    0,
                    0,
                    0],
               "2":[1,
                    1,
                    0,
                    1,
                    1,
                    0,
                    1],
               "3":[0,
                    1,
                    1,
                    1,
                    1,
                    0,
                    1],
               "4":[0,
                    0,
                    1,
                    1,
                    0,
                    1,
                    1],
               "5":[0,
                    1,
                    1,
                    0,
                    1,
                    1,
                    1],
               "6":[1,
                    1,
                    1,
                    0,
                    1,
                    1,
                    1],
               "7":[0,
                    0,
                    1,
                    1,
                    1,
                    0,
                    0],
               "8":[1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1],
               "9":[0,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1]}
    
    number = {"0":[],
              "1":[],
              "2":[],
              "3":[],
              "4":[],
              "5":[],
              "6":[],
              "7":[],
              "8":[],
              "9":[]}
    
    for k in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        for i in range(7):
            for _ in range(len_):
                number[k].append(number_[k][i])
        
    return number
