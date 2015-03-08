#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Power digit sum
Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''
import math


def getSum(n):
    number_str = str('%d' % n)
    sum = 0
    for ch in number_str:
        sum += int(ch)
    return sum


def main():
    n = math.pow(2, 1000)
    print getSum(n)

if __name__ == '__main__':
    main()
