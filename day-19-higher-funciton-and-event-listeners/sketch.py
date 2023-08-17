import turtle
from turtle import Turtle, Screen

ben = Turtle()
screen = Screen()


def move_forward():
    ben.forward(10)


def move_backward():
    ben.backward(10)


def turn_left():
    ben.left(10)


def turn_right():
    ben.right(10)


def clear():
    ben.clear()
    ben.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()