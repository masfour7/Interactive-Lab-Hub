Phillip O’Reggio (pno3), Mohammad Asfour (mya26)

![input settings](draftdrawing.png)

# Initial Project Proposal
## Big Idea
Essentially creating a trash enclosure with multiple bins. Each bins will be designated to collect a different material (i.e. compost, plastics, general waste)
When the user walks up to the trash enclosure, an decision making algorithm will be used to determine which type of material the trash the user is trying to throw away is based on the material of the trash, the enclosure will automatically open the lid of the respective enclosure it should go into
The waste enclosure will also be able to detect which bins are full to prevent any sort of trash overflow.

## Timeline
### Week 1 (11/15 - 11/22): 
- Make sure all parts needed are available
- Start exploring the algorithm that is going to identify the type of material that will be thrown
- Design process and testing the best possible design based on user testing

### Week 2 (11/22 - 11/29) - “Demonstrate that your project is functioning well enough for somebody to use and interact with it. This presentation will just be to the teaching team.”
Build the software that will use the algorithm: it would give the algorithm an input and takes an output back. Then do certain tasks
- Build an actual prototype
- Add sensor functionality to identify when the garbage is full
- User testing and feedback

### Week 3 (11/29 - 12/6):
- Improve the algorithm by widening the range of materials it accepts
- Build a more polished prototype
- User testing and feedback

### Week 4 (12/6 - 12/13):
- Make sure everything is working as intended
- User testing and feedback

## Parts Needed
This project will require several motors to automate the opening and closing of the lid of the trash can. It will require a camera to look at objects the user is trying to throw out, and then run the machine learning classifier to determine what type of waste the user has. In order to best detect how full the trash cans are, we intend to use the distance sensor placed towards the underside of the lid. To communicate how full the trash is, we intend to use lights to visually show the user if a certain bin is full. For actually constructing the trashcan and its compartments itself, we aren’t sure yet on the exact material, but will likely use a material for the lid that is light enough that the motors can move it without too much issue. We either will prototype most of it with cardboard, or are considering laser cutting or 3D printing parts.

- Webcam
- Distance Sensor
- Raspberry pi
- LED for each trash compartment
- Servo motors
- Material for the bin itself

## Risks/Contingencies
- Unable to develop an accurate waste classifier model
- Unable to create the physical trash can itself
- Unable to find enough sensors to complete the project
- Unable to interface pi with all the sensors needed
- Unable to create a program that is efficient enough to run on pi to complete all tasks

## Fall-back plan
Some issues that may arise is that we may either run out of time to complete all the features of the project, or find ourselves unable to acquire all the parts needed for the project. In those situations we intend to make a simpler version of this idea. One option is to remove the classification aspect and only have 1 compartment that automatically opens for the user when they get close. Another option is to pivot on the trashcan idea to instead focus on just the classification aspect using the webcam. It would look at the trash the user holds in front of the camera, and then the speaker would audibly say what type of trash it is.


## other links
Slides
https://docs.google.com/presentation/d/1koWn-A9DBmQv5UOUdNL5OAPvQidD9utu1aMnhL6Cs6s/edit##slide=id.g18d71ccba20_1_0

# Final Report
## Final Deliverable
In building our model trash can, we had to make some comprosmises between the design we aimed to make and what we could actually build. Since the motor we have is small, we scaled down bin to a small model. Also since we only have 1 motor, we had to alter the design and interaction a bit. Instead of the machine learning model opening up the proper bin, we instead indicate what it classified it as using the OLED for a color, and included a guide nearby so people understand the meaning of the colors. Whenever it detects any kind of trash, the lid opens up, making it easy to tell that the lid's actions is tied to what is currently in front of the sensor.

The design of the overall apparatus had to change a bit to account for scale, since when we scaled everything down, the webcam now was by far the largest piece of hardware involved. Also since we built it out of cardboard we had some issues with weighta and getting the entire thing to stay in position (espeically with the movement of the motor).


## Reflections
After making our product we learned that coding is only 1 small part of building a good interaction and making a sensible system. For out example, coding was by far the easiest part but what was far trickier was getting the right sensors in the right places, and doing so in a way that didn't make the garbage bin just fall apart. Even if we managed to get everything where it needed to, there was still the interaction side as often people would tno act how we expected. We assumed that they would just hold their objects in front of the camera, but people were sometimes confused on where to hold it. Also since the lid is controlled by a distance sensor as well as the camera, the lid might close and open unexpectedly, also confusing people. These were all things that got glossed over in our initial design of the bin but ended up being pretty important for the actual function of our idea.

I wish I knew about how difficult it would be getting the pieces and structure together, as I would of gotten a better material than cardboard boxes I had lying around and spent more time on making a good bin.


## Group Work Distributions

Mohammad
- training the model
- finding image data for the model
- getting the model to run on the pi

Phillip
- making the bin
- writing code for the lid, oled, sensors
