#!/usr/bin/env pybricks-micropython

"""
This files includes "managers" for devices, the main purpose for this is to create an "enviroment" to 
easily control an FLL robot.

All this classes use our "custom made" device controllers: MbMotor, MbColorSensor and MbGyroSensor
Mb stands for MbareteBot :p
"""

from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Button, Color
from pybricks.iodevices import Ev3devSensor
from pybricks.hubs import EV3Brick
from pybricks.tools import wait

import pickle

from .devices import MbMotor, MbColorSensor, MbGyroSensor
from .tools import RoboticTools

ev3 = EV3Brick()
status_msg = RoboticTools.status_msg

class DeviceManager():
    """
    A great tool to control the devices connected to the ev3. It can detect what devices are connected to the ev3 and tell if any was
    accidentally disconnected.

    The devices it can detect are from pybricks.ev3devices: ColorSensor, GyroSensor and Motor
    """

    def __init__(self):
        self.motors_ports = [Port.A, Port.B, Port.C, Port.D]
        self.sensors_ports = [Port.S1, Port.S2, Port.S3, Port.S4]
        self.available_sensors = [ColorSensor, GyroSensor]
        self.MOTORS = {
            "Motor": [],
            "Port": []
        }
        self.SENSORS = {
            "Sensor": [],
            "Port": []
        }

    def is_port_in_use(self, port):
        """
        Detects if a port is in use

        Returns:
            port (bool): True if there is something in that port else False
        """
        for motor_port in self.connected_devices()["Motors"]["Port"]:
            if str(port) == motor_port:
                return True

        for sensor_port in self.connected_devices()["Sensors"]["Port"]:
            if str(port) == sensor_port:
                return True
        return False

    def connected_devices(self, print_output=False):
        """
        Check what devices are connected to what ports

        Args:
            print_output (bool): It will display a message showing the devices that were found

        Returns:
            devices (dict): A dictionary with the sensors and motors that were found
        """

        self.MOTORS = {
            "Motor": [],
            "Port": []
        }
        self.SENSORS = {
            "Sensor": [],
            "Port": []
        }

        # Look for motor in every port
        for PORT in self.motors_ports:
            try:
                self.MOTORS["Motor"].append(type(Motor(PORT)).__name__)
                self.MOTORS["Port"].append(str(PORT))
            except Exception:
                pass

        # look for sensors in every port
        for SENSOR in self.available_sensors:
            for PORT in self.sensors_ports:
                try:
                    self.SENSORS["Sensor"].append(type(SENSOR(PORT)).__name__)
                    self.SENSORS["Port"].append(str(PORT))
                except Exception:
                    pass

        if print_output:
            print("\nDevices Found:")
            print("Motors:")
            if len(self.MOTORS["Motor"]) > 0:
                for PORT in self.MOTORS["Port"]:
                    print("Motor in", PORT)
            else:
                print("No motor found")

            print("\nSensors:")
            if len(self.SENSORS["Sensor"]) > 0:
                for SENSOR, PORT in zip(self.SENSORS["Sensor"], self.SENSORS["Port"]):
                    print(SENSOR, "in", PORT)
            else:
                print("No sensor found")

        return {"Motors": self.MOTORS, "Sensors": self.SENSORS}

    def load_devices(self):
        """
        Detect and save the devices that are connected to the ev3,
        the main purpose for this is to later check if any device was disconnected or something
        """
        self.devices = self.connected_devices()
        with open("connected_devices", "wb") as f:
            pickle.dump(self.devices, f)

    def analyse_ports(self):
        """
        Detect if any device was disconnected. This reads the devices that were registered with self.load_devices() and
        detect if they are still in the same position        
        """

        # Test motors
        errors = 0
        for port in self.devices["Motors"]["Port"]:
            try:
                Motor(eval(port))
            except Exception:
                errors += 1
                print("[ ERROR ] Motor is missing in", port)
                status_msg(False, port)

        for sensor, port in zip(self.devices["Sensors"]["Sensor"], self.devices["Sensors"]["Port"]):
            try:
                # Test for color sensor
                if sensor == "ColorSensor":
                    eval(sensor)(eval(port)).reflection()
                else:
                    # Test for gyro sensor
                    Ev3devSensor(eval(port)).read("GYRO-ANG")
            except Exception:
                print("[ ERROR ] Sensor is missing in", port)
                errors += 1
                status_msg(False, port)

        if errors > 0:
            ev3.light.on(Color.RED)

        print("\nJust found", errors, "errors while analysing ports!\n")


