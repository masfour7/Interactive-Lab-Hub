# Final Project - The Super Garbage
#### Group Members: Phillip O’Reggio (pno3) and Mohammad Asfour (mya26)

## 1. Project Plan
### Description (Big Idea)
Essentially creating a trash enclosure with multiple bins. Each bins will be designated to collect a different material (i.e. compost, plastics, general waste)
When the user walks up to the trash enclosure, an decision making algorithm will be used to determine which type of material the trash the user is trying to throw away is based on the material of the trash, the enclosure will automatically open the lid of the respective enclosure it should go into
The waste enclosure will also be able to detect which bins are full to prevent any sort of trash overflow.

### Timeline
#### Week 1 (11/15 - 11/22): 
- Make sure all parts needed are available
- Start exploring the algorithm that is going to identify the type of material that will be thrown
- Design process and testing the best possible design based on user testing

#### Week 2 (11/22 - 11/29) - “Demonstrate that your project is functioning well enough for somebody to use and interact with it. This presentation will just be to the teaching team.”
- Build the software that will use the algorithm: it would give the algorithm an input and takes an output back. Then do certain tasks
- Build an actual prototype
- Add sensor functionality to identify when the garbage is full
- User testing and feedback

#### Week 3 (11/29 - 12/6):
- Improve the algorithm by widening the range of materials it accepts
- Build a more polished prototype
- User testing and feedback

#### Week 4 (12/6 - 12/13):
- Make sure everything is working as intended
- User testing and feedback

### Parts Needed
This project will require several motors to automate the opening and closing of the lid of the trash can. It will require a camera to look at objects the user is trying to throw out, and then run the machine learning classifier to determine what type of waste the user has. In order to best detect how full the trash cans are, we intend to use the distance sensor placed towards the underside of the lid. To communicate how full the trash is, we intend to use lights to visually show the user if a certain bin is full. For actually constructing the trashcan and its compartments itself, we aren’t sure yet on the exact material, but will likely use a material for the lid that is light enough that the motors can move it without too much issue. We either will prototype most of it with cardboard, or are considering laser cutting or 3D printing parts.

- Webcam
- Distance Sensor
- Raspberry pi
- LED for each trash compartment
- Servo motors
- Material for the bin itself

### Risks/Contingencies
- Unable to develop an accurate waste classifier model
- Unable to create the physical trash can itself
- Unable to find enough sensors to complete the project
- Unable to interface pi with all the sensors needed
- Unable to create a program that is efficient enough to run on pi to complete all tasks

### Fall-back plan
Some issues that may arise is that we may either run out of time to complete all the features of the project, or find ourselves unable to acquire all the parts needed for the project. In those situations we intend to make a simpler version of this idea. One option is to remove the classification aspect and only have 1 compartment that automatically opens for the user when they get close. Another option is to pivot on the trashcan idea to instead focus on just the classification aspect using the webcam. It would look at the trash the user holds in front of the camera, and then the speaker would audibly say what type of trash it is.

### Slides
https://docs.google.com/presentation/d/1koWn-A9DBmQv5UOUdNL5OAPvQidD9utu1aMnhL6Cs6s/edit##slide=id.g18d71ccba20_1_0

## 2. Functioning Project
In building our model trash can, we had to make some comprosmises between the design we aimed to make and what we could actually build. **Since the motor we have is small, we scaled down bin to a small model**. Also since we only have 1 motor, we had to alter the design and interaction a bit. **Instead of the machine learning model opening up the proper bin, we instead indicate what it classified it as using the OLED for a color, and included a guide nearby so people understand the meaning of the colors**. Whenever it detects any kind of trash, the lid opens up, making it easy to tell that the lid's actions is tied to what is currently in front of the sensor.

The design of the overall apparatus had to change a bit to account for scale, since when we scaled everything down, the webcam now was by far the largest piece of hardware involved. Also since we built it out of cardboard we had some issues with weights and getting the entire thing to stay in position (espeically with the movement of the motor).

