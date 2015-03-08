#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math


def find_prime_factors(n):
    L = []
    upper = int(math.sqrt(n)) + 1
    for i in range(2, upper):
        while n % i == 0:
            L.append(i)
            n = n / i
    return L


def main():
    prime_factors = find_prime_factors(600851475143)
    print prime_factors[-1]

if __name__ == '__main__':
    main()
