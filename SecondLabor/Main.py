from MinimalDistance import *
from SpiderAndFly import *

__author__ = 'Wise'


def testing(number_test):
    points = [Point(-9, -6), Point(-6, -3), Point(-8, -8), Point(-5, -5)]
    if number_test == 0:
        points[0] = Point(10, 12)
        points[1] = Point(2, 4)
        points[2] = Point(4, 8)
        points[3] = Point(8, 2)
    elif number_test == 1:
        points[0] = Point(-10, 4)
        points[1] = Point(-4, 10)
        points[2] = Point(-2, 3)
        points[3] = Point(-7, 5)
    elif number_test == 2:
        points[0] = Point(2, -4)
        points[1] = Point(4, -2)
        points[2] = Point(8, -8)
        points[3] = Point(5, -5)
    elif number_test == 3:
        points[0] = Point(2, -4)
        points[1] = Point(4, -2)
        points[2] = Point(8, -8)
        points[3] = Point(5, -5)
    return points


def main():

    a = Point(0., 0.)
    b = Point(9., 9.)
    c = Point(6., 5.)
    d = Point(2., 10.)

    # v1 = Vector(a,b)
    # v2 = Vector(c,d)
    #
    # res = v1.intersection(v2)
    # print(res._x)
    # print(res._y)

    points = testing(0)

    # print(find_min(a, b, c, d))
    print(find_min_new(a, b, c, d))
    # print(find_min(points[0], points[1], points[2], points[3]))
    print(find_min_new(points[0], points[1], points[2], points[3]))

    spider = Point3D(2., 0., 3.)
    fly = Point3D(3., 5., 3.)
    pall = Point3D(10., 5., 6.)
    spider_man = SpiderAndFly(pall, spider, fly)
    print(spider_man.find_min_distanse())
    spider_man._first_itersection_point.showing()
    spider_man._second_itersection_point.showing()
    return

if __name__ == "__main__":
    main()
