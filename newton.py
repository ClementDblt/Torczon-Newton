from geometry import *
from utils import derivative


def newton(object, xn, precision):
    while object.f(xn) > precision:
        xn.x = xn.x - object.fx(xn.x) / derivative(object.fx, xn.x)
        xn.y = xn.y - object.fy(xn.y) / derivative(object.fy, xn.y)
    return xn


if __name__ == "__main__":
    from graphics import *
    from utils import EPSILON

    circle = Circle(250, 250, 100)
    x0 = Vector2(0, 0)
    point = newton(circle, x0, EPSILON).round()
    center = newton(circle.center, x0, EPSILON).round()
    canvas = createCanvas(500, 500)
    circle.draw(canvas)
    drawLine(canvas, center.x, center.y, point.x, point.y, "red")
    input("quit ?")