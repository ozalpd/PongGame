import math
from turtle import Turtle
from pong_screen import LINE_COLOR

COLOR_ON = "#D0E6D8"
COLOR_OFF = "#39424A"
FONT = ('Courier', 64, 'normal')
SEGMENT_SIZE = 14


class ScoreBoard:
    def __init__(self, pos_x: int, pos_y: int):
        self.digits = []
        self.score = 0
        for i in range(3):
            d = SevenSegmentDisplay(pos_x - (i * 3 * SEGMENT_SIZE), pos_y)
            self.digits.append(d)

    def increase_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        for d in self.digits:
            d.turn_off()
        self.digits[0].write_digit(self.score % 10)
        if self.score >= 100:
            self.digits[2].write_digit(math.floor(self.score / 100))
        if self.score >= 10:
            self.digits[1].write_digit(math.floor(self.score / 10))


class SevenSegmentDisplay:
    def __init__(self, pos_x: int, pos_y: int):
        self.segments = []
        for i in range(7):
            t = Turtle("square")
            t.penup()
            t.color(COLOR_OFF)
            t.shapesize(stretch_wid=0.25, stretch_len=1)
            t.goto(pos_x, pos_y)
            if i > 2:
                t.right(90)
            self.segments.append(t)
        self.segments[0].sety(pos_y + SEGMENT_SIZE)
        self.segments[1].sety(pos_y - SEGMENT_SIZE)
        self.segments[2].sety(pos_y - 3 * SEGMENT_SIZE)
        self.segments[3].setx(pos_x - SEGMENT_SIZE)
        self.segments[4].goto(pos_x - SEGMENT_SIZE, pos_y - 2 * SEGMENT_SIZE)
        self.segments[5].setx(pos_x + SEGMENT_SIZE)
        self.segments[6].goto(pos_x + SEGMENT_SIZE, pos_y - 2 * SEGMENT_SIZE)

    def turn_off(self):
        for s in self.segments:
            s.color(COLOR_OFF)

    def write_digit(self, dig_nr: int):
        digit = dig_nr % 10
        for s in self.segments:
            s.color(COLOR_ON)
        if digit == 0:
            self.segments[1].color(COLOR_OFF)
        elif digit == 1:
            for i in range(5):
                self.segments[i].color(COLOR_OFF)
        elif digit == 2:
            self.segments[3].color(COLOR_OFF)
            self.segments[6].color(COLOR_OFF)
        elif digit == 3:
            self.segments[3].color(COLOR_OFF)
            self.segments[4].color(COLOR_OFF)
        elif digit == 4:
            self.segments[0].color(COLOR_OFF)
            self.segments[2].color(COLOR_OFF)
            self.segments[4].color(COLOR_OFF)
        elif digit == 5:
            self.segments[5].color(COLOR_OFF)
            self.segments[4].color(COLOR_OFF)
        elif digit == 6:
            self.segments[5].color(COLOR_OFF)
        elif digit == 7:
            for i in range(1, 5):
                self.segments[i].color(COLOR_OFF)
        elif digit == 9:
            self.segments[4].color(COLOR_OFF)
