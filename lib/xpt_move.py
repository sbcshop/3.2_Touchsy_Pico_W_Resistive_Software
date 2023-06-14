from machine import Pin, SPI, Timer
from sys import implementation
from os import uname
import ili9341
from xglcd_font import XglcdFont
import mySetup

print(implementation.name)
print(uname()[3])
print(uname()[4])

print(SPI(0))
print(SPI(1))

led = Pin(25, Pin.OUT)

#=== variable share btween ISR and main loop ===
x_passedTo_ISR = 0
y_passwsTo_ISR = 0

EVT_NO = const(0)
EVT_PenDown = const(1)
EVT_PenUp   = const(2)
event = EVT_NO

TimerReached = False
#===============================================

def xpt_touch(x, y):
    global event, x_passedTo_ISR, y_passedTo_ISR
    event = EVT_PenDown
    x_passedTo_ISR = x
    y_passedTo_ISR = y

display = mySetup.createMyDisplay()
xptTouch = mySetup.createXPT(xpt_touch)

print('Loading fonts...')
print('Loading unispace')
unispace = XglcdFont('Unispace12x24.c', 12, 24)

display.clear()
display.draw_text(0, 0, ili9341.__name__, unispace,
                  ili9341.color565(255, 128, 0))
display.draw_text(0, 25, ili9341.implementation.name, unispace,
                  ili9341.color565(0, 0, 200))
display.draw_text(0, 50, str(ili9341.implementation.version), unispace,
                  ili9341.color565(0, 0, 200))

tim = Timer()
def TimerTick(timer):
    global TimerReached
    TimerReached = True

tim.init(freq=50, mode=Timer.PERIODIC, callback=TimerTick)

touching = False

lastX = lastY = 0

while True:
    curEvent = event
    event = EVT_NO
    if curEvent!= EVT_NO:
        if curEvent == EVT_PenDown:
            print("Pen Down")
            touching = True
            lastX = x_passedTo_ISR
            lastY = y_passedTo_ISR
    
            touchXY = xptTouch.get_touch()
            rawX = xptTouch.send_command(xptTouch.GET_X)
            rawY = xptTouch.send_command(xptTouch.GET_Y)
    
            display.clear()
            display.fill_circle(x_passedTo_ISR, y_passedTo_ISR,
                                8, ili9341.color565(0, 255, 0))
            print(str(x_passedTo_ISR) + ":" + str(y_passedTo_ISR) +
                  " / " + str(rawX) + ":" + str(rawY))
    
            if touchXY != None:
                touchX = touchXY[0]
                touchY = touchXY[1]
                display.fill_circle(touchX, touchY, 5, ili9341.color565(255, 0, 0))
                print(str(touchX) + ":" + str(touchY))
            
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
            if buff is not None:
                x, y = xptTouch.normalize(*buff)
                lastX = x
                lastY = y
                display.fill_circle(x, y, 1, ili9341.color565(255, 255, 255))
                print("... " + str(x) + " : " + str(y))
            else:
                event = EVT_PenUp
                touching = False
                led.off()
                display.fill_circle(lastX, lastY, 5, ili9341.color565(0, 0, 255))

print("- bye -")