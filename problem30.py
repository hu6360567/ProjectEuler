#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Digit fifth powers
Problem 30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4


The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''


powers = []
for x in range(10):
    powers.append(x**5)


def getLongest():
    i = 1
    while 10**i <= i * 9**5:
        i += 1
    return i


def isOK(num):
    result = 0
    tmp = num
    while tmp != 0:
        result += powers[tmp % 10]
        tmp /= 10
    return num == result


def main():
    sum = 0
    for num in xrange(2, 10**getLongest()):
        if isOK(num):
            sum += num
            print num
    print sum

if __name__ == '__main__':
    main()
