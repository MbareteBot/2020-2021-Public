#!/usr/bin/env pybricks-micropython
from mbarete import *

Robot = Robot()
Robot.ColorSensors.set_left_sensor(Port.S2)
print("Sensor", Robot.ColorSensors.left_sensor)
print(Robot.ColorSensors.left_sensor.port)
# print(Robot.Gyro.sensor)
# Robot.Motors.set_steering_motors(Port.A, Port.C)
# Robot.DeviceControl.load_devices()
# Robot.DeviceControl.is_port_in_use(Port.B)
# print(Robot.Motors.left_steering_motor.port)
# while True:
#     Robot.Motors.left_steering_motor.dc(50)
#     print()
# Robot.Motors.right_action_motor.run_time(800, 5000)
# Robot.Motors.run(Robot.Motors.left_action_motor, 500)
# menu = Menu(["home", "chao"])
# menu.setup()

# Robot = Robot()
# Tools = RoboticTools()
# Tools.devices_analysis()
# Robot.Motors.set_steering_motors(Port.A, Port.D, True)
# Robot.Gyro.set_sensor(Port.S1)
# Robot.straight(30)  # Move in a straight line for 30 cm
# Rotate the left steering motor by 300 degrees
# Robot.Motors.run(Robot.Motors.left_steeringMotor, 300)
# Robot.followLine(35, 100, Robot.ColorSensor.leftSensor)
