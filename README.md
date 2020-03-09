## HomeMonitorSystem_BuildInstructions
*__This repository will lay out the steps necessary to build a home monitor system using a Pi 4.__*

## Table of Contents
* [Introduction](#Introduction)
* [Required sensors/components](#RequiredSensors/Components)
* [SHT31-D sensor](#SHT31-D)
* [HC-SR501 sensor](#HC-SR501)
* [MQ-2 sensor](#MQ-2)
* [Recomended PCB Design](#RecomendedPCBDesign)

# <a name="Introduction"> Introduction </a>

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
1. The third sensor is the MQ-2. This sensor is the gas sensor of choice. This is an analog device which can detect the precense of multiple gases in the air. As the PI reads degital signals we need the assistance of a suplementary component, an analog to digital converter. 
You can follow this link to a pdf page for further information.
* [MQ-2 PDF](https://www.pololu.com/file/0J309/MQ2.pdf)
1. The first suplementary component is the MCP3008 Analog to Digital conerter. This component will allow us to change the analoge output from the Mq-2 sensor to readable digital signals for the PI. 
You can follow this link to the AdaFruit page for further information.
* [AdaFruit-MCP3008](https://www.adafruit.com/product/856)
1. The second suplementary component is the ??????????????????????/ buzzer

# <a name="SHT31-D"> SHT31-D sensor </a>
To be able to use this sensor, you will need to install adafruit-circuitpython-sht31d libraries in your PI.
After this is done, you will need to use the Pi SCL to connect to the sensor SCL and the Pi SDA to connect to sensor SDA. Ground can be connected to any of the six ground pins. There will be a recomendation in the PCB section of this file. The power must be connected to one of the two 3V pins on the PI.

# <a name="HC-SR501"> HC-SR501 sensor </a>
 
# <a name="MQ-2"> MQ-2 sensor </a>
  
# <a name="RecomendedPCBDesign"> Recomended PCB Desing </a>
This is our design for the PCB, yours may differ, but the idea should be somewhat similar to this.
