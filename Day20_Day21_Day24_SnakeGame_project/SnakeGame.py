from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#Create snake body
#Move the snake
#Control the snake
#Detect collision with food
#Create a scoreboard
#Detect collision with wall
#Detect collision with tail

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 265 or snake.head.xcor() < -265 or snake.head.ycor() > 265 or snake.head.ycor() < -265:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        # If head collides with any segment in the tail:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()





screen.exitonclick()

