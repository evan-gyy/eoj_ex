#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n = int(input())
for i in range(n):
    s = input()
    sl = []
    for j in s:
        if not sl:
            sl.append(j)
        else:
            if j != sl[-1]:
                sl.pop()
            else:
                sl.append(j)
    print(len(sl))