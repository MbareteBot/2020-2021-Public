#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Color

from setup_autonomous import *
from init_robot import setup

def main():
    
    Robot = setup()

    Robot.Ev3.light.on(Color.GREEN)
    # Main loop
    while True:
        for run in runs:
            if Robot.ColorSensor.front_sensor.color() == run.color_code(Color):
                Robot.lights.on(Color.YELLOW)
                run.main(Robot)

            if not Robot.active:
                Robot.active = True 


if __name__ == "__main__":
    main()
