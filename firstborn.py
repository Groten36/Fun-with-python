from turtle import *
size=5
def square(size):
    for i in range(4):
        forward(size)
        right(90)
for i in range(60):
        square(size)
        right(5)
        size+=5
#square(50)
#square(80)