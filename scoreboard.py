from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 30, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.show_score()

    def show_score(self):
        self.write(arg=f"{self.player_1_score}  {self.player_2_score}", align=ALIGNMENT, font=FONT)

    def increase_player_1_score(self):
        self.player_1_score += 1
        self.clear()
        self.show_score()

    def increase_player_2_score(self):
        self.player_2_score += 1
        self.clear()
        self.show_score()