from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, starting_pos):
        super().__init__()
        self.shape("square")
        self.color("white")

        # We need paddle width = 100 , height = 20
        # But all turtles are 20 x 20 defined
        # so stretch in width = 20 x 5
        # stretch in height = 20 x 1

        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(starting_pos)  # initialise the x and y coordinates

    # LIMITER SO PADDLES STOP AT FRAME BORDERS
    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
        else:
            self.goto(self.xcor(), 250)

    def go_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
        else:
            self.goto(self.xcor(), -250)
