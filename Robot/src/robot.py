#!/usr/bin/env pybricks-micropython

def main():
    from mbarete import Robot, Port
    from pybricks.parameters import Color, Button
    Robot = Robot()
    Robot.Ev3.screen.clear()
    Robot.Ev3.light.on(Color.RED)
    # Initialize devices
    Robot.Motors.set_steering_motors(Port.A, Port.D, False)
    Robot.Motors.set_action_motors(Port.B, Port.C)
    Robot.Gyro.set_sensor(Port.S1, False)
    Robot.ColorSensors.set_front_sensor(Port.S2)
    Robot.ColorSensors.set_left_sensor(Port.S3)
    Robot.ColorSensors.set_right_sensor(Port.S4)

    # Register all devices connected for future control
    Robot.DeviceControl.load_devices()

    Robot.Motors.left_steering_motor.run_time(400, 5000)

    Robot.Ev3.light.on(Color.GREEN)
    while True:
        if Button.CENTER in Robot.Ev3.buttons.pressed():
            # Move the robot
            Robot.straight(10)
            Robot.turn(90)
            break
