#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
tl = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C']
def convert(x, b=13):
    res = []
    while x:
        res.insert(0, tl[x % b])
        x = x // b
    res = ''.join([str(i) for i in res])
    if len(res) == 1:
        res = '0' + res
    elif len(res) == 0:
        res = '00'
    return res
a, b, c = map(int, input().split())
r = '#'
for i in [a, b, c]:
    r += convert(i)
print(r)

