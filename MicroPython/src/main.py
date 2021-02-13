#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port
from mbarete import Robot
from robotic_tools import RoboticTools
from menu import Screen, Menu

Robot = Robot()
Robot.Motors.set_steering_motors(Port.A, Port.D, True)
Robot.run_async(Robot.Motors.left_steering_motor.run_time, [500, 5000])
Robot.Motors.right_steering_motor.run_time(100, 2000)

# menu = Menu(["home", "chao"])
# menu.setup()

# Robot = Robot()
# Tools = RoboticTools()
# Tools.devices_analysis()
# Robot.Motors.set_steering_motors(Port.A, Port.D, True)
# Robot.Gyro.set_sensor(Port.S1)
# Robot.straight(30)  # Move in a straight line for 30 cm
# Rotate the left steering motor by 300 degrees
# Robot.Motors.run(Robot.Motors.left_steeringMotor, 300)
# Robot.followLine(35, 100, Robot.ColorSensor.leftSensor)
