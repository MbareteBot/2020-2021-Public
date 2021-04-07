#!/usr/bin/env pybricks-micropython

info = "c.py"

def color_code(Color):
    return Color.BLUE

def run(Robot):
    Robot.Motors.left_action_motor.run_angle(400, 400)
    Robot.run(10)