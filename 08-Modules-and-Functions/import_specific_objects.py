import turtle
from math import radians, cos


def square(length: int) -> None:
    """
    Draw a square of length `length`
    """
    for side in range(4):
        turtle.forward(length)
        turtle.right(90)


def encircled_square(length: int) -> None:
    """
    Draw a square of length `length`, then encloses it in a circle.
    """
    square(length)
    angle = radians(45)
    radius = length * cos(angle)
    turtle.right(135)
    turtle.circle(radius)


# encircled_square(300)
for s in range(72):
    # square(120)
    encircled_square(120)
    turtle.left(5)
turtle.done()
