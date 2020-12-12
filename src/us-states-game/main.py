import turtle as t
import pandas

screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

t.Turtle(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

count = []
while len(count) < 50:
    tim = t.Turtle()
    tim.hideturtle()
    tim.penup()
    answer_state = screen.textinput(title=f"{len(count)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        new_list = [i for i in all_states if i not in count]
        df = pandas.DataFrame(new_list)
        df.to_csv("missing_states.csv")
        break
    elif answer_state not in all_states:
        continue
    elif answer_state in all_states:
        state_data = data[data.state == answer_state]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(answer_state)
        if answer_state not in count:
            count.append(answer_state)


screen.exitonclick()
