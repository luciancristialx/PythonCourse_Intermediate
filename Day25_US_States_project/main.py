import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_df = pd.read_csv("50_states.csv")
all_states = states_df.state.to_list()
guessed_states = []

current_guess = 0

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/{len(states_df)} States correct",
            prompt = "What's another state name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row = states_df[states_df.state == answer_state]
        t.goto(int(row.x), int(row.y))
        t.write(answer_state)



