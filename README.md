## HomeMonitorSystem_BuildInstructions
*__This repository will lay out the steps necessary to build a home monitor system using a Pi 4.__*

## Table of Contents
* [Introduction](#Introduction)
* [Functionality](#Functionality)
* [Cost](#Cost)
* [Time Required](#Time)
* [Required sensors/components](#RequiredSensors/Components)
* [Hardware Assembly Procedure](#hardwareAss)
* [Recomended PCB Design](#RecomendedPCBDesign)
* [PCB/Soldering](#PCB/Soldering)
* [Library Installation](#Libconfig)
* [Uploading Software to Raspberry Pi](#Software)
* [Unit Testing](#UnitTesting)
* [Android App Building Instructions](#AppBuildInstruct)
* [Database Setup/Structure](#Database-Setup)

# <a name="Introduction"> Introduction </a>

These build instructions will grant you the ability to reproduce the Smart-Home-Monitor system from scratch. It includes in detail the cost, connections, and code on how to get these three sensors to work in unison. 

# <a name="Functionality"> Functionality </a>
This is the functionality of our project.
![Diagram](https://github.com/NicolasRojas-CENG/HomeMonitorSystem_BuildInstructions/blob/master/Images/Functionality.png?raw=true)

# <a name="Cost"> Cost </a>

````
Product & Team Costs                                                   

Pi 4 2GB Starter Kit - 32GB                                $119.95|
Willwin 2pcs MQ-2 Sensor - Gas/Smoke Sensor                $12.10 |
Adafruit Sensirion SHT31-D - Temperature & Humidity Sensor $13.95 |
Aukru 3X HC-SR501 Human Sensor Module                      $10.99 |
MCP3008 - 8-Channel 10-Bit ADC                             $3.75  |
Beep Alarm Sensor                                          $7.99  |
Seloky 143pcs Female Pin Header Socket                     $21.99 |
120pcs Jumber Wires                                        $9.69  |
Camera Module 5MP REV 1.3                                  $13.99 |

Total Price W/Tax

$242.17

````
# <a name="Time"> Required Time(h) </a>

### Hardware 
### 35
### Software-APP 
### 60
### Database  
### 20 
### Total Time
### 115


# <a name="RequiredSensors/Components"> Required sensors/components </a>
1.  For this project, we will need a Raspberry Pi 4 Model B, three main sensors plus camera, two supplementary components, and an optional component plus some tools.
Our CPU of choice is the Raspberry Pi 4 Model B. This will give us the ability to work with python code. It will also give us access to both 3.3V and 5v, as some sensors require different voltages. 
You can follow this link to the  raspberrypi.org website for further information.
![PI](https://github.com/NicolasRojas-CENG/HomeMonitorSystem_BuildInstructions/blob/master/Images/RaspberryPi4.jpg?raw=true)
* [RaspBerry PI](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)
1.  The first of our sensors is the SHT31-D. This is the temperature/humidity sensor of choice. For this specific project, we will be collecting temperature readings in Celcius, but you can change this to Fahrenheit.
You can follow this link to the AdaFruit page for further information.
![Temp](https://github.com/NicolasRojas-CENG/HomeMonitorSystem_BuildInstructions/blob/master/Images/sht31-d.jpg?raw=true)
* [AdaFruit-SHT31-D](https://www.adafruit.com/product/2857)
1. the socond of our sensors is the HC-SR501. This is the motion sensor of choice. It is a simple sensor which only requires power and a output singnal.
You can follow this link to a pdf page for further information.
* [HC-SR501 PDF](https://www.mpja.com/download/31227sc.pdf)
1. The camera is used in conjuction with the HC-SR501 sensor. ##Andrew please add more!!!
1. The third sensor is the MQ-2. This sensor is the gas sensor of choice. This is an analog device which can detect the precense of multiple gases in the air. As the PI reads degital signals we need the assistance of a suplementary component, an analog to digital converter. 
You can follow this link to a pdf page for further information.
![Smoke](https://github.com/NicolasRojas-CENG/HomeMonitorSystem_BuildInstructions/blob/master/Images/mq2.png?raw=true)
* [MQ-2 PDF](https://www.pololu.com/file/0J309/MQ2.pdf)
1. The first suplementary component is the MCP3008 Analog to Digital conerter. This component will allow us to change the analoge output from the Mq-2 sensor to readable digital signals for the PI. 
You can follow this link to the AdaFruit page for further information.
* [AdaFruit-MCP3008](https://www.adafruit.com/product/856)
1. The second suplementary component is the SunFounder Alarm Sensor. This component will allow us to create sound whenever gas has been detected by the Mq-2 Gas sensor. You can follow this link for further information.

* [SunFounder DC 3.3-5V Low Level Trigger Magnetic Beep Alarm Sensor](https://www.amazon.ca/gp/product/B014KQLE8Q/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1)
1. The optional component is the LED, which you would need a resistor as well. This LED is used to indicate when a new Temp/Hum reading is gathered.

# <a name="hardwareAss"> Hardware Assembly Procedure </a>
### SHT31-D sensor
To be able to use this sensor, you will need to install adafruit-circuitpython-sht31d libraries in your PI.
````
sudo pip3 install adafruit-circuitpython-sht31d
````
If you want to get temperature in Celcius, use:
````
-45 + (175 * temp / 65535.0)
````
If you want to get temperature in Fahrenheit, use:
````
-49 + (315 * temp / 65535.0).
````
````
Connections:
SHT31-D VCC to Raspberry Pi 3V
SHT31-D SDA to Raspberry Pi SDA
SHT31-D SCL to Raspberry Pi SCL
SHT31-D GND to Raspberry Pi GND
````

### HC-SR501 sensor
The HC-SR501 sensor along with the raspberry pi in order to be able to detect motion. The sensor has 3 pins: VCC, GND, OUT. The operational voltage for the sensor is between 5 and 20 volts with an output voltage of 3.3V when motion is detected and 0V when no motion is detected. For more details about this sensor you can check out the link below.
https://www.mpja.com/download/31227sc.pdf

````
Connections:
HC-SR501 VCC to Raspberry Pi 5V
HC-SR501 OUT to Raspberry Pi GPIO6
HC-SR501 GND to Raspberry Pi GND
````

 
### MQ-2 sensor
The first thing about the sensor that you must understand is, if you want to get the numerical gas readings, you must use the analog output on the sensor. The issue is the PI does not take analog as an input, which means that you will need to purchase a mcp3008 ADC. This converter will allow the analog input to get converted to a digital output for the PI. To start to install the `Adafruit MCP3008 Python Library.`
The reference my team used to install the library is right here. [MCP3008 Setup](https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008). Next, you can use the pin connections below or the PCB example to build you connections. 

````
 MCP3008 SPI
 
MCP3008 VDD to Raspberry Pi 5V
MCP3008 VREF to Raspberry Pi 5V
MCP3008 AGND to Raspberry Pi GND
MCP3008 DGND to Raspberry Pi GND
MCP3008 CLK to Raspberry Pi SPI0_SCLK
MCP3008 DOUT to Raspberry Pi SPIO_MISO
MCP3008 DIN to Raspberry Pi SPIO_MOSI
MCP3008 CS/SHDN to Raspberry Pi SPIO_CEO_N

MQ-2 SPI

MQ-2 VDD to Raspberry Pi 5v
MQ-2 GND to Raspberry Pi GND
MQ-2 AOUT to MCP3008 CH0

BEEP ALARM SPI

ALARM VDD to Raspberry Pi 5v
ALARM GND to Raspberry Pi GND
ALARM AOUT to Raspberry Pi GPIO 5
````

## BreadBoard Image 

![Breadboard](https://github.com/NicolasRojas-CENG/HomeMonitorSystem_BuildInstructions/blob/master/Images/Breadboard.jpg)


  
# <a name="RecomendedPCBDesign"> Recommended PCB Design </a>
This is our design for the PCB, yours may differ, but the idea should be somewhat similar to this.
![BACKGROUND_ATTRIBUTE](https://github.com/NicolasRojas-CENG/HomeMonitorSystem_BuildInstructions/blob/master/Images/PCB.PNG?raw=true)


# <a name="PCB/Soldering"> PCB/Soldering </a>

This is how you would solder the PCB.
This is the top view of the PCB:
![BACKGROUND_ATTRIBUTE](https://github.com/NicolasRojas-CENG/HomeMonitorSystem_BuildInstructions/blob/master/Images/Top_View.jpg?raw=true)

This is the bottom view of the PCB:
![BottomView](https://github.com/NicolasRojas-CENG/HomeMonitorSystem_BuildInstructions/blob/master/Images/Bottom_View.jpg?raw=true)

![PCB&Sensors](https://github.com/NicolasRojas-CENG/HomeMonitorSystem_BuildInstructions/blob/master/Images/Complete.jpg?raw=true)

# <a name="Libconfig"> Library installation </a>
Before uploading and running the source code on the Raspberry Pi it is important to install all the proper libraries for the
sensors.
1. Make sure you have your Raspberry Pi's terminal open through GUI or SSH connection.
2. Run the command "sudo pip3 install adafruit-circuitpython-sht31d"
This will install the libraries needed to use the sht31d
3. Run the command sudo "raspi-config" navigate to the "Interface" tab using the up and down arrows, and click enter. Next navigate to the "camera" option and change the option to enable. Next restart the Raspberry Pi.
4. Install Pyrebase by issuing "pip install pyrebase" command
5. Install Adafruit MCP3008 Python Library for ADC.

# <a name="Software"> Uploading Software to Raspberry Pi </a>
Once all the Libraries are installed sucussfully, you can download the python file to transfer to the Raspberry Pi.
[Source Code](ADD LINK HERE)

If you're using a mac, you can use an application called "cyberduck" to transfer the code. 
1. Click open connection
2. Change the connection protocol to SSH File Transfer Protocol
3. For the server option type the Raspberry Pi's IP address
4. Enter the username and password for the raspberry pi you're connecting to.
5. Drag and drop the downloaded software file to the directory of your choice.

# <a name="UnitTesting"> Unit Testing </a>
![Output](https://github.com/NicolasRojas-CENG/HomeMonitorSystem_BuildInstructions/blob/master/Images/Sample_Output.PNG?raw=true)


# <a name="AppBuildInstruct"> Android App Building Instructions </a>

The software was build using Android Studio Version 3.5.1. It is also required to ensure the classpath is set to 'com.android.tools.build:gradle:3.4.1' in the build.gradle file. In the second build.gradle 2 of the following dependance must be added. implementation 'com.squareup.picasso:picasso:2.71828' & implementation 'com.github.PhilJay:MPAndroidChart:v3.+' although these are already setup when downloading our app from github you may need to update the depenancies to a newer version, or change the classpath to work with an older version of Android Studio. 
The minimum API is 21 and supports devices running Andrioid Lollipop supporting approximately 85% of devices. 
The smartHomeMonitoring system is currently not on the Android app store so the only way to run it is buy checking out a project from version control, selecting github and pasting the URL 'https://github.com/getLiauba/SmartHomeSoftwarePRoject.git'
Setting up the database as per the databse configuration instructions is require to get your google-services.json file which
must be included within the application folder. ApplicationName/app/google-services.json.

# <a name="Database-Setup"> Database Setup/Structure </a>


### Database Setup

The database being used to support our application is Firebase. Firebase is a multi tool application that allows the user to control,grow, and analyize a database for your app. 

##### Steps to setup Firebase.
The main Steps are:
- Step 1: Create a Firebase project.
- Step 2: Register your app with Firebase
- Step 3: Add a Firebase configuration file(google-services.json)
- Step 4: Add Firebase SDKs to your app

Google provides a very easy to follow and indepth setup for firebase. Use the link below to setup your app for firebase. When on the website, make sure you have all the prerequisites, and once that is complete, option 1 is the recommended option to follow.

[Firebase Setup](https://firebase.google.com/docs/android/setup)

To find out information about your project like the WebApiKey,google-services.json config file or the APP ID. Click on the **Settings button**, beside *Project Overview* and then click on **Project Settings**

![firebasesettings](https://github.com/NicolasRojas-CENG/HomeMonitorSystem_BuildInstructions/blob/master/Images/firebasesetting.png)

Once the setup is complete, go into your project, click database and create a database. The structure of the database should be created like the one below.  


### Database Structure 

![Database](https://github.com/NicolasRojas-CENG/HomeMonitorSystem_BuildInstructions/blob/master/Images/DatabaseStructure.png?raw=true)


The main branch we have is the 'Member' branch this is where all the registered users and their devices are kept. Inside this 'Member' branch there are unique user ID's which contains more sub-branches such as Devices and uploads, as well as key value pairs of dob, email, timestamp. The branch 'uploads' contains key value pairs of a unique lable with a link to an image the device as captured. Within the Devices branch contains more branches with the names of each device linked to the users account, within this branch there are Gas-Readings, Humidity-Readings, Tempature-Readings which are used to store the data from the hardware device.


### Storage Structure 

The Storage category on firebase is used to store images that are taken by the camera. We then grab this data from firebase/storage and transfer it to the app via pyrebase. Create a directory in storage similar to the one in the pictures below. 

images/*images will be saved in here*

![Storagepic1](https://github.com/NicolasRojas-CENG/HomeMonitorSystem_BuildInstructions/blob/master/Images/storage1.png)

![Storagepic2](https://github.com/NicolasRojas-CENG/HomeMonitorSystem_BuildInstructions/blob/master/Images/storage2.png)






