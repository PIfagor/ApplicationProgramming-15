from Vector import Vector
__author__ = 'Wise'

def min(a,b):
    if a < b :
        return a
    else:
        return b

def find_min(a, b, c, d):
    ab = Vector(a, b)
    ac = Vector(a, c)
    ad = Vector(a, d)

    cd = Vector(c, d)
    ca = Vector(c, a)
    cb = Vector(c, b)

    bd = Vector(b, d)

    if ab.cros_product(ac)*ab.cros_product(ad) <= 0 & cd.cros_product(ca)*cd.cros_product(cb) <= 0:
        print("Intersection")
        return min(ac.length()+cb.length(), ad.length()+bd.length())
    else:
        print("Not intersection")
        return ab.length()