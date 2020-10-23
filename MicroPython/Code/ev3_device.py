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
        self.left_steeringMotor = 0
        self.right_steeringMotor = 0
        self.left_actionMotor = 0
        self.right_actionMotor = 0



        self.motor_direction = Direction.CLOCKWISE
        

        # Parameters
        self.full = 0
        self.steering = 0
        self.action = 0


    def setSteeringMotors(self, left_motor_port, right_motor_port, set_inverse_direction = False):

        if set_inverse_direction:
            self.motor_direction = Direction.COUNTERCLOCKWISE

        self.left_steeringMotor = Motor(left_motor_port, self.motor_direction)
        self.right_steeringMotor = Motor(right_motor_port, self.motor_direction)



    def setActionMotors(self, left_motor_port, right_motor_port):

        self.left_actionMotor = Motor(left_motor_port)
        self.right_actionMotor = Motor(right_motor_port)



    def run(self, motor, degrees, speed = 100, duty_limit = 20):


        self.SpeedControl.reset()
        self.Motors.reset(self.Motors.steering)

        Running = True

        while Running:


            if motor.angle() < degrees/2:
                error_value = degrees - (degrees - motor.angle())
            else:
                error_value = degrees - motor.angle()



            if error_value > 50:
                if motor.speed() < duty_limit:
                    Running = False
                    motor.hold()
                    wait(100)                    



            if error_value < 0.1 and error_value > -0.1:
                Running = False
                motor.hold()
                wait(100)



            SpeedControl.execute(error_value, speed * 0.007)

            motor.dc(SpeedControl.output)  





    def reset_angle(self, motors = self.full):

        if motors == self.steering or self.full:
            self.left_steeringMotor.reset_angle(0)
            self.right_steeringMotor.reset_angle(0)

        if motors == self.action or self.full:
            self.left_actionMotor.reset_angle(0)
            self.right_actionMotor.reset_angle(0)


        else:
            raise Exception("""Motors to reset should be named as following :
                                        - self.Motors.steering
                                        - self.Motors.action
                                        - self.Motors.full """)




    def stop(self, motors = self.full):

        if motors == self.steering or self.full:
            self.left_steeringMotor.hold()
            self.right_steeringMotor.hold()

        if motors == self.action or self.full:
            self.left_actionMotor.hold()
            self.right_actionMotor.hold()


        else:
            raise Exception("""Motor to stop should be named as following :
                                        - self.Motors.steering
                                        - self.Motors.action
                                        - self.Motors.full """)     

    
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

    # This class is only meant to control 1 GyroSensor

    def __init__(self):

        self.gyroSensor = 0
        self.gyro_direction = 1


    # You can also set the gyro to return an opposite value

    def setSensor(self, port, set_inverse_direction = False):

        if set_inverse_direction:
            self.gyro_direction = -1

        self.gyroSensor = Ev3devSensor(port)



    def reset(self):

        while True:

            self.gyroSensor.read("GYRO-CAL")

            wait(200)

            if self.getAngle() == 0:
                break

        wait(100)




    # This function returns the current gyro angle multiplied by 1 or -1
    def getAngle(self):

        return int(self.gyroSensor.read("GYRO-ANG")[0]) * self.gyro_direction





class RobotParameters():

    def __init__(self):

        self.left = "left"
        self.right = "right"
        self.front = "front"

        self.full = "full"





