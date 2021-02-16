#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Color, Button
from time import sleep


class Screen():
    def __init__(self, labels):
        self.labels = labels


class Menu():
    def __init__(self, labels):
        self.ev3 = EV3Brick()
        self.ev3.screen.clear()
        self.screen_width = self.ev3.screen.width - 1
        self.screen_height = self.ev3.screen.height
        self.labels = labels
        self.label_container_width = self.screen_width
        self.label_container_height = self.screen_height/len(self.labels)
        self.defaulf_font_height = 16
        self.active_label = 0
        self.label_color = Color.BLACK
        self.active_label_color = Color.WHITE

    def clear_screen(self):
        self.ev3.screen.clear()

    def draw(self):
        last_container_pos = -3
        label_color = Color.WHITE
        self.ev3.screen.clear()
        for label in self.labels:
            if self.labels.index(label) == self.active_label:
                self.ev3.screen.draw_box(
                    1, last_container_pos * ((self.active_label+2)), self.label_container_width, self.label_container_height, fill=True)
                self.label_color = self.active_label_color
            else:
                self.label_color = Color.BLACK

            # Draw and center vertically the label inside its rectangle
            self.ev3.screen.draw_text(10, last_container_pos - 2 + (
                self.label_container_height-1) / 2 - self.defaulf_font_height/2, label.upper(), text_color=self.label_color)
            last_container_pos += self.label_container_height
            # Underline the label
            self.ev3.screen.draw_line(
                0, last_container_pos, self.screen_width, last_container_pos)

    def main(self):
        last_pressed_button = None
        self.draw()
        while True:
            print(self.ev3.buttons.pressed())
            pressed_buttons = self.ev3.buttons.pressed()
            print("active", self.active_label)
            if Button.RIGHT in pressed_buttons:
                print("down")
                if self.active_label < len(self.labels) - 1:
                    self.active_label += 1
                self.draw()
            elif Button.LEFT in pressed_buttons:
                print("up")
                if self.active_label > 0:
                    self.active_label -= 1
                self.draw()
            sleep(0.09)
