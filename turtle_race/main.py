from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet!", "Which turtle will won the race? Enter a color: ")


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
positions = [-125, -75, -25, 25, 75, 125]

turtles = []
for i in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, positions[i])
    turtles.append(new_turtle)

is_on = False

if user_bet:
    is_on = True

while is_on:
    for turtle in turtles:
        if turtle.xcor() > 220:
            is_on = False
            if turtle.pencolor() == user_bet:
                print(f"You have won, the \"{turtle.pencolor()}\" turtle is the winner!")
            else:
                print(f"You have lost, the \"{turtle.pencolor()}\" turtle is the winner!")
        turtle.forward(random.randint(0, 10))
screen.exitonclick()
