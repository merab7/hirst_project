import turtle
import random
from turtle import Turtle, Screen

colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
          (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
          (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
          (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89),
          (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
          (176, 192, 208), (168, 99, 102)]

ku = Turtle()
turtle.colormode(255)
ku.speed("fastest")
ku.penup()
ku.setpos(-250, -200)
ku.pendown()


def painter():
    for _ in range(10):
        ku.color(random.choice(colors))
        ku.begin_fill()
        ku.circle(20)
        ku.end_fill()
        ku.penup()
        ku.forward(50)
        ku.pendown()


def backer():
    ku.penup()
    ku.left(90)
    ku.forward(50)
    ku.left(90)
    ku.forward(500)
    ku.left(180)


count = 0

while count < 10:
    painter()
    count += 1
    backer()

screen = Screen()
screen.exitonclick()
