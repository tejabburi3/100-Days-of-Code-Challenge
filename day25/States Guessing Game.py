import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("50_states.csv")
states_name=data['state'].to_list()
guessed_state=[]

while len(guessed_state)<50:
    answer_state=screen.textinput(title=f"{len(guessed_state)}/50 States Correct ", prompt="What's another state's name ? ").title()
   
    if answer_state in states_name and answer_state not in guessed_state:

        guessed_state.append(answer_state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data['state'] == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

    elif answer_state == "Exit":

        missing_states = [state for state in states_name if state not in guessed_state]

        new_data = pandas.DataFrame(missing_states, columns=["Missed States"])
        new_data.to_csv("States_Missed.csv")

        break
    else:
        continue
screen.exitonclick()
