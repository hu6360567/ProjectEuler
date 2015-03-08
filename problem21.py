#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Amicable numbers
Problem 21

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
import math


def getDivSum(n):
    sum = 1
    upper = int(math.sqrt(n)) + 1
    for x in xrange(2, upper):
        if n % x == 0:
            # x is a divisor of n
            sum += n / x + x
            if n / x == x:
                sum -= x
    return sum


def main():
    divSum = dict()
    sum = 0
    for x in xrange(1, 10001):
        result = getDivSum(x)
        divSum[x] = result
        if (result in divSum) and (divSum[result] == x) and (x != result):
            sum += x + result
    print sum

if __name__ == '__main__':
    main()
