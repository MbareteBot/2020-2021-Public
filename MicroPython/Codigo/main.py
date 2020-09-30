#!/usr/bin/env pybricks-micropython

from mbarete import *


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
Robot = Robot()

Robot.Gyro.setSensor(Port.S4, True)

Robot.ColorSensor.setLeftSensor(Port.S1)

Robot.Motors.setMotors(Port.A, Port.D, True)


#Robot.Straight(50, 0, 20)
Robot.Turn(-90)