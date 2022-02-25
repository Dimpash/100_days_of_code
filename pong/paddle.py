from turtle import Turtle


PADDLE_WIDTH = 20
PADDLE_LENGTH = 100
PADDLE_SEGMENT_COUNT = 5
MOVE_DISTANCE = 20



class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(position)
        self.setheading(90)

    def up_0(self):
        self.setheading(90)

    def down_0(self):
        self.setheading(270)

    def up(self):
        self.setheading(90)
        self.move()

    def down(self):
        self.setheading(270)
        self.move()

    def move(self):
        if (self.ycor() <= -240 and self.heading() == 270) or (self.ycor() >= 250 and self.heading() == 90):
            pass
        else:
            self.forward(MOVE_DISTANCE)
