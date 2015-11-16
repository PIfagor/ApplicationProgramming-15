from Vector import Vector
__author__ = 'Wise'


def min(a,b):
    if a < b :
        return a
    else:
        return b


def intersect(a, b, c, d):
    if a > b :
       a,b = b,a
    if c > d:
       c,d = d,c
    return max(a, c) <= min(b, d)



def find_min(a, b, c, d):
    ab = Vector(a, b)
    ac = Vector(a, c)
    ad = Vector(a, d)

    cd = Vector(c, d)
    ca = Vector(c, a)
    cb = Vector(c, b)

    bd = Vector(b, d)

    if intersect(a,b,c,d):
        print("Not intersection")
        return ab.length()

    elif ab.cros_product(ac)*ab.cros_product(ad) <= 0 and cd.cros_product(ca)*cd.cros_product(cb) <= 0:
        print("Intersection")
        return min(ac.length()+cb.length(), ad.length()+bd.length())
    else:
        print("Not intersection")
        return ab.length()


def find_min_new (a,b,c,d):
      ab = Vector(a, b)
      cd = Vector(c, d)

      res_intersection = ab.is_intersection(cd)
      if res_intersection == 0:
            print("One end of segment belongs another segment")
            return ab.length()
      elif res_intersection < 0:
            print("Not intersection")
            return ab.length()
      else:
            bd = Vector(b, d)
            ad = Vector(a, d)
            cb = Vector(c, b)
            ac = Vector(a, c)
            print("Intersection")
            return min(ac.length()+cb.length(), ad.length()+bd.length())
