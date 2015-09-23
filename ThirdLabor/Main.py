from SecondLabor.Point import Point
from Polygon import Polygon
__author__ = 'Wise'



# def testing(number_test):
#     points = [Point(-9, -6), Point(-6, -3), Point(-8, -8), Point(-5, -5)]
#     if number_test == 0:
#         points[0] = Point(10, 12)
#         points[1] = Point(2, 4)
#         points[2] = Point(4, 8)
#         points[3] = Point(8, 2)
#     elif number_test == 1:
#         points[0] = Point(-10, 4)
#         points[1] = Point(-4, 10)
#         points[2] = Point(-2, 3)
#         points[3] = Point(-7, 5)
#     elif number_test == 2:
#         points[0] = Point(2, -4)
#         points[1] = Point(4, -2)
#         points[2] = Point(8, -8)
#         points[3] = Point(5, -5)
#
#     return points



def main():
    points = [Point(2, 1), Point(2, 3), Point(4, 5), Point(6, 3), Point(6, 1), Point(5, 1), Point(4, 2)]
    poly = Polygon(points, True)
    print(poly.get_area())

    print(poly.is_point_belongs(Point(3, 2)))
    return

if __name__ == "__main__":
    main()