#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Even Fibonacci numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''


def fibonacci_upper():
    L = [1, 2]
    while L[-1] < 4000000:
        L.append(L[-1] + L[-2])
    return L


def main():
    L = fibonacci_upper()
    sum = 0
    for i in range(len(L)):
        if L[i] % 2 == 0:
            sum += L[i]
    print sum

if __name__ == '__main__':
    main()
