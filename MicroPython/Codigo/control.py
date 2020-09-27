
class PIDSystem():

    def __init__(self):

        self.ki_value = 0
        self.kd_value = 0
        self.kp_value = 0

        self.integral_value = 0
        self.derivative_value = 0
        self.error_value = 0
        self.last_error_value = 0
        self.pid_output = 0

        self.max_integral_value = 110


    def setPID(self, error_value, kp, kd, ki):

        self.kp_value = kp
        self.ki_value = kd
        self.kd_value = ki    

        self.error_value = error_value
        self.integral_value += self.error_value
        self.derivative_value = self.error_value  - self.last_error_value
        self.last_error_value = self.error_value

        if self.integral_value > self.max_integral_value:
            self.integral_value = self.max_integral_value

        if self.integral_value < -self.max_integral_value:
            self.integral_value = -self.max_integral_value


        self.pid_output = (self.error_value * self.kp_value) + (self.integral_value * self.ki_value) + (self.kd_value * self.kd_value)



    def reset(self):

        self.integral_value = 0
        self.derivative_value = 0
        self.error_value = 0
        self.last_error_value = 0
        self.pid_output = 0

        self.max_integral_value = 110


class OdometrySystem:

    def __init__(self):

        self.global_x_pos = 0
        self.global_y_pos = 0

        self.global_x_pos_log = []
        self.global_y_pos_log = []


    def updatePos(self, steeringMotors_average, heading):

        left_motor = ((self.left_steeringMotor.angle() * (6.24 * math.pi)) / 360)  - self.left_motor_degrees
        right_motor =  ((self.right_steeringMotor.angle() * (6.24 * math.pi)) / 360) - self.last_right_motor_degrees 

        motorsAverageDegrees = round((left_motor + right_motor) /2)


        self.global_x_pos += round(steeringMotors_average * math.cos(math.radians(heading)),1)
        self.global_y_pos += round(steeringMotors_average * math.sin(math.radians(-heading)),1)

        print("X:",self.global_x_pos)
        print("Y:",self.global_y_pos)


    def GoTo(self, x, y, MoveStraight_method, Turn_method):
        
        print(self.global_x_pos_log, self.global_y_pos_log, self.global_x_pos, self.global_y_pos)
        print("Target X,Y:", x,y)

        self.global_x_pos_log.append(self.global_x_pos)
        self.global_y_pos_log.append(self.global_y_pos)
        self.robot_moves += 1

        if self.robot_moves >= 2:

            Vector1_relX = x - self.global_x_pos
            Vector1_relY = y - self.global_y_pos

            Vector2_relX = self.global_x_pos_log[-2] - self.global_x_pos
            Vector2_relY = self.global_y_pos_log[-2] - self.global_y_pos

            cross_product = Vector1_relX  * Vector2_relY - Vector1_relY * Vector2_relX
            dot_product = (Vector1_relX  * Vector2_relX) + (Vector1_relY * Vector2_relY)

            target_heading = math.acos((dot_product / (math.sqrt(Vector1_relX**2 + Vector1_relY**2) * math.sqrt(Vector2_relX**2 + Vector2_relY**2))))

            if cross_product < 0:
                heading = (180 - (target_heading * (180/math.pi))) * -1
            else:
                heading = 180 - (target_heading * (180/math.pi)) 



        else:
            heading = math.atan2(y,x) * 180/math.pi




        distance_cm = round(math.sqrt((x - self.global_x_pos)**2 + (y - self.global_y_pos)**2 ),1)
            
        distance_degrees = ((distance_cm / (6.24 * math.pi)) * 360)

        print("Target Heading, DistanceCM, DistanceDegrees:", heading, distance_cm, distance_degrees)


        if heading != 0:
            Turn_method(-heading)

        self.updatePos()


        MoveStraight_method(distance_cm, 0, 20)

        
        self.updatePos()



        print("X:",self.global_x_pos)
        print("Y:",self.global_y_pos)