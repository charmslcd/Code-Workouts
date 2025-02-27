import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
CONTINUE = True


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.continue_generate = True
        self.collided = False
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color("black")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def car_collision(self, player):
        for car in self.all_cars:
            if player.distance(car) < 20:
                self.collided = True

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
