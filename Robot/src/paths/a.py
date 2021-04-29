#!/usr/bin/env pybricks-micropython

info = "a.py"

def color_code(Color):
    return Color.GREEN

def run(Robot):
    # bench
    Robot.drive(35, speed_kp=2)
    Robot.drive(15, -2, speed_kp=2.5)

    # slide
    Robot.Motors.left_action_motor.run_angle(800, 350)
    Robot.drive(-48, 1)
    Robot.wait(100)
    Robot.drive(30)
    Robot.turn(58)
    Robot.drive(63)
    Robot.Motors.right_action_motor.run_angle(800, 590)
    Robot.drive(-11, speed_kp=2)
    Robot.Motors.right_action_motor.run_angle(-800, 630)

    # basket
    Robot.drive(-20)
    Robot.drive_to_line(15, "BLACK", Robot.ColorSensors.right_sensor, speed_kp=1) 
    Robot.wait(100)
    Robot.drive(-6)
    Robot.wait(100)
    Robot.turn(-65)
    Robot.wait(100)
    Robot.drive(10)
    Robot.square_line()

    Robot.drive(23)
    Robot.turn(-61)
    Robot.run_async(Robot.Motors.left_action_motor.run_angle, (800, 200))
    Robot.drive(-12)
    Robot.Motors.left_action_motor.run_angle(-800, 550)
    Robot.drive(16)

    Robot.Motors.left_action_motor.run_angle(800, 4400)
    Robot.run_async(Robot.Motors.left_action_motor.run_angle, (-800, 3000))
    Robot.wait(700)
    Robot.drive(-17)
    Robot.turn(90)
    Robot.drive(-80, speed_kp=10)

# 1) Oro ( I) + Oxígeno 
# 2) Hierro ( III) + Oxígeno 
# 3) Bromo ( III) + Oxígeno 
# 4 Azufre ( VI) + Oxígeno 
# 5) Óxido de Litio + H2O 
# 6) Óxido de Bario + H2O 
# 7) Hidróxido de Aluminio + Ácido metafosforoso 
# 8) Hidróxido de Potasio + Ácido cloroso 