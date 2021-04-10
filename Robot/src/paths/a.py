#!/usr/bin/env pybricks-micropython

info = "a.py"

from pybricks.tools import wait

def color_code(Color):
    return Color.GREEN

def run(Robot):
    # bench
    Robot.run(35)
    Robot.run(15, speed_kp=2.5)

    # slide
    Robot.Motors.left_action_motor.run_angle(800, 350)
    Robot.run(-48, speed_kp=4)
    wait(100)
    Robot.run(20)
    Robot.turn(60)
    Robot.run(63)
    Robot.Motors.right_action_motor.run_angle(800, 590)
    Robot.run(-8, speed_kp=2)
    Robot.Motors.right_action_motor.run_angle(-800, 630)

    # basket
    Robot.run(-20)
    Robot.run_to_line(15, Robot.ColorSensors.right_sensor, color="BLACK", speed_kp=1) 
    wait(100)
    Robot.run(-6)
    wait(100)
    Robot.turn(-65)
    wait(100)
    Robot.run(15)
    Robot.square_line()
    Robot.run(23)
    Robot.turn(-68)
    Robot.run_async(Robot.Motors.left_action_motor.run_angle, (800, 200))
    Robot.run(-12)
    Robot.Motors.left_action_motor.run_angle(-800, 550)
    Robot.run(16)
    Robot.Motors.left_action_motor.run_angle(800, 4150)
    Robot.run_async(Robot.Motors.left_action_motor.run_angle, (-800, 3000))
    wait(700)
    Robot.run(-18)
    Robot.turn(90)
    Robot.run(-80)