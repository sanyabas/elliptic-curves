class FieldZp:
    def __init__(self, p):
        self._p = p

    def inverse(self, num: int) -> int:
        s, old_s = 0, 1
        r, old_r = self._p, num

        while r != 0:
            quotient = old_r // r

            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s

        gcd, x = old_r, old_s

        return x % self._p
