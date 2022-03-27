#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
r, c, n, k = map(int, input().split())
ones = []
for i in range(n):
    ones.append([int(x) - 1 for x in input().split()])
def count_ones(start, end):
    ret = 0
    for one in ones:
        if one[0] >= start[0] and one[1] >= start[1] and one[0] <= end[0] and one[1] <= end[1]:
            ret += 1
    return ret >= k
counter = 0
for i in range(r):
    for j in range(c):
        for ei in range(i, r):
            for ej in range(j, c):
                if count_ones((i, j), (ei, ej)):
                    counter += 1
print(counter)