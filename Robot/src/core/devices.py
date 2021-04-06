#!/usr/bin/env pybricks-micropython

"""
This files includes our "custom made" device controllers. All of this classes are made on top of 
classes from pybricks.ev3devices or pybricks.iodevices. 
This is so that we can add extra functionality to motors and sensors.
"""

from pybricks.parameters import Port, Direction, Color
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.iodevices import Ev3devSensor
from pybricks.tools import wait

from time import time
import threading
import pickle

from .tools import RoboticTools


status_msg = RoboticTools.status_msg

class MbMotor():
    """
    This class offers extra functionality to control a motor, besides the fact that you can detect if a motor got stalled 
    the main reason for this class is to solve a bug for pybricks.ev3devices.Motor. The bug is that when you set the motor 
    to move in a Direction.COUNTERCLOCKWISE sometime it failes to detect it. 
    
    This class is made on top of the exising pybricks.ev3devices.Motor class

    Args:
        port (Port): The port of the device
        clockwise_direction (bool): Sets the defualt movement of the motor clockwise or counterclockwise, True for clockwise else counterclockwise
        exit_exec (Function) = Function that returns True or False, the motor will stop if returns True
    """
    def __init__(self, port, clockwise_direction=True, exit_exec=lambda: False):
        try:
            self.core = Motor(port)
            self.port = port
            self.direction = 1 if clockwise_direction else -1
            self.exit_exec = exit_exec
        except Exception:
            status_msg(False, "Failed to initalize motor!")
    
    def angle(self):
        """
        Gets the distance the robot has moved in degrees

        Returns:
            angle (int): The distance the robot has moved in degrees
        """
        return self.core.angle() * self.direction

    def speed(self):
        """
        Gets the speed of the motor

        Returns:
            speed (int): The current speed of the motor
        """
        return self.core.speed() * self.direction

    def run_angle(self, speed, angle, wait=True):
        """
        Runs the motor to a specific angle

        Args:
            speed (int): The speed of the motor
            angle (int): Degrees to run the motor at
            wait (bool): Sets if the robot is going to stop for the motor to complete this method or not
        """
        def exec(self, speed, angle):
            self.reset_angle()
            while True:
                self.run(speed)
                if abs(self.angle()) > abs(angle) or self.exit_exec():
                    break
            self.hold()

        if wait:
            exec(self, speed, angle)
        else:
            threading.Thread(target=exec, args=[self, speed, angle]).start()

    def run_time(self, speed, msec, wait=True):
        """
        Runs the motor to a amount of time

        Args:
            speed (int): The speed of the motor
            msec (int): How much time to move the robot
            wait (bool): Sets if the robot is going to stop for the motor to complete this method or not
        """
        def exec(self, speed, msec):
            self.reset_angle()
            s = time()
            while True:
                self.run(speed)
                if round(time() - s, 2) * 1000 >= abs(msec) or self.exit_exec():
                    break
            self.hold()
        
        if wait:
            exec(self, speed, msec)
        else:
            threading.Thread(target=exec, args=[self, speed, msec]).start()

    def run(self, speed):
        """
        Runs the motor to a speed

        Args:
            speed (int): Speed to run at

        Note:
            speed parameter should be between -800 and 800
        """
        self.core.run(speed * self.direction)

    def dc(self, speed):
        """
        Runs the motor to a speed

        Args:
            speed (int): Speed to run at

        Note:
            speed parameter should be between -100 and 100
        """
        self.core.dc(speed * self.direction)

    def hold(self):
        """
        Stop the motor and hold its position
        """
        self.core.hold()
    
    def brake(self):
        """
        Passively stop the motor
        """
        self.core.brake()
    
    def stop(self):
        """
        No current is being aplied to the robot, so its gonna stop due to friction
        """
        self.core.stop() 

    def reset_angle(self, angle=0):
        """
        Set the motor angle

        Args:
            angle (int): Angle to set the motor at
        """
        self.core.reset_angle(angle)

    def is_stalled(self, min_speed):
        """
        Check if the motor got stalled

        If does so by receiving the minimun speed the robot should be moving at, that means this will probably gonna work best on a controled system 
        
        Args:
            min_speed (int): The minim speed the motor should be moving at
        """
        if abs(self.speed()) < abs(min_speed):
            return True 
        return False

    def __repr__(self):
        return "Motor Properties:\nPort: " + str(self.port) + "\nDefault Direction: " + str(self.direction)


class MbColorSensor(ColorSensor):
    """
    Class to controls a color sensor, this is really mostly pybricks.ev3devices.ColorSensor, the only extra functionality
    is that you can get the port the sensor is connected to

    Args:
        port (Port): Port the sensor is connected to
    """
    def __init__(self, port):
        try:
            ColorSensor(port)
        except Exception:
            status_msg(False, "Failed to initalize color sensor!")

        self.port = port

    def __repr__(self):
        return "Color Sensor Properties:\nPort: " + str(self.port) 


class MbGyroSensor():
    """
    Class to control a gyro sensor, the best feature is that you can calibrate the gyro sensor 
    This is build on top of pybricks.iodevices.Ev3devSensor

    Args:
        port (Port): The port the sensor is connected to
        clockwise_direction (bool): Sets if the default reading if the sensor would be clockwise or counterclockwise
    """

    def __init__(self, port, clockwise_direction=True):
        self.core = Ev3devSensor(port)  
        self.init_port = port
        self.direction = 1 if clockwise_direction else -1   
        self.angle_counter = 0
        self.port = port 

    def calibrate(self):
        """
        Calibrate the gyro sensor. During this process the robot should be perfectly still
        """
        try:
            for _ in range(3):
                self.core.read("GYRO-CAL")
                wait(100)
                if self.angle() == 0:
                    break
            wait(100)
            self.reset()
        except Exception:
            status_msg(False, ".calibrate()", "Gyro Sensor", self.init_port)

    def angle(self):
        """
        Gets the angle of the gyro sensor

        Returns:
            angle (int): The current angle of the gyro sensor
        """
        try:
            return (int(self.core.read("GYRO-ANG")[0]) * self.direction) - self.angle_counter
        except Exception:
            status_msg(False, ".angle()", "Gyro Sensor", self.init_port)

    def reset(self):
        """
        Resets the accumulated angle of the sensor, this does not affect the actual sensor angle but instead it make it looks like the sensor angle was reseated
        as it shows an appropiate value for the angle by using self.angle()
        """
        try:
            self.angle_counter = int(self.core.read("GYRO-ANG")[0]) * self.direction
        except Exception:
            status_msg(False, ".reset()", "Gyro Sensor", self.init_port)

    def __repr__(self):
        return "Gyro Properties:\nPort: {}\nDirection: {}".format(self.port, self.direction)
