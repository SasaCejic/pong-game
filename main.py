from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
t = Turtle()
t.pencolor("white")
t.hideturtle()
t.width(5)
t.penup()
t.goto(0, 280)
t.pendown()
t.setheading(270)

while t.ycor() > -280:
    t.forward(20)
    t.penup()
    t.forward(20)
    t.pendown()

scoreboard = Scoreboard()

screen.tracer(1)

paddle_1 = Paddle()
paddle_1.goto(-480, 0)
paddle_2 = Paddle()
paddle_2.goto(470, 0)
# screen.update()

screen.listen()

screen.onkey(fun=paddle_1.move_up, key="w")
screen.onkey(fun=paddle_1.move_down, key="s")

screen.onkey(fun=paddle_2.move_up, key="Up")
screen.onkey(fun=paddle_2.move_down, key="Down")

ball = Ball()

game_is_on = True

while game_is_on:
    ball.move()

    # Detect collision with a paddles
    if ball.distance(paddle_1) < 35 or ball.distance(paddle_2) < 35:
        ball.bounce_from_paddles()
    # Detect collision with top and bottom wall
    if ball.ycor() > 260 or ball.ycor() < -260:
        ball.bounce_from_walls()
    # Detect collision with right and left walls
    if ball.xcor() > 490:
        # game_is_on = False
        scoreboard.increase_player_1_score()
        screen.tracer(0)
        ball.refresh()
        screen.tracer(1)
    elif ball.xcor() < -490:
        # game_is_on = False
        scoreboard.increase_player_2_score()
        screen.tracer(0)
        ball.refresh()
        screen.tracer(1)

screen.exitonclick()