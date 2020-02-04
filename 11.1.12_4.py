class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def get_slope(self, point2):
        return (point2.y - self.y) / (point2.x - self.x)

    def get_line_to(self, point2):
        slope = self.get_slope(point2)
        y_intercept = self.y - slope * self.x
        return (slope, y_intercept)

point1x = int(input('Enter x of Point 1: '))
point1y = int(input('Enter y of Point 1: '))
point1 = Point(point1x, point1y)
point2x = int(input('Enter x of Point 2: '))
point2y = int(input('Enter y of Point 2: '))
point2 = Point(point2x, point2y)
print('Slope and y-intercept: ', point1.get_line_to(point2))
