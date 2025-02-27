from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
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

    # Detect food collision with food
    if snake.head.distance(food) < 15: # the food is 10x10, we add a buffer so that we know anything that collides will be less than 15 pixels
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #Dect collision with wall

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 250 or snake.head.ycor() < -280:
        # game_is_on = False
        scoreboard.reset()
        snake.reset()

    #Detect collition with tail
    #if head collides with any segment of the tail
        # trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            scoreboard.reset()
            snake.reset()


screen.exitonclick()

