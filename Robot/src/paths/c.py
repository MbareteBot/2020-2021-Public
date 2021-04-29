#!/usr/bin/env pybricks-micropython

info = "c.py"

def color_code(Color):
    return Color.RED

def run(Robot):

    Robot.drive(90)
    Robot.turn(100)
    Robot.drive(18)
    Robot.square_line(forward=False)
    Robot.wait(500)
    Robot.turn(-92)

    Robot.Motors.left_action_motor.run_angle(800, 900, wait=False)
    Robot.drive(5)
    Robot.drive_to_line(10)
    Robot.wait(1000)
    Robot.Motors.left_action_motor.run_angle(-800, 400, wait=False)
    Robot.drive(25)
    Robot.drive_to_line(5)

    
    # black tire figure
    Robot.Motors.left_action_motor.run_angle(800, 220, wait=False)
    Robot.Motors.right_action_motor.run_angle(-600, 350)
    Robot.Motors.right_action_motor.run_angle(400, 350, wait=False)

    # boccia arm
    Robot.drive(-12)

    # weight machine
    Robot.Motors.left_action_motor.run_angle(-400, 320, wait=False)
    Robot.drive(35)
    Robot.wait(100)
    Robot.drive_to_line(10)
    Robot.Motors.left_action_motor.run_angle(800, 700)

    # going to base
    Robot.Motors.left_action_motor.run_angle(-700, 1200, wait=False)
    Robot.drive(-88, speed_kp=10)
    Robot.turn(-55, speed_kp=9)
    Robot.drive(-70, speed_kp=10)