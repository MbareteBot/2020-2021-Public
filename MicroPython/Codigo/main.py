#!/usr/bin/env pybricks-micropython

from mbarete import *

Robot = Robot()


Robot.setSteeringMotors(Port.A, Port.D)

Robot.followLine(Robot.left_colorSensor, 0, Port.S4)

