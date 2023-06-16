# 3.2_Touchsy_Pico_W_Resistive_Software
<img src="https://github.com/sbcshop/3.2_Touchsy_HAT_Resistive_Software/blob/main/images/Touchsy%20banner.jpg">

Touchsy Pico W - the ultimate display solution for users who want an onboard controller with a versatile programming platform. This Github provides getting started guide for Resistive Variant of Touchsy Family.

With Touchsy Pico W, you can easily program your display with your preferred language and use it in various projects and applications, from IoT to robotics. The **Resistive** and [**Capacitive**](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/) touchscreen options allow you to choose the best option for your specific needs, and the additional GPIO pins allow you to connect more hardware to your display.

### Features:
- Official Raspberry Pi Pico W onboard for versatile programming options (Python, Arduino IDE, C, C++)
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
-	XPT2046 resistive touch controller 
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

### Interfacing Details
- Display and Resistive Touch controller interfacing with Pico W
    | Pico W | Display | Code variables | Function |
    |---|---|---|---|
    |GP6  | DC/SCL SPI | TFT_CLK_PIN  |Clock pin of SPI interface for Display|
    |GP7  | SDI SPI/SDA | TFT_MOSI_PIN | MOSI (Master OUT Slave IN) pin of SPI interface|
    |GP13 | CS/SPI CS  | TFT_CS_PIN   | Chip Select pin of SPI interface|
    |GP11 | WR/SPI D/C | TFT_DC_PIN   | Data/Command pin of SPI interface|
    |GP14 | RESET | TFT_RST_PIN  | Display Reset pin|
    |GP15 |Driven via Transistor| BL |Backlight of display|

  Display setting code snippets view (config.py):
  ```
    TFT_CLK_PIN = const(6)
    TFT_MOSI_PIN = const(7)
    
    TFT_CS_PIN = const(13)
    TFT_RST_PIN = const(14)
    TFT_DC_PIN = const(11)

    #inside createMyDisplay() method to configure display for SPI interface 
    spiTFT = SPI(0, baudrate=51200000, sck=Pin(TFT_CLK_PIN), mosi=Pin(TFT_MOSI_PIN))
    display = Display(spiTFT, dc=Pin(TFT_DC_PIN), cs=Pin(TFT_CS_PIN), rst=Pin(TFT_RST_PIN),rotation=180)
  ```
  
    | Pico W | Resistive Touch | Code variables | Function |
    |---|---|---|---|
    |GP2 | DCLK | XPT_CLK_PIN  |Clock pin of SPI interface for touch controller|
    |GP3 | DIN | XPT_MOSI_PIN | MOSI (Master OUT Slave IN) data pin of SPI interface|
    |GP4 | DOUT | XPT_MISO_PIN   | MISO (Master IN Slave OUT) data pin of SPI interface|
    |GP5 | CS | XPT_CS_PIN   | Chip Select pin of SPI interface|
    |GP10 | PENIRQ | XPT_INT | Touch controller Interrupt pin|

  Touch setting code snippets view(config.py):
  ```
    XPT_CLK_PIN = const(2)
    XPT_MOSI_PIN = const(3)
    XPT_MISO_PIN = const(4)  
    XPT_CS_PIN = const(5)
    XPT_INT = const(10)

    #inside createXPT(touch_handler) method to configure touch for SPI interface 
    spiXPT = SPI(0, baudrate=1000000, sck=Pin(XPT_CLK_PIN), mosi=Pin(XPT_MOSI_PIN), miso=Pin(XPT_MISO_PIN))
    xpt = Touch(spiXPT, cs=Pin(XPT_CS_PIN), int_pin=Pin(XPT_INT), int_handler=touch_handler)
  ```

- Pico W and micro SD card interfacing
    | Pico W | microSD Card | Function |
    |---|---|---|
    |GP18 | SCLK |Clock pin of SPI interface for microSD card |
    |GP19 | DIN  | MOSI (Master OUT Slave IN) data pin of SPI interface|
    |GP16 | DOUT | MISO (Master IN Slave OUT) data pin of SPI interface|
    |GP17 | CS   | Chip Select pin of SPI interface|

  Sdcard setting code snippets view:
  ```
    spi=SPI(0,sck=Pin(18),mosi=Pin(19),miso=Pin(16))
    sd=sdcard.SDCard(spi,Pin(17))
  ```
  
