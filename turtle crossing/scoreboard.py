from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-140, 250)
        self.font()

    def font(self):
        self.write(f"level: {self.level}", align="right", font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.font()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
