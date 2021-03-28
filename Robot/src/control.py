#!/usr/bin/env pybricks-micropython

import math
import pickle

class PidControl():

    def __init__(self, max_integral=800):

        self.integral = 0
        self.derivative = 0
        self.error = 0
        self.last_error = 0
        self.output = 0
        self.max_integral = max_integral

    def execute(self, error, kp=0, ki=0, kd=0, max_output=800, min_output=-800):
        self.error = error
        self.integral += error
        self.derivative = error - self.last_error
        self.last_error = error

        if self.integral > self.max_integral:
            self.integral = self.max_integral

        self.output = (self.error * kp) + (self.integral * ki) + (self.derivative * kd)

        if self.output > max_output:
            self.output = max_output

        if self.output < min_output:
            self.output = min_output 

    def reset(self):

        self.integral = 0
        self.derivative = 0
        self.error = 0
        self.last_error = 0
        self.output = 0



class Path():
    def __init__(self, name, color_code, coordenates):
        self.coordenates = coordenates
        self.name = name
        self.color_code = color_code
        self.path = []
        self.set_path(coordenates)

    def get_distance(self, xy1, xy2):
        return round(math.sqrt((xy1[0] - xy2[0])**2 + (xy1[1] - xy2[1])**2), 1)    

    def get_angle(self, xy1, xy2, xy3):
        v1_x, v1_y = xy1[0] - xy2[0], xy1[1] - xy2[1]
        v2_x, v2_y = xy3[0] - xy2[0], xy3[1] - xy2[1]
    
        try:
            dot_product = v1_x * v2_x + v1_y * v2_y
            heading = math.acos((dot_product / (math.sqrt(v1_x**2 + v1_y**2) * math.sqrt(v2_x**2 + v2_y**2)))) * 180/math.pi 
        except ZeroDivisionError:
            heading = 0

        x = v1_x * v2_y - v1_y * v2_x
        if x < 0:
            heading = -(180 - heading) 
        else:
            heading = 180 - heading

        return round(heading)
        

    def set_path(self, commands):
        # commands format should look like this:
        # [[10,10], [15,12], "r.Motors.left_action_motor.run_time(100, 100)"]
        # you pass in the instructions you want the robot to follow, it would be either a coordenate to go to or a specific command
        self.path = []
        for i in range(len(commands) - 1):
            if type(i).__name__ != "list":
                self.path.append(i)
                continue
            self.path.append(self.get_distance(coordenates[i], coordenates[i+1]))
            if i < len(coordenates) - 2:
                self.path.append(self.get_angle(coordenates[i], coordenates[i+1], coordenates[i+2]))

        return self.path