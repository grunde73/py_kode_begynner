# -*- coding: utf-8 -*-
"""
Dette er et lite Python program
"""
import turtle

colors = ["red", "blue", "yellow", "green", "orange", "purple"]

t = turtle.Pen()

turtle.bgcolor("black")

for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)

turtle.bye()