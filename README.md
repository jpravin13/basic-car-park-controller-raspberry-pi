# Design and Development of a Raspberry Pi-Based Car Park Controller: An Embedded Software Design Approach

## Abstract

This report presents the design and implementation of an automated car park controller system using a Raspberry Pi. The system, guided by principles from Jacob Beningo's book on embedded software design, employs a multitasking approach to manage entry and exit gates in a car park. The system integrates Infrared (IR) sensors and servo motors to control the gates, while an OLED display provides real-time information on available parking spaces. The project demonstrates the practical application of embedded systems in automating and optimizing everyday tasks, highlighting the seamless integration of hardware and software components in an embedded system environment. The report further discusses the project's methodology, results, and potential future improvements.

## 1.0 Introduction

Embedded systems are a cornerstone of the electronics industry today. They use a combination of hardware and software to perform specific tasks or functions within a larger system. This project focuses on designing and developing embedded software for a car park controller. The software will be developed using a multitasking approach on a Raspberry Pi board. The project will be guided by the principles and techniques outlined in Jacob Beningo's book on embedded software design.

### 1.1	Introduction to Embedded Software Design

Embedded software design is the process of creating software that is tailored to 	run on embedded systems. Embedded systems are computer systems designed to perform specific tasks or functions within larger systems. They are often found in various devices and appliances, such as smartphones, automobiles, medical equipment, industrial machinery, and home appliances.

The importance of embedded software design lies in its critical role in enabling 	the functionality and performance of embedded systems. Unlike general-purpose software, embedded software is tightly integrated with the hardware and must be optimized for resource-constrained environments. Efficient and reliable embedded software design is crucial to ensure the proper operation, real-time responsiveness, power efficiency, and safety of the embedded system.

### 1.2 Overview of the Embedded Software Design Life Cycle

Embedded software design life cycles often consist of numerous stages, including requirements analysis, system design, software development, testing, integration, and maintenance. Embedded software design life cycles are also typically lengthy. The following is a concise summary of each stage.

Gathering and analysing the embedded system's needs are two tasks that make up this stage, which is called "Requirements Analysis." It involves gaining an 	understanding of the functionality that is wanted, the performance limits, the hardware limitations, and any unique real-time needs.

The overall system architecture is defined at this step, which is known as the 	system design stage. It also entails selecting the proper microcontrollers or processors and dividing the software into its many modules or jobs, as well as identifying the hardware components that make up the system.
The actual coding of the software modules as well as their implementation takes place during this stage of the software development process. It's possible that the programming languages and tools that are used will change based on the embedded system and the requirements that are being met.

Individually and as a system, the software modules are tested to ensure that they 	conform to the requirements. Unit testing, integration testing, and testing at the system level are all a part of this stage. Functional, performance, and reliability testing are also a part of this stage.

When all the software modules have been thoroughly evaluated, they are integrated with the embedded system's hardware. At this point, it is necessary to test the behavior of the entire system in addition to confirming that all the individual modules are properly communicating with one another and synchronized.

After an embedded system has been put into action, it may need to be maintained throughout its lifecycle with tweaks such software updates, optimizations, and bug fixes to make sure it continues to function reliably and can adapt to new needs.

### 1.3 Human-machine Interface in the Context of Embedded Systems

The human-machine interface (HMI) in embedded systems refers to the interaction between the user or operator and the embedded system. It encompasses the hardware and software components that enable communication, control, and feedback between humans and machines.

In embedded systems, HMIs can vary widely depending on the nature and complexity of the system. They can range from simple button or keypad interfaces to more sophisticated graphical user interfaces (GUIs) with touchscreens, displays, and 	input devices like keyboards or joysticks.

The design of an effective HMI involves considering factors such as usability, 	ergonomics, and the specific tasks or operations that users need to perform. It includes designing intuitive interfaces, clear visual feedback, error handling mechanisms, and appropriate control mechanisms to ensure smooth and efficient interaction between the user and the embedded system.

### 1.4	Communication Protocols used in Embedded Systems

Embedded systems frequently require the ability to interface with other devices 	or computerised networks, including displays, actuators, sensors, and even other 	embedded systems. There are many different communication protocols that are utilised 	in order to make the flow of data more dependable and effective. The following are 	some communication protocols that are frequently used in embedded systems.

UART, which stands for "Universal Asynchronous Receiver/Transmitter," is a 	serial communication protocol that facilitates asynchronous serial data transfer between electronic devices. It is one of the most popular types of serial communication. Because it is so easy to use, it is frequently utilised for communication across shorter distances.
	
Serial Peripheral Interface, or SPI for short, is a synchronous serial communication protocol that enables full-duplex communication between a master device and many slave devices. Interconnecting microcontrollers, sensors, and memory devices are 	typical applications for this type of cable.

