from math import sqrt
from graphics import drawLine, clear


class Circle:
    def __init__(self, x, y, radius):
        self.center = Vector2(x, y)
        self.radius = radius
        self.radius2 = radius**2
        self.shape = None

    def __str__(self):
        return f"centre : {self.center}, rayon : {self.radius}"

    # Dessine le cercle
    def draw(self, canvas):
        self.shape = canvas.create_oval(self.center.x - self.radius, self.center.y - self.radius, self.center.x + self.radius, self.center.y + self.radius)
    
    # Evalue la distance entre le cercle et un point
    def distance(self, vector2):
        return abs(pow(vector2.x - self.center.x, 2) + pow(vector2.y - self.center.y, 2) - self.radius2)
    
    # Evalue f(x, y)
    def f(self, vector2):
        return (vector2.x - self.center.x)**2 + (vector2.y - self.center.y)**2 - self.radius2

    # Evalue l'expression de f(x, y) en fonction de x
    def fx(self, x):
        return (x - self.center.x)**2 - self.radius2 / 2
    
    # Evalue l'xpression de f(x, y) en fonction de y
    def fy(self, y):
        return (y - self.center.y)**2 - self.radius2 / 2


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, a):
        if isinstance(a, Vector2):
            return Vector2(self.x + a.x, self.y + a.y)
        return Vector2(self.x + a, self.y + a)

    def __sub__(self, a):
        if isinstance(a, Vector2):
            return Vector2(self.x - a.x, self.y - a.y)
        return Vector2(self.x - a, self.y - a)

    def __mul__(self, a):
        return Vector2(self.x * a, self.y * a)
    
    def __truediv__(self, a):
        assert a != 0, f"Division du point {self} par 0"
        return Vector2(self.x / a, self.y / a)
    
    # Evalue la distance entre un point et un autre
    def distance(self, vector2):
        return sqrt(pow(vector2.x - self.x, 2) + pow(vector2.y - self.y, 2))

    # Evalue f(x, y)
    def f(self, vector2):
        return (vector2.x - self.x)**2 + (vector2.y - self.y)**2

    # Expression de fx(x, y) en fonction de x pour le centre
    def fx(self, x):
        return (x - self.x)**2

    # Expression de fx(x, y) en fonction de y pour le centre
    def fy(self, y):
        return (y - self.y)**2

    # Arrondi entier du point
    def round(self):
        return Vector2(round(self.x), round(self.y))
    
    def norm(self):
        return sqrt(self.x**2 + self.y**2)
    
    def normalize(self):
        return self / self.norm()


class Simplex2:
    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        lineShape1 = None
        lineShape2 = None
        lineShape3 = None

    def __str__(self):
        return f"x1{self.x1}, x2{self.x2.x}, x3{self.x3.x}"

    def draw(self, canvas, color="black"):
        self.lineShape1 = drawLine(canvas, self.x1.x, self.x1.y, self.x2.x, self.x2.y, color)
        self.lineShape2 = drawLine(canvas, self.x2.x, self.x2.y, self.x3.x, self.x3.y, color)
        self.lineShape3 = drawLine(canvas, self.x3.x, self.x3.y, self.x1.x, self.x1.y, color)

    def clear(self, canvas):
        clear(canvas, self.lineShape1)
        clear(canvas, self.lineShape2)
        clear(canvas, self.lineShape3)

    def set_color(self, canvas, color):
        self.clear(canvas)
        self.draw(canvas, color)

    def reflexion(self, point):
        if point == self.x1:
            return Simplex2(point, point * 2 - self.x2, point * 2 - self.x3)
        elif point == self.x2:
            return Simplex2(point, point * 2 - self.x1, point * 2 - self.x3)
        else:
            return Simplex2(point, point * 2 - self.x2, point * 2 - self.x1)

    def expansion(self, point):
        if point == self.x1:
            return Simplex2(point, point * 3 - self.x2 * 2, point * 3 - self.x3 * 2)
        elif point == self.x2:
            return Simplex2(point, point * 3 - self.x1 * 2, point * 3 - self.x3 * 2)
        else:
            return Simplex2(point, point * 3 - self.x2 * 2, point * 3 - self.x1 * 2)

    def contraction(self, point):
        if point == self.x1:
            return Simplex2(point, (point + self.x2) / 2, (point + self.x3) / 2)
        elif point == self.x2:
            return Simplex2(point, (point + self.x1) / 2, (point + self.x3) / 2)
        else:
            return Simplex2(point, (point + self.x2) / 2, (point + self.x1) / 2)
    
    def closestTo(self, object):
        distX1 = object.distance(self.x1)
        distX2 = object.distance(self.x2)
        distX3 = object.distance(self.x3)
        if distX1 < distX2 and distX1 < distX3:
            return self.x1
        elif distX2 < distX1 and distX2 < distX3:
            return self.x2
        else:
            return self.x3


if __name__ =="__main__":
    from graphics import createCanvas
    
    canvas = createCanvas(500, 500)
    circle = Circle(250, 250, 100)
    point = Vector2(250, 250)
    pointCercle = Vector2(250, 150)
    point1 = Vector2(250, 240)
    point2 = Vector2(210, 270)
    point3 = Vector2(300, 290)
    simplexe = Simplex2(point1, point2, point3)

    print(circle)
    print(point)

    print("\n\nValeurs entre cercle et point :")
    print(circle.distance(point))
    print(circle.f(point))
    print(circle.fx(point.x))
    print(circle.fy(point.y))
    print("\n\nValeurs entre centre et point :")
    print(circle.center.distance(point))
    print(circle.center.f(point))
    print(circle.center.fx(point.x))
    print(circle.center.fy(point.y))
    print("\n\nValeurs entre cercle et pointCercle :")
    print(circle.distance(pointCercle))
    print(circle.f(pointCercle))
    print(circle.fx(pointCercle.x))
    print(circle.fy(pointCercle.y))
    print("\n\nValeurs entre centre et pointCercle :")
    print(circle.center.distance(pointCercle))
    print(circle.center.f(pointCercle))
    print(circle.center.fx(pointCercle.x))
    print(circle.center.fy(pointCercle.y))
    print("\n\nValeurs entre simplexe et cercle :")
    print(simplexe.closestTo(circle))
    print(circle.f(simplexe.closestTo(circle)))
    print(circle.fx(simplexe.closestTo(circle).x))
    print(circle.fy(simplexe.closestTo(circle).y))
    print("\n\nValeurs entre simplexe et centre :")
    print(simplexe.closestTo(circle.center))
    print(circle.center.f(simplexe.closestTo(circle.center)))
    print(circle.center.fx(simplexe.closestTo(circle.center).x))
    print(circle.center.fy(simplexe.closestTo(circle.center).y))

    simplexe.draw(canvas, "red")
    drawLine(canvas, point.x, point.y, pointCercle.x, pointCercle.y, "blue")
    circle.draw(canvas)
    simplexe.clear(canvas)
    input("continue ?")
    circle.draw(canvas)
    input("quit ?")