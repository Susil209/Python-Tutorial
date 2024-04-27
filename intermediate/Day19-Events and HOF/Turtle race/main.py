import turtle
from turtle import Turtle, Screen
import random

scr = Screen()
scr.setup(width=500, height=400)

colors = ['red', 'orange', 'yellow', 'blue', 'green', 'pink']
is_game_on = False

user_input = turtle.textinput(title="Make your bet.",
                              prompt="Choose a colour that will win?: ")

all_turtles = []

gap = 0
for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=-100 + gap)
    gap += 40
    all_turtles.append(tim)

if user_input:
    is_game_on = True


def check_winner(winner_color):
    if winner_color == user_input:
        print(f"You've won. The winner turtle color is {winner_color}.")
    else:
        print(f"You've lost. The winner turtle color is {winner_color}.")


while is_game_on:
    for turtle in all_turtles:
        # check if game over
        if turtle.xcor() > 230:
            is_game_on = False
            check_winner(turtle.pencolor())
        # else continue the game
        else:
            turtle.forward(random.randint(0, 10))

scr.exitonclick()
