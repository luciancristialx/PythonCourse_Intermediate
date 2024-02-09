import random
import turtle as t
from turtle import Turtle,Screen
# import colorgram
#
#Extract colors from image

# original_li_colors = colorgram.extract('SpotPainting.jpg', 30)
#
# new_li_colors = []
#
# def get_rgb(color):
#     rgb = color.rgb
#     red = rgb[0]
#     green = rgb[1]
#     blue = rgb[2]
#     new_color_properties = (red,green,blue)
#     return new_color_properties
#
# for color_item in original_li_colors:
#     new_li_colors.append(get_rgb(color_item))

t.colormode(255)
my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.hideturtle()

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49),
              (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31),
              (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216),
              (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]


def hirst_painting(x_axis, y_axis):
    x = -200
    y = -100
    my_turtle.penup()
    my_turtle.goto(x,y)
    for i in range(x_axis):
        for j in range(y_axis):
            my_turtle.dot(20,random.choice(color_list))
            my_turtle.penup()
            my_turtle.forward(50)
        y += 25
        my_turtle.goto(x,y)


hirst_painting(10,10)

screen = Screen()
screen.exitonclick()





