from SecondLabor.Point import Point
from Polygon import Polygon
__author__ = 'Wise'



def main():

    size = True
    n = 0
    #pointt = [Point(0, 0), Point(1, 3), Point(1, 2), Point(2, 3), Point(4, 1), Point(5, 1), Point(5, 0)]
    pointt = [Point(0, -4), Point(0, 2), Point(-3, -1), Point(3, -1), Point(-1, 0), Point(1, -2), Point(1, 0) , Point(-1, -2)]
    point = [Point(0, 5), Point(5, 0), Point(0, -5), Point(-5, 0)]
    points = []
    counter = 0
    control_point = 0
    with open('data.txt') as f:
        for line in f:
            int_list = [float(i) for i in line.split()]
            counter += 1
            if counter == 1:
                n = int_list[0]
                control_point = Point(int_list[1],int_list[2])
            else:
                if counter <= n+1:
                    points.append(Point(int_list[0],int_list[1]))
                #print int_list


    # for i in points:
    #     print(i._x   )
    #     print(  i._y)

    control_point = Point(2,2)

    poly = Polygon(pointt, False)
    print(poly.get_area())

    print(poly.is_point_belongs(control_point))
    print(poly.is_point_belongs_another(control_point))


    poly.write_to_file()

    return

if __name__ == "__main__":
    main()