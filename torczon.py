from geometry import *


def torczon(object, s, precision):
    closestPointS = s.closestTo(object)

    while object.distance(closestPointS) > precision:
        sr = s.reflexion(closestPointS)
        closestPointSR = sr.closestTo(object)
        if object.distance(closestPointSR) < object.distance(closestPointS):
            se = s.expansion(closestPointS)
            closestPointSE = se.closestTo(object)
            if object.distance(closestPointSE) < object.distance(closestPointSR):
                s = se
            else:
                s = sr
        else:
            s = s.contraction(closestPointS)
        closestPointS = s.closestTo(object)
    return closestPointS


if __name__ == "__main__":
    from graphics import *
    from utils import EPSILON

    circle = Circle(250, 250, 100)
    x1 = Vector2(250, 240)
    x2 = Vector2(210, 270)
    x3 = Vector2(300, 290)
    s = Simplex2(x1, x2, x3)
    point = torczon(circle, s, EPSILON)
    center = torczon(circle.center, s, EPSILON)
    canvas = createCanvas(500, 500)
    circle.draw(canvas)
    s.draw(canvas)
    drawLine(canvas, center.x, center.y, point.x, point.y, "red")
    input("quit ?")