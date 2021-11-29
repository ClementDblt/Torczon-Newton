from random import random
from tkinter import Canvas
from utils import generateCircles, drawCircles, EPSILON, isTangent, updateCircles, isAllTangent
from graphics import createCanvas, drawLine
from geometry import Circle, Simplex2, Vector2
from torczon import torczon
from newton import newton
import time
import sys
from matplotlib import pyplot


def mainTorczon(canvas, circles):
    start = time.time()
    ##### TORCZON INIT #####
    s = Simplex2(Vector2(0, 0), Vector2(1, 0), Vector2(0, 1))
    centers = []

    ##### TORCZON calcul des points, des centres et du rayon des cercles #####
    for circle in circles:
        centers.append(torczon(circle.center, s, EPSILON))
    radius = centers[0].distance(torczon(circles[0], s, EPSILON))

    # Si A et B ne sont pas tangents, on fait en sorte que A soit tangent à B
    if not isTangent(circles[0], circles[1]):
        vectorAB = centers[1] - centers[0]
        vectorM = vectorAB.normalize() * radius
        newCenter = centers[0] + vectorAB - vectorM * 2
        circles[0] = Circle(newCenter.x, newCenter.y, radius)
        centers[0] = torczon(circles[0].center, s, EPSILON)
        if canvas:
            updateCircles(canvas, circles)

    # Si B et C ne sont pas tangents, on fait en sorte que C soit tangent à B
    if not isTangent(circles[1], circles[2]):
        vectorBC = centers[2] - centers[1]
        vectorCB = centers[1] - centers[2]
        vectorM1 = vectorBC.normalize() * radius * -1
        vectorM2 = vectorCB.normalize() * radius
        newCenter = centers[2] + vectorCB - vectorM1 - vectorM2
        circles[2] = Circle(newCenter.x, newCenter.y, radius)
        centers[2] = torczon(circles[2].center, s, EPSILON)
        if canvas:
         updateCircles(canvas, circles)

    # On fait en sorte que C soit tangent à B et à A
    while not isAllTangent(circles):
        # Si A et C ne sont pas tangents
        if not isTangent(circles[0], circles[2]):
            # Peut-être calcul avec AC
            vectorCA = centers[0] - centers[2]
            vectorM = vectorCA.normalize() * radius
            newCenter = centers[2] + vectorCA - vectorM * 2
            circles[2] = Circle(newCenter.x, newCenter.y, radius)
            centers[2] = torczon(circles[2].center, s, EPSILON)
            if canvas:
                updateCircles(canvas, circles)
        # Si B et C ne soit pas tangents
        if not isTangent(circles[1], circles[2]):
            vectorBC = centers[2] - centers[1]
            vectorCB = centers[1] - centers[2]
            vectorM1 = vectorBC.normalize() * radius * -1
            vectorM2 = vectorCB.normalize() * radius
            newCenter = centers[2] + vectorCB - vectorM1 - vectorM2
            circles[2] = Circle(newCenter.x, newCenter.y, radius)
            centers[2] = torczon(circles[2].center, s, EPSILON)
            if canvas:
                updateCircles(canvas, circles)
    if canvas:
        drawTriangle(canvas, centers)
    return time.time() - start


