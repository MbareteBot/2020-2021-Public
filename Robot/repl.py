#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Button, Port
from src.core.setup import fll_robot
from src.test import test

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


print("======Repl======")
print('Type "exit" plus Return to exit')
print('Type "motor" plus Return to start Motor control')
print("MbRobot is initalized as Robot")

Robot = fll_robot()

while True:
        command = input(">>> ")
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
