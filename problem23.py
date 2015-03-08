#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Non-abundant sums
Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

A number whose proper divisors are less than the number is called deficient and a number whose proper divisors exceed the number is called abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
import math


def getDivSum(n):
    s = 0
    for i in range(1, n / 2 + 1):
        if n % i == 0:
            s += i
    return s


def getAbundant():
    L = []
    for x in xrange(1, 28124):
        if x < getDivSum(x):
            L.append(x)
    return L


def main():
    abundantList = getAbundant()
    L = [x for x in xrange(1, 28124)]
    l = []
    for i in xrange(len(abundantList)):
        for j in xrange(i, len(abundantList)):
            result = abundantList[i] + abundantList[j]
            l.append(result)
    print sum(set(L) - set(l))


if __name__ == '__main__':
    main()
