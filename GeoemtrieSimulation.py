import math

from Simulation import Simulation

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __neg__(self):
        return Punkt(-self.x, -self.y)

    def __add__(self, other):
        return Punkt(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Punkt(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Punkt(self.x * other, self.y * other)

    def runde(self):
        return Punkt(int(round(self.x)), int(round(self.y)))

class Matrix:
    def __init__(self, a, b, tx, c, d, ty):
        self.a = a
        self.b = b
        self.tx = tx
        self.c = c
        self.d = d
        self.ty = ty
        
    @staticmethod
    def identitaet():
        return Matrix(1, 0, 0, 0, 1, 0)
    
    @staticmethod
    def translation(punkt):
        return Matrix(1, 0, punkt.x, 0, 1, punkt.y)
    
    @staticmethod
    def rotation(winkel):
        winkelRad = math.radians(winkel)
        c = math.cos(winkelRad)
        s = math.sin(winkelRad)
        return Matrix(c, -s, 0, s, c, 0)
    
    def __mul__(self, other):
        if isinstance(other, Punkt):
            return Punkt(
                self.a * other.x + self.b * other.y + self.tx,
                self.c * other.x + self.d * other.y + self.ty,
            )
        
        if isinstance(other, Matrix):
            return Matrix(
                self.a * other.a + self.b * other.c,
                self.a * other.b + self.b * other.d,
                self.a * other.tx + self.b * other.ty + self.tx,
                self.c * other.a + self.d * other.c,
                self.c * other.b + self.d * other.d,
                self.c * other.tx + self.d * other.ty + self.ty,
            )
        
        return NotImplemented
    
class GeoemtrieSimulation(Simulation):
    def linie(self, p0, p1, farbe):
        p0i = p0.runde()
        p1i = p1.runde()

        x0 = p0i.x
        y0 = p0i.y
        x1 = p1i.x
        y1 = p1i.y

        dx = abs(x1 - x0)
        dy = -abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx + dy

        x = x0
        y = y0
        while True:
            self.setze(x, y, farbe)
            if x == x1 and y == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x += sx
            if e2 <= dx:
                err += dx
                y += sy

    def rechteck(self, p0, p1, farbe):
        self.linie(Punkt(p0.x, p0.y), Punkt(p0.x, p1.y), farbe)
        self.linie(Punkt(p0.x, p1.y), Punkt(p1.x, p1.y), farbe)
        self.linie(Punkt(p1.x, p1.y), Punkt(p1.x, p0.y), farbe)
        self.linie(Punkt(p1.x, p0.y), Punkt(p0.x, p0.y), farbe)

    def kreis(self, mittelpunkt, radius, farbe):
        bboxMinX = int(mittelpunkt.x - radius)
        bboxMaxX = int(mittelpunkt.x + radius)
        bboxMinY = int(mittelpunkt.y - radius)
        bboxMaxY = int(mittelpunkt.y + radius)

        r2 = radius * radius
        for y in range(bboxMinY, bboxMaxY + 1):
            for x in range(bboxMinX, bboxMaxX + 1):
                dx = x - mittelpunkt.x
                dy = y - mittelpunkt.y
                if dx * dx + dy * dy <= r2:
                    self.setze(x, y, farbe)

    def dreieck(self, a, b, c, farbe):
        self.linie(a, b, farbe)
        self.linie(b, c, farbe)
        self.linie(c, a, farbe)