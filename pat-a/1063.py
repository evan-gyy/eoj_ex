#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
l = []
for _ in range(int(input())):
    l.append(list(map(int, input().split()[1:])))
for _ in range(int(input())):
    a, b = map(lambda x: int(x) - 1, input().split())
    sim = len(set(l[a]) & set(l[b])) / len(set(l[a]) | set(l[b])) * 100
    print('{0:.1f}%'.format(sim))