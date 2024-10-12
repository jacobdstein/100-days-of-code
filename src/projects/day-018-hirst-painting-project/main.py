from random import choice
from turtle import *

"""
This is how to get the most frequent colors from an image using 'colorgram.py'
Make sure to delete the white colors from the list after you have extracted the colors in order to not contrast with
the background of the painting

import colorgram

colors = colorgram.extract("hirst.jpg", 30)
color_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    color_list.append((r, g, b))

print(color_list)
"""

color_list = [(56, 92, 135), (198, 162, 101), (149, 74, 53), (224, 201, 118), (134, 68, 85), (194, 185, 23),
              (139, 165, 190), (210, 92, 70), (64, 40, 52), (180, 19, 12), (123, 200, 160), (205, 154, 180),
              (30, 116, 75), (19, 171, 150), (202, 77, 81), (24, 26, 32), (68, 56, 90), (133, 28, 37), (47, 90, 42),
              (61, 82, 37), (221, 167, 194), (160, 210, 189), (224, 177, 169), (120, 114, 151), (31, 38, 33),
              (186, 188, 204)]

title("Hirst Painting")
colormode(255)

t = Turtle()
t.speed(0)
t.hideturtle()
t.penup()

for row in range(10):
    for col in range(10):
        t.goto(col * 50 - 250, row * 50 - 250)
        t.pendown()
        t.dot(20, choice(color_list))
        t.penup()

t.screen.mainloop()
