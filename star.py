from turtle import *
def star(size):
    for _ in range(5):
        forward(size)
        right(144)

def starSpin(repeats):
    size=10
    for _ in range(repeats):
        star(size)
        right(5)
        size+=5


starSpin(100)