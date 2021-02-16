#!/usr/bin/env pybricks-micropython
from mbarete import *


# Example
Robot = Robot()
Robot.set_steering_motors(Port.A, Port.D, False)
Robot.straight(30)
Robot.ColorSensors.set_left_sensor(Port.S2)
wait(3000)
print(Robot.ColorSensors.left_sensor.port)
print(Robot.ColorSensors.left_sensor.reflection())
