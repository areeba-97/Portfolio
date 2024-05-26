from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 22, "normal")


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore= int(data.read())

        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset (self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode = 'w') as data:
                data.write(f'{self.highscore}')
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("white")
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
