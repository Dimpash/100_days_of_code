from turtle import Turtle

MOVE = False
ALIGNMENT = "center"
FONT = ("Courier New", 80, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("yellow")
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", move=MOVE, font=FONT, align=ALIGNMENT)
        self.goto(100, 200)
        self.write(f"{self.r_score}", move=MOVE, font=FONT, align=ALIGNMENT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME  OVER", move=MOVE, font=FONT, align=ALIGNMENT)

    def increase_score_l(self):
        self.l_score += 1
        self.refresh()

    def increase_score_r(self):
        self.r_score += 1
        self.refresh()