![image](https://user-images.githubusercontent.com/60685289/207825344-adfefd50-99da-4ac3-bec0-65e0fc02b04d.png)
![WhatsApp Image 2022-12-15 at 4 40 44 AM](https://user-images.githubusercontent.com/60685289/207825851-b0bc67fb-95f9-4e89-98e2-0079c1a78438.jpeg)
![WhatsApp Image 2022-12-15 at 4 40 01 AM (1)](https://user-images.githubusercontent.com/60685289/207825857-0e06dd32-4b88-4bd5-bdca-af671e899428.jpeg)
![WhatsApp Image 2022-12-15 at 4 40 01 AM](https://user-images.githubusercontent.com/60685289/207825859-a472df0b-8554-4476-b874-be7d6cd796a4.jpeg)

## 3. Documentation of design process
![image](https://user-images.githubusercontent.com/60685289/207823282-5d3c993f-d410-4f1a-bf2e-b22fbcd776cc.png)
![image](https://user-images.githubusercontent.com/60685289/207823432-83710f99-ae06-4b04-9ebd-d72486984cf3.png)

![image](https://user-images.githubusercontent.com/60685289/207823545-b8bb82e7-c06e-4035-b999-4e804572497a.png)

## 4. Archive of all code & design patterns used in the final design.

- We got the data from: https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification
- Model trained is stored in ![keras_model](https://github.com/masfour7/Interactive-Lab-Hub/blob/Fall2022/finalProject/keras_model.h5)

Getting image recognition working
[![img](TODO fill this in)]

Early lid functionality
[![img](TODO fill this in)]

Image Recognition on the pi
[![img](TODO fill this in)]

Getting things to work after the demo
[![img](TODO fill this in)]

## 5. Video of someone using your project

## 6. Reflections
After making our product we learned that coding is only 1 small part of building a good interaction and making a sensible system. For out example, coding was by far the easiest part but what was far trickier was getting the right sensors in the right places, and doing so in a way that didn't make the garbage bin just fall apart. Even if we managed to get everything where it needed to, there was still the interaction side as often people would tno act how we expected. We assumed that they would just hold their objects in front of the camera, but people were sometimes confused on where to hold it.

For the demo itself, we ended up running into technical issues with both the code and apparatus, and endd up not being able to get the distance sensor or motor working in time. This made us have to change our interaction on the fly, since the lid opening and the distance were kind of important for potraying any kind of connection of the image classification to the operation of the bin. We pivoted to a setup where we held the object to the side of the bin and had the bin itself light up, which worked on a techincal level but was pretty not intuitive.

Despite this, we did learn a lot abou thte interaction. One big thing was how the speed of the pi's image recognition affected the interaction. The pi itself is kind of slow at classifying, taking several seconds for it to catch up and process what it sees. This means people would have to hold the object in front of the can for several seconds before the bin would light up as intended, which led to a lot of confusion at the actual demo.

Also from the TA and professor's feedback, we learnd that we should use some kind of platform/display to indicate to the user where they should hold the item. We had initially assumed the camera's direction would be enough, but this was a mistake on our part. 

Another thing to note is that the OLED's were so bright, it would shine onto the view of the camera, and in turn, affect the image classification. This made a lot of sense seeing it happen in person when we tested it and at the demo, but was definitely not something we considered in storyboarding or the early design stages.

Another thing we realized pretty immediately at the event is the need for a label describing te meaning of the colors. In our very early designs, we kin do fassumped the multuple bins would be color coded so that would of been an indicator to the user. However, in practice with our one bin, it was pretty cryptic.

I wish I knew about how difficult it would be getting the pieces and structure together, as I would of gotten a better material than cardboard boxes I had lying around and spent more time on making a good bin.

## 7. Group Work Distributions
We both helped each other and learned from each other's mistakes. But this was each one's focus:

Mohammad
- training the model
- finding image data for the model
- getting the model to run on the pi
- help Phillip with any challenges

Phillip
- making the bin
- writing code for the lid, oled, sensors
- help Mohammad with any challenges

## The End - Thank you for a great semester !! :D
