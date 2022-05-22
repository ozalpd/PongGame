import random
from turtle import Turtle
from pong_screen import PongScreen, LINE_COLOR, HALF_WIDTH, HALF_HEIGHT

MARGIN_TOP = 12
MARGIN_BOTTOM = 18


class Ball(Turtle):
    def __init__(self, pong: PongScreen):
        super().__init__(shape="square")
        self.color(LINE_COLOR)
        self.penup()
        self.direction = get_rand_direction()
        self.pong = pong
        self.sleep_time = 0.04

    def move(self):
        if self.is_on_top() or self.is_on_bottom():
            self.bounce(horizontally=False)
        x = self.xcor() + (self.direction[0] * self.pong.game_speed)
        y = self.ycor() + (self.direction[1] * self.pong.game_speed)
        self.goto(x, y)

    def beyond_left(self):
        return self.is_going_left() and self.xcor() <= -HALF_WIDTH

    def beyond_right(self):
        return self.is_going_right() and self.xcor() >= HALF_WIDTH

    def bounce(self, horizontally: bool):
        dir_x = self.direction[0]
        dir_y = self.direction[1]
        if horizontally:
            dir_x *= -1
        else:
            dir_y *= -1
        self.direction = (dir_x, dir_y)

    def check_collision(self, left_paddle: Turtle, right_paddle: Turtle):
        xcor = self.xcor()
        can_collide = self.is_going_left() and left_paddle.xcor() + 18 >= xcor
        if can_collide:
            if self.distance(left_paddle) < 60:
                self.bounce(horizontally=True)
                self.sleep_time *= 0.95
            return  # we don't need to check right paddle, if the left one is that close

        can_collide = self.is_going_right() and right_paddle.xcor() - 18 <= xcor
        if can_collide:
            if self.distance(right_paddle) < 60:
                self.bounce(horizontally=True)
                self.sleep_time *= 0.95

    def is_going_left(self):
        return self.direction[0] < 0

    def is_going_right(self):
        return self.direction[0] > 0

    def is_on_top(self):
        is_going_up = self.direction[1] > 0
        return is_going_up and self.ycor() >= HALF_HEIGHT - MARGIN_TOP

    def is_on_bottom(self):
        is_going_down = self.direction[1] < 0
        return is_going_down and self.ycor() <= MARGIN_BOTTOM - HALF_HEIGHT

    def refresh(self):
        self.direction = get_rand_direction()
        self.goto(0, 0)
        self.sleep_time = 0.04


def get_rand_direction():
    x = 0
    while x == 0:
        x = random.randint(-2, 2)
    y = 0
    speed_y = 3 - abs(x)  # to limit speed of ball
    while y == 0:
        y = random.randint(-1, 1)
    result = (x, y * speed_y)
    return result
