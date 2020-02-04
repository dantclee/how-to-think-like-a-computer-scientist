class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height *2

    def flip(self):
        self.width, self.height = self.height, self.width

r = Rectangle(Point(100, 50), 10, 5)
print('r before: ', r)
r.flip()
print('r after: ', r)
