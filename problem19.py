#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Counting Sundays
Problem 19

You are given the following information, but you may prefer to do some research for yourself.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''


def isLeapYear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return (year % 4 == 0)


def getNumber(base_day, year):
    sum = 1 if base_day % 7 == 0 else 0  # January
    normal_year = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31,
                   6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30}
    leap_year = dict(normal_year)
    leap_year[2] = 29
    mydict = (leap_year if isLeapYear(year) else normal_year)
    for month in xrange(1, 12):
        base_day += mydict[month]
        sum += 1 if base_day % 7 == 0 else 0
    return sum


def main():
    base_day = 365 % 7 + 1  # the weekday of 1901.1.1
    sum = 0
    for year in xrange(1901, 2001):
        sum += getNumber(base_day, year)
        base_day = (base_day + (366 if isLeapYear(year) else 365)) % 7
    print sum


if __name__ == '__main__':
    main()
