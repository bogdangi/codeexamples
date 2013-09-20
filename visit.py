#!/usr/bin/python
import argparse


def snailCrawling2D(matrix):
    """
    This is a programm which has to do snail crawling for 2D matrix

    0,0 0,1 0,2
    1,0 1,1 1,2
    2,0 2,1 2,2

        >>> for i in snailCrawling2D('3x3'): print '%d,%d' %i
        0,0
        0,1
        0,2
        1,2
        2,2
        2,1
        2,0
        1,0
        1,1

    0,0 0,1 0,2
    1,0 1,1 1,2

        >>> for i in snailCrawling2D('3x2'): print '%d,%d' %i
        0,0
        0,1
        0,2
        1,2
        1,1
        1,0

    0,0 0,1
    1,0 1,1
    2,0 2,1

        >>> for i in snailCrawling2D('2x3'): print '%d,%d' %i
        0,0
        0,1
        1,1
        2,1
        2,0
        1,0

    0,0 0,1 0,2

        >>> for i in snailCrawling2D('3x1'): print '%d,%d' %i
        0,0
        0,1
        0,2

    0,0
    1,0
    2,0

        >>> for i in snailCrawling2D('1x3'): print '%d,%d' %i
        0,0
        1,0
        2,0

    0,0 0,1
    1,0 1,1

        >>> for i in snailCrawling2D('2x2'): print '%d,%d' %i
        0,0
        0,1
        1,1
        1,0

    0,0 0,1

        >>> for i in snailCrawling2D('2x1'): print '%d,%d' %i
        0,0
        0,1

    0,0
    1,0

        >>> for i in snailCrawling2D('1x2'): print '%d,%d' %i
        0,0
        1,0

    0,0

        >>> for i in snailCrawling2D('1x1'): print '%d,%d' %i
        0,0

    """
    w, h = [int(i) for i in matrix.split('x')]
    i, j = 0, 0
    while w >= 1 and h >= 1:
        for i in xrange(i, i+w):
            yield (j, i)
        if h >= 1:
            if h <= 1:
                break
            h -= 1
            j += 1
        for j in xrange(j, j+h):
            yield (j, i)
        if w >= 1:
            if w <= 1:
                break
            w -= 1
            i -= 1
        for i in xrange(i, i-w, -1):
            yield (j, i)
        if h >= 1:
            h -= 1
            j -= 1
        for j in xrange(j, j-h, -1):
            yield (j, i)
        if w >= 1:
            w -= 1
            i += 1


def main():
    parser = argparse.ArgumentParser(description=u'The program snail crawling\
            2D matrix')
    parser.add_argument('matrix', metavar='A', type=str,
                        help='an string which has two integers separated by \
                                "x" e.g. "3x3"')
    args = parser.parse_args()
    for i in snailCrawling2D(args.matrix):
        print '%d,%d' % i

if __name__ == '__main__':
    main()
