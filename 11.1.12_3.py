class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def slope_from_origin(self):
        return self.y / self.x

pointx = int(input('Enter x of Point: '))
pointy = int(input('Enter y of Point: '))
point = Point(pointx, pointy)

print('Slope: ', point.slope_from_origin())
