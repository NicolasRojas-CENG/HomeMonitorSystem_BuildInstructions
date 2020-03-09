## HomeMonitorSystem_BuildInstructions
*__This repository will lay out the steps necessary to build a home monitor system using a Pi 4.__*

## Table of Contents
* [Introduction](#Introduction)
* [Required sensors/components](#RequiredSensors/Components)
* [Cost](#Cost)
* [SHT31-D sensor](#SHT31-D)
* [HC-SR501 sensor](#HC-SR501)
* [MQ-2 sensor](#MQ-2)
* [Recomended PCB Design](#RecomendedPCBDesign)
* [PCB/Soldering](#PCB/Soldering)
* [Library Installation](#Libconfig)
* [Uploading Software to Raspberry Pi](#Software)
* [Power Up](#PowerUp)
* [Unit Testing](#UnitTesting)

# <a name="Introduction"> Introduction </a>

These build instructions will grant you the ability to reproduce the Smart-Home-Monitor system from scratch. It includes in detail the cost, connections, and code on how to get these three sensors to work in unison. 

# <a name="RequiredSensors/Components"> Required sensors/components </a>
1.  For this project, we will need a Raspberry Pi 4 Model B, three main sensors plus camera, two supplementary components, and an optional component plus some tools.
Our CPU of choice is the Raspberry Pi 4 Model B. This will give us the ability to work with python code. It will also give us access to both 3.3V and 5v, as some sensors require different voltages. 
You can follow this link to the  raspberrypi.org website for further information.
* [RaspBerry PI](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)
1.  The first of our sensors is the SHT31-D. This is the temperature/humidity sensor of choice. For this specific project, we will be collecting temperature readings in Celcius, but you can change this to Fahrenheit.
You can follow this link to the AdaFruit page for further information.
* [AdaFruit-SHT31-D](https://www.adafruit.com/product/2857)
1. the socond of our sensors is the HC-SR501. This is the motion sensor of choice. It is a simple sensor which only requires power and a output singnal.
You can follow this link to a pdf page for further information.
* [HC-SR501 PDF](https://www.mpja.com/download/31227sc.pdf)
1. The camera is used in conjuction with the HC-SR501 sensor. ##Andrew please add more!!!
1. The third sensor is the MQ-2. This sensor is the gas sensor of choice. This is an analog device which can detect the precense of multiple gases in the air. As the PI reads degital signals we need the assistance of a suplementary component, an analog to digital converter. 
You can follow this link to a pdf page for further information.
* [MQ-2 PDF](https://www.pololu.com/file/0J309/MQ2.pdf)
1. The first suplementary component is the MCP3008 Analog to Digital conerter. This component will allow us to change the analoge output from the Mq-2 sensor to readable digital signals for the PI. 
You can follow this link to the AdaFruit page for further information.
* [AdaFruit-MCP3008](https://www.adafruit.com/product/856)
1. The second suplementary component is the SunFounder Alarm Sensor. This component will allow us to create sound whenever gas has been detected by the Mq-2 Gas sensor. You can follow this link for further information.

* [SunFounder DC 3.3-5V Low Level Trigger Magnetic Beep Alarm Sensor](https://www.amazon.ca/gp/product/B014KQLE8Q/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1)
1. The optional component is the LED, which you would need a resistor as well. This LED is used to indicate when a new Temp/Hum reading is gathered.
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

$316.86

````

# <a name="SHT31-D"> SHT31-D sensor </a>
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

# <a name="HC-SR501"> HC-SR501 sensor </a>
The HC-SR501 sensor along with the raspberry pi in order to be able to detect motion. The sensor has 3 pins: VCC, GND, OUT. The operational voltage for the sensor is between 5 and 20 volts with an output voltage of 3.3V when motion is detected and 0V when no motion is detected. For more details about this sensor you can check out the link below.

https://www.mpja.com/download/31227sc.pdf

 
# <a name="MQ-2"> MQ-2 sensor </a>
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

  
# <a name="RecomendedPCBDesign"> Recommended PCB Design </a>
This is our design for the PCB, yours may differ, but the idea should be somewhat similar to this.
![BACKGROUND_ATTRIBUTE](https://github.com/NicolasRojas-CENG/HomeMonitorSystem_BuildInstructions/blob/master/Images/PCB.PNG?raw=true)


# <a name="PCB/Soldering"> PCB/Soldering </a>


# <a name="Libconfig"> Library installation </a>


# <a name="Software"> Uploading Software to Raspberry Pi </a>


# <a name="PowerUp"> Power Up </a>


# <a name="UnitTesting"> Unit Testing </a>

















