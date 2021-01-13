from turtle import Turtle
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

df = pandas.read_csv('50_states.csv')
guessed_states = []
correct_answer = Turtle()
correct_answer.hideturtle()
correct_answer.penup()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        break
    for state in df.state:
        if answer_state == state:
            guessed_states.append(answer_state)
            state_coordinates_row = df[df.state == state]
            correct_answer.goto(int(state_coordinates_row.x), int(state_coordinates_row.y))
            correct_answer.write(state)

# states_to_learn.csv
missing_states = df.state.to_list()
print(missing_states)
for state in guessed_states:
    missing_states.remove(state)
states_to_study = pandas.DataFrame(missing_states)
states_to_study.to_csv('states_to_study')
