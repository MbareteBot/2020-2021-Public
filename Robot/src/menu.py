#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import Font
from pybricks.parameters import Color, Button
from time import sleep
from mbarete import Robot, Port
import threading
import robot


class Menu():
    def __init__(self, labels):
        self.ev3 = EV3Brick()
        self.ev3.screen.clear()
        self.screen_width = self.ev3.screen.width - 1
        self.screen_height = self.ev3.screen.height - 1
        self.labels = labels
        self.label_container_width = self.screen_width
        self.label_container_height = self.screen_height/len(self.labels)
        self.defaulf_font_height = 16
        self.active_label = 0

        self.main()

    def draw_menu(self):
        last_container_pos = -3
        self.ev3.screen.clear()
        for label in self.labels:
            if self.labels.index(label) == self.active_label:
                self.ev3.screen.draw_box(1, last_container_pos, self.label_container_width,
                                         last_container_pos + self.label_container_height, fill=True)
                label_color = Color.WHITE
            else:
                label_color = Color.BLACK

            # Draw and center vertically the label inside its rectangle
            self.ev3.screen.draw_text(10, last_container_pos - 2 + (
                self.label_container_height-1) / 2 - self.defaulf_font_height/2, label.upper(), text_color=label_color)

            last_container_pos += self.label_container_height
            # Underline the label
            self.ev3.screen.draw_line(
                0, last_container_pos, self.screen_width, last_container_pos)

    def draw_motor_control(self):

        self.ev3.screen.clear()
        self.ev3.screen.set_font(Font(size=40))

        labels_width = self.screen_width/3
        labels_height = self.screen_height/2

        # Output looks like this, the idea is to represent each button of the ev3 brick
        #  [D]
        # [C][B]
        #  [A]

        graphics_elements = [
            [self.ev3.screen.draw_box, [1, self.screen_height/2 - labels_height/2,
                                        labels_width, labels_height * 1.5, 10]],

            [self.ev3.screen.draw_text, [labels_width/2 - Font().text_width("C"),
                                         self.screen_height/2 - Font().text_height("C"), "C"]],

            [self.ev3.screen.draw_box, [labels_width, 1,
                                        labels_width * 2, labels_height, 10]],

            [self.ev3.screen.draw_text, [labels_width * 1.5 - Font().text_width("D"),
                                         labels_height/2 - Font().text_height("D"), "D"]],

            [self.ev3.screen.draw_box, [labels_width, self.screen_height/2,
                                        labels_width * 2, labels_height + self.screen_height/2, 10]],

            [self.ev3.screen.draw_text, [labels_width * 2.5 - Font().text_width("B")-1,
                                         self.screen_height/2 - Font().text_height("B"), "B"]],

            [self.ev3.screen.draw_box, [labels_width * 2, self.screen_height/2 - labels_height/2,
                                        labels_width * 3, labels_height * 1.5, 10]],

            [self.ev3.screen.draw_text, [labels_width * 1.5 - Font().text_width("A"),
                                         self.screen_height/2 + Font().text_height("A"), "A"]]]

        for element in graphics_elements:
            thread = threading.Thread(target=element[0], args=element[1])
            thread.start()

        self.handle_motor_control_input()

    def handle_motor_control_input(self):
        while True:
            pressed_buttons = self.ev3.buttons.pressed()
            if Button.LEFT in pressed_buttons:
                self.devices.right_action_motor.dc(50)
            elif Button.RIGHT in pressed_buttons:
                self.devices.right_action_motor.dc(-50)
            elif Button.DOWN in pressed_buttons:
                self.devices.left_steering_motor.dc(50)
            elif Button.UP in pressed_buttons:
                self.devices.right_steering_motor.dc(50)
            elif Button.CENTER in pressed_buttons:
                break
            else:
                self.devices.right_action_motor.brake()
                self.devices.left_action_motor.brake()
                self.devices.left_steering_motor.brake()
                self.devices.right_steering_motor.brake()

    def main(self):
        self.draw_menu()
        print("---Ev3---")
        while True:
            pressed_buttons = self.ev3.buttons.pressed()
            if Button.RIGHT in pressed_buttons or Button.DOWN in pressed_buttons:
                if self.active_label < len(self.labels) - 1:
                    self.active_label += 1
                self.draw_menu()
            elif Button.LEFT in pressed_buttons or Button.UP in pressed_buttons:
                if self.active_label > 0:
                    self.active_label -= 1
                self.draw_menu()
            elif Button.CENTER in pressed_buttons:
                if self.active_label == 0:
                    robot.main()

                elif self.active_label == 1:
                    self.devices = Robot().Motors
                    self.devices.set_steering_motors(Port.A, Port.D, False)
                    self.devices.set_action_motors(Port.B, Port.C)
                    self.ev3.screen.clear()
                    self.draw_motor_control()

                self.draw_menu()

            sleep(0.3)
