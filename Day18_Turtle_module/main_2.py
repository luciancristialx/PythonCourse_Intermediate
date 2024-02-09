import turtle as t
from turtle import Turtle,Screen
import random

#random walk
tim = t.Turtle()

directions = [0,90,180,270]
tim.pensize(15)
tim.speed(0)
t.colormode(255)

def random_color_generator():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

for _ in range(200):
    tim.color(random_color_generator())
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()