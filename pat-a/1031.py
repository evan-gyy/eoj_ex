#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
def calc(n):
    n += 2
    if n % 3 == 0:
        r = n // 3
        return r, r
    else:
        r = n // 3
        return r, r + n % 3
s = input()
h, w = calc(len(s))
l = []
for i in range(h-1):
    l.append(s[i] + ' '*(w-2) + s[len(s)-1-i])
l.append(s[h-1: h-1+w])
for i in l:
    print(i)
