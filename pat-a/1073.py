#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
a, b = input().split('E')
zeros = 0
for i in range(len(a)-1, -1, -1):
    if a[i] == '0':
        zeros += 1
    else:
        break
res = float(a) * 10 ** int(b)
if res == int(res):
    res = int(res)
res = str(res)
if zeros and res[-1] != '0':
    res += '0' * zeros
print(res)