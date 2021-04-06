#!/usr/bin/env pybricks-micropython

from core.mbarete import MbRobot, Port

def setup():
    Robot = MbRobot()
    Robot.Motors.set_steering_motors(Port.A, Port.D, False)
    Robot.Motors.set_action_motors(Port.B, Port.C)
    Robot.Gyro.set_sensor(Port.S1, False)
    Robot.ColorSensors.set_left_sensor(Port.S3)
    Robot.ColorSensors.set_right_sensor(Port.S2)
    return Robot

def test():
    Robot = setup()
    print("Testing Motors")
    Robot.Motors.left_steering_motor.angle()
    Robot.Motors.left_steering_motor.speed()
    
if __name__ == "__main__":
    setup()