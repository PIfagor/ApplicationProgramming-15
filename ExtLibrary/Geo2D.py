from __future__ import division
from math import sqrt

NAN = float('nan')
INF = float('inf')
DEBUG_MODE = True


def log(s):
    if DEBUG_MODE:
        print s
    return


@staticmethod
def set_debug(flag):
    assert isinstance(flag, int), "%r is not a bool" % flag
    DEBUG_MODE = flag
    return


class Point2D:
    def __init__(self, x, y=None):
        if y is None:  # init from tuple of 2 coords
            x, y = x
        self.X, self.Y = x, y

    def __str__(self):
        return '(%f;%f)' % (self.X, self.Y)

    def sqrDistanceTo(self, other):
        diffX, diffY = other.X - self.X, other.Y - self.Y
        return diffX * diffX + diffY * diffY

    def distanceTo(self, other):
        return sqrt(self.sqrDistanceTo(other))

    def __lt__(self, other):
        if not self.X == other.X:
            return self.X < other.X
        else:
            return self.Y < other.Y

    def __eq__(self, other):
        return other is not None and self.X == other.X and self.Y == other.Y

    def __cmp__(self, other):
        if self.X == other.X and self.Y == other.Y:
            return 0
        if self < other:
            return -1
        else:
            return 1


class Vector2D:
    def __init__(self, x, y=None):
        if y is None:  # init from tuple of 2 coords/points
            x, y = x
        if isinstance(x, Point2D):
            self.X, self.Y = y.X - x.X, y.Y - x.Y
        else:
            self.X = x
            self.Y = y

    def __str__(self):
        return '(%f,%f)' % (self.X, self.Y)

    def pseudoCrossProduct(self, b):
        return self.X * b.Y - self.Y * b.X


class Line2D:
    def __init__(self, a, b):
        if a == b:
            raise Exception("Cannot create a line from two equal points")
        self.point = a
        self.vector = Vector2D(b.X - a.X, b.Y - a.Y)

    def __str__(self):
        return '{%s,%s}' % (self.point, self.vector)

    def contains(self, point):
        v, p = self.vector, self.point
        ax, ay = v.X, v.Y
        x0, y0 = p.X, p.Y
        Ax, Ay = point.X, point.Y
        return ax * (Ay - y0) - ay * (Ax - x0) == 0

    # intersection of two lines, returns T
    def getIntersectionT(self, other):
        points = self.getTwoPoints() + other.getTwoPoints()
        (x1, y1), (x2, y2), (x3, y3), (x4, y4) = [(p.X, p.Y) for p in points]
        denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
        num = (x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)
        if denom == 0:
            if num == 0:
                return INF  # lines coincide
            else:
                return NAN  # lines are parallel
        return num / denom

    # returns Point2D or None
    def getIntersectionPoint(self, other):
        return self.getPoint(self.getIntersectionT(other))

    def coincides(self, other):
        return self.getIntersectionT(other) == INF

    def getPoint(self, t=0):
        if t in [NAN, INF]:
            return None
        x = self.point.X + t * self.vector.X
        y = self.point.Y + t * self.vector.Y
        return Point2D(x, y)

    def getVector(self):
        return self.vector

    def getTwoPoints(self):
        return self.point, Point2D(self.point.X + self.vector.X, self.point.Y + self.vector.Y)


