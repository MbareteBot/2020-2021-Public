#!/usr/bin/env pybricks-micropython

info = "b.py"

def color_code(Color):
    return Color.BLUE

def run(Robot):

    # step counter
    Robot.drive(78)
    Robot.drive_to_line(10, sensor=Robot.ColorSensors.right_sensor)
    Robot.drive(33, orientation=-1, speed_kp=1.6)
    Robot.Motors.right_action_motor.run_angle(-800, 1300, wait=False)
    Robot.wait(1000)
    Robot.drive(20, orientation=-2)
    Robot.Motors.right_action_motor.run_angle(800, 400, wait=False)
    Robot.drive_to_line(28)

    # row machine
    Robot.Motors.left_action_motor.run_angle(500, 200, wait=False)
    Robot.wait(200)
    Robot.drive(-3)
    Robot.drive(-15)
    Robot.Motors.left_action_motor.run_angle(-500, 250)

    # treadmill
    Robot.drive_to_line(18)
    Robot.turn(-90)
    Robot.drive(4)
    Robot.turn(-90)
    Robot.drive(-25, speed_kp=2)
    Robot.Motors.left_steering_motor.run_angle(-800, 1600)

    # blue tire
    Robot.drive(25)
    Robot.turn(85)
    Robot.square_line(False)
    Robot.drive(10)
    Robot.turn(91)
    Robot.drive(-35)
    Robot.Motors.left_action_motor.run_angle(800, 190)
    Robot.drive(-16)
    Robot.Motors.left_action_motor.run_angle(-800, 190)
    Robot.drive(-115)

    # Robot.Motors.left_action_motor.run_angle(800, 400, wait=False)
    # Robot.drive(-20)
    # Robot.drive_to_line(-10)
    # Robot.drive(-7)
    # Robot.Motors.left_action_motor.run_angle(-800, 300, wait=False)
    # Robot.drive(-5)
    # Robot.drive(-130)