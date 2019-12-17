import math


class Point:
    def __init__(self, point):
        (x, y) = point

        self.x = x
        self.y = y

    @staticmethod
    def infinity():
        return Point((None, None))

    def is_infinity(self):
        return self.x is None and self.y is None

    def clone(self):
        return Point((self.x, self.y))

    def __str__(self):
        return f'({self.x},{self.y})'
