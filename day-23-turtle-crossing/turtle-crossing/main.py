import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
level = Scoreboard()

screen.listen()
screen.onkey(player.player_up, "Up")
screen.onkey(player.player_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            level.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        level.level_completed()
        player.reset_position()
        car_manager.increase_speed()

    if car_manager.collided:
        print("Game Over")


screen.exitonclick()




