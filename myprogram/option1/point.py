# import libraries
from math import sqrt
from pygame.draw import circle
from pygame.draw import rect
from myprogram.interface import BLACK, WHITE, COLORS, LIGHT_COLORS


class Point:
    """
     A class to represent a two-dimensional data point.

     ...

     Attributes
     ----------
     x : float
         coordinates[0]
     y : float
         coordinates[1]
     label : None/int
         data is labeled after K - means predict

     Methods
     -------
     distance(point2):
         return value of distance between two points
    update_coordinates(x, y):
         update coordinates of point
    update_label(label):
         update label
    return_coordinates():
        return value of coordinates
    return_label():
         return label
    show(screen):
         draw point on the screen
    draw_boundary(screen):
         draw rectangle with color depends on label
         this function supports to draw boundaries after running K - means
     """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.label = None

    def distance(self, point2):
        """
        Calculate the distance between two points
        Parameter:
            point2 is another Point object
        Returns:
            value of distance (float)
        """
        return sqrt((self.x - point2.x) ** 2 + (self.y - point2.y) ** 2)

    def update_coordinates(self, x, y):
        self.x = x
        self.y = y

    def update_label(self, label):
        self.label = label

    def return_coordinates(self):
        return [self.x, self.y]

    def return_label(self):
        return self.label

    def show(self, screen):
        circle(screen, BLACK, (self.x + 50, self.y + 50), 6)
        if None == self.label:
            circle(screen, WHITE, (self.x + 50, self.y + 50), 5)
        else:
            circle(screen, COLORS[self.label], (self.x + 50, self.y + 50), 5)

    def draw_boundary(self, screen):
        if None != self.label:
            rect(screen, LIGHT_COLORS[self.label],
                 (self.return_coordinates()[0] + 50, self.return_coordinates()[1] + 50, 5, 5))


class PointCluster(Point):
    """
     A derived class of Point class.

     ...

     Attributes
     ----------
     same as base class
     x : float
         coordinates[0]
     y : float
         coordinates[1]
     label : None/int
         data is labeled after K - means predict

     Methods
     -------
    show(screen):
         draw point on the screen with size of circle is bigger

     """
    def show(self, screen):
        circle(screen, COLORS[self.label], (self.x + 50, self.y + 50), 10)
