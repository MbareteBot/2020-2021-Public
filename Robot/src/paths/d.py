#!/usr/bin/env pybricks-micropython

info = "d.py"

from pybricks.tools import wait

def color_code(Color):
    return Color.YELLOW

def run(Robot):
    Robot.drive(105)
    Robot.Motors.left_action_motor.run_angle(-800, 500)
    Robot.Motors.left_action_motor.run_angle(800, 500, wait=False)
    Robot.drive(-6)
    Robot.turn(90)
    Robot.drive(-45)
    Robot.drive_to_line(-10, sensor=Robot.ColorSensors.right_sensor)
    Robot.drive(31)
    Robot.Motors.right_action_motor.run_angle(-800, 1200, wait=False)
    Robot.wait(1000)
    Robot.drive(-9)
    Robot.Motors.right_action_motor.run_angle(800, 1200)
    # Robot.drive(-7)