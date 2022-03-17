#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n, k = map(int, input().split())
l = []
for _ in range(n):
    l.append(input().split())
l.sort(key=lambda x: (-int(x[-1]), int(x[1]), x[0]))
for i in range(k):
    m, amin, amax = map(int, input().split())
    print(f"Case #{i + 1}:")
    res = []
    p = 0
    flag = 0
    while m > 0 and p < len(l):
        if int(l[p][1]) >= amin and int(l[p][1]) <= amax:
            print(' '.join(l[p]))
            flag = 1
            m -= 1
        p += 1
    if not flag:
        print('None')