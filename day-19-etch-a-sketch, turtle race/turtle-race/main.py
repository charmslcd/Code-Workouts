from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()


screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? (Red, Orange, Yellow, Green, Blue, "
                                               "Indigo, Violet)")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
all_turtles = []

x_position = -200
y_position = -100
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=x_position, y=y_position)
    y_position += 28.5
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet.lower():
                print(f"You've won! {winner} finished first!")
            else:
                print(f"You lost. {winner} finished first.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()