from turtle import Turtle

MOVE = False
ALIGNMENT = "center"
FONT = ("Courier New", 8, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as f:
            self.high_score = int(f.read())
        self.penup()
        self.color("yellow")
        self.hideturtle()
        self.goto(0, 280)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Total score: {self.score}, High score: {self.high_score}", move=MOVE, font=FONT, align=ALIGNMENT)

    def restart_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.refresh()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME  OVER", move=MOVE, font=FONT, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.refresh()
