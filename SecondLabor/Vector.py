from Point import Point
from math import *
__author__ = 'Wise'


class Vector:
    def __init__(self, str, end):
        self._x = str._x - end._x
        self._y = str._y - end._y
        self._str = str
        self._end = end
        return

    def cros_product(self, another_vector):
        assert isinstance(another_vector, Vector), "%r is not a Vector" % another_vector
        return self._x * another_vector._y -  another_vector._x * self._y

    def length(self):
        return sqrt(self._x*self._x+self._y*self._y)

    def intersection(self, another_vector):
         assert isinstance(another_vector, Vector), "%r is not a Vector" % another_vector

         #this vector is ab another cd
         a = self._str
         b = self._end
         c = another_vector._str
         d = another_vector._end

         z1 = self.cros_product(Vector(a, c))
         z2 = self.cros_product(Vector(a, d))


         #assert z1*z2 != 0, " one Point belong another Vector"
         #assert  z1*z2 < 0, "Vectors never intersaction"

         px = c._x + (d._x - c._x) * abs(z1)/abs(z2-z1)
         py = c._y + (d._y - c._y) * abs(z1)/abs(z2-z1)
         return Point (px,py)

    def is_intersection(self, another_vector):
         assert isinstance(another_vector, Vector), "%r is not a Vector" % another_vector

         #this vector is ab another cd
         a = self._str
         c = another_vector._str
         d = another_vector._end

         z1 = self.cros_product(Vector(a, c))
         z2 = self.cros_product(Vector(a, d))

         if z1*z2 == 0: return 0
         if z1*z2 > 0: return -1

         return 1

    # def cros_product(self, vector, another_vector):
    #       return vector._x * another_vector._y -  another_vector._x * vector._y

