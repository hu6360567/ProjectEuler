#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
'''


def getDict():
    d = {}
    d[1] = 3  # one
    d[2] = 3  # two
    d[3] = 5  # three
    d[4] = 4  # four
    d[5] = 4  # five
    d[6] = 3  # six
    d[7] = 5  # seven
    d[8] = 5  # eight
    d[9] = 4  # nine
    d[10] = 3  # ten
    d[11] = 6  # eleven
    d[12] = 6  # twelve
    d[13] = 8  # thirteen
    d[14] = 8  # fourteen
    d[15] = 7  # fifteen
    d[16] = 7  # sixteen
    d[17] = 9  # seventeen
    d[18] = 8  # eighteen
    d[19] = 8  # nineteen
    d[20] = 6  # twenty
    d[30] = 6  # thirty
    d[40] = 5  # forty
    d[50] = 5  # fifty
    d[60] = 5  # sixty
    d[70] = 7  # seventy
    d[80] = 6  # eighty
    d[90] = 6  # ninety
    d[00] = 7  # hundred
    d[1000] = 11  # one thousand
    d['and'] = 3
    return d


def calcuateLetter(n, d):
    n_str = str(n)
    length = 0
    if n in d:
        return d[n]
    elif len(n_str) == 3:
        # over 100
        length += d[int(n_str[0])] + d[00]
        if n_str[1:] == '00':
            pass
        else:
            length += 3 + d[int(n_str[1:])]
    elif len(n_str) == 2:
        # from 21 to 99
        length += d[int(n_str[0]) * 10] + d[int(n_str[1])]
    d[n] = length
    return d[n]


def main():
    # get Base Dict
    base_dict = getDict()
    sum=0
    for index in range(1, 1001):
        sum+=calcuateLetter(index, base_dict)
    print sum

if __name__ == '__main__':
    main()
