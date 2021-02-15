#!/usr/bin/env pybricks-micropython
import math


class RoboticTools():

    def degrees_to_cm(self, degrees, wheel_diameter):
        return (degrees * (wheel_diameter * math.pi)) / 360

    def cm_to_degrees(self, cm, wheel_diameter):
        return (cm / (wheel_diameter * math.pi)) * 360
