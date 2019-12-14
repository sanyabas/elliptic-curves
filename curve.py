from .polynomial import Polynomial
from .point import Point


class CurveZp:
    def __init__(self, p: int, a: int, b: int):
        self._p = p
        self._a = a
        self._b = b

    def add(self, first: 'Point', second: 'Point'):
        if first.x == second.x:
            

class CurveGF:
    def __init__(self, p: 'Polynomial', a: int, b: int, c: int):
        self._p = p
        self._a = a
        self._b = b
        self._c = c

