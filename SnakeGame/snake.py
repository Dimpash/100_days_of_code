from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake_body = []
        # for i in range(0, 3):
        #     self.add_segment((-i*20, 0))
        # self.head = self.snake_body[0]
        self.create_snake()


    def add_segment(self, position):
        self.snake_body.append(Turtle(shape="square"))
        self.snake_body[-1].color("white")
        self.snake_body[-1].penup()
        self.snake_body[-1].goto(position)

    def create_snake(self):
        for segm in self.snake_body:
            segm.goto(1000, 1000)
        self.snake_body = []
        for i in range(0, 3):
            self.add_segment((-i * 20, 0))
        self.head = self.snake_body[0]

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move(self):
        for segm_n in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segm_n - 1].xcor()
            new_y = self.snake_body[segm_n - 1].ycor()
            self.snake_body[segm_n].setx(new_x)
            self.snake_body[segm_n].sety(new_y)
        self.head.forward(MOVE_DISTANCE)
        # self.snake_body[0].setx(self.snake_body[0].xcor() + MOVE_DISTANCE)
        # self.snake_body[0].sety(self.snake_body[0].ycor())



