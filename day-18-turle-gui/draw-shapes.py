from turtle import Turtle, Screen
import random

turtle_colors = ["cornflower blue", "medium blue", "deep sky blue", "powder blue", "dark turquoise",
                 "dark slate gray", "chartreuse", "dark olive green", "red", "blue", "slate blue"]
directions = [mel.right, mel.left]


def draw_shape(num_sides):
    used_colors = []
    angle = 360 / shape
    for _ in range(shape):
        mel.forward(100)
        mel.right(angle)


mel = Turtle()
mel.pensize(10)
mel.shape("turtle")


for shape in range(3, 11):
    color = random.choice(turtle_colors)
    mel.color(color)
    draw_shape(shape)



screen = Screen()
screen.exitonclick()