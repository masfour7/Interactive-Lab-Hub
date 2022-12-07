#!/usr/bin/env python3

from PIL import Image, ImageOps
from adafruit_servokit import ServoKit
import cv2
import numpy as np
import qwiic_led_stick
import sys
import tensorflow.keras
import time
import qwiic

# disrance
ToF = qwiic.QwiicVL53L1X()
if ToF.sensor_init() == None:  # Begin returns 0 on a good init
    print("Sensor is online\n")
# ml
# Disable scientific notation for clarity
np.set_printoptions(suppress=True)
img = None
webCam = False
if len(sys.argv) > 1 and not sys.argv[-1] == "noWindow":
    try:
        print("I'll try to read your image")
        img = cv2.imread(sys.argv[1])
        if img is None:
            print("Failed to load image file:", sys.argv[1])
    except:
        print(
            "Failed to load the image are you sure that:",
            sys.argv[1],
            "is a path to an image?",
        )
else:
    try:
        print("Trying to open the Webcam.")
        cap = cv2.VideoCapture(0)
        if cap is None or not cap.isOpened():
            raise ("No camera")
        webCam = True
    except:
        print("Unable to access webcam.")
# Load the model
model = tensorflow.keras.models.load_model("keras_model.h5")
# Load Labels:
labels = []
f = open("labels.txt", "r")
for line in f.readlines():
    if len(line) < 1:
        continue
    labels.append(line.split(" ")[1].strip())


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


predict_tolerance_lim = 1
cur_in_a_row = 0
last_pred = None

while True:
    # ml stuff
    if webCam:
        ret, img = cap.read()

    rows, cols, channels = img.shape
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    size = (224, 224)
    img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    # turn the image into a numpy array
    image_array = np.asarray(img)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    prediction = labels[np.argmax(prediction)]
    # print("I think its a:",labels[np.argmax(prediction)])
    if prediction == last_pred:
        cur_in_a_row += 1
    else:
        cur_in_a_row = 0

    print(f"prediction is a  {prediction}")
    # if cur_in_a_row >= predict_tolerance_lim:
    if prediction == "Cardboard":
        my_stick.set_all_LED_color(100, 0, 0)
    elif prediction == "Glass":
        my_stick.set_all_LED_color(0, 100, 0)
    elif prediction == "Metal":
        my_stick.set_all_LED_color(0, 0, 100)
    elif prediction == "Paper":
        my_stick.set_all_LED_color(100, 100, 0)
    elif prediction == "Plastic":
        my_stick.set_all_LED_color(100, 0, 100)
    elif prediction == "Trash":
        my_stick.set_all_LED_color(0, 100, 100)

    ToF.start_ranging()
    time.sleep(0.005)
    distance = ToF.get_distance()  # Get the result of the measurement from the sensor
    time.sleep(0.005)
    ToF.stop_ranging()

    distanceInches = distance / 25.4
    distanceFeet = distanceInches / 12.0

    print("Distance(mm): %s Distance(ft): %s" % (distance, distanceFeet))
    if distance > 100:
        close_lid()
    else:
        open_lid()

    # if webCam:
    #     if sys.argv[-1] == "noWindow":
    #        cv2.imwrite('detected_out.jpg',img)
    #        continue
    #     cv2.imshow('detected (press q to quit)',img)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         cap.release()
    #         break
    # else:
    #     break

    # cmd = input("> ")
    # if cmd == "o":
    #     open_lid()
    # elif cmd == "c":
    #     close_lid()
    # elif cmd == "r":
    #     my_stick.set_all_LED_cmd(100, 0, 0)
    # elif cmd == "g":
    #     my_stick.set_all_LED_cmd(0, 100, 0)
    # elif cmd == "b":
    #     my_stick.set_all_LED_cmd(0, 0, 100)
    # elif cmd == "q":
    #     exit(0)
