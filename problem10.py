#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import math


def isPrime(n):
    if n == 2:
        return True
    upper = int(math.sqrt(n)) + 1
    for x in xrange(2, upper):
        if n % x == 0:
            return False
    return True


def main():
    L = [2]
    while L[-1] < 2000000:
        i = L[-1] + 1
        while True:
            if isPrime(i):
                break
            else:
                i += 1
        L.append(i)
    L.pop()
    print sum(L)


if __name__ == '__main__':
    main()
