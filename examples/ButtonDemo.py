'''
For this example code external library used -> ili9341.py, xglcd_font.py, config.py
from lib folder-> https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Software/tree/main/lib
'''

from machine import Pin, SPI,Timer, UART,PWM
import ili9341
from xglcd_font import XglcdFont
from ili9341 import Display, color565
import time 
import config

buzzer = PWM(Pin(22)) #define PWM output pin GP22

#for resistive touchsy
button1 = Pin(9, Pin.IN, Pin.PULL_UP)
button2 = Pin(26, Pin.IN, Pin.PULL_UP)
button3 = Pin(27, Pin.IN, Pin.PULL_UP)
button4 = Pin(8, Pin.IN, Pin.PULL_UP)

def playtone(frequency): # function to play tone on buzzer with define frequency
    buzzer.duty_u16(5000)
    buzzer.freq(frequency)

def bequiet():	# Function to stop buzzer
    buzzer.duty_u16(0)

#GP15 connected to backlight of Display 
BL = Pin(15, Pin.OUT) # make as OUTPUT
BL.value(1) # set pin as HIGH i.e turns on BackLight

display = config.createMyDisplay() 	#configure display spi interface in config.py
unispace = XglcdFont('Unispace12x24.c', 12, 24) #using unispace font


display.clear()
display.draw_text(50, 25, '3.2" Touchsy', unispace,color565(0, 255, 255))
display.draw_text(75, 50, 'Pico W', unispace,color565(0, 255, 255))
display.draw_text8x8(65, 80,' Resistive ', color565(255, 255, 0))
display.draw_text(40, 130, "Press Button", unispace, color565(255, 250, 255))

while True:
    #read value of buttons, low when button pressed else high
    val1 = button1.value()
    val2 = button2.value()
    val3 = button3.value()
    val4 = button4.value()
    
    if val1 == 0:
        print("BT1 Pressed!")
        display.draw_text(50, 240, "BT1 Pressed..!", unispace, color565(255, 255, 0))
        playtone(1865)
        time.sleep(0.5)
    elif val2 == 0:
        print("BT2 Pressed!")
        display.draw_text(40, 240, "BT2 Pressed..!", unispace, color565(255, 255, 0))
        playtone(1865)
        time.sleep(0.5)
    elif val3 == 0:
        print("BT3 Pressed!")
        display.draw_text(40, 240, "BT3 Pressed..!", unispace, color565(255, 255, 0))
        playtone(1865)
        time.sleep(0.5)
    elif val4 == 0:
        print("BT4 Pressed!")
        display.draw_text(40, 240, "BT4 Pressed..!", unispace, color565(255, 255, 0))
        playtone(1865)
        time.sleep(0.5)
    else :
        bequiet()
        display.draw_text(40, 240, "                     ", unispace, color565(255, 255, 0))
    time.sleep(0.02)
    
