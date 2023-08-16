import turtle
from turtle import Turtle, Screen
import random

turtle_colors = ["cornflower blue", "medium blue", "deep sky blue", "powder blue", "dark turquoise",
                 "dark slate gray", "chartreuse", "dark olive green", "red", "blue", "slate blue"]
directions = [0, 90, 180, 270]


def draw_shape(num_sides):
    used_colors = []
    angle = 360 / shape
    for _ in range(shape):
        mel.forward(100)
        mel.right(angle)


def walk(angle):
    mel.forward(20)
    mel.setheading(angle)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


mel = Turtle()
mel.pensize(10)
mel.shape("turtle")
mel.speed(0)
turtle.colormode(255)

for shape in range(1000):
    mel.color(random_color())
    angle = random.choice(directions)
    walk(angle)



screen = Screen()
screen.exitonclick()