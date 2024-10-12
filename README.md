# DoorDarshan

DoorDarshan is a remote access control system that allows members of the RoboTech Club at NISER to remotely lock and unlock the door to the club's lab using Discord chat commands. It uses a Raspberry Pi computer interfaced with an electronic door lock and custom Discord bot software to provide secure keyless entry.
Authorized club members who have access to the DoorDarshan Discord channel can issue simple textual commands to toggle the state of the lock without needing physical keys. Additionally, a display screen positioned outside the lab door connects to the Raspberry Pi to showcase important club announcements, including upcoming events, authorized lab access lists, weather and time information. This project was conceived to enhance security and convenience of lab access. It also served as a hands-on IoT and robotics learning experience involving hardware integration, embedded programming, and software development. Overally, DoorDarshan demonstrates an automation solution for secure remote access control and management.

## Objectives

- **Develop an Integrated Access Control and Information System:** Design and implement a system using a Raspberry Pi and electronic solenoid lock, enabling door control via Discord commands and displaying information on an external screen.
- **Facilitate Monitoring and Transparency:** Utilize Discord commands for door access to log entry and exit, allowing clear monitoring of who accesses the club room and when.
- **Explore and Document Key Technical Concepts:** Design, learn and record important aspects of Raspberry Pi programming, electronic lock integration, Discord API usage, and real-time data display.
- **Educate and Engage Club Members:** This project also helps in learning and understanding how to make Discord bots using python. This documentation will not only serve as a record of the project's development but also as an educational resource for club members and others interested in similar technology applications.

## Literature Review
There are smart door systems that automatically close and open as per requirement. But applications at remote control of door *opening/closing* is limited and and overtly complicated.

## Physical Components/Materials Requirements
  - Raspberry Pi 3B+: Central computing unit for system control.
  - 12V Solenoid Lock: Electronic locking mechanism.
  - 5V Relay: To interface solenoid lock with Raspberry Pi and acts as voltage switching unit.
  - Raspberry Pi Power Supply: To power the Raspberry Pi.
  - 220V AC to 12V DC Adapter: Converts AC power to DC for the solenoid lock, cooling fan, speaker and display board.
  - 13-Inch Laptop Screen: External display for information.
  - Display Board: Interfaces the laptop screen with the Raspberry Pi.
  - Wires and Connectors: For electrical connections.
  - Plywood and 3D Printed Structures: Housing and mounting for components.
  - 12V Fan: For cooling the system.
  - Dual Speaker: To provide audio feedback or announcements.
  - Switches and barrel jacks.

