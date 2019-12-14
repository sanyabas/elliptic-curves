import math


class Point:
    def __init__(self, point):
        (x, y) = point

        self.x = x
        self.y = y

    @staticmethod
    def infinity():
        return Point((math.inf, math.inf))