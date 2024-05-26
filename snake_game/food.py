from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("red")
        self.penup()
        self.speed(0)
        self.refresh()


    def refresh(self):
        random_x = random.randint(-270,270)
        random_y = random.randint(-270,270)
        self.goto(random_x,random_y)

