from math import *
from SecondLabor.Vector import *
__author__ = 'Wise'


class Polygon:

    ordered_points = []

    def __init__(self, points,mode):
        if mode:
            self.points_arr = points
            self.make_poligon()
        else :
            self.ordered_points = points
            self.ordered_points.append(self.ordered_points[0])
        return

    def make_poligon(self):
        self.sort_by_X()
        main_line = Vector(self.points_arr[0], self.points_arr[len(self.points_arr)-1])
        for i in range(len(self.points_arr)):
            if main_line.cros_product(Vector(main_line._str, self.points_arr[i])) >= 0:
                self.ordered_points.append(self.points_arr[i])

        for i in range(len(self.points_arr)-1):
            if main_line.cros_product(Vector(main_line._str, self.points_arr[i])) < 0:
                self.ordered_points.append(self.points_arr[i])

        self.ordered_points.append(self.ordered_points[0])
        return

    def get_area(self):
       sums = 0.
       for i in range(len(self.ordered_points)-1):
           sums += (self.ordered_points[i+1]._y + self.ordered_points[i]._y)/2*(self.ordered_points[i+1]._x - self.ordered_points[i]._x)

       return abs(sums)

    def sort_by_X(self):
        for i in range(len(self.points_arr)):
            for j in range(i, len(self.points_arr)-1):
                if self.points_arr[j]._x > self.points_arr[j+1]._x:
                    temp = self.points_arr[j]
                    self.points_arr[j] = self.points_arr[j+1]
                    self.points_arr[j+1] = temp
        return

    def is_point_belongs(self,pointt):
        y = pointt._y
        x = pointt._x
        count = 0

        for i in range(len(self.ordered_points)-1):
            if (x < self.ordered_points[i]._x or x < self.ordered_points[i+1]._x) and y - self.ordered_points[i]._y == 0:
                    if i != 0 and (y - self.ordered_points[i-1]._y) * (y - self.ordered_points[i+1]._y) < 0:
                        count += 1
            elif (x < self.ordered_points[i]._x or x < self.ordered_points[i+1]._x) and ((y - self.ordered_points[i]._y) * (y - self.ordered_points[i+1]._y)) < 0 :
                count += 1
        return count % 2 != 0

    def write_to_file(self):
        f = open('result.txt','w')
        write_point = self.ordered_points
        del write_point[-1]
        size = len(write_point)
        f.write(str(size)+'\n')
        for point in write_point:
            f.write(str(point._x)+' '+str(point._y)+'\n')


        f.close() # you can omit in most cases as the destructor will call it