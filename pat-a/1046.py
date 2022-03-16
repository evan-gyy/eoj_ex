#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
dist = list(map(int, input().split()[1:]))
cycle = []
for i in range(len(dist)):
    left = dist[i - 1] if i > 0 else dist[-1]
    right = dist[i]
    cycle.append([left, right])
def find(a, b):
    pa, pb = a - 1, b - 1
    rd = 0
    while pa != pb:
        rd += cycle[pa][1]
        pa += 1
        if pa > len(cycle) - 1:
            pa = 0
    pa, pb = a - 1, b - 1
    ld = 0
    while pa != pb:
        ld += cycle[pa][0]
        pa -= 1
        if pa < 0:
            pa = len(cycle) - 1
    return min(rd, ld)
for i in range(int(input())):
    a, b = map(int, input().split())
    r = find(a, b)
    print(r)