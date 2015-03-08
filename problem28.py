#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Number spiral diagonals
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiralformed in the same way?
'''


def getCircleSum(n):
    if n == 1:
        return 1
    else:
        # 4 numbers in a cricle, each number increases 2*(n-1)
        # the last number in a circle is (2*n-1)^2
        # then the sum of a circle is 4*last_number-6*diff
        return 4 * ((2 * n - 1)**2) - 12 * (n-1)


def main():
    circles = (1001 + 1) / 2
    sum = 0
    for c in xrange(1, circles+1):
        tmp = getCircleSum(c)
        sum += tmp
    print sum

if __name__ == '__main__':
    main()
