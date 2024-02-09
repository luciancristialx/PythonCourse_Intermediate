from turtle import Turtle, Screen
import random

#draw different shapes
tim = Turtle()


color = ["brown","indigo","dark salmon","orange","green","steel blue","lavender","dark olive green"]


def draw_shape(num_sides):
    random_color = random.choice(color)
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)
        tim.color(random_color)


for i in range(3,11):
    draw_shape(i)


screen = Screen()
screen.exitonclick()