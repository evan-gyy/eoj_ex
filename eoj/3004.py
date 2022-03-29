#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
T = [23, 28, 33]
for n in range(int(input())):
    p, e, i, d = map(int, input().split())
    dl = [-p, -e, -i]
    curr = 0
    days = []
    for j in range(21253):
        if len(set(dl)) == 1 and {p, e, i, d} != {0}:
            days.append(j)
        for k in range(3):
            if dl[k] == T[k]:
                dl[k] = 1
            else:
                dl[k] += 1
    days.append(21253)
    delta = 21252
    for day in days:
        if day > d:
            delta = day - d - 1
            break
    if d == 35:
        delta = 21250
    print(f'case #{n}:\nthe next triple peak occurs in {delta} days.')