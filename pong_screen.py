from turtle import Screen, Turtle

HALF_WIDTH: int = 400  # When WIDTH or HEIGHT is divided by 2 result is float,
HALF_HEIGHT: int = 300  # I don't want to cast them to int repeatedly
WIDTH: int = 2 * HALF_WIDTH
HEIGHT: int = 2 * HALF_HEIGHT


class PongScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.bgcolor("#2F373E")
        self.screen.title("Pop's Pong Game")
        self.screen.tracer(0)
        pen = Turtle()
        pen.penup()
        pen.color("#E6E6E6")
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

    def exitonclick(self):
        self.screen.exitonclick()

    def listen(self, xdummy=None, ydummy=None):
        self.screen.listen(xdummy, ydummy)

    def update(self):
        self.screen.update()
