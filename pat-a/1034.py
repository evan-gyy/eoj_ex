#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n, k = map(int, input().split())
l = []
for i in range(n):
    a, b, t = input().split()
    t = int(t)
    flag = 0
    for j in l:
        if a in j[0] or b in j[0]:
            flag = 1
            j[1] += t
            for m in [a, b]:
                if m in j[0]:
                    j[0][m] += t
                else:
                    j[0][m] = t
            break
    if flag == 0:
        new = {}
        new[a] = t
        new[b] = t
        l.append([new, t])
res = []
for i in l:
    size = len(i[0])
    if size <= 2 or i[1] <= k:
        continue
    head = max(i[0].items(), key=lambda x: x[1])[0]
    res.append([head, size])
print(len(res))
res.sort(key=lambda x: x[0])
for r in res:
    print(r[0], r[1])