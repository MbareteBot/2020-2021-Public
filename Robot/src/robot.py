#!/usr/bin/env pybricks-micropython

def main():
    # from pybricks.ev3devices import Motor
    # from pybricks.parameters import Port, Direction
    # m = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    # m.run_time(500, 2000)
    # print(m)

    from mbarete import Robot, Port, wait
    from pybricks.parameters import Color, Button
    Robot = Robot()
    Robot.Ev3.screen.clear()
    Robot.Ev3.light.on(Color.RED)
    Robot.Motors.set_steering_motors(Port.A, Port.D, False)
    Robot.Gyro.set_sensor(Port.S1, False)
    # Initialize devices

    # print("ColorSensor:", Robot.ColorSensors.left_sensor.reflection())
    # print("Gyro1:", Robot.Gyro.angle())
    # Robot.Gyro.reset()
    # wait(2000)
    # Robot.Gyro.calibrate()
    # print("Gyro2:", Robot.Gyro.angle())

    Robot.ColorSensors.set_front_sensor(Port.S2)
    Robot.ColorSensors.set_left_sensor(Port.S3)
    Robot.ColorSensors.set_right_sensor(Port.S4)

    # Register all devices connected for future control
    # Robot.DeviceControl.load_devices()

    # Robot.Ev3.light.on(Color.GREEN)
    # # Main loop
    while True:
        if Button.CENTER in Robot.Ev3.buttons.pressed():
            # Move the robot
            Robot.ColorSensors.calibrate()
            break


if __name__ == "__main__":
    main()
