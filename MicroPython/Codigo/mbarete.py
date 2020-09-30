#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button
from pybricks.tools import wait, DataLog

from pybricks.iodevices import Ev3devSensor

from control import PIDSystem, RoboticTools
from ev3_device import MotorManager, ColorSensorManager, GyroSensorManager

import csv



ev3 = EV3Brick()


#ReadSensorData = open('SensorData.txt', 'r')

SensorValues = [] 

Control = PIDSystem()

Tools = RoboticTools()





class Robot:

    def __init__(self):

        self.Gyro = GyroSensorManager()
        self.Motors = MotorManager()
        self.ColorSensor = ColorSensorManager()


        self.error_log = []
    
        self.speedMotorA = 0
        self.speedMotorD = 0


    def LineSquaring(self):

        NotSkip = True
        SpeedMotorA = 300
        SpeedMotorD = 300

        Fase2Degrees = -150
        Running = True

        light_data = open("SensorData.txt","r")
        sensor_register = light_data.readlines()
        White = int(sensor_register[0])
        print("Color>",White)
        Fase = 0

        while Running:

            Checking = True
            NotSkip = True
            self.left_steeringMotor.run(SpeedMotorA)
            self.right_steeringMotor.run(SpeedMotorD)

            if self.left_colorSensor.reflection() >= White and NotSkip:
                self.left_steeringMotor.hold()
                while Checking:
                    self.right_steeringMotor.run(SpeedMotorD)
                    if self.right_colorSensor.reflection() > White:
                        self.right_steeringMotor.hold()

                        Fase += 1

                        if Fase == 2:
                            Running = False
                        else:
                            self.left_steeringMotor.run_angle(Fase2Degrees, 100, wait = False)
                            self.right_steeringMotor.run_angle(Fase2Degrees, 100)
                            ev3.speaker.beep()                        
                            ev3.speaker.beep()

                        NotSkip = False
                        Checking = False

                        SpeedMotorA = 300
                        SpeedMotorD = 300
                            

            elif self.right_colorSensor.reflection() >= White and NotSkip:
                self.right_steeringMotor.hold()

                while Checking:
                    self.left_steeringMotor.run(SpeedMotorA)
                    if self.left_colorSensor.reflection() > White:
                        self.left_steeringMotor.hold()

                        Fase += 1

                        if Fase == 2:
                            Running = False
                        else:
                            self.left_steeringMotor.run_angle(Fase2Degrees, 100, wait = False)
                            self.right_steeringMotor.run_angle(Fase2Degrees, 100)
                            ev3.speaker.beep()
                        
                        NotSkip = False
    
                        Checking = False
                        SpeedMotorA = 300
                        SpeedMotorD = 300

        self.left_steeringMotor.hold()
        self.right_steeringMotor.hold()

        wait(300)



    def Turn(self, target_angle):

        self.left_steeringMotor.reset_angle(0)
        self.right_steeringMotor.reset_angle(0)

        Control.reset()


        Turning = True
        while Turning:

            error_value = target_angle - Gyro.getAngle()

            Control.setPID(error_value, 0.5, 0.3, 0.1)

            self.left_steeringMotor.dc(Control.pid_output)
            self.right_steeringMotor.dc(Control.pid_output * -1)


            if  Control.error_value > -0.1 and Control.error_value < 0.1:
                Turning = False
                self.speedMotorA = 0
                self.speedMotorD = 0
            

        self.right_steeringMotor.hold()
        self.left_steeringMotor.hold()
        wait(100)
        #self.updatePos()
        print("\n---Turn---")
        print("\nTarget:",target_angle)
        print("Gyro:", self.gyroSensor.read("GYRO-ANG")[0])



    def Straight(self, target_distance, target_orientation, target_duty_limit, use_gyro = True):

        target_distance = Tools.cmToDegrees(target_distance, 6.24)

        Motors.reset()
        Gyro.reset()
        Control.reset()
                
        speed_kp = round(target_distance/ev3.battery.voltage()*0.1, 3)
        speed_ki = 0.1
        speed_kd = 0.2
        speed_error = 0
        speed_integral = 0
        speed_derivative = 0
        speed_last_error = 0
        speed_output = 0
        max_integral_value = 120


        Running = True
        
        while Running:

  
            if use_gyro:

                error_value = target_orientation - Gyro.getAngle()
                kp_value = 4
                ki_value = 0.1
                kd_value = 0.1
        
            else:

                error_value = Motors.right_steeringMotor.speed() - Motors.left_steeringMotor.speed()
                kp_value = 0.2
                ki_value = 0.001
                kd_value = 0.01


            Control.setPID(error_value, kp_value, ki_value, kd_value)






            speed_integral += speed_error
            speed_derivative = speed_error - speed_last_error
            speed_output = (speed_error * speed_kp) + (speed_integral * speed_ki) + (speed_derivative * speed_kd)

            if target_distance > 0:

                if Motors.right_steeringMotor.angle() < target_distance / 2:

                    speed_error = target_distance - (target_distance - (Motors.right_steeringMotor.angle())) 

                else:
                    speed_error = target_distance - Motors.right_steeringMotor.angle()


                    if speed_error < 1 and speed_error > -1:
                        Running = False


                if speed_output < 8:
                    speed_output = 8 


            else:

                speed_error = target_distance - Motors.right_steeringMotor.angle()

                if speed_output > -8:
                    speed_output = -8




            if speed_integral > max_integral_value:
                speed_integral = max_integral_value

            elif speed_integral < -max_integral_value:
                speed_integral = -max_integral_value


            print(Control.error_value)

            if Control.error_value < 0:

                Motors.left_steeringMotor.dc(speed_output)
                Motors.right_steeringMotor.dc(speed_output + abs(Control.pid_output))

            else:
                Motors.left_steeringMotor.dc(speed_output + abs(Control.pid_output))
                Motors.right_steeringMotor.dc(speed_output)               





                                                        

            # if target_distance < 0:

            #     if self.right_steeringMotor.angle() > target_distance/2:
            #         speed_error = target_distance - (target_distance - (self.right_steeringMotor.angle()))
            #     else:
            #         speed_error = target_distance - (self.right_steeringMotor.angle())

            #     if speed_integral < -120:
            #         speed_integral = -120


            #     if -self.MotorsAverageDegrees <= (target_distance * Correction_target_distance)/ 100:
            #         Running = False


            #     if self.MotorsAverageSpeed < -100 and MovedEnough == False:
            #         MovedEnough = True

            #     if self.MotorsAverageSpeed > -abs(target_duty_limit) and MovedEnough:
            #         Running = False
            #         StopDiagnostic = "Got Stalled" 

            #     if speed_output > -8:
            #         speed_output = -10               

                
            # else:

            #     if self.right_steeringMotor.angle() < target_distance/2:
            #         speed_error = target_distance - (target_distance - (self.right_steeringMotor.angle()))
            #     else:
            #         speed_error = target_distance - (self.right_steeringMotor.angle())

            #     if speed_integral > 120:
            #         speed_integral = 120


            #     if self.MotorsAverageDegrees >= (target_distance * Correction_target_distance)/ 100:
            #         Running = False


            #     if self.MotorsAverageSpeed > 100 and MovedEnough == False:
            #         MovedEnough = True

            #     if self.MotorsAverageSpeed < target_duty_limit and MovedEnough:
            #         Running = False
            #         StopDiagnostic = "Got Stalled" 

            #     if speed_output < 8:
            #         speed_output = 10




        Motors.stop()


    def LightSensorCalibration(self):

        WhiteColorValue = 70
        BlackColorValue = 15
        Speed = 200
        Running = True
        ev3.speaker.beep()

        while Running:
        
            if any(ev3.buttons.pressed()):

                while Running:

                    self.left_steeringMotor.run(Speed)
                    self.right_steeringMotor.run(Speed)

                    if self.left_colorSensor.reflection() > WhiteColorValue:
                        self.left_steeringMotor.hold()
                        while Running:
                            self.right_steeringMotor.run(Speed)
                            if self.right_colorSensor.reflection() > WhiteColorValue:
                                self.right_steeringMotor.hold()
                                WhiteColorValue = round(self.left_colorSensor.reflection())
                                wait(200)

                                while Running:
                                    self.left_steeringMotor.run(Speed)
                                    self.right_steeringMotor.run(Speed)
                                    if self.left_colorSensor.reflection() < BlackColorValue:
                                        self.left_steeringMotor.hold()
                                        while Running:
                                            self.right_steeringMotor.run(Speed)
                                            if self.right_colorSensor.reflection() < BlackColorValue:
                                                self.right_steeringMotor.hold()
                                                BlackColorValue = round(self.left_colorSensor.reflection())
                                                wait(200)
                                                Running = False


                ev3.screen.print(WhiteColorValue, BlackColorValue)
                SensorData = DataLog(name = 'SensorData', timestamp = False, extension = 'txt')
                SensorData.log(WhiteColorValue)
                SensorData.log(BlackColorValue)


    def followLine(self, target_line_value, distance, sensor):


        Control.reset()

        FollowingLine = True

        Speed = 40
        
        while FollowingLine:

            error_value = int(sensor.read("COL-REFLECT")[0]) - target_line_value


            Control.setPID(error_value, 0.2, 0.2, 2)

            if error_value > 0:

                self.left_steeringMotor.dc(Speed)
                self.right_steeringMotor.dc(Speed + Control.pid_output)

            else:
                self.left_steeringMotor.dc(Speed + abs(Control.pid_output))
                self.right_steeringMotor.dc(Speed)               



            



    #     LineTarget = (WhiteColorValue) / 2
    #     self.gyroSensor.reset_angle(0)
    #     Running = True

    #     Heading = 0
    #     Error = 0
    #     Speed = 50


    #     while Running:

    #         Robot.drive(Speed, Heading)

    #         Error = (LineTarget - self.left_colorSensor.reflection()) * 0.05

    #         Heading = (Error - self.gyroSensor.angle()) * 0.5

    #     for line in ReadSensorData:
                                
    #         reading_check = line[:-1]

    #         SensorValues.append(reading_check)

    #     TargetDegrees = 80
    #     #AdvancedMove(30,0,20,False)
    #     #Turn(90, False)


    #     Register = DataLog("Target", "Motor", "FinalOrientation")    




    def CheckDevices(self):


        self.motors_devices = [self.left_steeringMotor,self.right_steeringMotor,
                                self.letf_mainMotor,self.right_mainMotor]


        self.sensor_devices = [self.gyroSensor, self.left_colorSensor, 
                                self.right_colorSensor, self.top_colorSensor]



        for motors in range(0,len(self.motors_devices)):

            if self.motors_devices[motor] != 0:

                try:
                    self.motors_devices[motor].reset_angle(0)
                    print("Motor", self.motors_devices[motor], " = OK")

                except IOError:
                    print("Motor",  self.motors_devices[motor], " = ERROR")



        for sensor in range(0, len(self.sensor_devices)):

            if self.sensor_devices[sensor] != 0:

                try:
                    #self.sensor_devices[sensor].read("")
                    print("Motor", self.motors_devices[motor], " = OK")

                except IOError:
                    print("Motor",  self.motors_devices[motor], " = ERROR")



        
                
                


    def pathRun(self):
        RobotValues_txt = []

        with open("RobotValues.txt") as f:

            for line in f:
                                
                RobotValues_txt_Check = line[:-2]

                RobotValues_txt.append(RobotValues_txt_Check)

        print("\n---Robot Data---\n")    
        print(RobotValues_txt)
        print("Total Moves:", len(RobotValues_txt))
        print("\n---Robot Data---")    

        Index = 0
        Counter = 0
        for i in range(len(RobotValues_txt)):

            self.Move((float(RobotValues_txt[Index]) * 100)/100 , 0, 20)
            Counter += 1
            Index += 1

            if Counter < len(RobotValues_txt) - 1:
                self.Turn(float(RobotValues_txt[Index])*-1)

            else:
                break

            Counter += 1
            Index += 1

        ev3.speaker.beep()  