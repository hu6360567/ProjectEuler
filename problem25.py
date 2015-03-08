#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
1000-digit Fibonacci number
Problem 25

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
'''


def isOK(number):
    dig = 1
    while number >= 10:
        number /= 10
        dig += 1
    if dig >= 1000:
        return True
    else:
        return False


def main():
    F = [1, 1]
    while not isOK(F[-1]):
        F.append(F[-1] + F[-2])
    print len(F)

if __name__ == '__main__':
    main()
