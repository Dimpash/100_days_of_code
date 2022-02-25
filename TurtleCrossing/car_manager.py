from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def add_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(choice(COLORS))
        new_car.setheading(180)
        new_car.penup()
        new_car.goto(x=300, y=randint(-250, 250))
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            if car.xcor() > -320:
                car.forward(self.move_distance)
            else:
                self.cars.remove(car)
        self.refresh_cars()

    def refresh_cars(self):
        if randint(0, 6) == 0:
            self.add_car()