- Buttons, Buzzer and LED Interfacing with Pico W
    | Pico W | Buttons | Function |
    |---|---|---|
    |GP9 | BT1 |Programmable button|
    |GP26 | BT2 |Programmable button|
    |GP27 | BT3 |Programmable button|
    |GP8 | BT4 |Programmable button|
  
    | Pico W | Hardware |
    |---|---|
    |GP22 | Buzzer |
    |GP25 | LED (OnBoard Pico W) |

  Code snippets:
  ``` 
    buzzer = PWM(Pin(22)) #define PWM output
    button1 = Pin(9, Pin.IN, Pin.PULL_UP) #define input pin with PULLUP
  ```
- Breakout GPIOs
    | Pico W |Physical Pin | Multi-Function |
    |---|---|---|
    |GP0 | 1  | General IO / SPI0 RX / I2C0 SDA / UART0 TX |
    |GP1 | 2 | General IO / SPI0 CSn / I2C0 SCL / UART0 RX |
    |GP2 | 4 | General IO / SPI0 SCK / I2C1 SDA |
    |GP3 | 5 | General IO / SPI0 TX / I2C1 SCL |
    |GP28 | 34 | General IO / ADC2 / SPI1 RX |

### 1. Step to install boot Firmware
   - Every Touchsy board will be provided with boot firmware already installed, so you can directly go to step 2.
   - If, in any case, you are required to install firmware for your board, then you can follow the guide [here](https://github.com/sbcshop/EnkPi_7.5_Software/blob/main/Downloads/Pico%20W%20Micropython%20Firmware%20Installation%20Steps.pdf)

### 2. Onboard LED Blink 
   - Download **Thonny IDE** from [Download link](https://thonny.org/) as per your OS and install it.
   - Once done start **Thonny IDE application**, Connect Touchsy with a laptop/PC using a micro USB cable and the micro USB port on Pico W present on Touchsy.
   - Select device at the bottom right with a suitable COM port, as shown in the below figure. You might get a different COM port.
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img1.jpg" />
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img2.jpg" />
   - Write simple onboard blink Python code or [Download Led blink code](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Software/blob/main/examples/onboard_ledBlink.py), then click on the green run button to make your script run on Touchsy. 
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img3.jpg" />
     
     Now that we've reached this point, you're executing your script through Thonny IDE, so if you unplug Pico, it will stop running. To run your script without using an IDE, simply power up Touchsy and it should run your script, go to step 3. Once you have transferred your code to the Touchsy board, to see your script running, just plug in power either way using micro USB or Type C, both will work.

### 3. How to move your script on Pico W of Touchsy
   - Click on File -> Save Copy -> select Raspberry Pi Pico , Then save file as main.py
     
      <img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Software/blob/main/images/transfer_script_pico.gif" />
   
   In similar way you can add various python code files to Pico. Also you can try out sample codes given here in [examples folder](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Software/tree/main/examples). But make sure you have all required library files inside Pico W of Touchsy, if not only then follow below steps otherwise skip.
   - Mostly you will receive Touchsy with all required library files preinstalled. But in any case if you need to save library files from [lib](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Software/tree/main/lib) folder into Pico W of Touchsy, then download repo and follow below steps to move lib file into Pico of Touchsy.
      <img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Software/blob/main/images/multiple_file_transfer.gif" />
   
**NOTE: Don't rename _lib_ files** and also you will have to move related font file if used inside code.


### Example Codes
   Save whatever example code file you want to try as main.py in pico w as shown in above [step 3](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Software#3-how-to-move-your-script-on-pico-w-of-touchsy), also add related lib files with default name.
   - [Example 1]() : This code generates pattern, you can experiment to develop your favourite one
   - [Example 2]() : Try this code to display text, make sure to install library EnkPi_7in5.py
   - [Example 3]() : Play with some shapes like circle, square, etc.
   - [Example 4]() : To display images on EnkPi, this code need library EnkPi_7in5.py & pics.py and to follow this example you have to go through [Step by Step Guide to build byte array from Image](https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/Downloads/Step%20by%20Step%20Guide%20to%20create%20byte%20array%20from%20image.pdf)
   - and [More...](https://github.com/sbcshop/EnkPi_7.5_Software/tree/main/examples)
   
   Now you are ready to try out your own codes, **_Happy Coding!_**
   
## Resources
  * [Schematic](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Hardware/blob/main/Design%20Data/SCH%203.2%20Touchsy%20%20Pico%20w%20(Resistive).pdf)
  * [Hardware Files](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Hardware/tree/main)
  * [Step File](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Hardware/blob/main/Mechanical%20Data/STEP%20%203.2%20inch%20Touchsy%20based%20on%20PICO%20W%20(Resistive).step)
  * [MicroPython getting started for RPi Pico/Pico W](https://docs.micropython.org/en/latest/rp2/quickref.html)
  * [Pico W Getting Started](https://projects.raspberrypi.org/en/projects/get-started-pico-w)
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


