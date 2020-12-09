from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

tim = Turtle()
tim.color("white")
tim.pensize(3)
tim.hideturtle()
tim.penup()
tim.setposition(0, -300)
tim.left(90)
tim.pendown()
for _ in range(-300, 300, 10):
    tim.color("white")
    tim.forward(10)
    tim.color("black")
    tim.forward(10)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

interval = 0.1
is_on = True
while is_on:
    time.sleep(interval)
    screen.update()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.restart()
        score.l_point()
        interval -= 0.01
    elif ball.xcor() < -380:
        ball.restart()
        score.r_point()
        interval -= 0.001

    if score.r_score == 10:
        score.r_result()
        is_on = False
    elif score.l_score == 10:
        score.l_result()
        is_on = False


screen.exitonclick()
