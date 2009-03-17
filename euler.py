#!/usr/bin/env python

# Project Euler in Python (2.5)
# John Evans <john@jpevans.com>

import sys

def euler1():
    """Euler #1
    Answer: 233168

    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.

    """

    return sum(i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0)


def euler2():
    """Euler #2
    Answer: 4613732

    Each new term in the Fibonacci sequence is generated by adding the previous
    two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    Find the sum of all the even-valued terms in the sequence which do not
    exceed four million.

    """

    n, a, b = 2, 1, 2
    while True:
        c = a + b
        if c > 4000000:
            break
        if c % 2 == 0:
            n = n + c
        a, b = b, c
    return n



EULERS = [
    euler1,
    euler2
]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for n in sys.argv[1:]:
            n = int(n)
            print "%d: %d" % (n, eval("euler%d()" % n))
    else:
        for index, euler in enumerate(EULERS):
            print "%d: %d" % (index+1, euler())
