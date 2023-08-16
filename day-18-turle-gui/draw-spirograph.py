import turtle
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        mel.color(random_color())
        mel.setheading(mel.heading() + size_of_gap)
        mel.circle(100)


mel = turtle.Turtle()
mel.pensize(1)
mel.shape("turtle")
mel.speed(0)
turtle.colormode(255)

draw_spirograph(10)

screen = turtle.Screen()
screen.exitonclick()