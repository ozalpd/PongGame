from turtle import Screen, Turtle

HALF_WIDTH: int = 400  # When WIDTH or HEIGHT is divided by 2 result is float,
HALF_HEIGHT: int = 300  # I don't want to cast them to int repeatedly
WIDTH: int = 2 * HALF_WIDTH
HEIGHT: int = 2 * HALF_HEIGHT
BG_COLOR: str = "#2F373E"
LINE_COLOR: str = "#E6E6E6"


class PongScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.bgcolor(BG_COLOR)
        self.screen.tracer(0)
        self.is_game_on = True
        self.game_speed = 1
        self.set_title()
        self.player_exiting = False
        pen = Turtle()
        pen.penup()
        pen.color(LINE_COLOR)
        pen.pensize(4)
        pen.hideturtle()
        pen.speed("fastest")
        pen.sety(-HALF_HEIGHT)
        draw = True
        for i in range(-HALF_HEIGHT - 2, HALF_HEIGHT + 10, 12):
            if draw:
                pen.pendown()
                draw = False
            else:
                pen.penup()
                draw = True
            pen.sety(i)
        self.screen.update()

    def exit_game(self):
        self.is_game_on = False
        self.player_exiting = True

    def increase_speed(self):
        self.game_speed += 1
        self.set_title()

    def decrease_speed(self):
        if self.game_speed > 1:
            self.game_speed -= 1
            self.set_title()

    def set_title(self):
        self.screen.title(f"Pop's Pong Game,   speed: {self.game_speed}")
