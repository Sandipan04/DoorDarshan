# DoorDarshan

DoorDarshan is an access control system that allows members of the RoboTech Club at NISER to remotely lock and unlock the door to the club's lab using Discord chat commands. It uses a Raspberry Pi computer interfaced with an electronic door lock and custom Discord bot software to provide secure keyless entry. Authorized club members who have access to the DoorDarshan Discord channel can issue simple textual commands to toggle the state of the lock without needing physical keys. Additionally, a display screen positioned outside the lab door connects to the Raspberry Pi to showcase important club announcements, including upcoming events, authorized lab access lists, weather and time information. This project was conceived to enhance security and convenience of lab access. It also served as a hands-on IoT and robotics learning experience involving hardware integration, embedded programming, and software development. Overall, DoorDarshan demonstrates an automation solution for secure remote access control and management.

## Objectives

- **Develop an Integrated Access Control and Information System:** Design and implement a system using a Raspberry Pi and electronic solenoid lock, enabling door control via Discord commands and displaying information on an external screen.
- **Facilitate Monitoring and Transparency:** Utilize Discord commands for door access to log entry and exit, allowing clear monitoring of who accesses the club room and when.
- **Explore and Document Key Technical Concepts:** Design, learn and record important aspects of Raspberry Pi programming, electronic lock integration, Discord API usage, and real-time data display.
- **Educate and Engage Club Members:** This project also helps in learning and understanding how to make Discord bots using python.

## Methodology

- **Background Research:**
  - **Discord API and Python Integration:** The first step involved researching how to integrate the Discord API with Python to control Raspberry Pi GPIO pins. This integration was facilitated using the discord.py package, a Python module designed for creating Discord bots.
  - **Displaying Information and Running Simultaneous Processes:** Further research focused on how to display important information such as the list of authorized members, club events, and real-time data like weather and time, while ensuring the Python file containing the Discord bot runs simultaneously. The solution was found in the MichMich Magic Mirror application, which offers the necessary customizations and multitasking capabilities.

- **Materials Used:**
  - Raspberry Pi 3B+: Central computing unit for system control.
  - 12V Solenoid Lock: Electronic locking mechanism.
  - 5V Relay: To interface solenoid lock with Raspberry Pi.
  - Raspberry Pi Power Supply: To power the Raspberry Pi.
  - 220V AC to 12V DC Adapter: Converts AC power to DC for the solenoid lock, cooling fan, speaker and display board.
  - 13-Inch Laptop Screen: External display for information.
  - Display Board: Interfaces the laptop screen with the Raspberry Pi.
  - Wires and Connectors: For electrical connections.
  - Plywood and 3D Printed Structures: Housing and mounting for components.
  - 12V Fan: For cooling the system.
  - Dual Speaker: To provide audio feedback or announcements.

- **Design Iteration and Optimization:** Continuously iterate and update circuit design and software for optimizing power eficiency, safety and security.

- **Documentation and Education:** This documentation will not only serve as a record of the project's development but also as an educational resource for club members and others interested in similar technology applications.

## Observations

- **Power Supply Issue with Raspberry Pi:** Initially, a 5V 2A generic adapter was used to power the Raspberry Pi. However, this led to insufficient power for the device, affecting its ability to interface effectively with the relay for the solenoid lock and the display board. To resolve this, we upgraded to the original Raspberry Pi power supply, ensuring stable performance of the Raspberry Pi and its connected components.

- **Solenoid Lock Power Management:** The solenoid lock requires a 12V power supply to trigger its unlocking mechanism, but it was observed that maintaining 12V continuously, in the unlocked state, caused the lock to heat up rapidly. Further investigation revealed that while 12V is necessary for triggering the lock, only about 2-3V is needed to maintain its unlocked state. Consequently, the circuit design and Python program were modified to supply 12V to the lock only during the triggering phase and provide a lower voltage (3V) from the Raspberry Pi for the lock's maintenance phase. This adjustment significantly improved the lock's operational efficiency and safety.

## Team Members

1. [Sandipan Samanta](https://github.com/Sandipan04) | Development, Maintenance| 3rd Year Int. MSc. School of Mathematical Sciences
2. [Girija Sankar Ray](https://github.com/Alpha3125) | Development, Maintenance | 3rd Year Int. MSc. School of Mathematical Sciences
