#!/usr/bin/env pybricks-micropython

from init_robot import setup

print("Repl")
print("===============================")
print('Type "exit" plus Return to exit')
print("MbRobot is initalized as Robot")

Robot = setup()

while True:
    command = input(">>> ")
    if command != "exit":
        try:
            eval(command)
        except Exception as e:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)
        except KeyboardInterrupt as e:
            print(repr(e))
            Robot.Motors.left_steering_motor.hold()
            Robot.Motors.right_steering_motor.hold()
            Robot.Motors.left_action_motor.hold()
            Robot.Motors.right_action_motor.hold()
    else:
        break