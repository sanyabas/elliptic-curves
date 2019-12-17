from polynomial import Polynomial
from point import Point
from field import FieldZp


class CurveZp:
    def __init__(self, p: int, a: int, b: int):
        self._p = p
        self._a = a
        self._b = b
        self._field = FieldZp(p)

    def add(self, first: 'Point', second: 'Point'):
        if first.is_infinity():
            return second
        if second.is_infinity():
            return first
        if first.x == second.x:
            if first.y == 0 and second.y == 0:
                return Point.infinity()
            if first.y + second.y == 0:
                return Point.infinity()
            k = ((3 * first.x * first.x + self._a) * self._field.inverse(2 * first.y)) % self._p
        else:
            k = ((second.y - first.y) * self._field.inverse(second.x - first.x)) % self._p
        x3 = (k * k - first.x - second.x) % self._p
        y3 = (first.y + k * (x3 - first.x)) % self._p

        return Point((x3, -y3 % self._p))

    def mul(self, first: 'Point', second: int):
        result = Point.infinity()
        addend = first

        while second:
            if second & 1:
                result = self.add(result, addend)

            addend = self.add(addend, addend)

            second >>= 1

        return result


class CurveGF:
    def __init__(self, p: 'Polynomial', a: 'Polynomial', b: 'Polynomial', c: 'Polynomial'):
        self._p = p
        self._a = a
        self._b = b
        self._c = c

    def add(self, first: 'Point', second: 'Point'):
        if first.is_infinity():
            return second
        if second.is_infinity():
            return first
        if first.x == second.x:
            if second.y == self._a * first.x + first.y:
                return Point.infinity()
            k = ((first.x * first.x + self._a * first.y) * (self._a * first.x).invert(self._p)) % self._p
        else:
            k = ((first.y + second.y) * (first.x + second.x).invert(self._p)) % self._p
        x3 = (k * k + self._a * k + self._b + first.x + second.x) % self._p
        y3 = (first.y + k * (x3 + first.x)) % self._p

        return Point((x3, (self._a * x3 + y3) % self._p))

    def mul(self, first: 'Point', second: int):
        result = Point.infinity()
        addend = first

        while second:
            if second & 1:
                result = self.add(result, addend)

            addend = self.add(addend, addend)

            second >>= 1

        return result
