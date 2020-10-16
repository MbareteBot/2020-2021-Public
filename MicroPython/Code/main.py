#!/usr/bin/env pybricks-micropython

from mbarete import *

# This is an example code

Robot = Robot()

Robot.Gyro.setSensor(Port.S4, True)

Robot.ColorSensor.leftSensor(Port.S1)




Robot.Motors.setMotors(Port.A, Port.D, True)



Robot.Turn(-90) # Turn the robot by 90 degrees

Robot.Straight(30,0,20) # Move in a straight line for 30 cm, with a 0 angle orientation and with a duty limit of 20%