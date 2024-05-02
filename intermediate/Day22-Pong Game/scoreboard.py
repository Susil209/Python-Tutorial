from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        # clear screen
        self.clear()

        # for left score board
        self.goto(x=-100, y=200)
        self.write(arg=self.l_score, align="center", font=("Courier", 60, "normal"))

        # for right score board
        self.goto(x=100, y=200)
        self.write(arg=self.r_score, align="center", font=("Courier", 60, "normal"))

    def update_left_score(self):
        self.l_score += 1
        self.update_score()

    def update_right_score(self):
        self.r_score += 1
        self.update_score()
