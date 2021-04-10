#!/usr/bin/env pybricks-micropython

info = "a.py"

from pybricks.tools import wait

def color_code(Color):
    return Color.GREEN

def run(Robot):
    # bench
    Robot.run(35)
    Robot.run(15, speed_kp=2.5)
