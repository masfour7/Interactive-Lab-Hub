import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from datetime import datetime

import random

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

buttonA = digitalio.DigitalInOut(board.D23)
buttonA.switch_to_input()

buttonB = digitalio.DigitalInOut(board.D24)
buttonB.switch_to_input()

screen = 0

import os
# os.popen('sh /home/pi/text2speech/espeak_demo.sh')

x = random.randint(1, 100)
t = random.randint(1, 100)

z = x + t + 1

print(x, t, z)


while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
<<<<<<< HEAD
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    now = datetime.now()
    now_str = now.strftime("%m/%d/%Y %H:%M:%S")
    
    line1 = now_str
    line2 = "GOOD MORNING!!"
    line3 = "Wake up!!!"
    y = top
    
    if buttonA.value and buttonB.value:
        draw.text((x,y), line3, font=font, fill='#58815b')
        y += font.getsize(line3)[1]
    
    if buttonB.value and not buttonA.value: #just button A pressed
        draw.text((x,y), line1, font=font, fill='#58815b')
        y += font.getsize(line1)[1]
        draw.text((x,y), line2, font=font, fill='#f5cb42')
        y += font.getsize(line2)[1]
=======
    now = datetime.now()
    now_str = now.strftime("%m/%d/%Y %H:%M:%S")
    
    line1 = now_str
    line2 = "GOOD MORNING!!"
    line3 = "Wake Up!!!"
    
    y = top
    
    # if buttonA.value and buttonB.value:
    #     screen = 0

    if buttonB.value and not buttonA.value: #just button A pressed (yes)
        screen +=2
        x = random.randint(1, 100)
        t = random.randint(1, 100)

        z = x + t + 10
    
    if not buttonB.value and buttonA.value: #just button B pressed (no)
        screen += 1

    if screen == 0: # Alarm / first eqn
        os.popen('sh /home/pi/text2speech/espeak_demo.sh')
        draw.text((x,y), line3, font=font, fill='#f5cb42')
        y += font.getsize(line3)[1]
        draw.text((x,y), f'{x} + {t} = {z}', font=font, fill='#58815b')
        y += font.getsize(line3)[1]
        draw.text((x,y), "Yes (top button)?", font=font, fill='#58815b')
        y += font.getsize(line3)[1]
        draw.text((x,y), "No (bottom)?", font=font, fill='#58815b')
        y += font.getsize(line3)[1]


    if screen == 1 or screen == 3 or screen == 4: # correct
        draw.text((x,y), line1, font=font, fill='#58815b')
        y += font.getsize(line1)[1]
        draw.text((x,y), line2, font=font, fill='#f5cb42')
        y += font.getsize(line2)[1]

    if screen == 2: # wrong
        os.popen('sh /home/pi/text2speech/espeak_demo.sh')
        draw.text((x,y), "Wrong! Try Again..", font=font, fill='#f5cb42')
        y += font.getsize(line3)[1]
        draw.text((x,y), f'{x} + {t} = {z}', font=font, fill='#58815b')
        y += font.getsize(line3)[1]
        draw.text((x,y), "yes (top button) or no (bottom)?", font=font, fill='#58815b')
        y += font.getsize(line3)[1]
>>>>>>> 839533aed2eff5b896c9ab344569003470c5f7cc
        
    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
