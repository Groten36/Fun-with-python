from turtle import *
def triangle(size):
    for i in range(3):
        forward(size)
        right(120)

def polygon(sides):
        angle=(360/sides)
        for i in range(sides):
                forward(100)
                right(angle)
polygon(6)