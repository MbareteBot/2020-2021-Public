#!/usr/bin/env pybricks-micropython
import time
import threading
from time import sleep
from control import PIDSystem
from robotic_tools import RoboticTools
from ev3_device import MotorManager, GyroSensorManager, ColorSensorManager, DeviceManager, status_msg
from pybricks.parameters import Port, Button
from pybricks.hubs import EV3Brick
from pybricks.tools import wait


class Robot():

    # This class provides features to control an ev3 robot.

    def __init__(self):

        # Control system related classes
        self.HeadingControl = PIDSystem()
        self.SpeedControl = PIDSystem()
        self.Tools = RoboticTools()

        self.active = True # This will be used like a global switch
        
        # Ev3 control related classes
        self.Gyro = GyroSensorManager()
        self.Motors = MotorManager()
        self.ColorSensors = ColorSensorManager()
        self.DeviceControl = DeviceManager()
        self.Ev3 = EV3Brick()

        print("-------Robot Initialized-------")

        # Task handler
        self.run_async(self.handle_task)



    def handle_task(self):
        # This is gonna run asynchronously, works like a master switch
        while True:
            if Button.CENTER in self.Ev3.buttons.pressed(): 
                self.active = False
            sleep(0.09)


    def turn(self, angle):  

        if self.active:
            self.Motors.reset_angle("steering")
            self.SpeedControl.reset()
            self.Gyro.reset()
            moving = True
            min_speed = 50

            while moving:
                error_value = angle - self.Gyro.angle()

                self.SpeedControl.execute(error_value, 5, 0, 0)

                if angle > 0:
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


    def straight(self, distance, orientation=0, use_gyro=True, exit_exec=lambda: False):

        if self.active:

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

                # Speed control error logic 
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
                if moved_enough or exit_exec():
                    # Stop if the robot had either reached the target distance or got stalled or the execution is being cancelled by exit_exec method 
                    if (speed_error < 1 and speed_error > -1) or abs(self.Motors.left_steering_motor.speed()) < abs(min_speed) or exit_exec():
                        moving = False
                        self.Motors.stop("steering")


        def follow_line(self, target_value, distance, sensor):

            if self.active:
                    
                self.HeadingControl.reset()
                self.Motors.reset_angle("steering")
                speed = 400

                while True:

                    error_value = sensor.reflection() - target_value
                    self.HeadingControl.execute(error_value, 0.2, 0.2, 2)
                    if error_value > 0:
                        self.Motors.left_steering_motor.run(speed)
                        self.Motors.right_steering_motor.run(speed + self.HeadingControl.output)
                    else:
                        self.Motors.left_steering_motor.run(speed + abs(self.HeadingControl.output))
                        self.Motors.right_steering_motor.run(speed)
        
        
        def square_line(self):

            if self.active:

                speed = 150
                try:
                    white_value = eval(list(open("calibration_r"))[0])[0] - 10
                except Exception:
                    status_msg(False, ".square_line() needs calibration file made by self.ColorSensors.calibrate()")
                
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
                except Exception:
                    status_msg(False, ".square_line()", "ColorSensor", "any port")

    
    def run_to_line(self, sensor, aprox_distance):

        if self.active:
            try:
                white_value = eval(list(open("calibration_r"))[0])[0] - 10
            except Exception:
                status_msg(False, ".run_to_line() needs calibration file made by self.ColorSensors.calibrate()")

            # Check if the robot reached a white line
            def reached_line():
                if sensor.reflection() > white_value:
                    return True
                return False
            
            # The robot is gonna move a straight line and is gonna stop if it either reached
            # the aprox_distance or reached a white line
            self.straight(aprox_distance, exit_exec=reached_line)


    def run_async(self, _target, _args=[]):
        new_thread = threading.Thread(target=_target, args=_args)
        new_thread.start()