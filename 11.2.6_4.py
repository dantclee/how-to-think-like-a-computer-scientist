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
        """ Initialize rectangle with lower left corner at posn, with width w, height h """
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

    def contains(self, point):
        """ test if a Point object fall within the Rectangle object. """
        x_upper_bound = self.corner.x + self.width
        y_upper_bound = self.corner.y + self.height
        if (self.corner.x <= point.x < x_upper_bound) and (self.corner.y <= point.y < y_upper_bound):
            return True
        else:
            return False

r = Rectangle(Point(0, 0), 10, 5)
print(r.contains(Point(0, 0)))
print(r.contains(Point(3, 3)))
print(not r.contains(Point(3, 7)))
print(not r.contains(Point(3, 5)))
print(r.contains(Point(3, 4.99999)))
print(not r.contains(Point(-3, -3)))
