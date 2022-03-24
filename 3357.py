#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
d, k = map(int, input().split())
al = []
for i in range(k + 1):
    if i == 0:
        al.append(0)
    elif i == 1:
        al.append(1)
    else:
        if i > 100:
            break
        al.append(1 + d * (i - 1))
x = float(al.pop())
while al:
    x = al.pop() + 1 / x
print('{:.16f}'.format(x))