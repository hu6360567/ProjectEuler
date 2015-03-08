#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Lattice paths
Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''
from collections import namedtuple

Location = namedtuple("Location", ['x', 'y'])


def getGridPath(location, path_dict):
    if location in path_dict:
        return path_dict[location]
    else:
        x, y = location
        right_location = Location(x, y + 1)
        down_location = Location(x + 1, y)
        if x == 20:
            # only have right location
            path_dict[location] = getGridPath(right_location, path_dict)
        elif y == 20:
            # only have down location
            path_dict[location] = getGridPath(down_location, path_dict)
        else:
            path_dict[location] = getGridPath(
                right_location, path_dict) + getGridPath(down_location, path_dict)
        return path_dict[location]


def main():
    final_location = Location(x=20, y=20)
    path_dict = {final_location: 1}
    print getGridPath(Location(x=0, y=0), path_dict)

if __name__ == '__main__':
    main()
