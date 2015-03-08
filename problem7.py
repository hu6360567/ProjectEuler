#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
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
    while len(L) != 10001:
        i = L[-1] + 1
        while True:
            if isPrime(i):
                break
            else:
                i += 1
        L.append(i)
    print L[-1]

if __name__ == '__main__':
    main()