class Segment2D:
    def __init__(self, a, b=None):
        if b is None:  # init from tuple of 2 points
            a, b = a
        if b < a:
            temp = a
            a = b
            b = temp
        self.a, self.b = a, b

    def __str__(self):
        return '[%s,%s]' % (self.a, self.b)

    def sqrLength(self):
        return self.a.sqrDistanceTo(self.b)

    def length(self):
        return self.a.distanceTo(self.b)

    def __cmp__(self, other):
        if self.a == other.a:
            return self.b.__cmp__(other.b)
        else:
            return self.a.__cmp__(other.a)

    def contains(self, point):
        if point == self.a:
            return True
        if self.a == self.b:
            return False
        l = Line2D(self.a, self.b)
        t = l.getIntersectionT(Line2D(self.a, point))
        if not t == INF:
            return False
        return self.a <= point <= self.b

    # intersection of two segments, returns Segment2D or None
    def getIntersectionSegment(self, other):
        if self.length() == 0:
            if other.contains(self.a):
                return Segment2D(self.a, self.a)
            else:
                return None
        elif other.length() == 0:
            if self.contains(other.a):
                return Segment2D(other.a, other.a)
            else:
                return None
        a, b = Line2D(self.a, self.b), Line2D(other.a, other.b)
        t = a.getIntersectionT(b)
        if t == INF:  # corresponding lines coincide
            segments = sorted([self, other])
            x = max(segments[0].a, segments[1].a)
            y = min(segments[0].b, segments[1].b)
            if x > y:
                return None
            return Segment2D(x, y)
        elif 0 <= t <= 1 and 0 <= b.getIntersectionT(a) <= 1:  # segments intersect
            point = a.getPoint(t)
            return Segment2D(point, point)
        else:
            return None  # lines are parallel or intersect with not 0<=t<=1

    def getFirstPoint(self):
        return self.a;

class Triangle2D:
    def __init__(self, a, b=None, c=None):
        if b is None:  # init from tuple of 2 points
            a, b, c = a
        self.a, self.b, self.c = a, b, c

    def __str__(self):
        return 'Triangle2D<%s, %s, %s>' % (self.a, self.b, self.c)

    def orientedSquare(self):
        a = Vector2D(self.a, self.b)
        b = Vector2D(self.a, self.c)
        return 0.5 * a.pseudoCrossProduct(b)

    def square(self):
        return abs(self.orientedSquare())


class Polygon2D():
    def __init__(self, points):
        if len(points) < 3:
            raise Exception("Cannot create a polygon from less than 3 points")
        self.A = points
        self.A.append(points[0])

    def __str__(self):
        s = 'Polygon2D[%s' + ', %s' * (len(self.A) - 2) + ']'
        return s % tuple(self.A[0:-1])

    def getPoints(self):
        return self.A[:-1]

    def square(self):
        A = self.A
        return abs(sum([Triangle2D(A[0], A[i], A[i + 1]).orientedSquare() for i in range(1, len(A) - 2)]))

    def contains(self, p):
        A = self.A
        res = False
        i = -1
        while i < len(A) - 2:
            i += 1
            edge = Segment2D(A[i], A[i + 1])
            log(edge)
            if edge.contains(p):
                log('Edge contains p')
                return True
            # move rightwards horizontally from p
            maxX = max(A[i].X, A[i + 1].X)
            if maxX <= p.X:
                log('lies to the left of p')
                continue
            ray = Segment2D(p, Point2D(maxX, p.Y))
            intrsct = ray.getIntersectionSegment(edge)
            if intrsct is None:
                log('does not intersect with the ray')
                continue
            prevI, nextI = None, None
            if intrsct.length() == 0:
                if intrsct.a == A[i + 1]:
                    log('the ray contains the end vertice, ignored')
                    continue
                if intrsct.a == A[i]:
                    log('the ray contains the start vertice')
                    prevI = i - 1
                    nextI = i + 1
                else:
                    log('counted')
                    res = not res
            else:
                log('the ray contains the whole edge')
                prevI = i - 1
                nextI = i + 2
                # ignore the next edge
                i += 1
            if not prevI is None:
                if prevI == -1:
                    # since self.A has duplicated A[0]
                    prevI = -2
                nextI = nextI % len(A)
                if nextI == 0:
                    # since self.A has duplicated A[0]
                    nextI = 1
                # calculate whether A[prevI],A[nextI] lie on different sides of ray
                v = Vector2D(ray.a, ray.b)
                pseudoCrossProducts = [v.pseudoCrossProduct(Vector2D(p, P)) for P in (A[prevI], A[nextI])]
                if pseudoCrossProducts[0] * pseudoCrossProducts[1] < 0:
                    log('counted')
                    res = not res
                else:
                    log('ignored')
        return res

    @staticmethod
    def build(points):
        points = sorted(points)
        start, end = points[0], points[-1]
        splitter = Vector2D(start, end)
        upper, lower = [], []
        for point in points:
            if splitter.pseudoCrossProduct(Vector2D(start, point)) < 0:
                lower.insert(0, point)
            else:
                upper.append(point)
        return Polygon2D(upper + lower)
