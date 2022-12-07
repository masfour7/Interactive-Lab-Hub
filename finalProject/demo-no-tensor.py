#!/usr/bin/env python3

from PIL import Image, ImageOps
from adafruit_servokit import ServoKit
import cv2
import numpy as np
import qwiic_led_stick
import sys

# import tensorflow.keras
import time
import qwiic

# disrance
ToF = qwiic.QwiicVL53L1X()
if ToF.sensor_init() == None:  # Begin returns 0 on a good init
    print("Sensor is online\n")
# ml
# Disable scientific notation for clarity
# np.set_printoptions(suppress=True)
# img = None
# webCam = False
# if len(sys.argv) > 1 and not sys.argv[-1] == "noWindow":
#     try:
#         print("I'll try to read your image")
#         img = cv2.imread(sys.argv[1])
#         if img is None:
#             print("Failed to load image file:", sys.argv[1])
#     except:
#         print(
#             "Failed to load the image are you sure that:",
#             sys.argv[1],
#             "is a path to an image?",
#         )
# else:
#     try:
#         print("Trying to open the Webcam.")
#         cap = cv2.VideoCapture(0)
#         if cap is None or not cap.isOpened():
#             raise ("No camera")
#         webCam = True
#     except:
#         print("Unable to access webcam.")
# # Load the model
# model = tensorflow.keras.models.load_model("keras_model.h5")
# # Load Labels:
# labels = []
# f = open("labels.txt", "r")
# for line in f.readlines():
#     if len(line) < 1:
#         continue
#     labels.append(line.split(" ")[1].strip())
#

# servo
# kit = ServoKit(channels=16)
# servo = kit.servo[0]
# servo.set_pulse_width_range(500, 2500)

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
    try:
        ToF.start_ranging()  # Write configuration bytes to initiate measurement
        time.sleep(0.005)
        distance = (
            ToF.get_distance()
        )  # Get the result of the measurement from the sensor
        time.sleep(0.005)
        ToF.stop_ranging()

        distanceInches = distance / 25.4
        distanceFeet = distanceInches / 12.0

        print("Distance(mm): %s Distance(ft): %s" % (distance, distanceFeet))

    except Exception as e:
        print(e)
        # cmd = input("> ")
        # if cmd == "o":
        #     open_lid()
        # elif cmd == "c":
        #     close_lid()
        # else:
        #     exit(0)
