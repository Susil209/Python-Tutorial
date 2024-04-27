# Higher order function
import turtle
from turtle import Turtle, Screen

tim = Turtle()
scr = Screen()


def move_forward(step):
    tim.forward(step)


# Event listener onkey() event
turtle.listen()
turtle.onkey(fun=lambda: move_forward(10), key="space")  # lambda expression

scr.exitonclick()
