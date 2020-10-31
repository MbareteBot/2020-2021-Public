#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port
from mbarete import Robot


Robot = Robot()


# Initializing devices
Robot.Gyro.setSensor(Port.S4, True)
Robot.Motor.setSteeringMotors(Port.A, Port.D, True)
Robot.Motor.setActionMotors(Port.B, Port.C)
Robot.ColorSensor.leftSensor(Port.S1)

Robot.Motor.run(Robot.Motor.left_steeringMotor, 300)


Robot.Straight(30) # Move in a straight line for 30 cm

# Robot.Motors.run(Robot.Motors.left_steeringMotor, 300) # Rotate the left steering motor by 300 degrees

# Robot.followLine(35, 100, Robot.ColorSensor.leftSensor) 

