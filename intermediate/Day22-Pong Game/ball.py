from turtle import Turtle


# create and move a ball
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    # move the ball
    def move(self):
        # for movement of the ball diagonally from origin
        # through a straight line we have to maintain
        # a constant slope there +10 is added to both x and y

        new_xpos = self.xcor() + self.x_move
        new_ypos = self.ycor() + self.y_move
        self.goto(new_xpos, new_ypos)

    # bounce in y direction -> collision with the top and bottom wall
    def bounce_y(self):
        # inorder to bounce downward the x-cor is +10 moving right
        # but the y-cor should be -10 moving down.
        self.y_move *= -1

    # bugfix-  The ball bounces 4 times when it hits the paddle at the edge

    # bounce in x direction -> collision with the left or right paddle
    def bounce_x_left_paddle(self):
        self.x_move = (abs(self.x_move))
        self.ball_speed *= 0.8  # ball speed increased in each bounce with paddle

    def bounce_x_right_paddle(self):
        self.x_move = -(abs(self.x_move))
        self.ball_speed *= 0.8  # ball speed increased in each bounce with paddle

    def reset_position(self):
        self.home()
        self.ball_speed = 0.1
        self.bounce_x_left_paddle()