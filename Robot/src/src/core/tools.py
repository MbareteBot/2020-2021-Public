#!/usr/bin/env pybricks-micropython

from pybricks.media.ev3dev import Font
from pybricks.hubs import EV3Brick

ev3 = EV3Brick()
ev3.screen.set_font(Font(size=12))

class RoboticTools():
    """
    Tools that might be useful for robotics :p

    Args:
        wheel_diameter (float): To convert cm to distance in degrees for the wheels
    """

    def __init__(self, wheel_diameter=0):
        self.wheel_diameter = wheel_diameter

    def degrees_to_cm(self, degrees, wheel_diameter="default"):
        """
        Receives a distance in degrees and outputs the distance in cm

        Args:
            degrees (int, float): Distance in degrees
            wheel_diameter (float): Diameter of the wheel

        Returns:
            cm (int, float): Distance in cm
        """

        # making this "modular"
        wheel_diameter = self.wheel_diameter if wheel_diameter == "default" else wheel_diameter
        return (degrees * (wheel_diameter * 3.141)) / 360

    def cm_to_degrees(self, cm, wheel_diameter="default"):
        """
        Receives a distance in cm and outputs the distance in degrees

        Args:
            cm (int, float): Distance in cm
            wheel_diameter (float): Diameter of the wheel

        Returns:
            degrees (int, flaot): Distance in degrees
        """

        # making this "modular"
        wheel_diameter = self.wheel_diameter if wheel_diameter == "default" else wheel_diameter
        return (cm / (wheel_diameter * 3.141)) * 360

    @staticmethod
    def status_msg(succes, log, device="", port=""):
        """
        Prompt a message to the ev3, you can either pass a message to display or match the parameters to complete a specific format

        Args:
            log (str): Main message to prompt
            device (str): Name of the device that failed
            port (str): Port of the device that failed
        """
        
        if succes:
            print("[ OK ]", log)
        else:
            ev3.screen.print("[ ERROR ]", log, port)
            print("[ ERROR ]", log, ("is for a " + str(device) + ". No " + str(device) + " is connected to " + str(port)) if device != "" else "")

