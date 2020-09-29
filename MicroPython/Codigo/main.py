#!/usr/bin/env pybricks-micropython

from mbarete import *


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
Robot = Robot()

Robot.setSteeringMotors(Port.A, Port.D, True)
Robot.setColorSensor(Port.S1, Port.S2, Port.S3)
Robot.setGyroSensor(Port.S4, True)

Robot.Straight(50, 0, 20)