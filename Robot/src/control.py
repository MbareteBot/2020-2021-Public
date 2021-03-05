#!/usr/bin/env pybricks-micropython

import math


# This class is dedicated to run a PID calculation based on some parameters and its values can be used
# to control the robot.

class PIDSystem():

    def __init__(self):

        self.integral_value = 0
        self.derivative_value = 0
        self.error_value = 0
        self.last_error_value = 0
        self.pid_output = 0

        self.max_integral_value = 110

    def execute(self, error_value, kp=0, ki=0, kd=0):

        self.error_value = error_value
        self.integral_value += error_value
        self.derivative_value = error_value - self.last_error_value
        self.last_error_value = error_value

        if self.integral_value > self.max_integral_value:
            self.integral_value = self.max_integral_value

        elif self.integral_value < -self.max_integral_value:
            self.integral_value = -self.max_integral_value

        self.output = (self.error_value * kp) + \
            (self.integral_value * ki) + (self.derivative_value * kd)

    def reset(self):

        self.integral_value = 0
        self.derivative_value = 0
        self.error_value = 0
        self.last_error_value = 0
        self.pid_output = 0

        self.max_integral_value = 110


# -----------------------------------------------------------

class OdometrySystem:

    # ----This Class is still in development----
    # ----We are still working on this class, so please, give us your feedback---
    # ----We didnt have much time to test it, so its mostly theoretical so far---

    # This class is used to implement an odometry sistem for the robot.

    def __init__(self):

        self.global_x_pos = 0
        self.global_y_pos = 0

        self.global_x_pos_log = []
        self.global_y_pos_log = []

    # This function updates the robot current position, it receives how much each wheel has moved and
    # the angle the robot is oriented to.

    def updatePos(self, left_motor_degrees, right_motor_degrees, heading):

        left_motor = ((left_motor * (6.24 * math.pi)) / 360) - \
            last_left_motor_degrees
        right_motor = ((right_motor * (6.24 * math.pi)) /
                       360) - last_right_motor_degrees

        motors_average_degrees = round((left_motor + right_motor) / 2)

        self.global_x_pos += round(motors_average_degrees *
                                   math.cos(math.radians(heading)), 1)
        self.global_y_pos += round(motors_average_degrees *
                                   math.sin(math.radians(-heading)), 1)

        print("X:", self.global_x_pos)
        print("Y:", self.global_y_pos)

        last_left_motor_degrees = left_motor_degrees
        last_right_motor_degrees = right_motor_degrees

    def goTo(self, x_target, y_target, MoveStraight_function, Turn_function):

        # This function is used to make the robot go to a desired position.
        # It takes as parameters an x,y target, a funtion that makes the robot move in a straight line and
        # another funtion that makes the robot turn.

        # In this way this function takes that x,y target to get the angle and distance between the current position and
        # the desired position and uses those funtions to actually move the robot to that position

        # The MoveStraight_function should recive as a parameter a distance target im cm.
        # The Turn_function should recive as a parameter a target angle in degrees.

        print(self.global_x_pos_log, self.global_y_pos_log,
              self.global_x_pos, self.global_y_pos)
        print("Target X,Y:", x, y)

        self.global_x_pos_log.append(self.global_x_pos)
        self.global_y_pos_log.append(self.global_y_pos)

        self.robot_moves += 1

        if self.robot_moves >= 2:

            vector1_relX = x - self.global_x_pos
            vector1_relY = y - self.global_y_pos

            vector2_relX = self.global_x_pos_log[-2] - self.global_x_pos
            vector2_relY = self.global_y_pos_log[-2] - self.global_y_pos

            cross_product = vector1_relX * vector2_relY - vector1_relY * vector2_relX
            dot_product = (vector1_relX * vector2_relX) + \
                (vector1_relY * vector2_relY)

            target_heading = math.acos(
                (dot_product / (math.sqrt(vector1_relX**2 + vector1_relY**2) * math.sqrt(vector2_relX**2 + vector2_relY**2))))

            if cross_product < 0:
                heading = (180 - (target_heading * (180/math.pi))) * -1
            else:
                heading = 180 - (target_heading * (180/math.pi))

        else:
            heading = math.atan2(y_target, x_target) * 180/math.pi

        distance_cm = round(math.sqrt((x - self.global_x_pos)
                                      ** 2 + (y - self.global_y_pos)**2), 1)

        distance_degrees = ((distance_cm / (6.24 * math.pi)) * 360)

        if heading != 0:
            Turn_function(-heading)

        self.updatePos()

        MoveStraight_function(distance_cm, 0, 20)

        self.updatePos()

        print("X:", self.global_x_pos)
        print("Y:", self.global_y_pos)
