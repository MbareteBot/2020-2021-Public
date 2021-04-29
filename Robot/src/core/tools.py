#!/usr/bin/env pybricks-micropython

from pybricks.media.ev3dev import Font
from pybricks.hubs import EV3Brick
from pybricks.tools import DataLog
from pybricks.parameters import Port, Color, Button
    
class LogSystem:
    def __init__(self):
        self._ev3 = EV3Brick()
        self._ev3.screen.set_font(Font(size=12))
        self.last_log = ""
        self.log_files = []
        self.log_files_names = []

    def log(self, content, host=True, ev3=False, positivelog=None):
        """
        Prompt a message to the ev3, you can either pass a message to display or match the parameters to complete a specific format

        Args:
            content (str): Message to prompt
            positive (bool): If message is True append [ OK ] to the msg else append [ ERROR ]
            host (bool): Prompt to the host computer?
            ev3 (bool): Prompt to the ev3?
        """
        msg = (("[ OK ] " if positivelog else "[ ERROR ] ") if positivelog != None else "") + str(content)
        if host: 
            print(msg)
        if ev3:
            self._ev3.screen.print(msg)

    def clear_log(self):
        """
        Clear ev3 screen
        """
        self._ev3.screen.clear()

    def task_handler(_, task):
        """
        Decorator that wont raise exceptions but will prompt a message to the user.
        The idea behind this is that the user will never need to exit the current file to try again, and will get notified
        what the error was on the ev3 screen
        """
        def perform(*args, **kwargs):
            try:
                return task(*args, **kwargs) 
            except:
                LogSystem().log(task.__name__, host=True, ev3=True, positivelog=False)
        return perform
        
    def record(self, filename, target, state):
        """
        Log data to control error, if the filename wasnt used before a new file will be created

        Args:
            filename (str): Filename of the log file
            target (int, float, str, bool): Anything that is considered the target value of a system
            state (int, float, str, bool): Anything that is considered the current state value of a system
        """
        if filename not in self.log_files_names:
            self.log_files_names.append(filename)
            self.log_files.append(DataLog("Target", "State", "Error", name=filename))
        
        self.log_files_names.index(filename).log(target, state, target - state)


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
        Receive a distance in degrees and outputs the distance in cm

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
        Receive a distance in cm and outputs the distance in degrees

        Args:
            cm (int, float): Distance in cm
            wheel_diameter (float): Diameter of the wheel

        Returns:
            degrees (int, flaot): Distance in degrees
        """
        # making this "modular"
        wheel_diameter = self.wheel_diameter if wheel_diameter == "default" else wheel_diameter
        return (cm / (wheel_diameter * 3.141)) * 360


class Parameters:
    """
    Parameters (Color, Port)
    """
    def __init__(self):
        self.Color = Color
        self.Port = Port
        self.Button = Button