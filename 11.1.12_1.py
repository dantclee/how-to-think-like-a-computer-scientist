import math

class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

def distance(point1, point2):
    return math.sqrt((point2.x - point1.x)**2 + (point2.y - point1.y) **2)

point1x = int(input('Enter x of Point 1: '))
point1y = int(input('Enter y of Point 1: '))
point2x = int(input('Enter x of Point 2: '))
point2y = int(input('Enter y of Point 2: '))


print(distance(Point(point1x, point1y), Point(point2x, point2y)))
