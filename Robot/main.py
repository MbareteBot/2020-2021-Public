#!/usr/bin/env pybricks-micropython

from src.setup import FLLRobot, Paths
from src.repl import motor_control


def read_attachment(Robot, paths):
    print("Waiting for attachment...")
    Robot.Ev3.light.on(Robot.Parameters.Color.RED)
    while True:
        for path in paths:
            if Robot.ColorSensors.front_sensor.color() == path.color_code(Robot.Parameters.Color):
                print("Attachment recognized:", path.info) 
                return path

def handle_input(Robot):
    pressed_buttons = Robot.Ev3.buttons.pressed()
 
    last_pressed_button = None
    if Robot.Parameters.Button.CENTER in pressed_buttons:
        read_attachment(Robot, Paths()).run(Robot)
        Robot.Ev3.light.on(Robot.Parameters.Color.YELLOW)
        last_pressed_button = Robot.Parameters.Button.CENTER

    elif Robot.Parameters.Button.UP in pressed_buttons:
        print("Calibrate Gyro")
        Robot.Gyro.calibrate()
        last_pressed_button = Robot.Parameters.Button.UP

    elif Robot.Parameters.Button.DOWN in pressed_buttons:
        print("Calibrate color sensors")
        Robot.ColorSensors.calibrate(Robot.ColorSensors.left_sensor)
        last_pressed_button = Robot.Parameters.Button.DOWN

    elif Robot.Parameters.Button.RIGHT in pressed_buttons:
        print("Motor control")
        motor_control(Robot)
        last_pressed_button = Robot.Parameters.Button.RIGHT

    while last_pressed_button in Robot.Ev3.buttons.pressed():
        pass

def main():
    print("----MAIN----")
    Robot = FLLRobot()
    PATHS = Paths()
    Robot.Ev3.light.on(Robot.Parameters.Color.YELLOW)
    while True:
        
        handle_input(Robot)
        
        if not Robot.active:
            Robot.active = True

if __name__ == "__main__":
    main()