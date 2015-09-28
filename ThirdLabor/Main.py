from SecondLabor.Point import Point
from Polygon import Polygon
__author__ = 'Wise'



def main():

    size = True
    n = 0
    #points = [Point(2, 1), Point(2, 3), Point(4, 5), Point(6, 3), Point(6, 1), Point(5, 1), Point(4, 2)]
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

    poly = Polygon(points, False)
    print(poly.get_area())

    print(poly.is_point_belongs(control_point))

    poly.write_to_file()

    return

if __name__ == "__main__":
    main()