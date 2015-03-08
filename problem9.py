#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.   Find the product abc.
'''


def isPythagorean(a, b, c):
    return (a**2 + b**2) == c**2


def main():
    abc=[(a,b,1000-a-b) for a in xrange(1,1001) for b in xrange(1,1001) if a+b>500 ]
    for item in abc:
        if isPythagorean(item[0], item[1], item[2]):
            break
    print item[0]*item[1]*item[2]

if __name__ == '__main__':
    main()
