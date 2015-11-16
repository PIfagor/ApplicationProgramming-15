from Point import *
from Vector import Vector


class SpiderAndFly:
    def __init__(self, parallelepiped, spider, fly):
        assert isinstance(parallelepiped, Point3D), "%r is not a Point" % parallelepiped
        assert isinstance(spider, Point3D), "%r is not a Point" % spider
        assert isinstance(fly, Point3D), "%r is not a Point" % fly
        # assert type(parallelepiped) is Point, "parallelepiped is not a Point"

        assert spider._y == 0
        assert fly._y == parallelepiped._y

        self._parrel = parallelepiped
        self._spider = spider
        self._fly = fly

        return

    def set_intersection_points(self, main_vector, first_edge, second_edge, zero_coordinate, coordinate):
        assert isinstance(main_vector, Vector), "%r is not a Vector" % main_vector
        assert isinstance(first_edge, Vector), "%r is not a Vector" % first_edge
        assert isinstance(second_edge, Vector), "%r is not a Vector" % second_edge
        f_point = main_vector.intersection(first_edge)
        s_point = main_vector.intersection(second_edge)
        if zero_coordinate == 'z':
            self._first_itersection_point = Point3D(f_point._x,f_point._y,coordinate)
            self._second_itersection_point = Point3D(s_point._x,s_point._y,coordinate)
        elif zero_coordinate == 'x':
            self._first_itersection_point = Point3D(f_point._x,f_point._y,coordinate)
            self._second_itersection_point = Point3D(s_point._x,s_point._y,coordinate)
        elif zero_coordinate == 'y':
            self._first_itersection_point = Point3D(f_point._x,f_point._y,coordinate)
            self._second_itersection_point = Point3D(s_point._x,s_point._y,coordinate)
        else:
            assert True, "Not correct cordinate, try: x, y or z"
        return

    def find_min_distanse(self):
        px = self._parrel._x
        py = self._parrel._y
        pz = self._parrel._z

        sx = self._spider._x
        sy = self._spider._y
        sz = self._spider._z

        fx = self._fly._x
        fy = self._fly._y
        fz = self._fly._z

        # block 1
        new_spider = Point(sx,sy-sz)
        new_fly = Point(fx,fy+fz)
        min_dist_3d = Point3D(sx, sy-sz, 0).distanse(Point3D(fx, fy+fz, 0))
        min_dist = new_spider.distanse(new_fly)
        self.set_intersection_points(Vector(new_spider, new_fly), Vector(Point(0, 0), Point(px, 0)), Vector(Point(0, py), Point(px, py)), 'z', 0)

        # block 2
        new_spider = Point(sx, sy-pz+sz)
        new_fly = Point(fx,fy+pz-fz)
        temp_min_dist = new_spider.distanse(new_fly)
        if temp_min_dist < min_dist:
            min_dist = temp_min_dist
            self.set_intersection_points(Vector(new_spider, new_fly), Vector(Point(0, 0), Point(px, 0)), Vector(Point(0, py), Point(px, py)), 'z', pz)

        # block 3
        new_spider = Point(sz,sy-sx)
        new_fly = Point(fz,fy+fx)
        temp_min_dist = new_spider.distanse(new_fly)
        if temp_min_dist < min_dist:
            min_dist = temp_min_dist
            self.set_intersection_points(Vector(new_spider, new_fly), Vector(Point(0, 0), Point(pz, 0)), Vector(Point(0, py), Point(pz, py)), 'x', 0)

        # block 4
        new_spider = Point(sz, sy-px+sx)
        new_fly = Point(fz,fy+px-fx)
        temp_min_dist = new_spider.distanse(new_fly)
        if temp_min_dist < min_dist:
            min_dist = temp_min_dist
            self.set_intersection_points(Vector(new_spider, new_fly), Vector(Point(0, 0), Point(pz, 0)), Vector(Point(0, py), Point(pz, py)), 'x', pz)

        return min_dist
