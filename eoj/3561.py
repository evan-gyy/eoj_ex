#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
input()
ls = [int(i) for i in input().split()]
dist = [ls[i] - ls[i-1] for i in range(1, len(ls))]
k = max(dist, key=lambda x: dist.count(x))
for i in range(1, len(ls)):
    d = dist[i - 1]
    if d != k:
        ls[i] = ls[i - 1] + k
print(ls)