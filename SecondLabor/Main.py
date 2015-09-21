from Point import Point
from MinimalDistance import find_min


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

    return points



def main():
    a = Point(1, 5)
    b = Point(2, 12)
    c = Point(1, 5)
    d = Point(1, 5)

    points = testing(0)

    #print(find_min(a, b, c, d))
    print(find_min(points[0], points[1], points[2], points[3]))

    return

if __name__ == "__main__":
    main()