#!/usr/bin/env pybricks-micropython

info = "b.py"

def color_code(Color):
    return Color.RED

def run(Robot):
    Robot.Motors.left_action_motor.run_angle(400, 400)
    Robot.run(10)