I2C, which stands for "Inter-Integrated Circuit," is a serial communication 	system that enables devices to communicate with one another across very small 	distances. It can have many masters and multiple slaves. It is utilised for the purpose of 	connecting a variety of peripherals, such as EEPROMs, real-time clocks, and sensors.

CAN, which stands for Controller Area Network, is a robust serial communication protocol that is used extensively in a variety of industrial and automotive applications. It is notable for its fault-tolerant and deterministic qualities in addition to its support for high-speed connectivity.

Ethernet is a networking protocol that is commonly used for communication over local area networks (LANs). Embedded systems can now connect to the internet or communicate with other devices on the network thanks to this capability.

MQTT stands for "Message Queuing Telemetry Transport" and it is a lightweight publish-subscribe messaging protocol that is frequently used in Internet of 	Things (IoT) applications. It is optimized for devices with limited resources and allows 	the effective transfer of data over networks with variable reliability.

The choice of a communication protocol is determined by a number of different 	considerations, including the communication distance, the data rate, the power 	consumption, the real-time requirements, and the particular application needs of the 	embedded system.

### 1.4 Overview of Proposed Project
The project aims to address the inefficiencies and inconveniences associated with manual car park management. Traditional car parks often require human intervention for the operation of entry and exit gates and the monitoring of available parking spaces. This manual process can lead to errors, delays, and a lack of real-time information, causing inconvenience for both the car park operators and the users.

The importance of solving this problem lies in the increasing need for automation in our daily lives. Automated systems not only reduce the need for manual labor but also increase efficiency, accuracy, and convenience. In the context of a car park, an automated system can provide real-time information about available spaces, streamline the process of entry and exit, and ultimately enhance the user experience. Furthermore, the implementation of such a system using a Raspberry Pi and embedded software design principles serves as a practical demonstration of how embedded systems can be used to automate and optimize everyday tasks.

## 2.0 Objectives

2.1 Describe the concept of embedded software design using the life cycle, human machine interface and communication.

2.2 Design and develop the embedded software by using the suitable toolset based on the analysis of the user requirement and diagrams or other modelling languages.

## 3.0 Methodology
### 3.1 Conceptual Development
By adhering to the embedded software design life cycle concept, the user requirements are of main concern for the development of a car park controller system with a Raspberry Pi computer. In most scenarios without implementation of such systems in public parking lots, drivers would be at a lost as to whether or not there are vacant spots in the area. This would lead to an unnecessary waste of time on the consumer’s side thus, leading to an unpleasant customer experience. Besides, if drivers flock into a building without prior knowledge of vacancies, the traffic within the building would be congested. This justifies the need for a robust solution to prevent said scenarios. Therefore, a car park controller system is proposed. 

![Block Diagram](BlockDiagram_Concept.png)

The block diagram consists of the following components:

1. **Input Devices (IR Sensors)**: These are the devices that provide input to the Raspberry Pi. In this case, it would be the two Infrared (IR) sensors, one at the entrance and one at the exit.

2. **Processing Unit (Raspberry Pi)**: This is the Raspberry Pi itself, which processes the input received from the IR sensors and sends commands to the output devices.

3. **Output Devices (Servo Motors, OLED Display)**: These are the devices that receive commands from the Raspberry Pi and perform actions based on those commands. In this case, it would be the two Servo motors (one at the entrance and one at the exit) and the OLED display.

The arrows in the block diagram indicate the flow of information. The IR sensors send data to the Raspberry Pi, which processes the data and sends commands to the Servo motors and the OLED display. The Servo motors control the opening and closing of the entrance and exit gates, and the OLED display shows the number of available parking spaces.

### 3.2 System Construction
Adhering to the principle of "There is no hardware, only data", a prototype of the proposed system was constructed according to the block diagram constructed at the initial stage of development. The model, conjured using readily available sensor modules was then programmed in a bare-metal manner using Assembly language, whereby a high input at a GPIO pin would incur a high output to another GPIO pin. This would act as a proof-of-concept that input from the IR sensor would trigger voltage to the output, in this case a water pump that acts as a placeholder for a servo motor. Therefore, a foundation was developed where further developments can be performed in a modular manner. 

![BaremetalFlowchart](Flowchart_1_Baremetal.png)

However, a more intuitive and modular programming language has to be utilized to ensure flexibility and scalability for the development process. Therefore, Python was picked as the main programming language for the continuous development of the project.

A flowchart was designed to mimic the working mechanism of the system, whereby input from an IR sensor would trigger the servo motor to spin for a total of 90 degrees from its original position. As soon as the IR sensor detects that no object is present, the servo motor returns to its original position. 

