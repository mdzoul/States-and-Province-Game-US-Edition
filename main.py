import turtle
import pandas as pd


def show_state(ans):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(arg=f"{ans}", align="center", font=("Helvetica", 8, "normal"))


def end_game():
    turtle.goto(0, 0)
    turtle.hideturtle()
    turtle.write(arg="Congratulations!", align="center", font=("Helvetica", 72, "normal"))
    turtle.goto(0, -24)
    turtle.hideturtle()
    turtle.write(arg="You managed to guess all 50 states!", align="center", font=("Helvetica", 24, "normal"))


screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states.gif"
screen.setup(width=725, height=491)
screen.bgpic(image)

df = pd.read_csv("50_states.csv")
state_list = df["state"].to_list()
guessed_states = []
score = 0

all_states = 50
while score != all_states:
    answer = screen.textinput(title=f"{score}/50 States", prompt="What's another state's name?").title()
    if answer in state_list and answer not in guessed_states:
        guessed_states.append(answer)
        score += 1
        correct_state = df[df.state == answer]
        index = correct_state.index
        for i in index:
            x, y = correct_state.x[i], correct_state.y[i]
            show_state(answer)

end_game()
turtle.mainloop()
