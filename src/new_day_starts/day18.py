import random
import time
from turtle import *

tim = Turtle()
# tim.shape("arrow")
tim.pensize(2)
tim.speed("fastest")
colormode(255)


# colors = ["red", "brown", "yellow", "green", "gold", "black", "blue", "orange", "seaGreen", "darkBlue"]

def random_color():
    r = random.randint(0, 254)
    g = random.randint(0, 254)
    b = random.randint(0, 254)
    tim.color(r, g, b)


def draw_shape():
    direction = [0, 90, 270, 180]
    tim.forward(30)
    tim.setheading(random.choice(direction))


def draw_circle(angle):
    for _ in range(int(360/angle)):
        random_color()
        tim.circle(150)
        tim.setheading(tim.heading() + angle)


draw_circle(5)

# def draw_a_shape(sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(-angle)
#
#
# for sides_num in range(3, 11):
#     tim.color(colors[random.randint(0, 9)])
#     draw_a_shape(sides_num)


screen = Screen()
screen.exitonclick()
