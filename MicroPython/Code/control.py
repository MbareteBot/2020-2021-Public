import math


# This class is dedicated to run a PID calculation based on some parameters and its values can be used
# to control the robot.

class PIDSystem():

    def __init__(self):

        # The diferent PID values are set as arrays, that reason for is that you can use
        # the --same function-- to get a PID calculation multiple times in a --single loop--

        self.integral_value = []
        self.derivative_value = []
        self.error_value = []
        self.last_error_value = []
        self.pid_output = []

        self.max_integral_value = 110


    # This funtion needs an error_value and other values to run the PID calculation. 
    # and the last value it takes is an index parameter. 

    # An example for this is that you want to use this function twice in the same --loop--,
    # maybe one to control the robot heading and another to control the robot speed.
    # If you simply have all the PID parameters as variables, and use the same funtion twice in the same loop
    # those PID calculation funtions would overwrite each other.

    # That is why we set them as array, so that the programmer simply chooses wich position in the array
    # its parameters would take place. For example: to control the robot heading the programmer would only use
    # the first index, and to control the speed he would use the second index.


    # Example: 

    # while True:

    #   setPid(heading_error, kp, ki, kd, 0) ---> the heading calculation in first index

    #   setPid(speed_error, kp, ki, kd, 1) ---> the speed calculation in the second index



    def setPID(self, error_value, kp, ki, kd, index = 0):

        # Checks if the that index space is available, if its not, 
        # simply add 0 and that would occupate the index value.

        if index > len(self.error_value) - 1:
            self.integral_value.append(0)
            self.derivative_value.append(0)
            self.error_value.append(0)
            self.last_error_value.append(0)
            self.pid_output.append(0)


        self.error_value[index] = error_value
        self.integral_value[index] += error_value
        self.derivative_value[index] = error_value  - self.last_error_value[index]
        self.last_error_value[index] = error_value

        if self.integral_value[index] > self.max_integral_value:
            self.integral_value[index] = self.max_integral_value

        elif self.integral_value[index] < -self.max_integral_value:
            self.integral_value[index] = -self.max_integral_value


        self.pid_output[index] = (self.error_value * kp) + (self.integral_value * ki) + (self.kd_value * kd)



    def reset(self):

        self.integral_value = []
        self.derivative_value = []
        self.error_value = []
        self.last_error_value = []
        self.pid_output = []

        self.max_integral_value = 110






# -----------------------------------------------------------

class OdometrySystem:

    # ----This Class is still in development----
    # ----We are still working on this class, so please, give us your feedback about this code---
    # ----We didnt have much time to test it, so its basically mostly theoretical so far---

    # This class is used to implement an odometry sistem for the robot.

    def __init__(self):

        self.global_x_pos = 0
        self.global_y_pos = 0

        self.global_x_pos_log = []
        self.global_y_pos_log = []



    # This function updates the robot current position, it recieves how much each wheel has moved and 
    # the angle the robot is oriented to.

    def updatePos(self, left_motor_degrees, right_motor_degrees, heading):

        left_motor = ((left_motor * (6.24 * math.pi)) / 360)  - last_left_motor_degrees
        right_motor =  ((right_motor * (6.24 * math.pi)) / 360) - last_right_motor_degrees 

        motors_average_degrees = round((left_motor + right_motor) /2)


        self.global_x_pos += round(motors_average_degrees * math.cos(math.radians(heading)),1)
        self.global_y_pos += round(motors_average_degrees * math.sin(math.radians(-heading)),1)

        print("X:",self.global_x_pos)
        print("Y:",self.global_y_pos)

        last_left_motor_degrees = left_motor_degrees
        last_right_motor_degrees = right_motor_degrees






    def goTo(self, x_target, y_target, MoveStraight_function, Turn_function):

        # This function is used to make the robot go to a desired position.
        # It takes as parameters an x,y target, a funtion that makes the robot move in a straight line and
        # another funtion that makes the robot turn.

        # In this way this function takes that x,y target to get the angle and distance between the current position and
        # the desired position and uses those funtions to actually move the robot to that position

        # The MoveStraight_function should recive as a parameter a distance target im cm.
        # The Turn_function should recive as a parameter a target angle in degrees.
        
        print(self.global_x_pos_log, self.global_y_pos_log, self.global_x_pos, self.global_y_pos)
        print("Target X,Y:", x,y)

        self.global_x_pos_log.append(self.global_x_pos)
        self.global_y_pos_log.append(self.global_y_pos)

        self.robot_moves += 1

        if self.robot_moves >= 2:

            vector1_relX = x - self.global_x_pos
            vector1_relY = y - self.global_y_pos

            vector2_relX = self.global_x_pos_log[-2] - self.global_x_pos
            vector2_relY = self.global_y_pos_log[-2] - self.global_y_pos

            cross_product = vector1_relX  * vector2_relY - vector1_relY * vector2_relX
            dot_product = (vector1_relX  * vector2_relX) + (vector1_relY * vector2_relY)

            target_heading = math.acos((dot_product / (math.sqrt(vector1_relX**2 + vector1_relY**2) * math.sqrt(vector2_relX**2 + vector2_relY**2))))

            if cross_product < 0:
                heading = (180 - (target_heading * (180/math.pi))) * -1
            else:
                heading = 180 - (target_heading * (180/math.pi)) 



        else:
            heading = math.atan2(y_target, x_target) * 180/math.pi




        distance_cm = round(math.sqrt((x - self.global_x_pos)**2 + (y - self.global_y_pos)**2 ),1)
            
        distance_degrees = ((distance_cm / (6.24 * math.pi)) * 360)


        if heading != 0:
            Turn_function(-heading)


        self.updatePos()


        MoveStraight_function(distance_cm, 0, 20)

        
        self.updatePos()



        print("X:",self.global_x_pos)
        print("Y:",self.global_y_pos)








class RoboticTools():

    # Finally this is a class that provides the programmer with tools that might be useful in robotics.
    # Kind of empty right now, but its pretty useful.

    def degreesToCm(self, degrees, wheel_diameter):

        return (degrees * (wheel_diameter * math.pi)) / 360


    def cmToDegrees(self, cm, wheel_diameter):

        return (cm / (wheel_diameter * math.pi)) * 360



