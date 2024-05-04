from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


# create snake class
class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    # create snake
    def create_snake(self):
        for pos in POSITIONS:
            self.add_body(pos)

    def add_body(self, pos):
        new_snake = Turtle(shape="square")
        new_snake.color("green")
        new_snake.penup()
        new_snake.goto(pos)
        self.snake_body.append(new_snake)

    def reset(self):
        for body in self.snake_body:
            body.goto(1000, 1000)  # send snake to out of screen
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    # Extend the snake body segment
    def extend_body(self):
        # We hold the last segment element and get its position
        self.add_body(self.snake_body[-1].position())

        # Now this position will be passed
        # to add_body() which will add a new body segment at the end of snake_body list

    def move_body(self):
        # for loop from end to start range(start = len-1, stop = 0, step =-1)
        for body_num in range(len(self.snake_body) - 1, 0, -1):
            # we have 3 segments 3->2->1 on  screen, the idea is to start shift from 3 .
            # shift first 3 to 2 position and then 2 to 1 position and 1 forward.
            # In this way when turning left or right the tail follow head.
            new_xcor = self.snake_body[body_num - 1].xcor()
            new_ycor = self.snake_body[body_num - 1].ycor()
            self.snake_body[body_num].goto(new_xcor, new_ycor)
        self.snake_body[0].forward(20)  # head movement

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
