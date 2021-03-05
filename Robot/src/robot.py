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
    # Register devices for future control
    Robot.DeviceControl.load_devices()


    Robot.Ev3.light.on(Color.GREEN)
    # Main loop
    while True:

        if Button.DOWN in Robot.Ev3.buttons.pressed():
            Robot.Motors.left_steering_motor.run_time(500, 1000)
            Robot.straight(30)
            Robot.turn(90)
            Robot.run_to_line(Robot.ColorSensors.left_sensor, 30)
            break

        # Robot.active works as a main swith and if Robot.active = False then every previous "movement method" was skipped
        # so at this point setting Robot.active to True is gonna allow future "movement method" to happen again
        if not Robot.active:
            Robot.active = True 

if __name__ == "__main__":
    main()
