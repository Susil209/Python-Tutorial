from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 18, 'bold')




class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # read highscore from file
        with open("data.txt", mode="r") as f:
            self.high_score = int(f.read())

        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def score_increment(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, ALIGNMENT, FONT)
