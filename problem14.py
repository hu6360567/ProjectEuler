#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Longest Collatz sequence
Problem 14

The following iterative sequence is defined for the set of positive integers:
        n ---> n/2 (n is even)
        n ---> 3n+1 (n is ood)

Using the rule above and starting with 13, we generate the following sequence:
        13 -> 40 -> 20 -> 10 -> 5 ->16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
'''


def getChainLength(n, dictionary):
    if n in dictionary:
        return dictionary.get(n)
    elif n % 2 == 0:
        # n is even
        next = n / 2
        dictionary[next] = getChainLength(next, dictionary)
        return dictionary[next] + 1
    else:
        # n is odd
        next = 3 * n + 1
        dictionary[next] = getChainLength(next, dictionary)
        return dictionary[next] + 1


def main():
    chain_length = {1: 1}
    max_result = (1, 1)
    for index in xrange(1, 1000001):
        result = (index, getChainLength(index, chain_length))
        if result[1] > max_result[1]:
            max_result = result
    print max_result

if __name__ == '__main__':
    main()
