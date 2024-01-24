#Bibliotecas:
from time import sleep, time
from machine import Pin, PWM, ADC
import _thread

#Temperatuda da propria esp: esp32.raw_temperature() 
import esp32

#Bibliotecas próprias:
from button_hub import Button
import machine
from neopixel import NeoPixel
from pins import *
from numbers import *

version = [0, 1, 0]

def clock():
    global global_clock, t_0
    while True:
        t_ = time() - t_0
        h_ = int(t_/3600)
        m_ = int((t_%3600)/60)
        s_ = int(t_%60)

        if m_ < 10:
            m_ = "0" + str(m_)
        if s_ < 10:
            s_ = "0" + str(s_)
            
        global_clock = [str(h_), str(m_), str(s_)]
        sleep(0.2)

def pulse_buttons():
    global global_pont, t_0
    pause_ = 0.25
    while True:
        if botton_1_in.value():
            if global_pont[0] < 99:
                global_pont[0] += 1
            sleep(pause_)
        if botton_2_in.value():
            if global_pont[3] < 99:
                global_pont[3] += 1
            sleep(pause_)

        if botton_1_out.value():
            if global_pont[0] > 0:
                global_pont[0] -= 1
            sleep(pause_)
        if botton_2_out.value():
            if global_pont[3] > 0:
                global_pont[3] -= 1
            sleep(pause_)        

        if botton_1_set_in.value():
            if global_pont[1] < 9:
                global_pont[1] += 1
            sleep(pause_)
        if botton_2_set_in.value():
            if global_pont[2] < 9:
                global_pont[2] += 1
            sleep(pause_)

        if botton_1_set_out.value():
            if global_pont[1] > 0:
                global_pont[1] -= 1
            sleep(pause_)
        if botton_2_set_out.value():
            if global_pont[2] > 0:
                global_pont[2] -= 1
            sleep(pause_)

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
    part_1 = 7*len_number_1*6
    part_2 = 7*len_number_2*3
    num_leds = part_1 + part_2
    leds = NeoPixel(machine.Pin(pin_led), num_leds + 2) #Numero de leds mais 2 leds brancos

    ###Entradas:
    error_button = True
    while error_button:
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
        try:
            botton_on_off.value()
            error_button = False
        except AttributeError:
            error_button = True
            print("Erro no botao")
            leds[0] = [255, 255, 255]
            leds.write()
            sleep(0.5)
            leds[0] = [0, 0, 0]
            sleep(0.5)

    ###Tamanho dos números no placar:
    number_1 = new_number(len_number_1)
    number_2 = new_number(len_number_2)
    number_1_inverse = new_number(len_number_1, inverse = True)
    number_2_inverse = new_number(len_number_2, inverse = True)
    print("Saidas e entradas definidas")
    
    for i in range(part_1 + part_2):
        leds[i] = [250, 250, 250]
    leds.write()
    print("Todos leds acessos")

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
    on_all = False
    while on_all == False: 
        if botton_on_off.value() == 1:
            print("No botao 0")
            continue_ = True
            for i in range(10):
                print(f"No botao {i + 1}")
                if botton_on_off.value() == 0:
                    continue_ = False
                    print("Soltou o botão")
                if continue_:
                    animation_load(leds, num_leds)
                    #sleep(press_to_on/num_leds)
                    sleep(0.05)
                    if botton_on_off.value() == 1:
                        print("Feito")
                        on_all = True
                        continue_ = False
        del_leds(leds, num_leds)
        sleep(0.05)
    print("Ligou")
    #A partir daqui ele ligou...

    _thread.start_new_thread(clock,())
    _thread.start_new_thread(pulse_buttons,())
    
    #Loop principal: 
    while True:
        #Original:
        #final_values = [f"{global_pont[0]:02d}", global_pont[1], global_pont[2], f"{global_pont[3]:02d}", global_clock[0], global_clock[1]]
        #Com primeira placa invertida:
        final_values = [global_pont[1], f"{global_pont[0]:02d}", global_pont[2], f"{global_pont[3]:02d}", global_clock[0], global_clock[1]]

        final_values = list(map(str, final_values))
        final_values = "".join(final_values)

        #Com a primeira placa invertida:
        final_values = f"{final_values[1]}{final_values[0]}{final_values[2:]}"
        
        final_leds = []
        i = 0
        for part_number in final_values:
            if i < int(part_1/2): #Se for a placa invertida
                if i < part_1:
                    try:
                        final_leds.extend(number_1_inverse[part_number])
                    except:
                        final_leds.extend(number_1_inverse["0"])
                else:
                    try:
                        final_leds.extend(number_2_inverse[part_number])
                    except:
                        final_leds.extend(number_2_inverse["0"])
                i += 1
            else: #Se for a placa que não está invertida
                if i < part_1:
                    try:
                        final_leds.extend(number_1[part_number])
                    except:
                        final_leds.extend(number_1["0"])
                else:
                    try:
                        final_leds.extend(number_2[part_number])
                    except:
                        final_leds.extend(number_2["0"])

        for i in range(num_leds): #Pega a lista final_leds com os valores tratados e adiciona no display
            if i < 7*len_number_1*3:
                if final_leds[i]:
                    leds[i] = color_1
                else:
                    leds[i] = [0, 0, 0]
            elif i < 7*len_number_1*6:
                if final_leds[i]:
                    leds[i] = color_2
                else:
                    leds[i] = [0, 0, 0]
            else:
                try:
                    if final_leds[i]:
                        leds[i] = color_3
                    else:
                        leds[i] = [0, 0, 0]
                except:
                    print(i)

        for leds_point in range(leds_more):
            leds[num_leds + leds_point] = [255, 255, 255]
                    
        leds.write()
        
        sleep(0.05)
