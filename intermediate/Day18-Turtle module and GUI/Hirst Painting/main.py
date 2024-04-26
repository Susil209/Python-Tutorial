# import colorgram
import turtle
# Extract 6 colors from an image.
# colors = colorgram.extract("color.jpg", 20)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
# print(len(colors))

# rgb = colors[0].rgb
# print(tuple(rgb))
# print(type(rgb))

# list_of_colors = []
# for color in colors:
#     list_of_colors.append(tuple(color.rgb))
# print(list_of_colors)


from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.screensize(600, 600)
turtle.colormode(255)

color_list = [(236, 36, 110), (149, 24, 68), (215, 167, 52), (241, 73, 35), (9, 146, 92),
              (185, 160, 42), (26, 126, 193), (45, 191, 233), (252, 224, 0),
              (82, 22, 85), (243, 219, 56), (124, 192, 86), (185, 37, 105),
              (23, 171, 122), (214, 58, 24), (213, 131, 167)]

# tim.setx(-280)
# tim.sety(-280)
tim.penup()
tim.goto(-270, -240)

# print(tim.pos())
# print(screen.window_height())
# print(screen.window_width())

total_rows = 10
total_cols = 10
gaps = 50

turtle.speed("fastest")


def draw_in_a_row():
    for _ in range(total_cols):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(gaps)


# draw_in_a_row()


num_of_rows = 0

if num_of_rows == 0:
    draw_in_a_row()

while num_of_rows < total_rows - 1:
    tim.setheading(90)
    tim.forward(gaps)
    tim.setheading(180)
    tim.forward(total_cols * gaps)
    tim.setheading(0)
    draw_in_a_row()
    num_of_rows += 1

screen.exitonclick()
