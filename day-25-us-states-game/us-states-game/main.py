import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

FONT = ("Courier", 8, "normal")
ALIGNMENT = "center"

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
is_game_on = True
guessed_states = []
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()


def write_state(name, xcor, ycor):
    state = turtle.Turtle()
    state.penup()
    state.hideturtle()
    state.goto(xcor, ycor)
    state.write(f"{name}", align=ALIGNMENT, font=FONT)


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 correct states",
                                    prompt="What's another state name?")

    if answer_state == "Exit":
        states_to_learn_list = []
        for state in all_states:
            if state not in guessed_states:
                states_to_learn_list.append(state)

        states_to_learn = pd.DataFrame(states_to_learn_list, columns=["state"])
        states_to_learn.to_csv("states_to_learn.csv")
        break

    new_state_title = answer_state.title()
    if new_state_title in all_states and new_state_title not in guessed_states:
        guessed_states.append(new_state_title)
        state_data = data[data.state == new_state_title]
        state_name = new_state_title
        state_xcor = state_data.x.iloc[0]
        state_ycor = state_data.y.iloc[0]
        write_state(state_name, state_xcor, state_ycor)
        print(guessed_states)


# states_to_learn.csv
