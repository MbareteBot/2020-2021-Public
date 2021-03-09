#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Stop, Port, Direction, Color, Button
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.iodevices import Ev3devSensor
from pybricks.media.ev3dev import Font
from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from control import PIDSystem
import pickle

# All this classes are used to control ev3 devices (motors, gyro and color sensors).
# With this classes you can only have: 4 Motors, 1 Gyro and 3 Color Sensors



ev3 = EV3Brick()
ev3.screen.set_font(Font(size=12))


def status_msg(succes, log, device="", port=""):
    if succes:
        # ev3.screen.print("[ OK ]", log)
        print("[ OK ]", log)
    else:
        ev3.screen.print("[ ERROR ]", log, port)
        print("[ ERROR ]", log, ("is for a " + str(device) + " .No " + str(device) + " is connected to " + str(port)) if device != "" else "")


class MotorManager():

    # This class is meant to be used to control 2 "Steering" motors
    # and 2 "Action" motors dedicated to control attachments.

    def __init__(self):

        self.SpeedControl = PIDSystem()
        self.DeviceControl = DeviceManager()

        # All available motors
        self.left_steering_motor = None
        self.right_steering_motor = None
        self.left_action_motor = None
        self.right_action_motor = None
        self.motor_direction = Direction.CLOCKWISE

    def set_steering_motors(self, left_motor_port, right_motor_port, default_direction=True):

        if default_direction == False:
            self.motor_direction = Direction.COUNTERCLOCKWISE

        self.left_steering_motor = Motor(left_motor_port, self.motor_direction)
        self.right_steering_motor = Motor(right_motor_port, self.motor_direction)
        status_msg(True, "Left Steering Motor")
        status_msg(True, "Right Steering Motor")

    def set_action_motors(self, left_motor_port, right_motor_port):

        self.left_action_motor = Motor(left_motor_port)
        self.right_action_motor = Motor(right_motor_port)
        status_msg(True, "Left Action Motor")
        status_msg(True, "Right Action Motor")

    def reset_angle(self, motors):
        try:
            if motors == "steering":
                self.left_steering_motor.reset_angle(0)
                self.right_steering_motor.reset_angle(0)

            elif motors == "action":
                self.left_action_motor.reset_angle(0)
                self.right_action_motor.reset_angle(0)

            elif motors == "full":
                self.left_steering_motor.reset_angle(0)
                self.right_steering_motor.reset_angle(0)
                self.left_action_motor.reset_angle(0)
                self.right_action_motor.reset_angle(0)
        except Exception:
            status_msg(False, ".reset_angle()", "Motor", "some port")

    def stop(self, motors):
        try:
            if motors == "steering":
                self.left_steering_motor.brake()
                self.right_steering_motor.brake()

            elif motors == "action":
                self.left_action_motor.brake()
                self.right_action_motor.brake()

            elif motors == "full":
                self.left_steering_motor.brake()
                self.right_steering_motor.brake()
                self.left_action_motor.brake()
                self.right_action_motor.brake()
        except Exception:
            status_msg(False, ".stop()", "Motor", "some port")


class ColorSensorManager():

    # Class dedicated to control up to 3 color sensors (one in the left side of the robot,
    # another one in the right side and a third one (probably to recognize attachments by a color code).

    def __init__(self):

        self.left_sensor = None
        self.right_sensor = None
        self.front_sensor = None

    def set_left_sensor(self, port):
        self.left_sensor = MbColorSensor(port)
        status_msg(True, "Left Color Sensor")

    def set_right_sensor(self, port):
        self.right_sensor = MbColorSensor(port)
        status_msg(True, "Right Color Sensor")

    def set_front_sensor(self, port):
        self.front_sensor = MbColorSensor(port)
        status_msg(True, "Front Color Sensor")

    def calibrate(self, sensor):
        ev3.screen.print("Ready for calibration!")
        ev3.screen.print("Press center button to Start:")
        print("\n-------ColorSensors-------")
        print("Sensor calibration started!")
        ev3.screen.clear()
        running = True
        while running:
            if Button.CENTER in ev3.buttons.pressed():
                wait(1000)
                white_value = sensor.reflection()
                print("-> Value for white:", white_value)
                print("Waiting for input...")
                ev3.screen.print("\n->Value for white", white_value)
                ev3.screen.print("Press center button to continue:")
                while running:
                    if Button.CENTER in ev3.buttons.pressed():
                        wait(1000)
                        black_value = sensor.reflection()
                        print("-> Value for black:", black_value)
                        print("Waiting for input...")
                        ev3.screen.print("\n->Value for black", black_value)
                        ev3.screen.print("Press center button to Finish:")
                        wait(1000)
                        while running:
                            if Button.CENTER in ev3.buttons.pressed():
                                with open("calibration_r", "wb") as f:
                                    pickle.dump([white_value, black_value], f)
                                running = False
                                ev3.screen.clear()
        print("Sensor calibration finished!")
        print("-------ColorSensors-------\n")


