#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.iodevices import Ev3devSensor
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction

from control import PIDSystem



# All this clases are used to control the ev3 devices (motors, gyro and color sensors).

# With this classes you can only have: 4 Motors, 1 Gyro and 3 Color Sensors

# All the sensors are set as a Ev3devSensor from pybricks.iodevices. The main reason for this is that
# they can acces to more features.




# This MotorManager class is meant to be used to set 2 Steering motors and 2 "Action" motors dedicated to control attachments.

ev3 = EV3Brick()



class MotorManager():

    def __init__(self):

        self.Control = PIDSystem()

        self.left_steeringMotor = 0
        self.right_steeringMotor = 0

        self.left_actionMotor = 0
        self.right_actionMotor = 0

        self.motor_direction = Direction.CLOCKWISE
        self.gyro_direction = 1


    def setSteeringMotors(self, left_motor_port, right_motor_port, set_inverse_direction = False):

        if set_inverse_direction:
            self.motor_direction = Direction.COUNTERCLOCKWISE

        self.left_steeringMotor = Motor(left_motor_port, self.motor_direction)
        self.right_steeringMotor = Motor(right_motor_port, self.motor_direction)


    # This are the motors that control the attachments}
    # right now you can set them but they dont have a "personal" function
    def setActionMotors(self, left_motor_port, right_motor_port):

        self.left_actionMotor = Motor(left_motor_port)
        self.right_actionMotor = Motor(right_motor_port)



    def reset(self):

        self.left_steeringMotor.reset_angle(0)
        self.right_steeringMotor.reset_angle(0)


    def stop(self):

        Motors.left_steeringMotor.hold()
        Motors.right_steeringMotor.hold()
        wait(250)








 


class ColorSensorManager():

    #  Class dedicated to control up to 3 color sensors (one in the left part of the robot, 
    # another in the right part and a third one (probably to recognize attachments by a color code).


    def __init__(self):

        self.left_colorSensor = 0
        self.right_colorSensor = 0
        self.front_colorSensor = 0



    # The following functions lets you either set a sensor to a fisical port or get
    # the reflected value reading from the sensor
    def leftSensor(self, port = 0):

        if port != 0:
            self.left_colorSensor = Ev3devSensor(port)
        else:
            return int(self.left_colorSensor.read("COL-REFLECT")[0])


    def rightSensor(self, port = 0):
    
        if port != 0:
            self.right_colorSensor = Ev3devSensor(port)
        else:
            return int(self.right_colorSensor.read("COL-REFLECT")[0])



    def frontSensor(self, port = 0):

        if port != 0:
            self.front_colorSensor = Ev3devSensor(port)
        else:
            return int(self.front_colorSensor.read("COL-REFLECT")[0])






        


class GyroSensorManager():

    # This class is only meant to control 1 GyroSensor and the sensor is set as a Ev3devSensor so it can have acces to more methods
    # such as the "GYRO-CAL" mode.
    
    def __init__(self):

        self.gyroSensor = 0
        self.gyro_direction = 1


    # You can also set the gyro to return an opposite value

    def setSensor(self, port, set_inverse_direction = False):

        if set_inverse_direction:
            self.gyro_direction = -1

        self.gyroSensor = Ev3devSensor(port)



    def reset(self):

        self.gyroSensor.read("GYRO-CAL")



    # This return the current gyro angle multiplied by 1 or -1
    def getAngle(self):

        return int(self.gyroSensor.read("GYRO-ANG")[0]) * self.gyro_direction



