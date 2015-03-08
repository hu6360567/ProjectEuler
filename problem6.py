#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''


def sum_of_squares(n):
    result = 0
    for x in xrange(1, n + 1):
        result += x**2
    return result


def squares_of_sum(n):
    sum = 0
    for x in xrange(1, 1 + n):
        sum += x
    return sum**2


def main():
    L = []
    for x in xrange(1, 101):
        L.append(squares_of_sum(x) - sum_of_squares(x))
    print max(L)

if __name__ == '__main__':
    main()
