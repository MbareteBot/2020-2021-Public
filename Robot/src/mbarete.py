#!/usr/bin/env pybricks-micropython
import time
import threading
from control import PIDSystem
from robotic_tools import RoboticTools
from ev3_device import MotorManager, GyroSensorManager, ColorSensorManager, DeviceManager, status_msg
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
        moving = True
        min_speed = 50

        while moving:
            error_value = target_angle - self.Gyro.angle()

            self.SpeedControl.execute(error_value, 5, 0, 0)

            if target_angle > 0:
                if self.SpeedControl.output < min_speed:
                    self.SpeedControl.output = min_speed
            else:
                if self.SpeedControl.output > -min_speed:
                    self.SpeedControl.output = -min_speed

            self.Motors.left_steering_motor.run(self.SpeedControl.output)
            self.Motors.right_steering_motor.run(-self.SpeedControl.output)

            if error_value >= -1 and error_value <= 1:
                moving = False
                self.Motors.stop("steering")

    def straight(self, distance, orientation=0, duty_limit=20, use_gyro=True):

        self.SpeedControl.reset()
        self.HeadingControl.reset()
        self.Motors.reset_angle("steering")
        self.Gyro.reset()
        target_distance = self.Tools.cm_to_degrees(distance, 6.24)
        speed_error = 0
        speed_kp = 3.5
        speed_ki = 0
        speed_kd = 0

        moving = True
        moved_enough = False
        min_speed = 90 * (-1 if distance < 0 else 1)
        while moving:
            if use_gyro:
                heading_error = orientation - self.Gyro.angle()
                heading_kp = 2
                heading_ki = 0.1
                heading_kd = 0.1
            else:
                heading_error = self.Motors.right_steering_motor.speed() - self.Motors.left_steering_motor.speed()
                heading_kp = 0.2
                heading_ki = 0.001
                heading_kd = 0.01

            # Speed and heading control
            self.HeadingControl.execute(heading_error, heading_kp, heading_ki, heading_kd)
            self.SpeedControl.execute(speed_error, speed_kp, speed_ki, speed_kd)

            # Speed control error logic when moving forward
            if abs(self.Motors.right_steering_motor.angle()) < abs(target_distance / 2):
                speed_error = target_distance - (target_distance - self.Motors.right_steering_motor.angle())
            else:
                moved_enough = True
                speed_error = target_distance - self.Motors.right_steering_motor.angle()

            # Sets minimun speed for the motors
            if abs(self.SpeedControl.output) < abs(min_speed):
                self.SpeedControl.output = min_speed

            self.Motors.left_steering_motor.run(self.SpeedControl.output)
            self.Motors.right_steering_motor.run(self.SpeedControl.output + abs(self.HeadingControl.output))

            # When the robot has moved at least halfway
            if moved_enough:
                # Stop if the robot had either reached the target distance or got stalled 
                if (speed_error < 1 and speed_error > -1) or abs(self.Motors.left_steering_motor.speed()) < abs(min_speed):
                    moving = False
                    self.Motors.stop("steering")


    def follow_line(self, target_value, distance, sensor):

        self.HeadingControl.reset()
        self.Motors.reset_angle("steering")
        speed = 400

        while True:

            error_value = sensor() - target_value
            self.HeadingControl.execute(error_value, 0.2, 0.2, 2)
            if error_value > 0:
                self.Motors.left_steering_motor.run(speed)
                self.Motors.right_steering_motor.run(speed + self.HeadingControl.output)
            else:
                self.Motors.left_steering_motor.run(speed + abs(self.HeadingControl.output))
                self.Motors.right_steering_motor.run(speed)

    def square_line(self):
        speed = 150
        white_value = eval(list(open("calibration_r"))[0])[0] - 10
        try:
            for repetition in range(2):
                while True:
                    # Keep moving the left motor until it reaches a white line
                    if self.ColorSensors.left_sensor.reflection() < white_value:
                        self.Motors.left_steering_motor.run(speed)
                    else:
                        print("left ok in", repetition)
                        self.Motors.left_steering_motor.hold()

                    # Keep moving the right motor until it reaches a white line
                    if self.ColorSensors.right_sensor.reflection() < white_value:
                        self.Motors.right_steering_motor.run(speed)
                    else:
                        print("right ok in", repetition)
                        self.Motors.right_steering_motor.hold()

                    # If both sensors are on the white line, go backwards and repeat the procces one more time
                    if self.ColorSensors.right_sensor.reflection() > white_value and self.ColorSensors.left_sensor.reflection() > white_value:
                        print("both ok in", repetition)
                        if repetition == 0:
                            self.Motors.left_steering_motor.run_angle(-speed, 60, wait=False)
                            self.Motors.right_steering_motor.run_angle(-speed, 60)
                        break

                self.Motors.stop("steering")
        except:
            status_msg(False, ".square_line()", "ColorSensor", "any port")

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
