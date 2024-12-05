from turtle import *
import math


def square(length: int) -> None:
    """
    Draw a square of length `length`
    """
    for side in range(4):
        forward(length)
        right(90)


def encircled_square(length: int) -> None:
    """
    Draw a square of length `length`, then encloses it in a circle.
    """
    square(length)
    angle = math.radians(45)
    radius = length * math.cos(angle)
    right(135)
    circle(radius)


encircled_square(300)
# for s in range(72):
#     square(120)
#     left(5)
done()
