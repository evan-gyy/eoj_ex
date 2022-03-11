#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
s, h = map(int, input().split())
tap = {}
for i in range(int(input())):
    hi, vi = map(int, input().split())
    if hi != h:
        tap[hi] = vi
tap = dict(sorted(tap.items(), key=lambda x: x[0], reverse=True))
hl = [i[0] for i in tap.items()]
vl = [i[1] for i in tap.items()]
t = 0
for i in range(len(hl)):
    t += s * (h - hl[i]) / sum(vl[i:])
    h = hl[i]
print('{0:.10f}'.format(t))