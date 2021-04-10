#!/usr/bin/env pybricks-micropython

from .robot import MbRobot, Port

def fll_robot():
    Robot = MbRobot()
    Robot.Motors.set_steering_motors(Port.A, Port.D, False)
    Robot.Motors.set_action_motors(Port.B, Port.C)
    Robot.Gyro.set_sensor(Port.S1, False)
    Robot.ColorSensors.set_sensors(Port.S3, Port.S2, Port.S4)
    return Robot

if __name__ == "__main__":
    fll_robot()
    