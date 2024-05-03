from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# Create a turtle player that starts at the bottom of the screen
# and listen for the "Up" keypress to move the turtle
# north.
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        if self.ycor() <= FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        return True if self.ycor() >= FINISH_LINE_Y else False

    def starting_position(self):
        self.goto(STARTING_POSITION)
