from turtle import Turtle
import random


class Food(Turtle):  # inherit from turtle class so, we can fo everything a turtle can do

    def __init__(self):
        # all of this will happen when we generate food object from food class
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # normal pixel is 20x20 so half of that is 0.5 10x10
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)  # the screen is 600x600 so that is -300 to 300, we dont want the edge
        random_y = random.randint(-280, 240)  # so we will generate number from -280 to 280 for both x and y coordinates
        self.goto(random_x, random_y)

