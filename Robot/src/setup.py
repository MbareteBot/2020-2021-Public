from .paths import a, b, c, d
from .core.robot import MbRobot

def Paths():
    return (a, b, c, d)

def FLLRobot():
    Robot = MbRobot()
    Robot.Motors.set_steering_motors(Robot.Parameters.Port.A, Robot.Parameters.Port.D, False)
    Robot.Motors.set_action_motors(Robot.Parameters.Port.B, Robot.Parameters.Port.C)
    Robot.Gyro.set_sensor(Robot.Parameters.Port.S1, False)
    Robot.ColorSensors.set_sensors(Robot.Parameters.Port.S3, Robot.Parameters.Port.S2, Robot.Parameters.Port.S4)
    return Robot