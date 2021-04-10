#!/usr/bin/env pybricks-micropython

import math

class PidController():
    """
    Provides functionality to execute a PID controller

    Args:
        kp (int, float): Proportional gain
        ki (int, float): Integral gain
        kd (int, float): Derivative gain
        max_integral (int, float): Sets the maximun value the Integral term can achieve
    """
    def __init__(self, 
                 kp=0, 
                 ki=0, 
                 kd=0, 
                 max_integral=800):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.max_integral = max_integral

        self.proportional = 0
        self.integral = 0
        self.derivative = 0
        self.error = 0
        self.last_error = 0
        self.output = 0

    def execute(self, error):
        """
        Executes the PID control calculation. It doesnt returns anything as the ideal is to use self.output to use the calculation result

        Args:
            error (int, float): The error value in the system

        Returns:
            output (int, float): The PID output
        """
            
        self.error = error
        self.proportional = error * self.kp 
        self.integral = (self.integral + error) * self.ki 
        self.derivative = (error - self.last_error) * self.kd
        self.last_error = error

        if self.integral > self.max_integral:
            self.integral = self.max_integral

        self.output = self.proportional + self.integral + self.derivative

        return self.output

    def settings(self, 
                kp=None, 
                ki=None, 
                kd=None, 
                max_integral=None):
        """
        Allows to set certaing parameters of the PID Controller

        Args:
            kp (int, float): Proportional gain
            ki (int, float): Integral gain
            kd (int, float): Derivative gain
            max_integral (int, float): Sets the maximun value the Integral term can achieve
        """

        self.kp = kp if kp != None else self.kp 
        self.ki = ki if ki != None else self.ki 
        self.kd = kd if kd != None else self.kd 
        self.max_integral = max_integral if max_integral != None else self.max_integral 

    def reset(self):
        """
        Resets Proportional, Integral and Derivate terms to zero
        """

        self.proportional = 0
        self.integral = 0
        self.derivative = 0
        self.error = 0
        self.last_error = 0
        self.output = 0

    def __repr__(self):
        return "PID Controller:\nProportional: {}\nIntegral: {}\nDerivative: {}\nKp: {}\nKi: {}\nKd: {}\nMax Integral: {}".format(self.proportional, self.integral, self.derivative, self.kp, self.ki, self.kd, self.max_integral)


class Path:
    """
    This class is used to create a path that the robot can perform based on Cartesian coordinates.
    The input is a series of coordenates you want the robot the follow and it outputs 
    the path you made with coordenates as a path that would make the robot to 
    move straight and turn to follow that path.

    Example:
        >>> Path([0.0, 4.5, 6.2, 7.8]) # the coordenates to follow 
        >>> [6.4, 108, 3.6, -137, 6.1] # the actual path the robot is gonna use

        The robot would follow the path like this:
            MOVE_STRAIGHT 6.4cm
            TURN 108°
            MOVE_STRAsIGHT 3.6cm
            TURN -137°
            MOVE_STRAIGHT 6.1cm

    Note:
        The angle to turn will always be between -180 to 180
    """

    def __init__(self, coordenates):
        """
        
        Args:
            coordenates (List): The path the robot is going to follow
        """
        self.coordenates = coordenates
        self.set_path(coordenates)

    def get_distance(self, xy1, xy2):
        """
        Gets the distance between two points
        
        Args:
            xy1 (List): The coordenates of the first point
            xy2 (List): The coordenates of the second point

        Returns:
            distance (int): The distance between the two points
        """
        
        return round(math.sqrt((xy1[0] - xy2[0])**2 + (xy1[1] - xy2[1])**2), 1)    

    def get_angle(self, xy1, xy2, xy3):
        """
        Gets the angle between two vectors, in this particular case it also needs the origin of the vectors 
        that should be the same from both

        Args:
            xy1 (List): The head of the first vector
            xy2 (List): The origin between the two vectors
            xy2 (List): The head of the second vector

        Returns:
            angle (int): The angle between the two vectors, will always be between -180 and 180
        """

        v1_x, v1_y = xy1[0] - xy2[0], xy1[1] - xy2[1]
        v2_x, v2_y = xy3[0] - xy2[0], xy3[1] - xy2[1]

        try:
            dot_product = v1_x * v2_x + v1_y * v2_y
            angle = math.acos((dot_product / (math.sqrt(v1_x**2 + v1_y**2) * math.sqrt(v2_x**2 + v2_y**2)))) * 180/math.pi 
        except ZeroDivisionError:
            angle = 0

        x = v1_x * v2_y - v1_y * v2_x
        if x < 0:
            angle = -(180 - angle) 
        else:
            angle = 180 - angle

        return round(angle)
        
    def set_path(self, coordenates):
        """
        Computes all the math to create a path the robot can follow (distances and angles)

        Args:
            coordenates (List): The coordenates to follow

        Returns:
            self.path (List): The final path the robot can follow
        """
        self.path = []
        for i in range(len(coordenates) - 1):
            self.path.append(self.get_distance(coordenates[i], coordenates[i+1]))
            if i < len(coordenates) - 2:
                self.path.append(self.get_angle(coordenates[i], coordenates[i+1], coordenates[i+2]))

        return self.path