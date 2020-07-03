import sys


def parse(file_name):
    voc = dict()
    with open(file_name) as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            print('skip zero line', i)
            continue

        ls = line.split(',')
        # print(ls)
        if len(ls) == 1:
            voc[ls[0]] = ''
        elif len(ls) == 2:
            voc[ls[0]] = ls[1].strip()
        else:
            raise Exception(file_name, 'error at line', i)
    return voc


if __name__ == '__main__':
    assert len(sys.argv) == 3
    source = parse(sys.argv[1])
    destination = parse(sys.argv[2])

    count = 0
    with open(sys.argv[2], 'a') as f:
        for k, v in source.items():
            if k in destination:
                print('skip existed word', k)
                continue
            string = k + ', ' + v if v else k
            print(string, file=f)
            count += 1

    print(count, 'items appended')
