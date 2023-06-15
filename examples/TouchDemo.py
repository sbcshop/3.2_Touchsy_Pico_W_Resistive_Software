from machine import Pin, SPI, Timer
from sys import implementation
import ili9341
from xglcd_font import XglcdFont
from ili9341 import Display, color565
import config
import os
import time 

#GP15 connected to backlight of Display 
BL = Pin(15, Pin.OUT) # make as OUTPUT
BL.value(1) # set pin as HIGH i.e turns on BackLight

#GPIO connected to onboard LED of Pico W  
led = Pin(25, Pin.OUT) # make as OUTPUT

button1 = Pin(9, Pin.IN, Pin.PULL_UP)

#=== variable share btween ISR and main loop ===
x_passedTo_ISR = 0
y_passwsTo_ISR = 0

EVT_NO = const(0)
EVT_PenDown = const(1)
EVT_PenUp   = const(2)
event = EVT_NO

TimerReached = False
#===============================================

def xpt_touch(x, y): #Function to handle Screen Touch operation
    global event, x_passedTo_ISR, y_passedTo_ISR
    event = EVT_PenDown
    x_passedTo_ISR = x
    y_passedTo_ISR = y

display = config.createMyDisplay() #display spi setup
xptTouch = config.createXPT(xpt_touch) #touch spi setup 
unispace = XglcdFont('Unispace12x24.c', 12, 24) #using Unispace font

display.clear()
display.clear()
display.draw_text(50, 25, '3.2" Touchsy', unispace,color565(0, 255, 255))
display.draw_text(75, 50, 'Pico W', unispace,color565(0, 255, 255))
display.draw_text8x8(65, 80,' Resistive ', color565(255, 255, 0))
display.draw_text8x8(20, 300,'Press, Hold and move Pen', color565(255, 255, 0))

tim = Timer()
def TimerTick(timer):
    global TimerReached
    TimerReached = True

tim.init(freq=80, mode=Timer.PERIODIC, callback=TimerTick)

touching = False

lastX = lastY = 0


while True:
    curEvent = event
    event = EVT_NO
    if curEvent!= EVT_NO:
        if curEvent == EVT_PenDown:
            touching = True
            lastX = x_passedTo_ISR
            lastY = y_passedTo_ISR
    
            touchXY = xptTouch.get_touch()
            rawX = xptTouch.send_command(xptTouch.GET_X)
            rawY = xptTouch.send_command(xptTouch.GET_Y)
            
            display.fill_circle(x_passedTo_ISR, y_passedTo_ISR,
                                8, ili9341.color565(0, 255, 0))
            print(str(x_passedTo_ISR) + ":" + str(y_passedTo_ISR) +
                  " / " + str(rawX) + ":" + str(rawY))
    
            if touchXY != None:
                touchX = touchXY[0]
                touchY = touchXY[1]
            
        elif curEvent == EVT_PenUp:
            print("Pen Up")
            pass
        else:
            print("unknown event!!!")
           
    if TimerReached:
        TimerReached = False  
        if touching:
            led.toggle()
            buff = xptTouch.raw_touch()
            if button1.value() == 0:
                    display.clear()
            if buff is not None:
                x, y = xptTouch.normalize(*buff)
                lastX = x
                lastY = y
                display.fill_circle(x, y, 1, ili9341.color565(0, 255, 0))
                print("... " + str(x) + " : " + str(y))
        
    time.sleep(0.02)
    

