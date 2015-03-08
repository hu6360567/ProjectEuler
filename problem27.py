#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Quadratic primes
Problem 27

Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n² - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''
import math

primeSet = set()


def isPrime(n):
    if n <= 0:
        return False
    if n in primeSet:
        return True
    if n == 2:
        primeSet.add(n)
        return True
    upper = int(math.sqrt(n))
    for x in xrange(2, upper):
        if n % x == 0:
            return False
    primeSet.add(n)
    return True


def getNumber(a, b):
    # n^2+an+b
    number = 0
    while True:
        tmp = number**2 + a * number + b
        if not isPrime(tmp):
            break
        else:
            number += 1
    return number


def main():
    for x in xrange(2, 1001):
        isPrime(x)
    b_list = list(primeSet)
    max = 0
    result = 0
    for a in xrange(-1000, 1001):
        for b in b_list:
            tmp = getNumber(a, b)
            if tmp > max:
                result = a * b
                max = tmp
    print result

if __name__ == '__main__':
    main()
