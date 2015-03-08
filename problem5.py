#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


def devided(n):
    # print 'devided %d' % n
    for x in xrange(2, 21):
        if not n % x == 0:
            return False
    return True


def find_multiple():
    i = 2520
    while not devided(i):
        i += 10
    return i


def main():
    print find_multiple()

if __name__ == '__main__':
    main()
