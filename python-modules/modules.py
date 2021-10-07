
import sys


def main():
    v = sys.version_info
    print(v)
    # sys.version_info(major=3, minor=9, micro=7, releaselevel='final', serial=0)
    print(*v)
    # 3 9 7 final 0
    print('Python version {}.{}.{}'.format(*v))
    # Python version 3.9.7


if __name__ == '__main__':
    main()
