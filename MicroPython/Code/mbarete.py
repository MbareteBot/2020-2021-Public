#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Stop, Button
from pybricks.tools import wait, DataLog


# Local files
from control import PIDSystem, RoboticTools
from ev3_device import MotorManager, ColorSensorManager, GyroSensorManager




ev3 = EV3Brick()


Tools = RoboticTools()




# This class has built-in features to control an EV3 robot.

class Robot:

    def __init__(self):

        self.Control = PIDSystem()
        self.Gyro = GyroSensorManager()
        self.Motors = MotorManager()
        self.ColorSensors = ColorSensorManager()


        self.error_log = []
    
        self.speedMotorA = 0
        self.speedMotorD = 0



    def Turn(self, target_angle):

        self.Motors.reset()
        self.Gyro.reset()
        self.Control.reset()

        Turning = True

        while Turning:

            error_value = target_angle - self.Gyro.getAngle()

            self.Control.setPID(error_value, 0.5, 0.3, 0.1)

            self.left_steeringMotor.dc(self.Control.pid_output)
            self.right_steeringMotor.dc(self.Control.pid_output * -1)


            if  self.Control.error_value > -0.1 and self.Control.error_value < 0.1:

                Turning = False
                self.Motors.stop()
 
       




    def Straight(self, target_distance, target_orientation, target_duty_limit, use_gyro = True):


        # This funtionts allows the robot to accelerate and deccelrate as it gets towards a target distance.
        # And also control the robot heading.

        target_distance = Tools.cmToDegrees(target_distance, 6.24)

        self.Motors.reset()
        self.Gyro.reset()
        self.Control.reset()
                
        speed_kp = round(target_distance / ev3.battery.voltage() * 0.1, 3)
        speed_ki = 0.1
        speed_kd = 0.2

        Running = True


        moved_enough = False
        
        while Running:

  
            if use_gyro:

                heading_error = target_orientation - self.Gyro.getAngle()
                heading_kp = 4
                heading_ki = 0.1
                heading_kd = 0.1

            else:

                heading_error = self.Motors.right_steeringMotor.speed() - self.Motors.left_steeringMotor.speed()
                heading_kp = 0.2
                heading_ki = 0.001
                heading_kd = 0.01




            self.Control.setPID(heading_error, heading_kp, heading_ki, heading_kd, 0)

            self.Control.setPID(speed_error, speed_kp, speed_ki, speed_kd, 1)




            if target_distance > 0:

                if self.Motors.right_steeringMotor.angle() < target_distance / 2:

                    speed_error = target_distance - (target_distance - (self.Motors.right_steeringMotor.angle())) 

                else:

                    moved_enough = True

                    speed_error = target_distance - self.Motors.right_steeringMotor.angle()



                if self.Control.pid_output[1] < 8:
                    self.Control.pid_output[1] = 8 



            else:


                if self.Motors.right_steeringMotor.angle() < target_distance / 2:

                    speed_error = target_distance - (target_distance - (self.Motors.right_steeringMotor.angle())) 

                else:

                    moved_enough = True

                    speed_error = target_distance - self.Motors.right_steeringMotor.angle()



                if self.Control.pid_output[1] > -8:
                    self.Control.pid_output[1] = -8 






            # This check if the robot has acctually reached the target distance and stops the robot.
            if moved_enough:
                
                if speed_error < 1 and speed_error > -1:

                    Running = False

                    self.Motors.stop()






            # Here the robot implements the PID calculation to control the motors.

            if self.Control.error_value[0] < 0:

                self.Motors.left_steeringMotor.dc(self.Control.pid_output[1])
                self.Motors.right_steeringMotor.dc(self.Control.pid_output[1] + abs(self.Control.pid_output[0]))

            else:
                self.Motors.left_steeringMotor.dc(self.Control.pid_output[1] + abs(self.Control.pid_output[0]))
                self.Motors.right_steeringMotor.dc(self.Control.pid_output[1])               






    def followLine(self, target_line_value, distance, sensor):

        # This funtion simply follows a line

        self.Control.reset()
        self.Motors.reset()

        FollowingLine = True

        Speed = 40

        while FollowingLine:


            if sensor == "left":
                error_value = self.ColorSensors.leftSensor() - target_line_value

            else if sensor == "right":
                error_value = self.ColorSensors.rightSensor() - target_line_value

            else:

                raise Exception('Sensor should be declared as {} or {}'.format('"left"', '"right"'))



            self.Control.setPID(error_value, 0.2, 0.2, 2)



            if error_value > 0:

                self.left_steeringMotor.dc(Speed)
                self.right_steeringMotor.dc(Speed + self.Control.pid_output[0])

            else:
                self.left_steeringMotor.dc(Speed + abs(self.Control.pid_output[0]))
                self.right_steeringMotor.dc(Speed)               



            
