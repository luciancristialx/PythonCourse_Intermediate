from turtle import Turtle
import random

FOOD_SHAPE = "square"
FOOD_COLOR = "green"
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_len = 0.5,stretch_wid = 0.5)
        self.color(FOOD_COLOR)
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-255, 255)
        random_y = random.randint(-255, 255)
        self.goto(random_x, random_y)