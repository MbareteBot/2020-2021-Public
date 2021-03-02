#!/usr/bin/env pybricks-micropython

def main():
    # ---EXAMPLE CODE---
    from mbarete import Robot, Port, wait
    from pybricks.parameters import Color, Button
    Robot = Robot()
    Robot.Ev3.screen.clear()
    Robot.Ev3.light.on(Color.RED)
    # Initialize devices
    Robot.Gyro.set_sensor(Port.S1, False)
    Robot.ColorSensors.set_front_sensor(Port.S2)
    Robot.ColorSensors.set_left_sensor(Port.S3)
    Robot.ColorSensors.set_right_sensor(Port.S4)
    Robot.Motors.set_steering_motors(Port.A, Port.D, False)
    
    # Register all devices connected for future control
    Robot.DeviceControl.load_devices()

    Robot.Ev3.light.on(Color.GREEN)
    # Main loop
    while True:
        if Button.CENTER in Robot.Ev3.buttons.pressed():
            Robot.straight(30)
            break


if __name__ == "__main__":
    main()
