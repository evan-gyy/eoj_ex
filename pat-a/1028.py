#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n, m = map(int, input().split())
l = []
for i in range(n):
    id, name, score = input().split()
    l.append([id, name, score])
if m == 1:
    l.sort(key=lambda x: int(x[0]))
elif m == 2:
    l.sort(key=lambda x: (x[1], int(x[0])))
else:
    l.sort(key=lambda x: (int(x[2]), int(x[0])))
for i in l:
    print(' '.join(i))