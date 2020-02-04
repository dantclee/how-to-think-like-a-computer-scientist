class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def reflect_x(self):
        return Point(self.x, -self.y)

point1x = int(input('Enter x of Point 1: '))
point1y = int(input('Enter y of Point 1: '))
point1 = Point(point1x, point1y)
point2 = point1.reflect_x()
print('original point: ', point1)
print('new point: ', point2)