def mainNewton(canvas, circles):
    start = time.time()
    ##### NEWTON INIT #####
    centers = []

    ##### NEWTON calcul des points, des centres et du rayon des cercles #####
    for circle in circles:
        centers.append(newton(circle.center, Vector2(0, 0), EPSILON))
    radius = centers[0].distance(newton(circles[0], Vector2(0, 0), EPSILON))

    # Si A et B ne sont pas tangents, on fait en sorte que A soit tangent à B
    if not isTangent(circles[0], circles[1]):
        vectorAB = centers[1] - centers[0]
        vectorM = vectorAB.normalize() * radius
        newCenter = centers[0] + vectorAB - vectorM * 2
        circles[0] = Circle(newCenter.x, newCenter.y, radius)
        centers[0] = newton(circles[0].center, Vector2(0, 0), EPSILON)
        if canvas:
            updateCircles(canvas, circles)

    # Si B et C ne sont pas tangents, on fait en sorte que C soit tangent à B
    if not isTangent(circles[1], circles[2]):
        vectorBC = centers[2] - centers[1]
        vectorCB = centers[1] - centers[2]
        vectorM1 = vectorBC.normalize() * radius * -1
        vectorM2 = vectorCB.normalize() * radius
        newCenter = centers[2] + vectorCB - vectorM1 - vectorM2
        circles[2] = Circle(newCenter.x, newCenter.y, radius)
        centers[2] = newton(circles[2].center, Vector2(0, 0), EPSILON)
        if canvas:
            updateCircles(canvas, circles)

    # On fait en sorte que C soit tangent à B et à A
    while not isAllTangent(circles):
        # Si A et C ne sont pas tangents
        if not isTangent(circles[0], circles[2]):
            # Peut-être calcul avec AC
            vectorCA = centers[0] - centers[2]
            vectorM = vectorCA.normalize() * radius
            newCenter = centers[2] + vectorCA - vectorM * 2
            circles[2] = Circle(newCenter.x, newCenter.y, radius)
            centers[2] = newton(circles[2].center, Vector2(0, 0), EPSILON)
            if canvas:
                updateCircles(canvas, circles)
        # Si B et C ne soit pas tangents
        if not isTangent(circles[1], circles[2]):
            vectorBC = centers[2] - centers[1]
            vectorCB = centers[1] - centers[2]
            vectorM1 = vectorBC.normalize() * radius * -1
            vectorM2 = vectorCB.normalize() * radius
            newCenter = centers[2] + vectorCB - vectorM1 - vectorM2
            circles[2] = Circle(newCenter.x, newCenter.y, radius)
            centers[2] = newton(circles[2].center, Vector2(0, 0), EPSILON)
            if canvas:
                updateCircles(canvas, circles)
    if canvas:
        drawTriangle(canvas, centers)
    return time.time() - start

# Calcule et affiche le triangle tangent aux cercles et l'affiche
def drawTriangle(canvas, centers):
    points = []

    for i in range(3):
        vectorM = (centers[i] + centers[i - 1]) / 2
        x = centers[i - 2].x - vectorM.x
        y = centers[i - 2].y - vectorM.y
        points.append(Vector2(vectorM.x + (2.15 * x), vectorM.y + (2.15 * y)))
    for i in range(3):
        drawLine(canvas, points[i - 1].x, points[i - 1].y, points[i].x, points[i].y)


if __name__ == "__main__":
    display = True
    nIterations = 1
    torczonTime = 0
    newtonTime = 0
    canvasT = None
    canvasN = None
    torczonTimes = []
    newtonTimes = []
    iterations = []
    if len(sys.argv) >= 2:
        if sys.argv[1].lower() == "true":
            display = True
        elif sys.argv[1].lower() == "false":
            display = False
        else:
            print("\nUsage : py main.py display \"nombre itérations\"\nExemple : py main.py True 100")
            quit()
    if len(sys.argv) == 3:
        try:
            nIterations = int(sys.argv[2])
        except ValueError:
            print("\nUsage : py main.py display \"nombre itérations\"\nExemple : py main.py True 100")
            quit()
    elif len(sys.argv) > 3:
        print("\nUsage : py main.py display \"nombre itérations\"\nExemple : py main.py True 100")
        quit()
    for i in range(nIterations):
        circlesT = generateCircles()
        circlesN = circlesT.copy()
        if display:
            canvasT = createCanvas(500, 500, "Torczon")
            canvasN = createCanvas(500, 500, "Newton")
            drawCircles(canvasT, circlesT)
            input("press [Enter] to continue...")
        torczonTime += mainTorczon(canvasT, circlesT)
        torczonTimes.append(torczonTime)
        if display:
            input("press [Enter] to continue...")
            drawCircles(canvasN, circlesN)
            input("press [Enter] to continue...")
        newtonTime += mainNewton(canvasN, circlesN)
        newtonTimes.append(newtonTime)
        iterations.append(i + 1)
    pyplot.plot(iterations, torczonTimes, "r--", label="torczon")
    pyplot.plot(iterations, newtonTimes,  "b-.", label="newton")
    pyplot.xlabel("Itérations", size=14)
    pyplot.ylabel("Millisecondes", size=14)
    pyplot.legend()
    pyplot.show()
    #print(f"Temps de calcul Torczon : {round(torczonTime * 1000, 2)}ms\nTemps de calcul Newton : {round(newtonTime * 1000, 2)}ms")
    #input("press [Enter] to quit...")