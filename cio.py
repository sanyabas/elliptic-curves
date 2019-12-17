import re

from polynomial import Polynomial
from point import Point


def read_input():
    with open('input.txt') as f:
        curve_type = next_line(f)

        if curve_type == 'gf':
            return read_n_curve(f)
        else:
            return read_z_curve(f)


def read_n_curve(file):
    args = dict()

    n = parse_int(next_line(file))
    args['p'] = Polynomial.get_irreducible(n)
    args['a'] = Polynomial(parse_int(next_line(file)))
    args['b'] = Polynomial(parse_int(next_line(file)))
    args['c'] = Polynomial(parse_int(next_line(file)))
    tasks = read_tasks(file, Polynomial)

    return 'gf', args, tasks


def read_z_curve(file):
    args = dict()
    args['p'] = parse_int(next_line(file))
    args['a'] = parse_int(next_line(file))
    args['b'] = parse_int(next_line(file))
    tasks = read_tasks(file, int)

    return 'zp', args, tasks


def parse_int(string):
    if string.startswith('0x'):
        return int(string, 16)
    if string.startswith('0b'):
        return int(string, 2)
    return int(string)


def read_tasks(file, constructor):
    tasks = []
    lines = next_lines(file)
    for line in lines:
        if line.startswith('a'):
            tasks.append(parse_add(line, constructor))
        else:
            tasks.append(parse_mul(line, constructor))

    return tasks


def parse_add(task: str, constructor):
    [match] = re.findall(r'\((.*?),(.*?)\) \((.*?),(.*?)\)', task)
    [x1, y1, x2, y2] = map(constructor, map(parse_int, match))

    first = Point((x1, y1))
    second = Point((x2, y2))

    return {
        'type': 'A',
        'first': first,
        'second': second
    }


def parse_mul(task: str, constructor):
    [match] = re.findall(r'\((.*?),(.*?)\) \d+', task)
    [x1, y1, m] = map(constructor, map(parse_int, match))

    return {
        'type': 'M',
        'first': Point((x1, y1)),
        'second': m
    }


def next_line(file):
    return file.readline().strip().lower()


def next_lines(file):
    return map(lambda s: s.strip().lower(), file.readlines())
