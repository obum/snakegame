from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.3, stretch_wid=0.3)
        self.color("red")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 265)
        self.goto(random_x, random_y)


