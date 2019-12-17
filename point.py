import math


class Point:
    def __init__(self, point):
        (x, y) = point

        self.x = x
        self.y = y

    @staticmethod
    def infinity():
        return Point((math.inf, math.inf))

    def clone(self):
        return Point((self.x, self.y))

    def __str__(self):
        return f'({self.x},{self.y})'
