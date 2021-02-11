#!/usr/bin/env pybricks-micropython


import time
from control import PIDSystem
from robotic_tools import RoboticTools
from ev3_device import (MotorManager, GyroSensorManager, ColorSensorManager)
from pybricks.hubs import EV3Brick


class Robot():

    # This class provides features to control an ev3 robot.

    def __init__(self):

        # Control system related classes
        self.HeadingControl = PIDSystem()
        self.SpeedControl = PIDSystem()
        self.Tools = RoboticTools()

        # Ev3 control related classes
        self.Gyro = GyroSensorManager()
        self.Motors = MotorManager()
        self.ColorSensor = ColorSensorManager()
        self.Ev3 = EV3Brick()

    def turn(self, target_angle):

        self.Motors.reset_angle(self.Motors.steering)

        self.SpeedControl.reset()

        Turning = True

        while Turning:

            error_value = target_angle - self.Gyro.get_angle()

            self.SpeedControl.execute(error_value, 0.5, 0.3, 0.1)

            self.Motors.left_steeringMotor.dc(self.SpeedControl.output)
            self.Motors.right_steeringMotor.dc(self.SpeedControl.output * -1)

            if error_value > -0.1 and error_value < 0.1:

                Turning = False
                self.Motors.stop(self.Motors.steering)

    def straight(self, target_distance, target_orientation=0, target_duty_limit=20, use_gyro=True):

        self.SpeedControl.reset()
        self.HeadingControl.reset()
        self.Motors.reset_angle(self.Motors.steering)
        self.Gyro.reset()
        target_distance = self.Tools.cm_to_degrees(target_distance, 6.24)

        speed_error = 0
        # Calculate the speed control kp value based on how much battery the robot has left
        # the less battery it has the higher the value
        speed_kp = round(target_distance /
                         (self.Ev3.battery.voltage() * 0.03), 3)
        print('speed kp', speed_kp)
        speed_ki = 0.4
        speed_kd = 0.4

        Running = True
        moved_enough = False
        min_speed = 20

        while Running:
            if use_gyro:
                heading_error = target_orientation - self.Gyro.get_angle()
                heading_kp = 2
                heading_ki = 0.1
                heading_kd = 0.1

            else:
                heading_error = self.Motors.right_steeringMotor.speed(
                ) - self.Motors.left_steeringMotor.speed()
                heading_kp = 0.2
                heading_ki = 0.001
                heading_kd = 0.01

            # Speed and heading control
            self.HeadingControl.execute(
                heading_error, heading_kp, heading_ki, heading_kd)

            self.SpeedControl.execute(
                speed_error, speed_kp, speed_ki, speed_kd)

            # Speed control error logic when moving forward
            if target_distance > 0:

                if self.Motors.right_steeringMotor.angle() < target_distance / 2:
                    speed_error = target_distance - \
                        (target_distance - (self.Motors.right_steeringMotor.angle()))
                else:
                    moved_enough = True
                    speed_error = target_distance - self.Motors.right_steeringMotor.angle()

                # Sets a minimun value for the speed control output in order to force the robot to move at that minimun speed
                if self.SpeedControl.output < min_speed:
                    self.SpeedControl.output = min_speed

            # The exact same logic than the previous block but for moving backwards
            else:

                if self.Motors.right_steeringMotor.angle() > target_distance / 2:
                    speed_error = target_distance - \
                        (target_distance - (self.Motors.right_steeringMotor.angle()))
                else:
                    moved_enough = True
                    speed_error = target_distance - self.Motors.right_steeringMotor.angle()

                if self.SpeedControl.output > -min_speed:
                    self.SpeedControl.output = -min_speed

            # This check if the robot has acctually reached the target distance and stops the robot.
            if moved_enough:
                if speed_error < 1 and speed_error > -1:
                    Running = False
                    self.Motors.stop(self.Motors.steering)

            if heading_error > 0:
                self.Motors.left_steeringMotor.run(self.SpeedControl.output)
                self.Motors.right_steeringMotor.run(
                    self.SpeedControl.output + abs(self.HeadingControl.output))

            else:
                self.Motors.left_steeringMotor.run(
                    self.SpeedControl.output + abs(self.HeadingControl.output))
                self.Motors.right_steeringMotor.run(self.SpeedControl.output)
            #print("speed", self.SpeedControl.output)

    def follow_line(self, target_value, distance, sensor):

        self.HeadingControl.reset()
        self.Motors.reset_angle(self.Motors.steering)

        FollowingLine = True

        Speed = 40

        while FollowingLine:

            error_value = sensor() - target_value

            self.HeadingControl.execute(error_value, 0.2, 0.2, 2)

            if error_value > 0:

                self.Motors.left_steeringMotor.dc(Speed)
                self.Motors.right_steeringMotor.dc(
                    Speed + self.HeadingControl.output)

            else:
                self.Motors.left_steeringMotor.dc(
                    Speed + abs(self.HeadingControl.output))
                self.Motors.right_steeringMotor.dc(Speed)

    def run_csv(self):

        import csv
        with open('mbdata.csv') as csv_file:

            # ONLY USES THE THIRD ROW FROM THE CSV FILE
            csv_reader = list(csv.reader(csv_file, delimiter=','))[2]

            # THE ELEMENTS IN THE ARRAY ARE LOADED AS STRINGS, CHANGE THAT
            robotPath = [eval(row) for row in csv_reader]

            # PERFORM EACH ACTION FROM THE CSV FILE (TURN AND DRIVE STRAIGHT)
            for element in range(len(robotPath)):

                self.Straight(robotPath[element])

                if element < len(robotPath) - 1:
                    self.Turn(robotPath[element])
