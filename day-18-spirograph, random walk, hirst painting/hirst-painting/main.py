import random

import colorgram
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.colormode(255)


def paint_dots():
    turtle.showturtle()
    list_size = len(colors_list)
    turtle.dot(20, random.choice(colors_list))
    turtle.forward(50)
    turtle.hideturtle()


# Colorgram
colors = colorgram.extract('image.jpg',30)

colors_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_color = (r, g, b)
    colors_list.append(rgb_color)

# 10x10
# dot 20 in size space 50

turtle.shape("classic")
turtle.penup()
turtle.hideturtle()
start_pos = turtle.pos()
turtle.showturtle()
turtle.speed(0)

y_axis = [(-250, -250), (-250, -200), (-250, -150), (-250, -100), (-250, -50), (-250, -0), (-250, 50), (-250, 100),
          (-250, 150), (-250, 200)]

for y in y_axis:
    turtle.goto(y)
    for x in range(10):
        paint_dots()


screen.exitonclick()