Then, further instructions were added into the base flowchart to account for another pair of IR sensor and servo motor. This would mimic the working mechanism of existing car park controller systems with entrance and exit gantry gates.

Intuitively, drivers would want to know if a car park has vacant spaces before entering into one. Therefore, an OLED display is added onto the system to inform potential users of the number of spaces available in the car park. Whenever a car enters the car park, a digit is subtracted from the default number of vacant spaces available. When a vehicle exits the car park, a digit is added onto the last value. Additionally, if the OLED displays that the car park is FULL, the servo motor would not move even with the detection of an object.

![PythonFlowchart](Flowchart_2_Python.png)

The system is designed within Fritzing, an open-source EDA software. The pin connections were determined by referring to the documentation provided on the Pi Foundation's official website. 

![CircuitDesign](Embedded_Sketch_bb.png)

Include information on GPIO pins and PWM for the purpose of this project if the pins were used for IR sensors and pins were used for servo motor. 

| Component             | Pin Type | GPIO Number |
|-----------------------|----------|-------------|
| IR Sensor (Entrance) | Input    | 14          |
| IR Sensor (Exit)     | Input    | 15          |
| Servo Motor (Entrance)| Output  | 18           |
| Servo Motor (Exit)   | Output   | 13         |
| OLED Display         | I2C      | SCL, SDA    |

The OLED Display uses the I2C interface, which is a two-wire interface using the SCL (clock line) and SDA (data line) which are general for most models of the Raspberry Pi.

Therefore, the circuit is constructed by adhering to the pin connections and the circuit diagram.

## 4.0 Results and Discussion
The Python program is then started using the command sudo python3 test.py in order for the program to gain access to all GPIO pins, preventing errors.

For testing purposes, a model car was placed at the entrance, where the IR sensor detects a HIGH input.

![Result_1](CarAtEntrance_Use.png)

The HIGH input of the IR sensor sends a signal to the Raspberry Pi to incur a voltage at GPIO 18, triggering the servo motor to spin for a total of 90 degrees clockwise, thus opening the gate of the car park prototype entrance.

![Result_2](EntranceOpens_Use.png)

The system works as programmed because the number of vacant spots is reduced by 1 as shown in the subsequent figure. 

![Result_3](SlotsReduce.png)

3 more cars are sent into the car park, thus occupying the 4 slots that were available. This triggers the OLED to display the text "FULL", indicating that the car park has no more vacant spots left. Any car at the entrance would not be able to enter due to a condition in the code that leaves the output voltage as 0 even if a HIGH value is detected at the input.

![Result_4](CarCantEnterFULL.png)

As soon as a car leaves the car park through the exit, the number of vacant spots increases by 1 from the last value.

![Result_5](SlotIncrease.png)

Therefore, the system proposed is a successful proof-of-concept that can be deployed and is highly flexible and scalable.

The automated car park controller system performed reasonably well in tests, demonstrating its capability to effectively manage a car park's entry and exit gates and monitor the availability of parking spaces. However, during testing, it was observed that the servo motors exhibited some jittering. This issue was traced back to a lack of sufficient voltage. To address this, future iterations of the system could consider using a more robust power supply or implementing voltage regulation measures to ensure the servo motors receive the necessary voltage for smooth operation.

During the project's implementation, several challenges were encountered. One of the initial challenges was setting up the Raspberry Pi in headless mode. This was a crucial step, as it allowed for remote operation of the Raspberry Pi without the need for a separate monitor or keyboard. The issue was resolved by setting up Wi-Fi credentials using the Raspberry Pi Imager. Once this was done, it was possible to connect to the Raspberry Pi's terminal via SSH over the same network, enabling remote access and control.

Another challenge was coding the program without a Graphical User Interface (GUI). This was particularly important as the system needed to operate autonomously without user interaction. To overcome this challenge, Nano, the built-in text editor in Raspberry Pi, was used. The code was saved as a .py file and executed using the command python3 test.py, which allowed the program to run perfectly.

These challenges provided valuable learning experiences and highlighted the importance of problem-solving and adaptability in the field of embedded systems design. Despite these hurdles, the project was successful, and the system was able to effectively automate the operation of a car park.

