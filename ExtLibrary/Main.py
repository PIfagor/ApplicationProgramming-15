from Geo2D import *

__author__ = 'Wise'


def test(maya):
    assert isinstance(maya, int), "%r is not a int" % maya
    if maya == 0:
         srcpath = 'NotPolygon.txt'
         with open(srcpath) as src:
            coords = [float(x) for x in src.readline().split(' ')]
            points = [Point2D(coords[x], coords[x+1]) for x in range(0, len(coords), 2)]
            polygon = Polygon2D.build(points)
            print polygon
    elif maya == 1:
        srcpath = 'PointAndPolygon.txt'
        with open(srcpath) as src:
            coords = [float(x) for x in src.readline().split(' ')]
            points = [Point2D(coords[x], coords[x+1]) for x in range(0, len(coords), 2)]
            A = points[0]
            polygon_points = points[1:]
            poly = Polygon2D(polygon_points)
            res = poly.contains(A)
            print(res)
    elif maya == 2:
        srcpath = 'NotPolygon.txt'
        with open(srcpath) as src:
            coords = [float(x) for x in src.readline().split(' ')]
            polygon_points = [Point2D(coords[x], coords[x+1]) for x in range(0, len(coords), 2)]
            poly = Polygon2D(polygon_points)
            res = poly.square()
            print(res)
    elif maya == 3:
        srcpath = 'Segment.txt'
        with open(srcpath) as src:
            coords = [float(x) for x in src.readline().split(' ')]
            pp = [Point2D(coords[x], coords[x+1]) for x in range(0, len(coords), 2)]
            a = pp[0]
            b = pp[1]
            c = pp[2]
            d = pp[3]
            ab = Segment2D(a, b)
            cd = Segment2D(c, d)
            # print(ab)
            # print(cd)
            res = ab.getIntersectionSegment(cd)
            if not res:
              print('Not interction!')
              print ('Min distance: %s' % ab.length())
            else:
              print('Interction!')
              print ('Point of interction: %s' %res.getFirstPoint())
              print ('Min distance: %s' % min(Segment2D(a, c).length()+Segment2D(c, b).length(), Segment2D(a, d).length() + Segment2D(d, b).length()))


def main():
    test_number = 3
    test(test_number)

    return

if __name__ == "__main__":
    main()
