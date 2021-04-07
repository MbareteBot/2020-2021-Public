#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Button
from src.core.init import fll_robot


def motor_control(Robot):
    print("====Motor Control====")
    print("Press Ctrl+C to exit")
    speed = 80
    try:
        while True:
            pressed_buttons = Robot.Ev3.buttons.pressed()

            if Button.LEFT in pressed_buttons:
                Robot.Motors.left_action_motor.dc(speed)
            elif Button.RIGHT in pressed_buttons:
                Robot.Motors.right_action_motor.dc(speed)
            elif Button.DOWN in pressed_buttons:
                Robot.Motors.left_steering_motor.dc(speed)
            elif Button.UP in pressed_buttons:
                Robot.Motors.right_steering_motor.dc(speed)

            elif Button.CENTER in pressed_buttons:
                speed *= -1
                while Button.CENTER in Robot.Ev3.buttons.pressed():
                    pass

            else:
                Robot.Motors.left_action_motor.hold()
                Robot.Motors.right_action_motor.hold()
                Robot.Motors.left_steering_motor.hold()
                Robot.Motors.right_steering_motor.hold()
    except KeyboardInterrupt:
        print()

def main():
    print("======Repl======")
    print('Type "exit" plus Return to exit')
    print('Type "motor" plus Return to start Motor control')
    print("MbRobot is initalized as Robot")

    Robot = fll_robot()

    while True:
            command = input(">>> ")
            if command != "exit":
                if command == "motor":
                    motor_control(Robot)
                else:
                    try:
                        eval(command)
                    except KeyboardInterrupt as e:
                        print(repr(e))
                        Robot.Motors.left_steering_motor.hold()
                        Robot.Motors.right_steering_motor.hold()
                        Robot.Motors.left_action_motor.hold()
                        Robot.Motors.right_action_motor.hold()
                    except Exception as e:
                        if hasattr(e, "message"):
                            print(e.message)
                        else:
                            print(e)
        else:
            break


if __name__ == "__main__":
    main()