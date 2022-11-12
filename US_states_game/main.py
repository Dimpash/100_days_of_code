import turtle

import pandas

MOVE = False
ALIGNMENT = "center"
FONT = ("Courier New", 8, 'normal')

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data["state"].to_list()

text_turtle = turtle.Turtle()
text_turtle.penup()
text_turtle.hideturtle()

right_answers = []
states_to_learn = all_states

while len(right_answers) < 50:
    answer_state = turtle.textinput(title=f"Guess the State, {len(right_answers)}/50",
                                    prompt="What's another state's name?")
    answer_state = answer_state.title()
    print(answer_state)
    answer_state_data = data[data["state"] == answer_state]
    if answer_state == "Exit":
        break
    if len(answer_state_data) > 0:
        # answ_ser_x = answer_state_data["x"] # Alternative
        # x = answ_ser_x.to_list()[0]
        x = int(answer_state_data.x)
        # answ_ser_y = answer_state_data["y"] # Alternative
        # y = answ_ser_y.to_list()[0]
        y = int(answer_state_data["y"])
        text_turtle.goto(x, y)
        # text_turtle.write(answer_state, move=MOVE, font=FONT, align=ALIGNMENT) # Alternative
        text_turtle.write(answer_state_data["state"].item(), move=MOVE, font=FONT, align=ALIGNMENT)
        right_answers.append(answer_state)
        states_to_learn.remove(answer_state)
        # screen.title(f"U.S. States Game. {len(right_answers)}/50")


my_dict = {'state': states_to_learn}
df = pandas.DataFrame.from_dict(my_dict)
df.to_csv("states_to_learn.csv")


turtle.mainloop()  # The alternative to screen.exitonclick()
# screen.exitonclick()

