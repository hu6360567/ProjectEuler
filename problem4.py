#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


def isPalindromic(n):
    n_str = str(n)
    for i in range(len(n_str) / 2):
        if not n_str[i] == n_str[-i-1]:
            return False
    return True


def main():
    list = [(x, y) for x in range(100, 999) for y in range(100, 999)]
    L = []
    for x, y in iter(list):
        if isPalindromic(x * y):
            L.append(x * y)
    print max(L)

if __name__ == '__main__':
    main()
