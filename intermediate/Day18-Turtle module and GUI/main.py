import turtle
from turtle import Turtle, Screen
import random

my_turtle = Turtle()
screen = Screen()
screen.screensize(500, 700)

my_turtle.shape("turtle")
my_turtle.color("blue")

# draw a square
# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.right(90)

# draw dashed lines
# for _ in range(10):
#     my_turtle.pendown()
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)


#  draw different shapes
colors = ['blue', 'green', 'red', 'yellow', 'orange', 'black', 'pink', 'violet']


# size = 3
# while size < 11:
#     for _ in range(size):
#         my_turtle.pencolor(colors[size - 3])
#         my_turtle.forward(100)
#         my_turtle.right(360 / size)
#     size += 1


# random walk
# turn = [0, 90, 180, 270]
# my_turtle.pensize(5)
#
#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return tuple((r, g, b))


#
#
turtle.colormode(255)
# for _ in range(30):
#     # my_turtle.color(random.choice(colors))
#     my_turtle.color(random_color())
#     my_turtle.forward(30)
#     my_turtle.setheading(random.choice(turn))
#     my_turtle.speed('fast')


# draw a spirograph
my_turtle.speed("fastest")


def draw_spirograph(size_of_tilt):
    # no of circles based on tilt between two circles
    for _ in range(360 // 5):
        # change color on every iteration
        my_turtle.color(random_color())
        my_turtle.circle(100)
        # set title on every new circle by current_heading + tilt
        my_turtle.setheading(my_turtle.heading() + size_of_tilt)


draw_spirograph(5)

screen.exitonclick()
