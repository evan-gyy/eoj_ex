#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
from queue import PriorityQueue as PQ
q, n = map(int, input().split())
dic = {}
for i in range(n):
    idx, m = input().split()
    if m == '0':
        continue
    names = input().split()
    for name in names:
        if name in dic:
            dic[name].put((int(idx), idx))
        else:
            dic[name] = PQ()
            dic[name].put((int(idx), idx))
query = input().split()
for i in query:
    if i in dic:
        size = dic[i].qsize()
        r = ' '.join([dic[i].get()[1] for _ in range(size)])
        print(i, size, r)
    else:
        print(i, 0)