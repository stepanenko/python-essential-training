
def main():
    # Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step.
    seq = range(11)
    print_list(seq)  # 0 1 2 3 4 5 6 7 8 9 10


def print_list(o):
    for x in o:
        print(x, end=' ')
    print()


if __name__ == '__main__':
    main()
