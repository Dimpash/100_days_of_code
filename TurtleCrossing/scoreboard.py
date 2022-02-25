from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f"Level: {self.score}", font=FONT)

    def increase_score(self):
        self.score += 1
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT)
