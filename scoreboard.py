from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 10, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.highest_score = 0
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write(arg=f"GAME OVER", move=True, align="center", font=FONT)

    def update_scoreboard(self):
        self.goto(-0, 270)
        self.write(arg=f"Score : {self.score}", move=True, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
