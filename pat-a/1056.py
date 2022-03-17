#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
np, ng = map(int, input().split())
weight = list(map(int, input().split()))
order = list(map(int, input().split()))
rank = {}
next = weight[:]
turn = 0
while True:
    if len(next) == 1:
        rank[1] = next
        break
    tl = []
    temp = []
    lose = []
    count = 1
    for i in range(len(next)):
        if turn == 0:
            tl.append(next[order[i]])
        else:
            tl.append(next[i])
        if count == ng or i == len(next) - 1:
            maxw = max(tl)
            temp.append(maxw)
            tl.remove(maxw)
            lose += tl
            tl = []
            count = 1
        else:
            count += 1
    rank[len(temp) + 1] = lose
    next = temp
    turn += 1
res = [0 for _ in range(np)]
for k, v in rank.items():
    for i in v:
        res[weight.index(i)] = k
print(' '.join(str(i) for i in res))

