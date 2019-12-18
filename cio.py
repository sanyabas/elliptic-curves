import re

from os import linesep
from polynomial import Polynomial
from point import Point


def read_input(filename):
    with open(filename) as f:
        curve_type = next_line(f)

        if curve_type == 'gf':
            return read_n_curve(f)
        else:
            return read_z_curve(f)


def write_results(tasks):
    result = []
    with open('output.txt', 'w') as f:
        for task in tasks:
            if task['type'] == 'A':
                result.append(format_add(task['first'], task['second'], task['result'], task['base']))
            else:
                result.append(format_mul(task['first'], task['second'], task['result'], task['base']))
        f.writelines(result)


def format_add(first: 'Point', second: 'Point', result: 'Point', base: int) -> str:
    return f'{first.format(base)} + {second.format(base)} = {result.format(base)}{linesep}'


def format_mul(first: 'Point', second: int, result: 'Point', base: int) -> str:
    formatters = {
        2: bin,
        10: str,
        16: hex
    }
    formatter = formatters[base]

    return f'{first.format(base)} * {formatter(second)} = {result.format(base)}{linesep}'


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
    base = get_base(string)
    if base == 16:
        return int(string, 16)
    if base == 2:
        return int(string, 2)
    return int(string)


def get_base(string: str) -> int:
    if string.startswith('0x'):
        return 16
    if string.startswith('0b'):
        return 2
    return 10


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
        'second': second,
        'base': get_base(match[0])
    }


def parse_mul(task: str, constructor):
    [match] = re.findall(r'\((.*?),(.*?)\) ([\d\w]+)', task)
    [x1, y1, m] = map(parse_int, match)
    [x1, y1] = map(constructor, [x1, y1])

    return {
        'type': 'M',
        'first': Point((x1, y1)),
        'second': m,
        'base': get_base(match[0])
    }


def next_line(file):
    return file.readline().strip().lower()


def next_lines(file):
    return map(lambda s: s.strip().lower(), file.readlines())
