#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
def rank(l, a):
    return sorted(l, reverse=True).index(a) + 1
nl, cl, ml, el, al = [], [], [], [], []
n, m = map(int, input().split())
for i in range(n):
    inp = list(map(int, input().split()))
    nl.append(inp[0])
    cl.append(inp[1])
    ml.append(inp[2])
    el.append(inp[3])
    al.append((inp[0]+inp[1]+inp[2])/3)
for i in range(m):
    name = int(input())
    if name not in nl:
        print('N/A')
        continue
    j = nl.index(name)
    rl = [rank(el, el[j]), rank(ml, ml[j]), rank(cl, cl[j]), rank(al, al[j])]
    max_rank = n
    max_sbj = ''
    for r in range(len(rl)):
        if rl[r] <= max_rank:
            max_rank = rl[r]
            max_sbj = ['E', 'M', 'C', 'A'][r]
    print(max_rank, max_sbj)

