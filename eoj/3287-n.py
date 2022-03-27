#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n, k = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
l.sort(key=lambda x: x[0])
t = 0
while l:
    curr = min(l, key=lambda x: abs(x[0]))
    idx = l.index(curr)
    tk = k
    pos = 0
    while tk:
        t += abs(curr[0] - pos)
        pos = curr[0]
        if curr[1] > tk:
            l[idx][1] -= tk
            tk = 0
        elif curr[1] <= tk:
            tk -= curr[1]
            if idx == 0 and len(l) > 1:
                next = l[1]
            elif idx == len(l) - 1 and len(l) > 1:
                next = l[idx-1]
            elif idx > 0 and idx < len(l) - 1:
                next = min(l[idx-1], l[idx+1], key=lambda x: abs(x[0]-pos))
            else:
                l.remove(curr)
                break
            l.remove(curr)
            curr = next
            idx = l.index(curr)
print(t)