#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.iodevices import Ev3devSensor
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor, TouchSensor
from pybricks.parameters import Stop, Port, Direction
from pybricks.tools import wait

from control import PIDSystem


# All this classes are used to control the ev3 devices (motors, gyro and color sensors).

# With this classes you can only have: 4 Motors, 1 Gyro and 3 Color Sensors

# All the sensors are set as Ev3devSensors from pybricks.iodevices. The main reason for this is that
# they can access to more features.


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

        # Parameters
        self.full = 0
        self.steering = 0
        self.action = 0

    def set_steering_motors(self, left_motor_port, right_motor_port, default_direction=True):

        if not default_direction:
            self.motor_direction = Direction.COUNTERCLOCKWISE

        self.left_steering_motor = Motor(left_motor_port, self.motor_direction)
        self.left_steering_motor.port = left_motor_port
        self.right_steering_motor = Motor(
            right_motor_port, self.motor_direction)
        self.right_steering_motor.port = right_motor_port

    def set_action_motors(self, left_motor_port, right_motor_port):

        self.left_action_motor = Motor(left_motor_port)
        self.right_action_motor = Motor(right_motor_port)

    def run(self, motor, degrees, speed=100, duty_limit=20):

        degrees = degrees
        motor.reset_angle(0)
        Running = True
        moved_enough = False

        while Running:

            error_value = degrees - motor.angle()

            if abs(error_value) > abs(degrees) * 0.25 and moved_enough == False:
                moved_enough = True

            if moved_enough:

                # if motor.speed() < duty_limit:
                #     Running = False
                #     motor.hold()
                #     wait(100)

                if error_value < 0.1 and error_value > -0.1:
                    print("finish")
                    Running = False
                    motor.hold()
                    wait(100)

            motor.dc(speed)

        print("done angle:", motor.angle())

    def reset_angle(self, motors):

        if motors == self.steering:
            self.left_steering_motor.reset_angle(0)
            self.right_steering_motor.reset_angle(0)

        elif motors == self.action:
            self.left_action_motor.reset_angle(0)
            self.right_action_motor.reset_angle(0)

        elif motors == self.full:
            self.left_steering_motor.reset_angle(0)
            self.right_steering_motor.reset_angle(0)
            self.left_action_motor.reset_angle(0)
            self.right_action_motor.reset_angle(0)

        else:
            raise Exception("""Motors to reset should be named as following :
                                        - self.Motors.steering
                                        - self.Motors.action
                                        - self.Motors.full """)

    def stop(self, motors):

        if motors == self.steering:
            self.left_steering_motor.hold()
            self.right_steering_motor.hold()

        elif motors == self.action:
            self.left_action_motor.hold()
            self.right_action_motor.hold()

        elif motors == self.full:
            self.left_steering_motor.hold()
            self.right_steering_motor.hold()
            self.left_action_motor.hold()
            self.right_action_motor.hold()
        else:
            raise Exception("""
Motor to stop should be named as following:
 - self.Motors.steering
 - self.Motors.action
 - self.Motors.full """)
        wait(250)


class ColorSensorManager():

    # Class dedicated to control up to 3 color sensors (one in the left part of the robot,
    # another one in the right part and a third one (probably to recognize attachments by a color code).

    def __init__(self):

        self.left_sensor = None
        self.right_sensor = None
        self.front_sensor = None

    # The following functions lets you either initialize a sensor to an ev3 port or get
    # the reflected value reading from that sensor.

    def set_left_sensor(self, port):
        self.left_sensor = ColorSensor(port)
        self.left_sensor.port = port

    def set_right_sensor(self, port):
        self.right_sensor = ColorSensor(port)
        self.right_sensor.port = port

    def set_front_sensor(self, port):
        self.front_sensor = ColorSensor(port)
        self.front_sensor.port = port


class GyroSensorManager():

    # This class is only meant to control 1 GyroSensor

    def __init__(self):
        self.sensor = None
        self.gyro_direction = 1

    # You can also set the gyro to return an opposite value

    def set_sensor(self, port, set_inverse_direction=False):
        if set_inverse_direction:
            self.gyro_direction = -1
        self.sensor = Ev3devSensor(port)
        try:
            self.sensor.read("GYRO-ANG")
        except:
            raise Exception(
                """
A Gyro sensor is not connected to the specified port:
 * Check the cables to sensor.
 * Check the port settings in your script.
""")

    def calibrate(self):
        while True:
            self.gyro.read("GYRO-CAL")
            wait(200)
            if self.get_angle() == 0:
                break
        wait(100)

    # This function returns the current gyro angle multiplied by 1 or -1
    def get_angle(self):
        return int(self.sensor.read("GYRO-ANG")[0]) * self.gyro_direction


class DeviceManager():

    def __init__(self):
        self.motors_ports = [Port.A, Port.B, Port.C, Port.D]
        self.sensors_ports = [Port.S1, Port.S2, Port.S3, Port.S4]
        self.available_sensors = [ColorSensor, GyroSensor, TouchSensor]
        self.MOTORS = {
            "Motor": [],
            "Port": []
        }
        self.SENSORS = {
            "Sensor": [],
            "Port": []
        }

    def is_port_in_use(self, port):

        for motor_port in self.devices["Motors"]["Port"]:
            if str(port) == motor_port:
                return True

        for sensor_port in self.devices["Sensors"]["Port"]:
            if str(port) == sensor_port:
                return True
        return False

    def load_devices(self):
        print("Loading devices info...")
        # LOOK FOR MOTORS IN EVERY PORT
        for PORT in self.motors_ports:
            try:
                self.MOTORS["Motor"].append(type(Motor(PORT)).__name__)
                self.MOTORS["Port"].append(str(PORT))
            except:
                pass
        # LOOK FOR EVERY SINGLE SENSOR TYPE IN EVERY PORT
        for SENSOR in self.available_sensors:
            for PORT in self.sensors_ports:
                try:
                    self.SENSORS["Sensor"].append(type(SENSOR(PORT)).__name__)
                    self.SENSORS["Port"].append(str(PORT))
                except:
                    pass

        # Print output
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

        # Load all devices
        self.devices = {"Motors": self.MOTORS, "Sensors": self.SENSORS}

        return self.devices

    # This is based on devices that were recorded with self.load_devices()
    def analyse_ports(self):
        for port in self.devices["Motors"]["Port"]:
            try:
                eval(devices["Motors"][0])(Port)
            except:
                print("[ ERROR ] Motor is missing in", port)
        for sensor, port in zip(self.devices["Sensors"]):
            eval(sensor)
