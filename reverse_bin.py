#!/usr/bin/python
import argparse


def reverseBin(number):
    """
    This is a program reverse a number as a binary e.g.:
        13 = 1101 -> 1011 = 11
        101 = 1100100 -> 0010011 = 19

        >>> print reverseBin(13)
        11
        >>> print reverseBin(100)
        19

    """
    return int(bin(number)[:1:-1], 2)


def main():
    parser = argparse.ArgumentParser(description=u'The program snail crawling\
            2D matrix')
    parser.add_argument('number', metavar='N', type=int,
                        help='an integer to binary reverse')
    args = parser.parse_args()
    reverseBin(args.number)

if __name__ == '__main__':
    main()
