#!/usr/bin/env python3

from adafruit_servokit import ServoKit
import qwiic_led_stick
import sys
import time

# servo
kit = ServoKit(channels=16)
servo = kit.servo[0]
servo.set_pulse_width_range(500, 2500)

# light
my_stick = qwiic_led_stick.QwiicLEDStick()
if my_stick.begin() == False:
    print(
        "\nThe Qwiic LED Stick isn't connected to the sytsem. Please check your connection",
        file=sys.stderr,
    )


def open_lid():
    servo.angle = 120


def close_lid():
    servo.angle = 0


def set_all_colors(r, g, b):
    assert (r in range(101)) and (g in range(101)) and (b in range(101))
    my_stick.set_all_LED_color(r, g, b)


while True:
    cmd = input("> ")
    if cmd == "o":
        open_lid()
    elif cmd == "c":
        close_lid()
    elif cmd == "r":
        my_stick.set_all_LED_cmd(100, 0, 0)
    elif cmd == "g":
        my_stick.set_all_LED_cmd(0, 100, 0)
    elif cmd == "b":
        my_stick.set_all_LED_cmd(0, 0, 100)
    elif cmd == "q":
        exit(0)
