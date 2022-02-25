from turtle import Turtle


BALL_DIAMETER = 20
BALL_POSITION = (0, 0)
DEFAULT_TIME_OUT = 0.1


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)
        # self.ball.setheading(30)
        self.kx = 1
        self.ky = 1
        self.time_out = DEFAULT_TIME_OUT

    def move(self):
        new_x = self.xcor() + self.kx * 10
        new_y = self.ycor() + self.ky * 10
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.ky = -self.ky

    def bounce_paddle(self):
        self.kx = -self.kx
        self.faster()

    def start_position(self):
        self.goto(BALL_POSITION)
        self.bounce_paddle()
        self.time_out = DEFAULT_TIME_OUT

    def faster(self):
        if self.time_out > 0:
            self.time_out -= 0.005
