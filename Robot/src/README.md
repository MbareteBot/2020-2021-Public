# Hi there!!


This folder includes all the code we use for the current FLL Replay 2020-2021 Season.
The code is divided into diferent classes, each one is reponsible for a different aspect of our robot.

### Files and classes description:
- control.py:
  - PIDSystem: Provides with functions to run a PID calculation.
  - OdometrySystem: Allows the use of sensors to estimate change in position over time. 
  
- ev3_device.py:
  - MotorManager: Facilitates control of ev3 Motors.
  - ColorSensorManager: Facilitates control of ev3 color sensors.
  - GyroSensorManager: Facilitates control of an ev3 gyro sensor.
 
- robotic_tools:
  - RoboticTools: Minimal mathematical "tools" that might be useful for robotics.
 
- mbarete.py:
  - Robot: Allows general control of ev3 robot.
  
- main.py: Main file that gets executed on the ev3 robot and its the combination of all 3 past files and classes.


### Set Up intruccions:
#### Visual Studio Code
1. Clone this repository.
2. Install and activate the LEGO Education EV3 extension or make your own ssh connection with the robot.
3. Run the main.py file and start coding!.




