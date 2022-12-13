# WannaDance

# Contributors:
* Kenneth Alvarez
* Trevor Morcott


# Big idea: 	
Imagine you are at a social event and you bump into someone, how do you prevent any conflict? To settle any issues between the two of you, we can start a dancing game! The game would resemble the famous Dance Dance Revolution Game where users have a dance pad on the ground and start breaking it down! To do this both users will step on the pads at the same time, music will begin to play, and a projector as well as LED lights will tell the two users what pad to dance on. Once they finish they both will be declared a winner.


# Demo Video:
https://drive.google.com/file/d/1a5BjfniB0WJinnXDSP1-J19pE2uYzRqN/view


# User Test:
https://drive.google.com/file/d/1MZ_m2w_3HE83bu4nLB7K-AD5JYx3Pc-o/view?usp=sharing 


# Parts Needed:
* SparkFun Qwiic OLED Display x 1
* Canvas(10x10ft) x 1
* Adafruit MPR121 Capacitive Touch Sensor QT x 1
* Led lights x 3
* Speaker x 1
* Top Greener Smart plug x 3
* Alligator Clips x 12
* Duck Tape * 1
* Scissors * 1
* Tin Foil Roll * 1


# Setup:
1. Grab the canvas and separate using duck tape the canvas into 3 columns
2. With two copper tape strips, apply in between each column
3. Find the middle of the canvas and place two rows of duck tape to indicate the separation of the dance pad(Don't forget to cut the copper tape in the middle of the canvas)
4. Grab the 12 alligator clips and clip them to the ends of the canvas where the copper tape stops
5. At the other end of the alligator clips, connect them to the to the capacitive sensor
6. To put together the raspberry pi, connect the capcitive sensor and the lcd screen using qwiic connectors
7. Clone the repo to the raspberry pi and run 'python wanna_dance'


# Timeline:
* Week 12: Gathered the necessary materials and programmed the skeleton code
* Week 13: Polished the code and start putting together physical product
* Week 14: Debug any leftover issues in the code and complete physical product 
* Week 15: Final product ready for demo and has been tested with users


# Verplank Diagram of the System:
![IMG_0486](https://user-images.githubusercontent.com/46539140/206017602-06789347-c7ac-4244-a381-73c01a4b4129.jpg)


# State Diagram:
<img width="1454" alt="Screenshot 2022-12-06 at 2 33 18 PM" src="https://user-images.githubusercontent.com/46539140/206005282-cc125d87-5fc7-4ad2-b2bd-4c54e84982e3.png">

# Smart Plug and Tasmota setup 

One of the major pieces of our project and game was the interactive use of holiday lights using smart plugs.  These smart plugs were TopGreener 10A Power Monitoring Plug flashed with an earlier Tasmota 9.X version.

It took significant effort to get the smart plugs to work reliabily within the limits of Cornell Tech's campus and the networking configurations.  As this was a major piece of our work and on suggestion from TA Ilan Mandel, we have made a documentation guide and FAQ based on our experience setting up the plugs and his accompanying help making that happen.  We hope this can be shared and be of use to future students who may want to use these devices or similar ones.  The guide covers setting up the Top Greener Plugs specifically but can also be broadly applied to any Tasmota flashed device.  Please let us know if there are any suggestions or edits to this document by those who read this and we will update accordingly!

**The guide and FAQ can be found at https://docs.google.com/document/d/1nkVzLo6AtSgI2CKPTVwlr4yHGvH9T-VcPqXod2XLeYs/edit?usp=sharing** 

![image](https://user-images.githubusercontent.com/112022260/207453135-a09cbf7c-cd1d-42f6-8b63-a54428b15845.png)
![image](https://user-images.githubusercontent.com/112022260/207453173-11c90a3c-6ac9-496a-af61-e63af891bb7f.png)
![image](https://user-images.githubusercontent.com/112022260/207453206-4d65b726-a786-4e45-8e44-1f4b65a7b1d4.png)
![image](https://user-images.githubusercontent.com/112022260/207453236-c13ed74d-7bf8-4f6c-9bf8-d6e2d653055e.png)
![image](https://user-images.githubusercontent.com/112022260/207453278-e093b1b3-d0b3-4533-89b5-7a800d4b75c5.png)
![image](https://user-images.githubusercontent.com/112022260/207453325-a7615ee3-52fb-4647-b138-ec68b9d5fadd.png)






# Progression Pictures(In Order of Evolution):

We first started by brainstorming designs and how to feasibly make the project with our materials
![IMG_0418](https://user-images.githubusercontent.com/46539140/206000893-ccedec00-bb08-4807-8f3c-0ace1a660b2e.jpg)

We then began development by sealing off the edges of the canvas
![IMG-1954](https://user-images.githubusercontent.com/112022260/207450351-6bca01ae-8891-4228-87c8-0bf6582ac308.jpg)

Once we had the initial shape, we added the longer columns strips and began to test connectivity
![IMG-1957](https://user-images.githubusercontent.com/112022260/207450319-0ca11bb2-06cb-4ea6-a9a1-a85771fb6b4c.jpg)



We continued to build out the larger dancefloor and added details
![IMG_0419](https://user-images.githubusercontent.com/46539140/206001396-1ad45e6b-1a5e-41e9-a3af-f6bb5cf6e26a.jpg)
![69143610260__8E92C3EF-3FF3-4E60-ACC6-7F870D9DF4C8](https://user-images.githubusercontent.com/46539140/206001020-606a1ae0-8f02-4acf-b2af-2153534f40b0.jpg)


We first got a prototype game working with half of the mat integrating the lights from the earlier steps
![69144620194__46881899-DD6E-4C79-B8E1-6B5475B1D535](https://user-images.githubusercontent.com/46539140/206002124-a88a759c-bc8e-4725-9fb6-88074aacb0d5.jpg)
![IMG-1979](https://user-images.githubusercontent.com/112022260/207450416-ead7b672-653e-4eab-9214-7ee5fd00bd5c.jpg)
![IMG_0428](https://user-images.githubusercontent.com/46539140/206002770-fd42fc13-1088-4450-ad84-549fdf8678ff.jpg)


We then expanded back out and got the full game working
![IMG_0478](https://user-images.githubusercontent.com/46539140/206003144-346c6f2f-1039-4052-894f-9ffe52dda4c4.jpg)
The expanded length required extending the copper strips and gator clips we had using additional wiring.  It created a very crowded capacitive board that was sensitive to movement.
![69145903669__958712EB-D8CC-4B20-9E49-166AE9653600](https://user-images.githubusercontent.com/46539140/206001792-b7b2dff6-e7f6-45f1-a7c5-bce1708e59d4.jpg)
![69197682019__35E0287C-9D6F-4BBA-A420-52519FCEC644](https://user-images.githubusercontent.com/46539140/206002454-f444b749-3df4-4b1b-bb64-750353c3edcb.jpg)




# Challenges:
Some of the major obstacles that we came across when constructing our final project was specifically with the smart plugs. There were several network issues due to the security layer so we had to switch to a private network. Specifically "Device_Farm" which is maintained by a lab at Cornell Tech. In addition, we also faced some trouble when constructing the physical device. There were some design challenges when considering conductive sensing using the capcitive sensor. To solve this, sensing was significantly better using tin foil that was applied to the bottom of the user's shoes. 


# Potential Improvements;
1. Since we have a small LCD screen showing the user's scores, we could add code to have it vocally output through a speaker 
2. Find a conductive material that is more durable than copper tape since the tape easily rips with greater force
3. Figure out a way to make the tin foil shoes reusable


# Group Work Distribution:
* Trevor: 
  - Smart Plug Configuration(MQTT/Network Compatibility)
  - Mat Setup
  - Game Refactoring
  - Single and Multiplayer Functionality
* Kenneth: 
  - Created game skeleton(Working LCD and Capacitive Sensors)
  - Mat Setup
  - Added music functionality
  - Game Refactoring
  - Single and Multiplayer Functionality
