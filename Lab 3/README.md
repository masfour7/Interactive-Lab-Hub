# Chatterboxes
**Mohammad Asfour (one person)**
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Web Camera If You Don't Have One

Students who have not already received a web camera will receive their [IMISES web cameras](https://www.amazon.com/Microphone-Speaker-Balance-Conference-Streaming/dp/B0B7B7SYSY/ref=sr_1_3?keywords=webcam%2Bwith%2Bmicrophone%2Band%2Bspeaker&qid=1663090960&s=electronics&sprefix=webcam%2Bwith%2Bmicrophone%2Band%2Bsp%2Celectronics%2C123&sr=1-3&th=1) on Thursday at the beginning of lab. If you cannot make it to class on Thursday, please contact the TAs to ensure you get your web camera. 

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. There are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2022
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2022Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.

### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using the microphone and speaker on your webcamera. In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

------------Please look at file custom_shell.sh

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. 
Now, we need to find out where your webcam's audio device is connected to the Pi. Use `arecord -l` to get the card and device number:
```
pi@ixe00:~/speech2text $ arecord -l
**** List of CAPTURE Hardware Devices ****
card 1: Device [Usb Audio Device], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```
The example above shows a scenario where the audio device is at card 1, device 0. Now, use `nano vosk_demo_mic.sh` and change the `hw` parameter. In the case as shown above, change it to `hw:1,0`, which stands for card 1, device 0.  

Now, look at which camera you have. Do you have the cylinder camera (likely the case if you received it when we first handed out kits), change the `-r 16000` parameter to `-r 44100`. If you have the IMISES camera, check if your rate parameter says `-r 16000`. Save the file using Write Out and press enter.

Then try `./vosk_demo_mic.sh`

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

------------ Please look at file called custom_shell2.sh

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*
![image](https://user-images.githubusercontent.com/60685289/192426599-ae732148-cea3-40af-ac6a-7fcee2cfacab.png)

Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

\*\***Please describe and document your process.**\*\*

- Hey Alaa, would you like to watch something?
--- Yes, sure
- Cool, are you looking to watch a movie or would you like a specific channel?
--- Movie
- what type of movie would you be interested in?
--- Horror!
- Try this and let me know if you want something else: (show a movie)
--- Something else
- try this: (another movie)
--- that's good
- Enjoy!

### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*
https://user-images.githubusercontent.com/60685289/192426661-201f92b7-b987-42e4-881b-ea2e5b6a3706.mov

When asked what type of movie to watch, he replied with "open to anything." This opened another option to what I thought would be possible.
Also, it turns out I would have to check after 30 seconds he/she liked the movie or would prefer something else.

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*


# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...
2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?
3. Make a new storyboard, diagram and/or script based on these reflections.

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

*Include videos or screencaptures of both the system and the controller.*

------

### Feedback & Process:
The feedback I got for Lab3 part 1 was relevantly good but mostly classmates said that it was a bit similar to other things existing elsewhere. So I wanted to come up with a novel, yet simple concept. What if I could help blind people? It might be hard for them to find the medicine they are looking for. Using an APDS9960 I can measure the proximity of their hand to the medicine they're looking for and let them know how close they are, using audio.

### System & idea explanation:
Two devices for blind people: one can be installed on the human ear. Another one is on the medicine itself.
It will go through 3 stages:

Part1: the device on the ear would ask if the person is facing any symptoms. Based on that, give him/her the best medicine available at home or recommend him to go to the doctor.

Part2: a device on the medicine will start helping the blind person to look for it. When the person touches it, it will let him/her know

Part3: the device on the ear will answer any questions the person might have about each medcine such as how many pieces to take per week.

### Design & Testing the system:
I went through multiple design stages. I started with a device that can be installed on the watch and then went to a more helpful one that can be installed on the ears. Also I added a second device that can be installed on the medicine itself to give the person a sense that the medicine is speaking to him/her.

Then I enhanced the device by using some anticipation of misunderstanding and improving the timing of response given by the devices. That was implemented by testing the prototype with two users after I told them to close their eyes. I made the device speak ceratain sentences when it doesn't get what the user is saying. Also, I noticed from the testing that it would be better to increase the time allowance for the user to answer the device

This my final storyboard that explaind the 3 parts process:
![image](https://user-images.githubusercontent.com/60685289/193746054-2bed6d7c-7b79-4084-a16e-95d51f9fddbb.png)

### What worked well about the system and what didn't?

Although it recognizes certain words needed for symptoms for example, it still lacks the efficiency. Also it can answer some few questions but is still very basic on this aspect and needs a lot of improvement.

### What worked well about the controller and what didn't?

When the hand completly holds the wanted medicine it correctly identifies that and lets the person know about it. However, it doesn't correctly identify how close the hand is to the wanted medicine.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

It is easy to use sensors with the pi so many other additions can be included in the system to help blind people. For example, it can automatically remind them to take a certain medicine at a specific time based on a set described by their doctor.

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

This system can create a dataset for symptoms. It can get more vocabulary to include for symptoms that could help in finding the best medicine to take. Measuring the temperature could also be benificial to help people know if the current temparature is good for a particular type of medicine.

### video
https://user-images.githubusercontent.com/60685289/193748648-d0389c08-fb90-4654-aee2-1cda0cf17df0.mov


