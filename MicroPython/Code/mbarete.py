#!/usr/bin/env pybricks-micropython


from control import RoboticTools
from ev3_device import MotorManager, ColorSensorManager, GyroSensorManager, Parameters




Device = RobotParameters()



class Robot:

    # This class provides features to control an ev3 robot.


    def __init__(self):

        # Control system related classes
        self.HeadingControl = PIDSystem()
        self.SpeedControl = PIDSystem()
        self.Tools = RoboticTools()



        # Ev3 control related classes
        self.Gyro = GyroSensorManager()
        self.Motor = MotorManager()
        self.ColorSensors = ColorSensorManager()



    def Turn(self, target_angle):

        self.Motor.reset(self.Motor.steering)

        self.SpeedControl.reset()


        Turning = True

        while Turning:

            error_value = target_angle - self.Gyro.getAngle()


            self.SpeedControl.execute(error_value, 0.5, 0.3, 0.1)


            self.left_steeringMotor.dc(self.SpeedControl.output)
            self.right_steeringMotor.dc(self.SpeedControl.output * -1)


            if  error_value > -0.1 and error_value < 0.1:

                Turning = False
                self.Motor.stop()
 
       




    def Straight(self, target_distance, target_orientation = 0, target_duty_limit = 20, use_gyro = True):


        self.SpeedControl.reset()
        self.HeadingControl.reset()
        self.Motor.reset(self.Motor.steering)


        target_distance = Tools.cmToDegrees(target_distance, 6.24)

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

                heading_error = self.Motor.right_steeringMotor.speed() - self.Motor.left_steeringMotor.speed()
                heading_kp = 0.2
                heading_ki = 0.001
                heading_kd = 0.01




            self.SpeedControl.execute(heading_error, heading_kp, heading_ki, heading_kd)

            self.HeadingControl.execute(speed_error, speed_kp, speed_ki, speed_kd)




            if target_distance > 0:

                if self.Motor.right_steeringMotor.angle() < target_distance / 2:

                    speed_error = target_distance - (target_distance - (self.Motor.right_steeringMotor.angle())) 

                else:

                    moved_enough = True

                    speed_error = target_distance - self.Motor.right_steeringMotor.angle()



                if self.SpeedControl.output < 8:
                    self.SpeedControl.output = 8 



            else:


                if self.Motor.right_steeringMotor.angle() < target_distance / 2:

                    speed_error = target_distance - (target_distance - (self.Motor.right_steeringMotor.angle())) 

                else:

                    moved_enough = True

                    speed_error = target_distance - self.Motor.right_steeringMotor.angle()



                if self.SpeedControl.output > -8:
                    self.SpeedControl.output = -8 






            # This check if the robot has acctually reached the target distance and stops the robot.
            if moved_enough:
                
                if speed_error < 1 and speed_error > -1:

                    Running = False

                    self.Motor.stop()





            if heading_error < 0:

                self.Motor.left_steeringMotor.dc(self.SpeedControl.output)
                self.Motor.right_steeringMotor.dc(self.SpeedControl.output + abs(self.HeadingControl.output))

            else:
                self.Motor.left_steeringMotor.dc(self.SpeedControl.output + abs(self.HeadingControl.output))
                self.Motor.right_steeringMotor.dc(self.SpeedControl.output)               





    def followLine(self, target_value, distance, sensor):

        self.HeadingControl.reset()
        self.Motor.reset(self.Motor.steering)

        FollowingLine = True

        Speed = 40

        while FollowingLine:


            error_value = int(self.ColorSensors.sensor.read("COL-REFLECT")[0]) - target_line_value


            self.HeadingControl.execute(error_value, 0.2, 0.2, 2)



            if error_value > 0:

                self.left_steeringMotor.dc(Speed)
                self.right_steeringMotor.dc(Speed + self.HeadingControl.output)

            else:
                self.left_steeringMotor.dc(Speed + abs(self.HeadingControl.output))
                self.right_steeringMotor.dc(Speed)               



            
