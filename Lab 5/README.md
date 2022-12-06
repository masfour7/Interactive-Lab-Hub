# Observant Systems

**Mohammad Asfour Only**


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

## Prep

1. Spend about 10 Minutes doing the Listening exercise as described in [ListeningExercise.md](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2022/Lab%205/ListeningExercise.md)
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2022/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:
1. Pull the new Github Repo.(Please wait until thursday morning. There are still some incompatabilities to make the assignment work.)
1. Raspberry Pi
1. Webcam 

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show the filledout answers for the Contextual Interaction Design Tool.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV
A more traditional method to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python. We included 4 standard OpenCV examples: contour(blob) detection, face detection with the ``Haarcascade``, flow detection (a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (e.g. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example. 

The following command is a nicer way you can run and see the flow of the `openCV-examples` we have included in your Pi. Instead of `ls`, the command we will be using here is `tree`. [Tree](http://mama.indstate.edu/users/ice/tree/) is a recursive directory colored listing command that produces a depth indented listing of files. Install `tree` first and `cd` to the `openCV-examples` folder and run the command:

```shell
pi@ixe00:~ $ sudo apt install tree
...
pi@ixe00:~ $ cd openCV-examples
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

The flow detection might seem random, but consider [this recent research](https://cseweb.ucsd.edu/~lriek/papers/taylor-icra-2021.pdf) that uses optical flow to determine busy-ness in hospital settings to facilitate robot navigation. Note the velocity parameter on page 3 and the mentions of optical flow.

Now, connect your webcam to your Pi and use **VNC to access to your Pi** and open the terminal. Use the following command lines to try each of the examples we provided:
(***it will not work if you use ssh from your laptop***)

```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***

### Contours
![image](https://user-images.githubusercontent.com/60685289/197372119-29ebb24f-6ef1-43c0-b8f5-2ebcfa18e9c0.png)

The contours detection can be used for drawing. Whether it's artists or a normal person who wants to get the lines of the picture correct for the initial dimensions.

### face-detection
![image](https://user-images.githubusercontent.com/60685289/197372196-101bbcb4-c30b-4e5a-aee6-a73c9edb0030.png)

Face detection can be used in automatic door openning. Instead of hiring a door person, you can have this!

### flow-detection
![image](https://user-images.githubusercontent.com/60685289/197372262-3bc9d1aa-60ff-40da-8ffd-9c723c7a1d42.png)

Flow detection can be used to see if something has moved in a house. You know how we see in horror movies where things move by itself; this can help us confirm that haha.

### object detection
![image](https://user-images.githubusercontent.com/60685289/197372605-4ff99a17-9b36-4eb1-ae40-6f13af6332ff.png)

Object detection can help us see how many people are waiting for the bus loop. If they are a lot, an additional bus can get activated to accomodate for that.

#### Filtering, FFTs, and Time Series data. 
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU or Microphone data stream could create a simple activity classifier between walking, running, and standing.

To get the microphone working we need to install two libraries. `PyAudio` to get the data from the microphone, `sciPy` to make data analysis easy, and the `numpy-ringbuffer` to keep track of the last ~1 second of audio. 
Pyaudio needs to be installed with the following comand:
``sudo apt install python3-pyaudio``
SciPy is installed with 
``sudo apt install python3-scipy`` 

Lastly we need numpy-ringbuffer, to make continues data anlysis easier.
``pip install numpy-ringbuffer``

Now try the audio processing example:
* Find what ID the micrpohone has with `python ListAvalibleAudioDevices.py`
    Look for a device name that includes `USB` in the name.
* Adjust the variable `DEVICE_INDEX` in the `ExampleAudioFFT.py` file.
    See if you are getting results printed out from the microphone. Try to understand how the code works.
    Then run the file by typing `python ExampleAudioFFT.py`



Using the microphone, try one of the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

```
#Threshold Detection
if volume > 55:
    print("The volume is greater than 55: ", volume)
```

**2. Set up a running averaging** Can you set up a running average over one of the variables that are being calculated.[moving average](https://en.wikipedia.org/wiki/Moving_average)

```
#Running Average
if len(VolumeHistory) != 0:
    print("The volume running average is: ", np.sum(VolumeHistory) / len(VolumeHistory))
```

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

```
# Peak Detection
if len(VolumeHistory) > 2:
    peak_threshold = 10
    if (VolumeHistory[-3] - VolumeHistory[-2] < -peak_threshold) and (VolumeHistory[-2] - VolumeHistory[-1] > peak_threshold):
        print("Peak has been detected")
```
                        

For technical references:

* Volume Calculation with [RootMeanSqare](https://en.wikipedia.org/wiki/Root_mean_square)
* [RingBuffer](https://en.wikipedia.org/wiki/Circular_buffer)
* [Frequency Analysis](https://en.wikipedia.org/wiki/Fast_Fourier_transform)


**\*\*\*Include links to your code here, and put the code for these in your repo--they will come in handy later.\*\*\***

The link to the code is [here](https://github.com/masfour7/Interactive-Lab-Hub/blob/Fall2022/Lab%205/ExampleAudioFFT.py).

### (Optional Reading) Introducing Additional Concepts
The following sections ([MediaPipe](#mediapipe) and [Teachable Machines](#teachable-machines)) are included for your own optional learning. **The associated scripts will not work on Fall 2022's Pi Image, so you can move onto part B.** However, you are welcome to try it on your personal computer. If this functionality is desirable for your lab or final project, we can help you get a different image running the last OS and version of python to make the following code work.

#### MediaPipe

A more recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Alt Text](mp.gif)

To get started, create a new virtual environment with special indication this time:

```
pi@ixe00:~ $ virtualenv mpipe --system-site-packages
pi@ixe00:~ $ source mpipe/bin/activate
(mpipe) pi@ixe00:~ $ 
```

and install the following.

```
...
(mpipe) pi@ixe00:~ $ sudo apt install ffmpeg python3-opencv
(mpipe) pi@ixe00:~ $ sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr25
(mpipe) pi@ixe00:~ $ pip3 install mediapipe-rpi3 pyalsaaudio
```

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(mpipe) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(mpipe) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53. 

~~\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\*~~

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)



#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

![Alt Text](tm.gif)

To get started, create and activate a new virtual environment for this exercise with special indication:

```
pi@ixe00:~ $ virtualenv tmachine --system-site-packages
pi@ixe00:~ $ source tmachine/bin/activate
(tmachine) pi@ixe00:~ $ 
```

After activating the virtual environment, install the requisite TensorFlow libraries by running the following lines:
```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

This might take a while to get fully installed. After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

Some experimentation with the Teachable Machine Learning. It is awesome! Classifying mouse, phone, and none. The image below shows my experiment.
![image](https://user-images.githubusercontent.com/60685289/197421225-f707d404-98d4-4fb7-a163-9ad1d42359ec.png)

~~**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***~~


*Don't forget to run ```deactivate``` to end the Teachable Machines demo, and to reactivate with ```source tmachine/bin/activate``` when you want to use it again.*


### Part B
### Construct a simple interaction.

* Pick one of the models you have tried, and experiment with prototyping an interaction.
* This can be as simple as the boat detector showen in a previous lecture from Nikolas Matelaro.
* Try out different interaction outputs and inputs.
* Fill out the ``Contextual Interaction Design Tool`` sheet.[Found here.](ThinkingThroughContextandInteraction.png)

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

The model I picked is the Teachable Machine. We always throw garbage and each time we would have to choose which category we have to throw it in. Sometimes we do not know the answer and throw it in the wrong place. There might be technologies out there that do that but since they are not yet in the mass market it is worth implementing something like or even better than them. At least from a user experience point of view. 

Let's say you want to throw a plastic bottle of water, you can throw it in one place only and the machine would identify the location it should go to; in this case, the plastic side. It will show you a display telling you what the result was. Also, there would be a button to identify if the machine's result is something you agree with.
![image](https://user-images.githubusercontent.com/60685289/197424250-75f6b0a1-be20-45ae-bd90-aa179e76fd6d.png)
![image](https://user-images.githubusercontent.com/60685289/197424374-4b209905-4fbf-402c-8c5d-fc8aef4f4f9c.png)


### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it do what it is supposed to do?
3. When does it fail?
4. When it fails, why does it fail?
5. Based on the behavior you have seen, what other scenarios could cause problems?

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?
1. How bad would they be impacted by a miss classification?
1. How could change your interactive system to address this?
1. Are there optimizations you can try to do on your sense-making algorithm.

The test was relatively succesful. I classifes objects (watter bottle, milk, perfume) correctly when held close to the webcam. However, when my face appears it becomes hard for it to classify them. This is probably because there are much more similarities in the pictures where my face is in them. So the best thing to do is to always remove background of the object and this would improve it by a lot. Other scenarios that may cause problem is showing different types of milk let's say; with different colors. 

Someone who throws the garbage would normally just trust the machine to do its job. The problem arises when the garbage collectors find that somethings are mismatched. This would be big impact; but again humans sometimes make these mistakes so probably they are somewhat used to this? But since it's a machine, they might not welcome any mistakes by it. The problem is accuracy with all the different types of objects that exist out there. 

One solution is to train a huge amount of images with different types, colors and then train the model. Another one is as said before take the background off any object that comes into the garbage, then classify it. The two images below show my prototype:

![image](https://user-images.githubusercontent.com/60685289/197425954-e19238bb-0517-4486-8f21-e5d138c97af7.png)
![image](https://user-images.githubusercontent.com/60685289/197425983-95d0dd3c-7a0f-4959-814f-450a7fa4c14b.png)

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

For this part, I added a background class to the garbage classifier as well. This can be used for identifying the type of object that is thrown in the garbage can. Then, show the user what the result is and an option manually change the result. Then, the garbage should automatically put it in its right place. Agood environment for it would be in the outside since this might take a lot of space. Also, inside the garbage there should be light always on to be able to classify the images (bad environment). The classification will break if multiple items were thrown in the garbage at once, since the classifier only works for one item at a time. It might show the wrong classification for one of the items and include it with other. Lastly this device should have a nice design which is the most important thing. The noise shouldn't be too lowed when putting the items in the right place. It should do it as fast as possible to give a place for the next item.

A short video that shows how the classifier works is below: 


https://user-images.githubusercontent.com/60685289/197429126-dc49f650-9e09-42a1-8c7b-6ac07204a2ec.mp4


### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***

For this part of the lab, I finished building my design and implemented a first prtotype that at least helped me to test the interaction with users. I also added a way to show a display where users can input whether the classification by the machine was correct or not; this well help in making the machine more accurate by learning from new data. I also added a couple more examples for the machine to learn and tested it. The result for these specific examples were great which hints that adding more examples could work as great as this also.

### Diagram:

![image](https://user-images.githubusercontent.com/60685289/199490598-4498eb47-3f89-4962-832b-8685dc2f58ea.png)

### prototype:

![image](https://user-images.githubusercontent.com/60685289/199491305-4a153782-20a7-42f2-9af7-fd96bef748a8.png)
![image](https://user-images.githubusercontent.com/60685289/199491346-bb0f5a34-7e0a-4cf9-926b-b0925104f460.png)


### Video:

https://user-images.githubusercontent.com/60685289/199491449-5d242c37-677c-45f4-88d4-829aec7f193a.mp4
