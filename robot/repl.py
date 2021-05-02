#!/usr/bin/env pybricks-micropython

from src.setup import FLLRobot
from src.test import test

def motor_control(Robot):
    print("====Motor Control====")
    print("Press Ctrl+C to exit")
    speed = 80
    try:
        while True:
            pressed_buttons = Robot.Ev3.buttons.pressed()

            if Robot.Parameters.Button.LEFT in pressed_buttons:
                Robot.Motors.left_action_motor.dc(speed)
            elif Robot.Parameters.Button.RIGHT in pressed_buttons:
                Robot.Motors.right_action_motor.dc(speed)
            elif Robot.Parameters.Button.DOWN in pressed_buttons:
                Robot.Motors.left_steering_motor.dc(speed)
            elif Robot.Parameters.Button.UP in pressed_buttons:
                if Robot.Parameters.Button.DOWN in pressed_buttons:
                    Robot.Motors.left_action_motor.hold()
                    Robot.Motors.right_action_motor.hold()
                    Robot.Motors.left_steering_motor.hold()
                    Robot.Motors.right_steering_motor.hold()
                    break
                Robot.Motors.right_steering_motor.dc(speed)
            elif Robot.Parameters.Button.CENTER in pressed_buttons:
                speed *= -1
                while Robot.Parameters.Button.CENTER in Robot.Ev3.buttons.pressed():
                    pass
            else:
                Robot.Motors.left_action_motor.hold()
                Robot.Motors.right_action_motor.hold()
                Robot.Motors.left_steering_motor.hold()
                Robot.Motors.right_steering_motor.hold()

    except KeyboardInterrupt:
        print()

if __name__ == "__main__":

    print("======Repl======")
    print('Type "exit" plus Return to exit')
    print('Type "motor" plus Return to start Motor control')
    print("MbRobot is initalized as Robot")

    Robot = FLLRobot()
    print("robot motors:", Robot.Motors)
    while True:
            try:
                command = input(">>> ")
            except KeyboardInterrupt:
                print("EXIT")
                break
            if command == "exit":
                break
            elif command == "motor":
                motor_control(Robot)
            elif command == "test":
                test()
            else:
                try:
                    eval(command)
                except Exception as e:
                    if hasattr(e, "message"):
                        print(e.message)
                    else:
                        print(e)
                except KeyboardInterrupt as e:
                    print(repr(e))
                    Robot.Motors.left_steering_motor.hold()
                    Robot.Motors.right_steering_motor.hold()
                    Robot.Motors.left_action_motor.hold()
                    Robot.Motors.right_action_motor.hold()

