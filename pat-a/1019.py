#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n, b = map(int, input().split())
def trans(n, b):
    res = []
    while n:
        res.insert(0, str(n % b))
        n = n // b
    return res
def judge(l):
    res = l == [l[i] for i in range(len(l)-1, -1, -1)]
    return 'Yes' if res else 'No'
r = trans(n, b)
print(judge(r))
print(' '.join(r))
