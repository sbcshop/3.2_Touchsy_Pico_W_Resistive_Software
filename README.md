# 3.2_Touchsy_Pico_W_Resistive_Software
<img src="https://github.com/sbcshop/3.2_Touchsy_HAT_Resistive_Software/blob/main/images/Touchsy%20banner.jpg">

Touchsy Pico W - the ultimate display solution for users who want an onboard controller with a versatile programming platform. This Github provides getting started guide for Resistive Variant of Touchsy Family.

With Touchsy Pico W, you can easily program your display with your preferred language and use it in various projects and applications, from IoT to robotics. The **Resistive** and [**Capacitive**](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/) touchscreen options allow you to choose the best option for your specific needs, and the additional GPIO pins allow you to connect more hardware to your display.

### Features:
- Official Raspberry Pi Pico W onboard for versatile programming options (Python, Arduino IDE, C, C++)
-	Available in two variants: Resistive and Capacitive touchscreen
-	SD card slot for storage and data transfer
-	Battery port connector with Battery Management for portable use (3.7V Lithium)
-	4 programmable buttons for customizable control options
-	Additional GPIO pins breakout for connecting more hardware
-	Additional Type C to power board
-	Additional power supply facility for use with other peripheral

### Specifications:
-	Operating voltage of pins 3.3V and board supply 5V
-	3.2” Display with resolution 240 × 320
-	ILI934 Display Driver
-	FT6236 capacitive touch controller (Capacitive Variant)
-	XPT2046 resistive touch controller (Resistive Variant)
-	Appearance: RGB
-	Colors: 65K/262K
-	Viewing Angle(in degree): Left:70, Right:70, Up:50, Down:70 
-	Operating Temperature is -20℃~70℃
-	Storage Temperature is -30℃~80℃

## Getting Started with 3.2 Touchsy Pico W Resistive
### Pinout
<img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Software/blob/main/images/Touchsy%20Pico%20Res%20pinout.jpg">

- (1) 3.2” Resistive Touch Display 

- (2) Battery connector

- (3) Additional GPIO breakout as JST PH

- (4) SD card slot

- (5) RPi Pico W

- (6) Programmable Buttons

- (7) Buzzer

- (8) Power pins breakout 

- (9) Type C input power

### Interfacing Info
led = Pin(25, Pin.OUT)

BL = Pin(15, Pin.OUT)
BL.value(1)
button1 = Pin(9, Pin.IN, Pin.PULL_UP)
button2 = Pin(26, Pin.IN, Pin.PULL_UP)
button3 = Pin(27, Pin.IN, Pin.PULL_UP)
button4 = Pin(8, Pin.IN, Pin.PULL_UP)

XPT_CLK_PIN = const(2)
XPT_MOSI_PIN = const(3)
XPT_MISO_PIN = const(4)

XPT_CS_PIN = const(5)
XPT_INT = const(10)

| Pico | Display | Code variables | Function |
|---|---|---|---|
|GP6  | SCL | TFT_CLK_PIN  |Clock pin of SPI interface for Display|
|GP7  | SDA | TFT_MOSI_PIN | Data IN pin of SPI interface|
|GP13 | CS  | TFT_CS_PIN   | Chip Select pin of SPI interface|
|GP11 | D/C | TFT_DC_PIN   | Data/Command pin of SPI interface|
|GP14 | RST | TFT_RST_PIN  | Display Reset pin|

| Pico | Touch | Code variables | Function |
|---|---|---|---|
|GP2 | T_CLK | XPT_CLK_PIN  |Clock pin of SPI interface for XPT2046 touch controller|
|GP3 | T_DIN | XPT_MOSI_PIN | Data IN pin of SPI interface|
|GP4 |  | XPT_MISO_PIN   | Chip Select pin of SPI interface|
|GP5 | DC | XPT_CS_PIN   | Data/Command pin of SPI interface|
|GP10 | RST | XPT_INT | Touch controller Reset pin|


spi=SPI(0,sck=Pin(18),mosi=Pin(19),miso=Pin(16))

| Pico | SD Card | Function |
|---|---|---|
|GPIO | TFT_CS |Chip Select pin|

| Pico | Buttons | Function |
|---|---|---|
|GPIO | TFT_CS |Chip Select pin|

| Pico | Buzzer | Function |
|---|---|---|
|GPIO | TFT_CS |Chip Select pin|

## Documentation
  * [Schematic](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Hardware/blob/main/Design%20Data/SCH%203.2%20Touchsy%20%20Pico%20w%20(Resistive).pdf)
  * [Hardware Files](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Hardware/tree/main)
  * [Step File](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Hardware/blob/main/Mechanical%20Data/STEP%20%203.2%20inch%20Touchsy%20based%20on%20PICO%20W%20(Resistive).step)
  * [MicroPython getting started for RPI](https://docs.micropython.org/en/latest/rp2/quickref.html)
  * [RP2040 Datasheet](https://github.com/sbcshop/HackyPi-Hardware/blob/main/Documents/rp2040-datasheet.pdf)


## Related Products
   * [3.2" Touchsy ESP32](https://shop.sb-components.co.uk/products/touchsy-3-2-lcd-display-for-all-sbcs-mcus?variant=40536352096339) - 3.2" Touchsy ESP32 with Resistive and Capacitive version. 
   * [3.2" Touchsy Pico W](https://shop.sb-components.co.uk/products/touchsy-3-2-lcd-display-for-all-sbcs-mcus?variant=40536352129107) - 3.2" Touchsy Pico W with Resistive and Capacitive version.
   * [3.2" Touchsy Breakout](https://shop.sb-components.co.uk/products/touchsy-3-2-lcd-display-for-all-sbcs-mcus?variant=40536352161875) - 3.2" Touchsy Breakout with Resistive and Capacitive version.
   * [3.2" Touchsy HAT](https://shop.sb-components.co.uk/products/touchsy-3-2-lcd-display-for-all-sbcs-mcus?variant=40536352063571) - 3.2" Touchsy HAT with Resistive version for Raspberry Pi.
   * [1.28" Round Touch LCD HAT](https://shop.sb-components.co.uk/products/1-28-round-touch-lcd-hat-for-raspberry-pi?_pos=1&_sid=b6ecd2f9c&_ss=r) - 1.28" Round Touch LCD HAT for Raspberry Pi.

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>


