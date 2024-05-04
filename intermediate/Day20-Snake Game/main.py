from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)  # Turn turtle animation on/off and set delay for update drawings.

# create snake
snake = Snake()

# create food
food = Food()

# create scoreboard
score = Scoreboard()

# snake movement, Control the snake with keystroke
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# move the snake body
is_game_on = True
while is_game_on:
    screen.update()  # update the screen after each iteration
    time.sleep(0.1)  # sleep or delay for 0.1 second after screen update

    # move the body
    snake.move_body()

    # detect collision with food
    if snake.head.distance(food) < 15:  # here we take 15 px buffer
        # change food position
        food.refresh()

        # extend snake body
        snake.extend_body()

        # update score on collision
        score.score_increment()

    # detect a collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # is_game_on = False
        # score.game_over()
        score.reset()
        snake.reset()

    # Detect collision with the tail
    for body_part in snake.snake_body[1:]:  # starting from 1st index
        # if body_part == snake.head:
        #     pass

        # if snake head collision with other body parts then game over
        if body_part.distance(snake.head) < 10:
            # is_game_on = False
            score.reset()
            snake.reset()

screen.exitonclick()
