#!/usr/bin/env pybricks-micropython

from mbarete import Robot


Robot = Robot()


# Initializing devices
Robot.Gyro.setSensor(Port.S4, True)

Robot.ColorSensor.leftSensor(Port.S1)
Robot.ColorSensor.rightSensor(Port.S2)
Robot.ColorSensor.frontSensor(Port.S3)

Robot.Motor.setMotors(Port.A, Port.D, True)
Robot.Motor.setActionMotors(Port.B, Port.C)




Robot.Turn(90) # Turn the robot by 90 degrees

Robot.Straight(30) # Move in a straight line for 30 cm

Robot.Motors.run(Robot.Motors.left_steeringMotor, 300) # Rotate the left steering motor by 300 degrees

Robot.followLine(35, 100, Robot.ColorSensor.left_colorSensor) 

