#!/usr/bin/env pybricks-micropython

from mbarete import *

# This is an example code

Robot = Robot()

Robot.Gyro.setSensor(Port.S4, True)

Robot.ColorSensor.setLeftSensor(Port.S1)

Robot.Motors.setMotors(Port.A, Port.D, True)



Robot.Turn(-90)