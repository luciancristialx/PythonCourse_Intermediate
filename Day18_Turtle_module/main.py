import turtle as t
from turtle import Screen
import random
#from turtle import * - import everything
#import turtle as t - aliases

#draw spirograph
tim = t.Turtle()
t.colormode(255)
tim.speed(0)

def random_color_generator():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color_generator())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()