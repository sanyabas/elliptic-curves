class Point:
    funcs = {
        2: bin,
        10: str,
        16: hex
    }

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
        return self.format()

    def format(self, base=10):
        formatter = Point.funcs[base]
        return 'O' if self.is_infinity() else f'({formatter(self.x)},{formatter(self.y)})'
