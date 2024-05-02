# Requirements / Structure:
# ------------------------------------
# 1. Create the screen
# 2. Create and move a paddle
# 3. Create another paddle
# 4. Create a ball and make it move
# 5. Detect collision with wall and bounce
# 6. Detect collision with paddle
# 7. Detect when paddle misses
# 8. Keep Score

# Create the screen

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

#             |             |
#             |             |
#             |             |
# ------------|------------ 600
#             |             |
#             |             |
#             |             |
# ---------- 800 ----------


# bugfix-  Controlling Pong paddles at the same time

# it involves setting a small state machine to manually handle the key presses and going a level under
# the turtle screen object to bind functions to the Tkinter canvas itself.

# State machine to track which keys are pressed
keys_pressed = {}

screen = Screen()
screen.title(titlestring="Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # turn off the animation

# Create and move a paddle


#  |
#  |                                20
#  |                            ___________
#  |                        50  |         |
#  |                            |         |
#  |                            |         |
#  |                            |         |
# 0|----------------------------|-----|---|---- 400
#  |                         340|    350  |360
#  |                            |         |
#  |                            |         |
#  |                            |         |
#  |                            -----------
#  |                                 20
#  |
#                                Right paddle

# Create left and right paddle objects
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

# Create a ball and make it move
ball = Ball()

# create score board
score = ScoreBoard()


# Callback for KeyPress event listener. Sets key pressed state to True
def pressed(event):
    keys_pressed[event.keysym] = True


# Callback for KeyRelease event listener. Sets key pressed state to False
def released(event):
    keys_pressed[event.keysym] = False


# Set up the event listeners, bypassing the Turtle Screen to use the underlying TKinter canvas directly
# This needs to be done to get access to the event object so the state machine can determine which key was pressed
def set_key_binds():
    for key in ["Up", "Down", "w", "s"]:
        screen.getcanvas().bind(f"<KeyPress-{key}>", pressed)
        screen.getcanvas().bind(f"<KeyRelease-{key}>", released)
        keys_pressed[key] = False


# move the turtle/paddle with keystrokes

# Create another paddle

# listen screen
screen.listen()
set_key_binds()

# left paddle
# screen.onkeypress(fun=l_paddle.go_up, key="w")
# screen.onkeypress(fun=l_paddle.go_down, key="s")
# # right paddle
# screen.onkeypress(fun=r_paddle.go_up, key="Up")
# screen.onkeypress(fun=r_paddle.go_down, key="Down")

is_game_on = True

while is_game_on:
    # adding a time delay after each iteration
    # Need to sleep or else the paddles move very, very fast...
    time.sleep(ball.ball_speed)

    # Check state of key presses and respond accordingly
    if keys_pressed["w"]:
        l_paddle.go_up()
    if keys_pressed["s"]:
        l_paddle.go_down()
    if keys_pressed["Up"]:
        r_paddle.go_up()
    if keys_pressed["Down"]:
        r_paddle.go_down()

    screen.update()  # refresh the page/screen
    ball.move()

    # Detect collision with wall and bounce

    # The height of the  screen is 600px means from origin 300 up
    # in y cor and -300 down in -y cor. If the ball cor exceed the
    # range then collision happened.

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # bounce in y direction
        ball.bounce_y()

    # Detect collision with paddle

    # LOGIC
    # The distance method is used to find the distance between two
    # turtle objects(ball,paddle) like ball.distance(paddle) <20
    # but the problem here is
    # in case of paddle the distance is measured from its center to
    # the center of the ball. But what if the ball collides at the
    # edge of the paddle then the distance is more than 20

    # To overcome this issue we have to add another condition to
    # take the ball's x-cor > 340 and the length of the screen is
    # 400 to right of origin and distance between ball and paddle
    # less than 50

    # condition for right paddle collision with ball
    r_paddle_collision = ball.distance(r_paddle) < 50 and ball.xcor() > 320

    # condition for left paddle collision with ball
    l_paddle_collision = ball.distance(l_paddle) < 50 and ball.xcor() < -320

    # Detect collision with left paddle
    if l_paddle_collision:
        ball.bounce_x_left_paddle()
    if r_paddle_collision:
        ball.bounce_x_right_paddle()

    # Detect when paddle misses

    # right paddle misses, reset and update left score board
    if ball.xcor() > 380:
        ball.reset_position()
        score.update_left_score()

    # left paddle missed, reset and update right score board
    if ball.xcor() < -380:
        ball.reset_position()
        score.update_right_score()

screen.exitonclick()
