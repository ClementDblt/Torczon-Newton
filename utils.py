from geometry import *
from random import random
from graphics import clear


EPSILON = 10**(-6)


def derivative(f, x):
    return (f(x + EPSILON) - f(x)) / EPSILON

def intersect(circle, others):
    for other in others:
        if circle.center.distance(other.center) <= circle.radius * 2:
            return True
    return False

def isTangent(circle, other):
    distance = circle.center.distance(other.center)
    radius = circle.radius + other.radius
    if distance >= radius - 0.1 and distance <= radius + 0.1:
        return True
    return False

def isAllTangent(circles):
    if not isTangent(circles[0], circles[1]) or not isTangent(circles[0], circles[2]) or not isTangent(circles[1], circles[2]):
        return False
    return True

def generateCircles():
    circlesRadius = round(random() * 50 + 50)
    circles = []
    for i in range(3):
        position = Vector2(round(random() * 300 + 100), round(random() * 300 + 100))
        circle = Circle(position.x, position.y, circlesRadius)
        while intersect(circle, circles):
            position = Vector2(round(random() * 300 + 100), round(random() * 300 + 100))
            circle = Circle(position.x, position.y, circlesRadius)
        circles.append(circle)
    return circles

def drawCircles(canvas, circles):
    for circle in circles:
        circle.draw(canvas)

def updateCircles(canvas, circles):
    clear(canvas)
    for circle in circles:
        circle.draw(canvas)