class MotorManager():
    """
    Great tool to control motors. It offers an interface to use motors for steering and attachments,
    It reffers to the motors that are going to be use for steering as "steering" motors and
    "action" motors to the motors that are going to be use for attachments.
    So far its kind of empty but will get better, i guess :)

    Args:
        exit_exec (Function): Function that returns True or False, motors will stop if returns True
    """

    def __init__(self, exit_exec=lambda: False):

        self.left_steering_motor = None
        self.right_steering_motor = None
        self.left_action_motor = None
        self.right_action_motor = None

        self.exit_exec = exit_exec

    def set_steering_motors(self, left_motor_port, right_motor_port, clockwise_direction=True):
        """
        Sets the steering motors on the robot

        Args:
            left_motor_port (Port): Port on the which the left steering motor is connected
            right_motor_port (Port): Port on the which the right steering motor is connected
            clockwise_direction (bool): Sets the motor default direction to clockwise or counterclockwise
        """
        self.left_steering_motor = MbMotor(left_motor_port, clockwise_direction, exit_exec=self.exit_exec)
        self.right_steering_motor = MbMotor(right_motor_port, clockwise_direction, exit_exec=self.exit_exec)

    def set_action_motors(self, left_motor_port, right_motor_port):
        """
        Sets the motors that would probably be used for attachments

        Args:
            left_motor_port (Port): Port on the which the left action motor is connected
            right_motor_port (Port): Port on the which the right action motor is connected
        """
        self.left_action_motor = MbMotor(left_motor_port, exit_exec=self.exit_exec)
        self.right_action_motor = MbMotor(right_motor_port, exit_exec=self.exit_exec)

    def __repr__(self):
        return "Motor Manager Properties:\n-Left-Steering-{}\n-Right-Steering-{}\n-Left-Action-{}\n-Right-Action-{}".format(self.left_steering_motor, self.right_steering_motor, self.left_action_motor, self.right_action_motor)


class ColorSensorManager():

    """
    Class to control up to 3 color sensors. The idea is that there is one color sensor in the left side of the robot, 
    another one in the right side and a third one (probably to recognize attachments by a color code)
    """
    def __init__(self):
        self.left_sensor = None
        self.right_sensor = None
        self.front_sensor = None

    def set_sensors(self, left_sensor_port=None, right_sensor_port=None, front_sensor_port=None):
        """
        Sets sensors to control

        Args:
            left_sensor_port (Port): Port where the left sensor is connected to
            right_sensor_port (Port): Port where the right sensor is connected to
            front_sensor_port (Port): Port where the front sensor is connected to
        """
        self.left_sensor = MbColorSensor(left_sensor_port) if left_sensor_port != None else None
        self.right_sensor = MbColorSensor(right_sensor_port) if right_sensor_port != None else None
        self.front_sensor = MbColorSensor(front_sensor_port) if front_sensor_port != None else None

    def calibrate(self, sensor):
        """
        Runs a program to "calibrate" the color sensors (human interection is needed). Creates a file that stores the values for
        a white and a black line, this will not affect the readings of the sensors, that means to use the "calibrated" sensors
        you would need to read that file 
        """
        ev3.screen.clear()
        ev3.screen.print("Ready for calibration!")
        ev3.screen.print("Press center button to Start:")
        print("\n-------ColorSensors-------")
        print("Sensor calibration started!")
        running = True
        while running:
            if Button.CENTER in ev3.buttons.pressed():
                last_pressed_btns = ev3.buttons.pressed()
                white_value = sensor.reflection()
                print("White:", white_value)
                print("Waiting for input...")
                ev3.screen.print("\n->Value for white", white_value)
                ev3.screen.print("Press center button to continue:")
                while Button.CENTER in ev3.buttons.pressed():
                    pass
                while running:
                    if Button.CENTER in ev3.buttons.pressed():
                        wait(100)
                        black_value = sensor.reflection()
                        print("Black:", black_value)
                        print("Waiting for input...")
                        ev3.screen.print("\n->Value for black", black_value)
                        ev3.screen.print("Press center button to Finish:")
                        wait(100)
                        while Button.CENTER in ev3.buttons.pressed():
                            pass
                        while running:
                            if Button.CENTER in ev3.buttons.pressed():
                                with open("calibration_r", "wb") as f:
                                    pickle.dump([white_value, black_value], f)
                                running = False
                                ev3.screen.clear()
        ev3.light.on(Color.GREEN)
        print("Sensor calibration finished!")
        print("-------ColorSensors-------\n")

    def __repr__(self):
        return "ColorSensors Properties:\n-Left {}\n-Right {}\n-Front {}".format(self.left_sensor, self.right_sensor, self.front_sensor)


class GyroSensorManager():
    """
    Provides featurures to read angles, reset and calibrate a gyro sensor
    """
    def __init__(self):
        self.core = None

    @property
    def port(self):
        return self.core.port

    def set_sensor(self, port, clockwise_direction=True):
        """
        Set sensor

        Args:
            port (Port): Port to the which the sensor is connected to
            clockwise_direction (bool): Defines the default sign of the angle readings, clockwise or counterclockwise
        """
        self.core = MbGyroSensor(port, clockwise_direction)

    def angle(self):
        """
        Gets the accumulated angle of the sensor
        """
        return self.core.angle()

    def calibrate(self):
        """
        Calibrate the sensor. The robot should be perfectly still while doing this process
        """
        self.core.calibrate()

    def reset(self):
        """
        Resets the accumulated angle of the sensor
        """
        self.core.reset()

    def __repr__(self):
        return self.core.__repr__()

