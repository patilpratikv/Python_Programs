'''
I write this program to understand the 'class' in python.
It calculates different legacy values such as distance between points, slope of line &
volume and surface area of a cylinder.
Example:
    INPUT : Line((3, 2), (8, 10)) OUTPUT : Line.distance() = 9.433981 Line.slope() = 1.6
    INPUT : Cylinder(2, 3)        OUTPUT : Cylinder.surface_area() = 94.356  Cylinder.volume() = 56.6136
'''


class Line(object):

    def __init__(self, co_ord_1, co_ord_2):
        self.co_ord_x1 = co_ord_1[0]
        self.co_ord_y1 = co_ord_1[1]
        self.co_ord_x2 = co_ord_2[0]
        self.co_ord_y2 = co_ord_2[1]

    def distance(self):
        return (((self.co_ord_x2 - self.co_ord_x1)**2) + ((self.co_ord_y2 - self.co_ord_y1)**2))**(1.0/2)

    def slope(self):
        return (self.co_ord_y2 - self.co_ord_y1)/float((self.co_ord_x2 - self.co_ord_x1))


class Cylinder(object):

    pi = 3.1452

    def __init__(self, height=1, radius=1):
        self.height = float(height)
        self. radius = float(radius)

    def volume(self):
        return Cylinder.pi * self.radius**2 * self.height

    def surface_area(self):
        return (2 * Cylinder.pi * self.radius) * (self.height + self.radius)

# EOF
