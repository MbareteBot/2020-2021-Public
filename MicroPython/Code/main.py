#!/usr/bin/env pybricks-micropython

from mbarete import Robot


Robot = Robot()


# Initializing devices
Robot.Gyro.setSensor(Port.S4, True)

Robot.ColorSensor.leftSensor(Port.S1)

Robot.Motors.setMotors(Port.A, Port.D, True)




Robot.Turn(90) # Turn the robot by 90 degrees

Robot.Straight(30) # Move in a straight line for 30 cm