## 5.0 Conclusion and Future Works
All in all, the project "Programming Embedded System with Raspberry Pi: Car Park Controller" successfully demonstrated the integration of various embedded system components to create an efficient and automated car park controller system. By leveraging the capabilities of the Raspberry Pi, IR sensors, servo motors, and an OLED display, the project achieved the desired functionalities of managing entry and exit gates, displaying the number of empty slots, and indicating when the parking is full. Through the implementation of this project, several key aspects of embedded systems were addressed. Firstly, the hardware setup required careful consideration of connecting the IR sensors and servo motors to the Raspberry Pi's GPIO pins, ensuring proper communication and control. This involved understanding the electrical connections and interfacing with the Raspberry Pi's software capabilities. Secondly, the software development phase was crucial in realizing the functionality of the car park controller system. Programming in Python enabled the utilization of the Raspberry Pi's GPIO library and allowed for precise control over the servo motors and IR sensors. Additionally, the integration of an OLED display required the installation and usage of relevant libraries, demonstrating the ability to work with external displays in an embedded system context. The project highlighted the importance of real-time sensing and response mechanisms in embedded systems. The IR sensors played a vital role in detecting the presence of cars at both entry and exit gates, enabling the servo motors to respond accordingly by opening or closing the gates. This interaction demonstrated the seamless integration of hardware and software components, showcasing the capabilities of an embedded system in providing automated control. Furthermore, the use of an OLED display added a valuable visual component to the system. By constantly updating and displaying the number of empty slots, the display provided real-time information to drivers, simplifying the parking process and enhancing user experience. The ability to adapt and communicate crucial information in an embedded system environment exemplifies the practical applications and benefits of such systems in real-world scenarios. Overall, the project "Programming Embedded System with Raspberry Pi: Car Park Controller" successfully showcased the development and implementation of an embedded system that effectively managed car park entry and exit gates. Through the integration of IR sensors, servo motors, and an OLED display, the system demonstrated the power and versatility of embedded systems, combining hardware and software components to deliver automated control and real-time information. This project serves as a valuable example of the practical applications of embedded systems and the possibilities they offer in optimizing various aspects of our daily lives.

The current design of the automated car park controller system, while effective, offers several avenues for future enhancements and modifications. One of the significant improvements could be the integration of the system with a mobile application. This application could provide users with real-time updates on the availability of parking spaces, enable them to reserve spaces, and even offer navigation assistance within the car park. This would significantly enhance user convenience and streamline the parking process.

Another potential upgrade could be the incorporation of image recognition technology. This technology could be used to identify vehicles as they enter and exit the car park, paving the way for advanced features such as automatic billing based on vehicle identification or tracking the duration of a vehicle's stay in the car park.

The system's accuracy and reliability could be further improved by employing advanced sensor technology. While the current system uses IR sensors to detect the presence of cars, the use of more sophisticated sensors, such as LiDAR or ultrasonic sensors, could enhance the system's car detection capabilities.

In terms of scalability, the current design is well-suited for small to medium-sized car parks. However, for larger or multi-story car parks, the system would need to be scaled up. This could involve using multiple Raspberry Pis or a more powerful controller, along with a more complex sensor network, to manage the increased demand.

Energy efficiency is another area where future iterations of the system could be improved. This could be achieved by using low-power components or implementing energy-saving modes during periods of low activity, thereby reducing the system's overall energy consumption.

Lastly, the system could benefit from the addition of security features. These could include CCTV integration for monitoring purposes or an alarm system to alert operators to unauthorized access. These features would not only enhance the security of the car park but also provide peace of mind to users.

These potential improvements and modifications not only serve to enhance the functionality of the car park controller system but also offer valuable opportunities for learning and applying advanced concepts in the field of embedded systems and software design.

## 6.0 References
## References
1. Aswini, R., & Kalaimathi, B. (2019). Automatic Car Parking System Using Raspberry-Pi with Cloud Storage Environment. Institute of Electrical and Electronics Engineers. [Link](https://ieeexplore.ieee.org/document/8878771)
2. Jabbar, W. A., & Wei, L. (2021). An IoT Raspberry Pi-based parking management system for smart campus. ScienceDirect. [Link](https://www.sciencedirect.com/science/article/abs/pii/S2542660521000317)
3. Atiqur, R. (2020). Automated smart car parking system using raspberry Pi 4 and iOS application. ResearchGate. [Link](https://www.researchgate.net/publication/347108063_Automated_smart_car_parking_system_using_raspberry_Pi_4_and_iOS_application)
4. Gavali, A. (n.d.). Smart Parking System Using the Raspberry Pi and Android. Mondi. [Link](https://www.mondi.az/uploads/catalogues/1534981934Smart%20Parking%20System%20Using-4539.pdf)
5. Baburaj, E. (2021). Smart Autonomous Car Parking For the Modern Vehicles. Institute of Physics. [Link](https://iopscience.iop.org › article › pdf)

## 7.0 Appendices

### 7.1 Demonstration Video
https://odysee.com/benc4513_b022010234_b022010228_b021910124_assignment

### 7.2 Source Code
