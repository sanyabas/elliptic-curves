from cio import read_input
from curve import CurveZp, CurveGF


curve_map = {
    'zp': CurveZp,
    'gf': CurveGF
}


def main():
    curve_type, args, tasks = read_input()
    constructor = curve_map[curve_type]
    curve = constructor(**args)

    for task in tasks:
        if task['type'] == 'A':
            result = curve.add(task['first'], task['second'])
        else:
            result = curve.mul(task['first'], task['second'])
        print(result)


if __name__ == '__main__':
    main()
