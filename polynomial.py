import re


class Polynomial:
    _irreducible = {
        2: 'x^2+x+1',
        3: 'x^3+x+1',
        4: 'x^4+x+1',
        5: 'x^5+x^2+1',
        6: 'x^6+x+1',
        7: 'x^7+x^3+1',
        8: 'x^8+x^4+x^3+x^2+1',
        9: 'x^9+x^4+1',
        10: 'x^10+x^3+1',
        11: 'x^11+x^2+1',
        12: 'x^12+x^6+x^4+x+1',
        13: 'x^13+x^4+x^3+x+1',
        14: 'x^14+x^10+x^6+x+1',
        15: 'x^15+x+1',
        16: 'x^16+x^12+x^3+x+1',
        17: 'x^17+x^3+1',
        18: 'x^18+x^7+1',
        19: 'x^19+x^5+x^2+x+1',
        20: 'x^20+x^3+1',
        163: 'x^163+x^7+x^6+x^3+1',
        233: 'x^233+x^74+1',
        283: 'x^283+x^12+x^7+x^5+1',
        409: 'x^409+x^87+1',
        571: 'x^571+x^10+x^5 +x^2+1'
    }

    def __init__(self, bits: int):
        self._bits = bits

    def __str__(self):
        return bin(self._bits)

    def __index__(self):
        return self._bits

    @staticmethod
    def get_irreducible(n: int) -> 'Polynomial':
        if n not in Polynomial._irreducible:
            raise Exception("Couldn't find a polynomial")

        return Polynomial.parse_polynomial(Polynomial._irreducible[n])

    @staticmethod
    def parse_polynomial(string: str) -> 'Polynomial':
        result = 0
        monomials = re.findall(r'([\w\d])(?:\^(\d*))?', string)

        for factor, exponent in monomials:
            exponent = 0 if factor == '1' else exponent or 1
            result += (1 << int(exponent))

        return Polynomial(result)

    def clone(self):
        return Polynomial(self._bits)

    def __eq__(self, other: 'Polynomial') -> bool:
        return self._bits == other._bits

    def __add__(self, other: 'Polynomial') -> 'Polynomial':
        return Polynomial(self._bits ^ other._bits)

    def __len__(self):
        return self._bits.bit_length()

    def __mul__(self, other: 'Polynomial') -> 'Polynomial':
        result = Polynomial(0)
        addend = self.clone()
        otherbits = other._bits
        while otherbits:
            shift = otherbits & 1
            if shift:
                result += addend
            addend <<=1
            otherbits >>= 1

        return result

    def __mod__(self, other: 'Polynomial') -> 'Polynomial':
        first = self.clone()
        while len(first) >= len(other):
            len_dif = len(first) - len(other)
            first += Polynomial(other._bits << len_dif)

        return first

    def __lshift__(self, other: int) -> 'Polynomial':
        return Polynomial(self._bits << other)

    def __rshift__(self, other: int) -> 'Polynomial':
        return Polynomial(self._bits >> other)

    def _polydiv(self, divisor):
        quotient = Polynomial(0)
        remainder = self.clone()
        while len(remainder) >= len(divisor):
            product = Polynomial(1 << (len(remainder) - len(divisor)))
            quotient += product
            remainder += product * divisor

        return quotient

    # def invert(self, p: 'Polynomial') -> 'Polynomial':
    #     p1, p2 = self.clone(), p.clone()
    #     x1, x2 = Polynomial(1), Polynomial(0)
    #
    #     while p2 != Polynomial(1):
    #         p1_len = len(p1)
    #         p2_len = len(p2)
    #
    #         if p1_len == p2_len:
    #             p1, p2 = p2, p1 + p2
    #             x1, x2 = x2, x1 + x2
    #         elif p1_len < p2_len:
    #             p1, p2 = p2, (p1 << (p2_len - p1_len)) + p2
    #             x1, x2 = x2, (x1 << (p2_len - p1_len)) + x2
    #         else:
    #             p1, p2 = p2, (p2 << (p1_len - p2_len)) + p1
    #             x1, x2 = x2, (x2 << (p1_len - p2_len)) + x1
    #
    #     return x2 % p

    def invert(self, p):
        old_t, t = Polynomial(0), Polynomial(1)
        old_r, r = p, self.clone()
        while r != Polynomial(0):
            quotient = old_r._polydiv(r)
            old_r, r = r, old_r + quotient * r
            old_t, t = t, old_t + quotient * t

        assert old_r._bits == 1  # old_r is the gcd
        return old_t % p
