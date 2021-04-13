#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Color, Button

from src.core.setup import fll_robot
from src.paths import a, b, c 

paths = [a, b, c]


def wait_for_attachment(Robot):
    print("Waiting for attachment...")
    Robot.Ev3.screen.print("Waiting for attachment...")
    Robot.Ev3.light.on(Color.RED)
    while True:
        for path in paths:
            if Robot.ColorSensors.front_sensor.color() == path.color_code(Color):
                print("Attachment recognized:", path.info) 
                Robot.Ev3.screen.print(path.info)
                return path

def wait_for_button(Robot):
    print("Waiting for button...")
    Robot.Ev3.light.on(Color.YELLOW)
    Robot.Ev3.screen.print("Waiting for button...")
    while True:
        if Button.CENTER in Robot.Ev3.buttons.pressed():
            break
    print("Started")
    Robot.Ev3.light.on(Color.GREEN)

def main():
    Robot = fll_robot()
    wait_for_button(Robot)
    while True:
        path = wait_for_attachment(Robot)
        
        wait_for_button(Robot)

        path.run(Robot)

        if not Robot.active:
            Robot.active = True 

        wait_for_button(Robot)

if __name__ == "__main__":
    main()
