#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Factorial digit sum
Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''


def main():
    product = 1
    sum = 0
    for x in xrange(1, 101):
        product *= x
    product_str = str(product)
    for n in product_str:
        sum += int(n)
    print sum

if __name__ == '__main__':
    main()