## Software Requirements
  - [Shell Script](https://www.geeksforgeeks.org/introduction-linux-shell-shell-scripting/): To run a sequence of commands in an Operating System. (Here it is to execute the pm2 command)
  - [pm2](https://en.wikipedia.org/wiki/PM2_(software)#:~:text=PM2%20or%20Process%20Manager%202,in%202013%20by%20Alexandre%20Strzelewicz.): Process Manager for node.js applications (Here it is MagicMirror)
  - node.js
  - [MagicMirror](https://magicmirror.builders/)
  - python 3
  - [discord.py](https://discordpy.readthedocs.io/en/stable/) python library
  - Discord server / channel with bot integration


## Theory and Methodology
- **Motivational idea:** There is an requirement of internet based communication for all clients (*lab members*) with the common server at the door (*Door-Darshan*). Due to availability of 24x7 Wifi accessibility in the lab (*through NISER's Intranet*) , the RPi 3B with its Wifi capabilities can always be set connected with it.
A 12V solenoid lock can be used to lock the door after the door closer arm engages. It normally stays closed without any provided voltage. To open the lock, an initial supply of 9 ~ 12 V is required. After opening, a minor supply of voltage ~ 3V is required to keep it engaged.
A python file which always runs on startup can act as the central unit which intakes command comming through Discord's server and process accordingly to control the Relay module, speakers and MagicMirror display.
 
- **Background Research:**
  - **Discord API and Python Integration:** The first step involved researching how to integrate the Discord API with Python to control Raspberry Pi GPIO pins. This integration was facilitated using the discord.py package, a Python module designed for creating Discord bots.

  - **Displaying Information and Running Simultaneous Processes:** Further research focused on how to display important information such as the list of authorized members, club events, and real-time data like weather and time, while ensuring the Python file containing the Discord bot runs simultaneously. The solution was found in the [MichMich Magic Mirror](https://github.com/MagicMirrorOrg/MagicMirror) application (visit their [_website_](https://magicmirror.builders/)), which offers the necessary customizations and multitasking capabilities.

- **Design Iteration and Optimization:** Continuously iterate and update circuit design and software for optimizing power eficiency, safety and security.

## Diagrams
![Circuitry](https://github.com/rtcniser/2023-YY_DoorDarshan_ACTIVE/blob/main/Photos/DD_labelled.jpg)
Some modules are not rigorously labelled since they are subject to replacement. It's highly important that the person maintaining the system takes upon initiative to conceptually understand its working.
![Labelled Circuitry](https://github.com/rtcniser/2023-YY_DoorDarshan_ACTIVE/blob/main/Photos/circuit_diagram.jpg)
_There is also chances for minor mistakes!_
## Execution Flow
![Execution Flow](https://github.com/rtcniser/2023-YY_DoorDarshan_ACTIVE/blob/main/Photos/execution_flow.jpg)
## Directory Tree
Magic Mirror <br />
&emsp;&emsp;|--config <br />
&emsp;&emsp;|&emsp;&emsp;|--config.js &emsp;&emsp;_#Change this file for importing modules in MM and changing settings of MM and its modules._ <br />
&emsp;&emsp;|&emsp;&emsp;: <br />
&emsp;&emsp;|--modules <br />
&emsp;&emsp;|&emsp;&emsp;|--MMM-PythonPrint &emsp;&emsp;_#Module for running a python file and display output on the screen._ <br />
&emsp;&emsp;:&emsp;&emsp;|&emsp;&emsp;|--doordarshan.py &emsp;&emsp;_#Python file for discord bot and controlling the lock._ <br />
&emsp;&emsp; &emsp;&emsp;|&emsp;&emsp;: <br />
&emsp;&emsp; &emsp;&emsp;|--MMM-HTMLBox &emsp;&emsp;_#Modules for displaying a html file on the screen._ <br />
&emsp;&emsp; &emsp;&emsp;|&emsp;&emsp;|--lab_access.html &emsp;&emsp;_#HTML file containing list of people having access to the lab._ <br />
&emsp;&emsp; &emsp;&emsp;|&emsp;&emsp;: <br />
&emsp;&emsp; &emsp;&emsp;|--MMM-Wallpaper &emsp;&emsp;_#Module for keeping/changing wallpaper of the MM Screen._ <br />
&emsp;&emsp; &emsp;&emsp;|&emsp;&emsp;: <br />


## Troubleshooting / Known Problems
- Solenoid lock heating issue
  - This means it is getting constant 12V power supply.
  - Case 1 : Mechanical failure of the relay or the wires connected to the relay.
  - Case 2 : Software failure, i.e., doordarshan.py is not running or stuck. In this case, type `pm2 log mm` in the terminal to get the actual issue.
- Raspberry Pi heating issue
  - Check if the 12V fan is working properly
  - Check if there's too much CPU load on RPi by using the command `htop`. The reasons for CPU overload can be ambiguous.
  - Try rebooting and check if the problem still persists.
- RPi 3B+ has low RAM (1GB), so it connot perform multiple tasks simultaneously. Also, it is better to increase the swap memory to 512 - 1024 MB. Check out this [guide](https://pimylifeup.com/raspberry-pi-swap-file/).
- RPi low voltage warning
  - This means RPi is not getting the rated voltage / current.
  - Check if RPi original adapter is used.
- Module not working
  - Check by manually running a code to test the module. The module can be removed (_might be tedious to put back, also do note the connections_) to manually check in another setup.
  - Check if there is no [common ground]([url](https://www.sentera.eu/en/faq/g/what-is-a-common-ground/993)) error.
  - Try replacing the module in case it is not working.
- If you see a diode somewhere, it is to prevent back current.
- For any other issues
  - First check if doordarshan.py is running or not by sending `.hello` in discord.
  - If python file (discord bot) is working properly, check all the wires, connections and hardware components.
  - If python file is not working then check the output of `pm2 log mm` in terminal.
  - If python file is running but not getting connected to discord server, check network settings and the discord bot token and its persmissions. There might be changes by Discord itself.
  - If MM is not working, again check the output of `pm2 log mm` in terminal.
- Note
  - If the config file is changed in MM, first run `npm run config:check` in terminal inside the MagicMirror directory to check for issues before starting MagicMirror.
## Scope of Improvement
- This README (documentation) can be improved.
- The casing of the whole system can be accurately designed and improved.
- Safety standards of the system can be improved such that even forceful tampering doesnot cause electrical shocks.
- More beneficial features like face recognition, fingerprint scanning, and integration with other IoT based systems in the lab can be done.
- Already present features can be simplified.

## Some Observations During Developement!

- **Power Supply Issue with Raspberry Pi:** Initially, a 5V 2A generic adapter was used to power the Raspberry Pi. However, this led to insufficient power for the device, affecting its ability to interface effectively with the relay for the solenoid lock and the display board. To resolve this, we upgraded to the original Raspberry Pi power supply, ensuring stable performance of the Raspberry Pi and its connected components.

- **Solenoid Lock Power Management:** The solenoid lock requires a 12V power supply to trigger its unlocking mechanism, but it was observed that maintaining 12V continuously, in the unlocked state, caused the lock to heat up rapidly. Further investigation revealed that while 12V is necessary for triggering the lock, only about 2-3V is needed to maintain its unlocked state. Consequently, the circuit design and Python program were modified to supply 12V to the lock only during the triggering phase and provide a lower voltage (3V) from the Raspberry Pi for the lock's maintenance phase. This adjustment significantly improved the lock's operational efficiency and safety.

# Team Members

1. [Sandipan Samanta](https://github.com/Sandipan04) | Developer, Hardware/Software Integration | Int. Msc. Batch 21
2. [Girija Sankar Ray](https://github.com/Alpha3125) | oncept Idea, Developer | Int. Msc. Batch 21

_Contact us for any help required!_
   
*DoorDarshan is the improvement to MagicMirror which was initially developed by Jyothis KJ, student of Int. Msc. Batch 18.*
