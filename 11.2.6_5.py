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
        """ return the position of lower left corner, width and height of a rectangule object."""
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def area(self):
        """ return the area of a rectangle object. """
        return self.width * self.height

    def perimeter(self):
        """ return the perimeter of a rectangle object."""
        return self.width * 2 + self.height *2

    def flip(self):
        """ flip the width and the height of a rectangle object."""
        self.width, self.height = self.height, self.width

    def contains(self, point):
        """ test if a Point object fall within a rectangle object.
        Assume that a rectangle at (0,0) with width 10 and height 5 has open upper bounds on the width and height,
        i.e. it stretches in the x direction from [0 to 10), where 0 is included but 10 is excluded, and from [0 to 5) in the y direction.
        So it does not contain the point (10, 2)."""
        x_upper_bound = self.corner.x + self.width
        y_upper_bound = self.corner.y + self.height
        if (self.corner.x <= point.x < x_upper_bound) and (self.corner.y <= point.y < y_upper_bound):
            return True
        else:
            return False

    def get_all_points_perimeter(self):
        """ Get all points on the perimeter of a rectangle object into a list of tuples. """
        self.point_perimeter = set([])
        x_coordinate_lower_right_corner = self.corner.x + self.width
        y_coordinate_upper_left_corner = self.corner.y + self.height
        # get points on the base of the Rectangle object
        for base in range(x_coordinate_lower_right_corner):
            self.point_perimeter.add((base, self.corner.y))
        # get points on the left edge of the Rectangle object
        for left_edge in range(y_coordinate_upper_left_corner):
            self.point_perimeter.add((self.corner.x, left_edge))
        #get points on the right edge of the Rectangle object
        for right_edge in range(y_coordinate_upper_left_corner):
            self.point_perimeter.add(((x_coordinate_lower_right_corner), right_edge))
        # get points on the top of the Rectangle object
        for top in range(x_coordinate_lower_right_corner):
            self.point_perimeter.add((top, (y_coordinate_upper_left_corner)))
        return self.point_perimeter

    def collision_detection(self, rectangle):
        """ check if two rectangle objects overlap. """
        for tuple in rectangle.get_all_points_perimeter():
            (x_coordinate, y_coordinate) = tuple
            point = Point(x_coordinate, y_coordinate)
            if self.contains(point):
                return True
        return False

r1 = Rectangle(Point(0, 0), 10, 5)
r2 = Rectangle(Point(10, 5), 10, 5)
print(r1.collision_detection(r2))
