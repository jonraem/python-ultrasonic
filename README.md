# python-ultrasonic

Ultrasonic distance meter for Raspberry Pi. Written in Python.

About
-
This was a project for a university course about embedded processor systems. It is an ultrasonic measuring device for measuring distance in both meters and feet. A prompt based terminal UI asks the user whether to measure in meters or feet and when to initiate measuring.

To be able simulate our project, you need to have a Raspberry Pi with Raspbian OS, a breadboard, jump cables and the HC-SR04 ultrasonic ranger. Attached you will find a picture of the final connection. As the code suggests, use GPIO pin 18 for output and GPIO pin 23 for input.

You need to transfer the Python file to your Raspberry Pi. We used SCP. The normal <code>UI.py</code> file has comments about the program's execution in Finnish. During testing we found that the comments disrupted the execution of the code so another version without comments was created for demonstrating purposes.

For a description of the project in Finnish, see the PDF file found in this repository. In the img folder you can find some pictures of the components and an example what the prompt based UI looks like.

This was a group project. Our team consisted of Joni Rämö, Teemu Tähtinen and Minna Isomäki.

![alt tag](img/P1030215.JPG)
