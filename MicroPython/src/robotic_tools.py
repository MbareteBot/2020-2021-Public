#!/usr/bin/env pybricks-micropython


from pybricks.ev3devices import (Motor, ColorSensor, GyroSensor, TouchSensor)
from pybricks.parameters import Port
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import Font
import math
ev3 = EV3Brick()
ev3.screen.clear()
ev3.screen.set_font(Font(size=1))
MOTORS_PORTS = [Port.A, Port.B, Port.C, Port.D]
SENSORS_PORTS = [Port.S1, Port.S2, Port.S3, Port.S4]
AVAILABLE_SENSORS = [ColorSensor, GyroSensor, TouchSensor]
MOTORS = {
    "Motor": [],
    "Port": []
}
SENSORS = {
    "Sensor": [],
    "Port": []
}


def consoleMsg(status, device, port):
    print(("[INFO] Found" if status else "[INFO] Didnt found"),
          device.__name__, "on", port)


def ev3Msg(status, device, port):
    ev3.screen.print(("[INFO] Found" if status else "[INFO] Didnt found"),
                     device.__name__, "on", port)


class RoboticTools():

    def devices_analysis(self):
        print("Loading devices info...")
        print("[Motors Report]\n")
        # LOOK FOR MOTORS IN EVERY PORT
        ev3.screen.print("\nMOTORS:")
        for PORT in MOTORS_PORTS:
            try:
                MOTORS["Motor"].append(Motor(PORT))
                MOTORS["Port"].append(str(PORT))
                consoleMsg(True, Motor, PORT)
                ev3Msg(True, Motor, PORT)
            except Exception:
                consoleMsg(False, Motor, PORT)
                ev3Msg(False, Motor, PORT)

        # LOOK FOR EVERY SINGLE SENSOR TYPE IN EVERY PORT
        print("\n\n[Sensors report]")
        ev3.screen.print("\nSENSORS:")
        for SENSOR in AVAILABLE_SENSORS:
            print("\nLooking for", SENSOR.__name__, "in every port")
            for PORT in SENSORS_PORTS:
                try:
                    SENSORS["Sensor"].append(SENSOR(PORT))
                    SENSORS["Port"].append(str(PORT))
                    consoleMsg(True, SENSOR, PORT)
                    ev3Msg(True, SENSOR, PORT)
                except:
                    consoleMsg(False, SENSOR, PORT)
                    ev3Msg(False, SENSOR, PORT)

        print("\nDevices Found:")
        print("Motors:")
        if len(MOTORS["Motor"]) > 0:
            for PORT in MOTORS["Port"]:
                print("Motor in", PORT)
        else:
            print("No motor found")

        print("\nSensors:")
        if len(SENSORS["Sensor"]) > 0:
            for SENSOR, PORT in zip(SENSORS["Sensor"], SENSORS["Port"]):
                print(type(SENSOR).__name__, "in", PORT)
        else:
            print("No sensor found")

    def degrees_to_cm(self, degrees, wheel_diameter):

        return (degrees * (wheel_diameter * math.pi)) / 360

    def cm_to_degrees(self, cm, wheel_diameter):

        return (cm / (wheel_diameter * math.pi)) * 360
