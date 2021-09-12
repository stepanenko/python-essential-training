
def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print(a)  # will be in a different order each time
    print(b)  # will be in a different order each time
    print_set(a)  # will be in a different order each time
    print_set(b)  # will be in a different order each time


def print_set(o):
    print('{', end='')
    for x in o:
        print(x, end='')
    print('}')


if __name__ == '__main__':
    main()
