import turtle
from turtle import Turtle, Screen

tim = Turtle()
scr = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def head_anticlockwise():
    tim.setheading(tim.heading() + 10)


#     or, tim.left(10)

def head_clockwise():
    tim.setheading(tim.heading() - 10)


#    or, rim.right(10)

def clear_drawing():
    tim.clear()
    tim.reset()


# Event listener onkey() event
turtle.listen()
turtle.onkey(fun=move_forward, key="w")
turtle.onkey(fun=move_backward, key="s")
turtle.onkey(fun=head_anticlockwise, key="a")
turtle.onkey(fun=head_clockwise, key="d")
turtle.onkey(fun=clear_drawing, key="c")

scr.exitonclick()
