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
        return self._bits

    @staticmethod
    def get_irreducible(n: int) -> 'Polynomial':
        if n not in Polynomial._irreducible:
            raise Exception("Couldn't find a polynomial")

        return Polynomial.parse_polynomial(Polynomial._irreducible[n])

    @staticmethod
    def parse_polynomial(string: str) -> 'Polynomial':
        result = 0
        monomials = re.findall(r'([\w\d])(?:\^(\d))?', string)

        for factor, exponent in monomials:
            exponent = 0 if factor == '1' else exponent or 1
            result += (1 << exponent)

        return Polynomial(result)
