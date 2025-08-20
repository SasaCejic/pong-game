from turtle import Turtle
import random

NUMBERS_TO_GENERATE = list(range(-100, -19)) + list(range(21, 101))

class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.refresh()

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_from_paddles(self):
        self.x_move *= -1

    def bounce_from_walls(self):
        self.y_move *= -1

    def refresh(self):
        self.goto(0,0)
        self.x_move = random.choice(NUMBERS_TO_GENERATE)
        self.y_move = random.choice(NUMBERS_TO_GENERATE)
