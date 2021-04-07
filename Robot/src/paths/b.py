#!/usr/bin/env pybricks-micropython

info = "b.py"

def color_code(Color):
    return Color.RED

def run(Robot):
    print("1.")
    Robot.Motors.left_action_motor.run_angle(400, 400)
    print("2.")
    Robot.run(10)
    print("3.")
    print("ColoSensor:", Robot.ColorSensors.left_sensor.reflecion())