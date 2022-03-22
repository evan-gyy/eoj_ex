#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
m, n, k = map(int, input().split())
p, q = 1, 1
for i in range(k):
    if p > m:
        p = 1
    if q > n:
        q = 1
    print(p, q)
    p += 1
    q += 1
