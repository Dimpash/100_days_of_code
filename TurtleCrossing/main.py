import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

runner = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=runner.move, key="Up")
# # screen.onkey(fun=print("erwerw"), key="w")
# screen.onkey(fun=runner.move, key="Up")

# screen.update()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # cars.refresh_cars()
    car_manager.move_cars()

    # Finishing the level
    if runner.ycor() >= FINISH_LINE_Y:
        scoreboard.increase_score()
        runner.restart()
        car_manager.move_distance += 2

    # Collision with a car
    for car in car_manager.cars:
        if car.distance(runner) < 20:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()