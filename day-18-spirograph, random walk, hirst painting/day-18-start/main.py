

# -----------Spirograph----------

from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
# radius = 100

timmy = Turtle()
timmy.speed("fastest")
timmy.shape("classic")


def random_color():
    r_color = random.randint(0, 255)
    g_color = random.randint(0, 255)
    b_color = random.randint(0, 255)
    color_tuple = (r_color, g_color, b_color)
    return color_tuple


def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap_size)


draw_spirograph(1)


screen.exitonclick()




# ------------------------ Random Walk -------------------------
# screen = Screen()
# screen.colormode(255)
#
# drunk_turtle = Turtle()
# drunk_turtle.shape("circle")
# drunk_turtle.pensize(5)
# drunk_turtle.speed("fastest")
#
#
# def random_walk():
#     drunk_turtle.hideturtle()
#     random_direction = random.randint(1, 4) * 90
#     drunk_turtle.setheading(random_direction)
#     drunk_turtle.forward(10)
#
# def random_color():
#     r_color = random.randint(0, 255)
#     g_color = random.randint(0, 255)
#     b_color = random.randint(0, 255)
#     color_tuple = (r_color, g_color, b_color)
#     return color_tuple
#
#
# random_len = random.randint(1, 500)
# print(f"Loop for: {random_len}")
# for count in range(random_len):
#     print(count)
#     drunk_turtle.color(random_color())
#     random_walk()
#
# screen.exitonclick()






# ---------------SHAPES: Triange/Square/Pentagon/Hexagon/Heptagon/Octogaon/Nonagon/Decagon-----------------------

# screen = Screen()
# screen.colormode(255)
#
# tim = Turtle()
# tim.shape("turtle")
#
#
# def draw_shape(sides):
#     angle = 360 / number_of_sides
#     print(f"{number_of_sides}: {angle} degrees")
#     for _ in range(number_of_sides):
#         tim.forward(50)
#         tim.right(angle)
#
#
# for number_of_sides in range(3, 11):
#     r_color = random.randint(0, 255)
#     g_color = random.randint(0, 255)
#     b_color = random.randint(0, 255)
#     tim.pencolor(r_color, g_color, b_color)
#     draw_shape(number_of_sides)
#
# screen.exitonclick()