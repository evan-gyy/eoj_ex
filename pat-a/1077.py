#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
s = ''
l = []
for i in range(int(input())):
    l.append(input())
m = min(l, key=lambda x: len(x))
flag = 1
for i in range(len(m)):
    p = -(i + 1)
    curr = l[0][p]
    for j in l[1:]:
        if j[p] != curr:
            flag = 0
    if flag == 0:
        break
    else:
        s = curr + s
print(s if s else 'nai')