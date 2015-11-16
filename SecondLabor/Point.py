__author__ = 'Wise'
from math import  sqrt

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        return

    def equals(self, another_point):
        return self._x == another_point._x and self._y == another_point._y

    def distanse(self, another_point):
        assert isinstance(another_point, Point), "%r is not a Point" % another_point
        return sqrt((self._x - another_point._x)*(self._x - another_point._x) + (self._y - another_point._y)*(self._y - another_point._y) )


class Point3D:
    def __init__(self, x, y,z):
        self._x = x
        self._y = y
        self._z = z
        return

    def equals(self, another_point):
        assert isinstance(another_point, Point3D), "%r is not a Point" % another_point
        return self._x == another_point._x and self._y == another_point._y and self._z == another_point._z

    def distanse(self, another_point):
        assert isinstance(another_point, Point3D), "%r is not a Point" % another_point
        return sqrt((self._x - another_point._x)*(self._x - another_point._x) + (self._y - another_point._y)*(self._y - another_point._y) + (self._z - another_point._z)*(self._z - another_point._z))