from Point import Point
from math import sqrt
__author__ = 'Wise'


class Vector:
    def __init__(self, str, end):
        self._x = str._x - end._x
        self._y = str._y - end._y
        return

    def cros_product(self, another_vector):
        return self._x * another_vector._y -  another_vector._x * self._y

    def length(self):
        return sqrt(self._x*self._x+self._y*self._y)

    # def cros_product(self, vector, another_vector):
    #      return vector._x * another_vector._y -  another_vector._x * vector._y

