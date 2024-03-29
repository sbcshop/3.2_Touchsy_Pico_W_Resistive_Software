'''
For this example code external library used ili9341.py, xglcd_font.py, config.py 
from lib folder-> https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Software/tree/main/lib
'''

from machine import Pin, SPI
import ili9341
from xglcd_font import XglcdFont
from ili9341 import Display, color565
import config


#GP15 connected to backlight of Display 
BL = Pin(15, Pin.OUT) # make as OUTPUT
BL.value(1) # set pin as HIGH i.e turns on BackLight

display = config.createMyDisplay() 	#configure display spi interface in config.py
unispace = XglcdFont('Unispace12x24.c', 12, 24) #using unispace font


display.clear()
#method use with custom fonts-> display.draw_text(x,y,your_text, font, color)
#method use with default font-> display.draw_text8x8(x,y,your_text, color)
display.draw_text(50, 25, '3.2" Touchsy', unispace,color565(0, 255, 255))
display.draw_text(75, 50, 'Pico W', unispace,color565(0, 255, 255))
display.draw_text8x8(65, 80,' Resistive ', color565(255, 255, 0))
display.draw_text(40, 130, "Hello...", unispace, color565(255, 250, 255))
