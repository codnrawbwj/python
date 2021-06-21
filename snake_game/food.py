from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super(Food, self).__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.color("purple")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(x=randint(-14, 14) * 20, y=randint(-14, 14) * 20)
