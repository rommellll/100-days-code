import random

import colorgram
import turtle

# color list from cologram
color_list = [(246, 240, 244), (235, 241, 246), (1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216), (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179)]

# colors = colorgram.extract('hirst-painting.webp', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     rgb_colors.append(rgb_color)
# print(rgb_colors)

ben = turtle.Turtle()
turtle.setworldcoordinates(-250,-250,250,250)
turtle.colormode(255)
ben.speed(10)
ben.penup()
ben.hideturtle()

x = -225
y = -225
for _ in range(10):
    for _ in range(10):
        ben.setposition(x, y)
        color = random.choice(color_list)
        ben.dot(30,color)
        ben.forward(50)
        x += 50
    y += 50
    x = -225


screen = turtle.Screen()
screen.exitonclick()