import re

from .polynomial import Polynomial


def read_input():
    args = {}
    with open('read') as f:
        type = next_line(f)

        if type == 'n':
            args = read_n_curve(f)
        else:
            args = read_z_curve(f)


def read_n_curve(file):
    args = dict()
    args['p'] = parse_polynomial(next_line(file))
    args['a'] = parse_int(next_line(file))
    args['b'] = parse_int(next_line(file))
    args['c'] = parse_int(next_line(file))
    args['tasks'] = read_tasks(file)

    return args


def read_z_curve(file):
    args = dict()
    args['p'] = parse_int(next_line(file))
    args['a'] = parse_int(next_line(file))
    args['b'] = parse_int(next_line(file))
    args['tasks'] = read_tasks(file)

    return args


def parse_polynomial(string: str):
    result = 0
    monomials = re.findall(r'([\w\d])(?:\^(\d))?', string)

    for factor, exponent in monomials:
        exponent = 0 if factor == '1' else exponent or 1
        result += (1 << exponent)

    return Polynomial(result)


def parse_int(string):
    if string.startswith('0x'):
        return int(string, 16)
    if string.startswith('0b'):
        return int(string, 2)
    return int(string)


def read_tasks(file):
    pass


def next_line(file):
    return file.readline().strip().lower()