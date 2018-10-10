import math


class Point:
    x = 0
    y = 0

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Polygon:
    n = 0
    points = []

    def __init__(self, lst = []):
        self.n = len(lst)
        self.points = lst[:]

    def __str__(self):
        s = ''
        for x in self.points:
            s += str(x) + ' '
        return str(self.n) + ': ' + s

    def fromCoords(self, coords):
        xlist = coords[::2]
        ylist = coords[1::2]
        return Polygon([Point(xlist[i], ylist[i]) for i in range(len(xlist))])

    def perim(self):
        s = self.points[0].distance(self.points[-1])
        for i in range(self.n - 1):
            s += self.points[i].distance(self.points[i + 1])
        return s

    def square(self):
        def s3(a, b, c):
            ab = a.distance(b)
            bc = b.distance(c)
            ac = a.distance(c)
            p = (ab + bc + ac) / 2
            return math.sqrt(p * (p - ab) * (p - bc) * (p - ac))

        s = 0
        for i in range(1, self.n - 1):
            s += s3(self.points[0], self.points[i], self.points[i + 1])
        return s


n = int(input())
ans = [0, -1]
for i in range(n):
    plg = Polygon(lst=list(input().split())[1:])
    if plg.square() >= ans[0]:
        ans = [plg.square(), i + 1]
print(ans[1])
