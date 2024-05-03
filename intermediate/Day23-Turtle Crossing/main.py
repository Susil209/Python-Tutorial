import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# create player
player = Player()

# create car manager
car = CarManager()

# create scoreboard
score = Scoreboard()

# event listener
screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create and move car
    car.generate_car()
    car.move()

    # Detect when the turtle player collides
    # with a car and stop the game if this happens.

    for new_car in car.all_cars:
        if new_car.distance(player) <= 25:
            game_is_on = False
            score.game_over()

    # Detect when the player has reached the other side
    if player.is_at_finish_line():
        player.starting_position()
        car.speed_up()
        # update score
        score.update_score()
