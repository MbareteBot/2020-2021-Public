#!/usr/bin/env pybricks-micropython
import time
import threading
from control import PIDSystem
from robotic_tools import RoboticTools
from ev3_device import MotorManager, GyroSensorManager, ColorSensorManager, DeviceManager
from pybricks.parameters import Port
from pybricks.hubs import EV3Brick
from pybricks.tools import wait


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
        self.ColorSensors = ColorSensorManager()
        self.DeviceControl = DeviceManager()
        self.Ev3 = EV3Brick()

        print("-------Robot Initialized-------")

    def turn(self, target_angle):

        self.Motors.reset_angle("steering")
        self.SpeedControl.reset()
        self.Gyro.reset()
        print("gyro after reset for turn", self.Gyro.angle())
        moving = True
        min_speed = 50

        while moving:
            print("gyro in turn", self.Gyro.angle())
            error_value = target_angle - self.Gyro.angle()

            self.SpeedControl.execute(error_value, 5, 0, 0)

            print("error", error_value)

            if target_angle > 0:
                if self.SpeedControl.output < min_speed:
                    self.SpeedControl.output = min_speed
            else:
                if self.SpeedControl.output > -min_speed:
                    self.SpeedControl.output = -min_speed

            print("output for motors", self.SpeedControl.output)
            self.Motors.left_steering_motor.run(self.SpeedControl.output)
            self.Motors.right_steering_motor.run(-self.SpeedControl.output)

            if error_value >= -1 and error_value <= 1:
                moving = False
                self.Motors.stop("steering")

    def straight(self, target_distance, target_orientation=0, target_duty_limit=20, use_gyro=True):

        self.SpeedControl.reset()
        self.HeadingControl.reset()
        self.Motors.reset_angle("steering")
        self.Gyro.reset()
        target_distance = self.Tools.cm_to_degrees(target_distance, 6.24)

        speed_error = 0
        # Calculate the speed control kp value based on how much battery the robot has left
        # the lower battery the higher the value
        speed_kp = 3.5
        speed_ki = 0
        speed_kd = 0

        moving = True
        moved_enough = False
        min_speed = 90

        while moving:
            if use_gyro:
                heading_error = target_orientation - self.Gyro.angle()
                heading_kp = 2
                heading_ki = 0.1
                heading_kd = 0.1

            else:
                heading_error = self.Motors.right_steering_motor.speed(
                ) - self.Motors.left_steering_motor.speed()
                heading_kp = 0.2
                heading_ki = 0.001
                heading_kd = 0.01

            # Speed and heading control
            self.HeadingControl.execute(heading_error,
                                        heading_kp, heading_ki, heading_kd)

            self.SpeedControl.execute(speed_error,
                                      speed_kp, speed_ki, speed_kd)

            # Speed control error logic when moving forward
            if target_distance > 0:
                if self.Motors.right_steering_motor.angle() < target_distance / 2:
                    speed_error = target_distance - \
                        (target_distance - (self.Motors.right_steering_motor.angle()))
                else:
                    moved_enough = True
                    speed_error = target_distance - self.Motors.right_steering_motor.angle()

                # Sets a minimun value for the speed control output in order to force the robot to move at that minimun speed
                if self.SpeedControl.output < min_speed:
                    self.SpeedControl.output = min_speed

            # The exact same logic than the previous block but when moving backwards
            else:

                if self.Motors.right_steering_motor.angle() > target_distance / 2:
                    speed_error = target_distance - \
                        (target_distance - (self.Motors.right_steering_motor.angle()))
                else:
                    moved_enough = True
                    speed_error = target_distance - self.Motors.right_steering_motor.angle()

                if self.SpeedControl.output > -min_speed:
                    self.SpeedControl.output = -min_speed

            if heading_error > 0:
                self.Motors.left_steering_motor.run(self.SpeedControl.output)
                self.Motors.right_steering_motor.run(
                    self.SpeedControl.output + abs(self.HeadingControl.output))

            else:
                self.Motors.left_steering_motor.run(
                    self.SpeedControl.output + abs(self.HeadingControl.output))
                self.Motors.right_steering_motor.run(self.SpeedControl.output)

            # This check if the robot has acctually reached the target distance and stops the robot.
            if moved_enough:
                if speed_error < 1 and speed_error > -1:
                    moving = False
                    self.Motors.stop("steering")

    def follow_line(self, target_value, distance, sensor):

        self.HeadingControl.reset()
        self.Motors.reset_angle("steering")
        FollowingLine = True
        Speed = 40

        while FollowingLine:

            error_value = sensor() - target_value
            self.HeadingControl.execute(error_value, 0.2, 0.2, 2)
            if error_value > 0:
                self.Motors.left_steering_motor.dc(Speed)
                self.Motors.right_steering_motor.dc(
                    Speed + self.HeadingControl.output)
            else:
                self.Motors.left_steering_motor.dc(
                    Speed + abs(self.HeadingControl.output))
                self.Motors.right_steering_motor.dc(Speed)

    def square_line(self):
        pass

    def run_csv(self):

        import csv
        with open('mbdata.csv') as csv_file:

            # ONLY USES THE THIRD ROW FROM THE CSV FILE
            csv_reader = list(csv.reader(csv_file, delimiter=','))[2]

            # THE ELEMENTS IN THE ARRAY ARE LOADED AS STRINGS, CHANGE THAT
            robotPath = [eval(row) for row in csv_reader]

            # PERFORM EACH ACTION FROM THE CSV FILE (TURN AND DRIVE STRAIGHT)
            for element in range(len(robotPath)):

                self.straight(robotPath[element])

                if element < len(robotPath) - 1:
                    self.turn(robotPath[element])

    def run_async(self, _target, _args=[]):
        new_thread = threading.Thread(target=_target, args=_args)
        new_thread.start()
