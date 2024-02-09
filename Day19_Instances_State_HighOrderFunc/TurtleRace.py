from turtle import Turtle,Screen
import random

screen_width = int(input("Please enter screen width: "))
screen_height = int(input("Please enter screen height: "))

is_race_on = False
screen = Screen()
screen.setup(width = screen_width,height = screen_height)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []


for turtle_index in range(0,len(turtle_colors)):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(turtle_colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = (-screen_width/2+20), y = y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > (screen_width/2-20):
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)




















screen.exitonclick()