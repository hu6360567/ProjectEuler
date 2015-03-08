#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Lexicographic permutations
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''


def getTotal(prefix):
    suffix = 10 - prefix
    result = 1
    for x in xrange(1, suffix + 1):
        result *= x
    return result


def main():
    sum = 0
    result = ''
    number = [x for x in range(10)]
    for prefix in xrange(1, 11):
        for x in number:
            if sum + getTotal(prefix) >= 1000000:
                result += str(x)
                number.remove(x)
                break
            else:
                sum += getTotal(prefix)
    print result

if __name__ == '__main__':
    main()
