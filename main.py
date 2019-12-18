from sys import argv
from cio import read_input, write_results
from curve import CurveZp, CurveGF


curve_map = {
    'zp': CurveZp,
    'gf': CurveGF
}


def main():
    curve_type, args, tasks = read_input(argv[1] if len(argv) > 1 else 'input.txt')
    constructor = curve_map[curve_type]
    curve = constructor(**args)

    for task in tasks:
        if task['type'] == 'A':
            task['result'] = curve.add(task['first'], task['second'])
        else:
            task['result'] = curve.mul(task['first'], task['second'])
    print(tasks)
    write_results(tasks)


if __name__ == '__main__':
    main()