class GyroSensorManager():

    @property
    def port(self):
        self.sensor.port

    def set_sensor(self, port, default_direction=True):
        self.sensor = MbGyroSensor(port, default_direction)
    
    def calibrate(self):
        self.sensor.calibrate()

    def angle(self):
        return self.sensor.angle()

    def reset(self):
        self.sensor.reset()

    def __str__(self):
        return self.sensor.__str__()
    


class DeviceManager():

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
        for motor_port in self.connected_devices()["Motors"]["Port"]:
            if str(port) == motor_port:
                return True

        for sensor_port in self.connected_devices()["Sensors"]["Port"]:
            if str(port) == sensor_port:
                return True
        return False

    def connected_devices(self, print_output=False):
        self.MOTORS = {
            "Motor": [],
            "Port": []
        }
        self.SENSORS = {
            "Sensor": [],
            "Port": []
        }

        # LOOK FOR MOTORS IN EVERY PORT
        for PORT in self.motors_ports:
            try:
                self.MOTORS["Motor"].append(type(Motor(PORT)).__name__)
                self.MOTORS["Port"].append(str(PORT))
            except Exception:
                pass
        # LOOK FOR EVERY SINGLE SENSOR TYPE IN EVERY PORT
        for SENSOR in self.available_sensors:
            for PORT in self.sensors_ports:
                try:
                    self.SENSORS["Sensor"].append(type(SENSOR(PORT)).__name__)
                    self.SENSORS["Port"].append(str(PORT))
                except Exception:
                    pass

        # Print output
        if print_output:
            print("Loading devices info...\n")
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
        # Load all connected devices
        self.devices = self.connected_devices()

    # This is based on devices that were registered with self.load_devices()
    def analyse_ports(self):
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


class Device():

    def __init__(self, port):
        self._port = port
        self.connected_devices = DeviceManager()
        self.connected_devices.load_devices()

    @property
    def port(self):
        if self.connected_devices.is_port_in_use(self._port):
            return self._port
        else:
            return None


class MbColorSensor(ColorSensor, Device):

    def __init__(self, port):
        try:
            ColorSensor(port)
            Device.__init__(self, port)
        except Exception:
            status_msg(False, "Failed to initalize motor!")


class MbGyroSensor(Device):

    def __init__(self, port, positive_direction=True):
        self.sensor = Ev3devSensor(port)  
        self.init_port = port
        self.direction = 1 if positive_direction else -1   
        self.angle_counter = 0
        Device.__init__(self, port)

    def calibrate(self):
        try:
            for _ in range(3):
                self.sensor.read("GYRO-CAL")
                wait(100)
                if self.angle() == 0:
                    break
            wait(100)
        except Exception:
            status_msg(False, ".calibrate()", "Gyro Sensor", self.init_port)

    def angle(self):
        try:
            return (int(self.sensor.read("GYRO-ANG")[0]) * self.direction) - self.angle_counter
        except Exception:
            status_msg(False, ".angle()", "Gyro Sensor", self.init_port)

    def reset(self):
        try:
            self.angle_counter = int(self.sensor.read("GYRO-ANG")[0]) * self.direction
        except Exception:
            status_msg(False, ".reset()", "Gyro Sensor", self.init_port)

    def __str__(self):
        return "Gyro Properties:\n-----------------\nPort: " + str(self.port) + "\nDefault Direction: " + str(self.direction)
