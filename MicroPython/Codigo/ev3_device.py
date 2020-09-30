#!/usr/bin/env pybricks-micropython
from pybricks.iodevices import Ev3devSensor
from pybricks.parameters import Port, Direction

class MotorManager():

    def __init__(self):

        self.left_steeringMotor = 0
        self.right_steeringMotor = 0
        self.letf_mainMotor = 0
        self.right_mainMotor = 0

        self.motor_direction = Direction.CLOCKWISE
        self.gyro_direction = 1


    def setMotors(self, left_motor_port, right_motor_port, set_inverse_direction = False):

        if set_inverse_direction:
            self.motor_direction = Direction.COUNTERCLOCKWISE

        self.left_steeringMotor = Motor(left_motor_port, self.motor_direction)
        self.right_steeringMotor = Motor(right_motor_port, self.motor_direction)



    def reset(self):

        self.left_steeringMotor.reset_angle(0)
        self.right_steeringMotor.reset_angle(0)


    def stop(self):

        Motors.left_steeringMotor.hold()
        Motors.right_steeringMotor.hold()
        wait(250)


    
class ColorSensorManager():

    def __init__(self):

        self.sensors = [self.left_colorSensor = 0,
                        self.right_colorSensor = 0,
                        self.top_colorSensor = 0]


    def setLeftSensor(self, port):

        self.sensors[0] = Ev3devSensor(port)


    def setRightSensor(self, port):

        self.sensors[1] = Ev3devSensor(port)


    def setFrontSensor(self, port):

        self.sensors[2] = Ev3devSensor(port)

    def getReflected(self):

        sensor_values = []

        for sensor in range(0, len(self.sensors)):
            if self.sensors[sensor] != 0:
                sensor_values.append(int(self.sensors[sensor].read("COL-REFLECT")[0]))

        return sensor_values

        
        
    
class GyroSensorManager():

    def __init__(self):

        self.gyroSensor = 0
        self.gyro_direction = 1

    def setSensor(self, port, set_inverse_direction):

        if set_inverse_direction:
            self.gyro_direction = -1

        self.gyroSensor = Ev3devSensor(port)

    def reset(self):

        self.gyroSensor.read("GYRO-CAL")


    def getAngle(self):

        return int(self.gyroSensor.read("GYRO-ANG")[0])



