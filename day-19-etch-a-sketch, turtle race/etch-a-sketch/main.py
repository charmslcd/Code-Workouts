from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backwards():
    timmy.back(10)


def move_right():
    timmy.right(10)


def move_left():
    timmy.left(10)


def reset_sketch():
    timmy.reset()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=reset_sketch, key="c")



screen.exitonclick()