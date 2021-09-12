
def main():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']  # list
    print_list(game)


def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
    print()


if __name__ == '__main__':
    main()
