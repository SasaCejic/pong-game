from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def move_up(self):
        if self.ycor() < 240:
            self.sety(self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -240:
            self.sety(self.ycor() - 20)
