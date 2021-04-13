from .core.setup import fll_robot

Robot = fll_robot()

def test():
    Robot.Motors
    Robot.Motors.left_steering_motor
    Robot.Motors.right_steering_motor
    Robot.Motors.left_action_motor
    Robot.Motors.right_action_motor
    Robot.Motors.left_steering_motor.run(1)
    Robot.Motors.left_steering_motor.dc(1)
    Robot.Motors.left_steering_motor.brake()
    Robot.Motors.left_steering_motor.run_angle(1,1)
    Robot.Motors.left_steering_motor.run_time(0,0)
    Robot.Motors.left_steering_motor.reset_angle()
    Robot.Motors.left_steering_motor.is_stalled()

    Robot.Gyro
    Robot.Gyro.angle()
    Robot.Gyro.reset()
    Robot.Gyro.calibrate()

    Robot.ColorSensors
    Robot.ColorSensors.left_sensor.reflection()
    Robot.ColorSensors.right_sensor.reflection()
 
    print("[ TEST ] All test finished succesfully")
    return True
