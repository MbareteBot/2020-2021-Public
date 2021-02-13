#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.iodevices import Ev3devSensor
from pybricks.ev3devices import Motor
from pybricks.parameters import Stop
from pybricks.tools import wait
from pybricks.parameters import Port, Direction


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

        # All available motors
        self.left_steering_motor = 0
        self.right_steering_motor = 0
        self.left_action_motor = 0
        self.right_action_motor = 0

        self.motor_direction = Direction.CLOCKWISE

        # Parameters
        self.full = 0
        self.steering = 0
        self.action = 0

    def set_steering_motors(self, left_motor_port, right_motor_port, default_direction=True):

        if not default_direction:
            self.motor_direction = Direction.COUNTERCLOCKWISE

        self.left_steering_motor = Motor(left_motor_port, self.motor_direction)
        self.right_steering_motor = Motor(
            right_motor_port, self.motor_direction)

    def set_action_motors(self, left_motor_port, right_motor_port):

        self.left_action_motor = Motor(left_motor_port)
        self.right_action_motor = Motor(right_motor_port)

    def run(self, motor, degrees, speed=100, duty_limit=20):

        raw_degrees = degrees
        degrees = abs(degrees)
        self.SpeedControl.reset()
        motor.reset_angle(0)

        Running = True

        moved_enough = False

        if degrees > 0:
            orientation = 1
        else:
            orientation = -1

        while Running:

            if abs(motor.angle()) < degrees/2:
                error_value = degrees - (degrees - abs(motor.angle()))
            else:
                error_value = degrees - abs(motor.angle())

            if error_value > degrees * 0.25 and moved_enough == False:
                moved_enough = True

            if moved_enough:

                if (motor.speed() / 8) < duty_limit:
                    Running = False
                    motor.hold()
                    wait(100)

                if error_value < 0.1 and error_value > -0.1:
                    Running = False
                    motor.hold()
                    wait(100)

            self.SpeedControl.execute(error_value, speed * 0.007)

            motor.dc(self.SpeedControl.output * orientation)

        Running = False

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
            raise Exception("""Motor to stop should be named as following :
                                        - self.Motors.steering
                                        - self.Motors.action
                                        - self.Motors.full """)
        print("stop")
        wait(250)


class ColorSensorManager():

    # Class dedicated to control up to 3 color sensors (one in the left part of the robot,
    # another one in the right part and a third one (probably to recognize attachments by a color code).

    def __init__(self):

        self.left_colorSensor = 0
        self.right_colorSensor = 0
        self.front_colorSensor = 0

    # The following functions lets you either initialize a sensor to an ev3 port or get
    # the reflected value reading from that sensor.

    def left_sensor(self, port=0):

        if port != 0:
            self.left_colorSensor = Ev3devSensor(port)
        else:
            return int(self.left_colorSensor.read("COL-REFLECT")[0])

    def right_sensor(self, port=0):

        if port != 0:
            self.right_colorSensor = Ev3devSensor(port)
        else:
            return int(self.right_colorSensor.read("COL-REFLECT")[0])

    def front_sensor(self, port=0):

        if port != 0:
            self.front_colorSensor = Ev3devSensor(port)
        else:
            return int(self.front_colorSensor.read("COL-REFLECT")[0])


class GyroSensorManager():

    # This class is only meant to control 1 GyroSensor

    def __init__(self):

        self.gyroSensor = 0
        self.gyro_direction = 1

    # You can also set the gyro to return an opposite value

    def set_sensor(self, port, set_inverse_direction=False):

        if set_inverse_direction:
            self.gyro_direction = -1

        self.gyroSensor = Ev3devSensor(port)

    def reset(self):

        while True:

            self.gyroSensor.read("GYRO-CAL")

            wait(200)

            if self.get_angle() == 0:
                break

        wait(100)

    # This function returns the current gyro angle multiplied by 1 or -1

    def get_angle(self):

        try:
            return int(self.gyroSensor.read("GYRO-ANG")[0]) * self.gyro_direction
        except:
            raise Exception(
                "Check if GyroSensor is initalized on a correct Port")
