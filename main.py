#Bibliotecas:
from time import sleep, time
from machine import Pin, PWM, ADC
import _thread

#Temperatuda da propria esp: esp32.raw_temperature() 
import esp32

#Bibliotecas próprias:
from ws2812b_hub import Leds, color, numbers
from button_hub import Button
from ports import *

def clock():
    import global_clock, t_0
    while True:
        t_ = time() - t_0
        m_ = int(t_ / 60)
        s_ = int(t_ % 60)
            
        global_clock = [m_, s_]
        sleep(0.02)

def pulse_buttons():
    global global_pont, t_0
    while True:
        if botton_1_in.value():
            if global_pont[0] < 99:
                global_pont[0] += 1
            sleep(0.4)
        if botton_2_in.value():
            if global_pont[3] < 99:
                global_pont[3] += 1
            sleep(0.4)

        if botton_1_out.value():
            if global_pont[0] > 1:
                global_pont[0] -= 1
            sleep(0.4)
        if botton_2_out.value():
            if global_pont[3] > 1:
                global_pont[3] -= 1
            sleep(0.4)        

        if botton_1_set_in.value():
            if global_pont[0] < 9:
                global_pont[1] += 1
            sleep(0.4)
        if botton_2_set_in.value():
            if global_pont[0] < 9:
                global_pont[2] += 1
            sleep(0.4)

        if botton_1_set_out.value():
            if global_pont[0] > 0:
                global_pont[1] -= 1
            sleep(0.4)
        if botton_2_set_out.value():
            if global_pont[0] > 0:
                global_pont[2] -= 1
            sleep(0.4)

        k = 0
        while botton_reset.value():
            if k >= 20: #5 segundos
                global_pont = [0, 0, 0, 0]
                t_0 = time()
                break
            k+=1
            sleep(0.25)
        

if __name__ == "__main__":
####   ____        __ _       _      /\/|               
####  |  _ \  ___ / _(_)_ __ (_) ___|/\/   ___  ___   _ 
####  | | | |/ _ \ |_| | '_ \| |/ __/ _ \ / _ \/ __| (_)
####  | |_| |  __/  _| | | | | | (_| (_) |  __/\__ \  _ 
####  |____/ \___|_| |_|_| |_|_|\___\___/ \___||___/ (_)
####                             )_)                      
    ###Saídas:
    tape = Leds(door = pin_led, width = 7*(6+3))

    ###Entradas:
    botton_on_off = Button(pin_botton_on_off)
    botton_reset = Button(pin_botton_reset)
    botton_1_in = Button(pin_botton_1_in)
    botton_1_out = Button(pin_botton_1_out)
    botton_1_set_in = Button(pi_botton_1_set_in)
    botton_1_set_out = Button(pi_botton_1_set_out)
    botton_2_in = Button(pin_botton_2_in)
    botton_2_out = Button(pin_botton_2_out)
    botton_2_set_in = Button(pi_botton_2_set_in)
    botton_2_set_out = Button(pi_botton_2_set_out)

####   _____                     _                  _           
####  | ____|_  _____  ___ _   _| |_ __ _ _ __   __| | ___    _ 
####  |  _| \ \/ / _ \/ __| | | | __/ _` | '_ \ / _` |/ _ \  (_)
####  | |___ >  <  __/ (__| |_| | || (_| | | | | (_| | (_) |  _ 
####  |_____/_/\_\___|\___|\__,_|\__\__,_|_| |_|\__,_|\___/  (_)
####                                                            
    global_pont = [0, 0, 0, 0]
    global_clock = [0, 0]
    t_0 = time()

    #Enquanto não liga:
    while True: 
        if botton_on_off.value() == 1:
            sleep(1)
            if botton_on_off.value() == 1:
                break
        sleep(0.05)
    #A partir daqui ele ligou...

    Leds.numbers = numbers

    _thread.start_new_thread(clock,())
    _thread.start_new_thread(pulse_buttons,())
    
    #Loop principal: 
    while True:
        Leds.add_numbers(values = f"{global_pont[0]:02d}{global_pont[1]}{global_pont[2]}{global_pont[3]:02d}{global_clock[0]:02d}{global_clock[1]:02d}")
        sleep(0.08)
        
            
