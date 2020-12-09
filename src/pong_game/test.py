from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(800, 700)

tim.color("black")
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

screen.exitonclick()
