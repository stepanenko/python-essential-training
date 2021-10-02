
def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    # initialize parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator
    i = start
    while i <= stop:
        yield i
        i += step


def main():
    for i in inclusive_range(20):
        print(i, end=' ', flush=True)
    print()

    for i in inclusive_range(3, 15):
        print(i, end=' ', flush=True)
    print()

    for i in inclusive_range(1, 25, 3):
        print(i, end=' ', flush=True)
    print()

    # the following throws TypeError: expected at most 3 arguments, got 4
    # for i in inclusive_range(1, 25, 3, 5):
    #     print(i, end=' ', flush=True)
    # print()


if __name__ == '__main__':
    main()
