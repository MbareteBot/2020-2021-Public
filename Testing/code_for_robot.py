#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

motor = Motor(Port.A)
while True:
    command = input("$: ")
    if command == "w":
        motor.run_time(100, 500)
