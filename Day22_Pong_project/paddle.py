from turtle import Turtle

PADDLE_SHAPE = "square"
PADDLE_COLOR = "white"
PADDLE_WIDTH = 5
PADDLE_HEIGHT = 1
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_len = PADDLE_HEIGHT, stretch_wid = PADDLE_WIDTH)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
