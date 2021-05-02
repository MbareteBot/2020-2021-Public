#!/usr/bin/env pybricks-micropython

def read_attachment(Robot):
    print("Waiting for attachment...")
    Robot.Ev3.light.on(Color.RED)
    while True:
        for path in paths:
            if Robot.ColorSensors.front_sensor.color() == path.color_code(Color):
                print("Attachment recognized:", path.info) 
                return path

def wait_for_button(Robot):
    print("Waiting for button...")
    Robot.Ev3.light.on(Color.YELLOW)
    while True:
        if Button.CENTER in Robot.Ev3.buttons.pressed():
            break
    print("Started")
    Robot.Ev3.light.on(Color.GREEN)