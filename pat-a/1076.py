#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
from collections import deque

n, limit = map(int, input().split())
trigger = [[] for _ in range(n)]
for i in range(n):
    _, *f = map(int, input().split())
    for j in f:
        trigger[j - 1].append(i)

_, *query = map(lambda x: int(x) - 1, input().split())
for q in query:
    dq = deque([[q, 0]])
    visit = [False for _ in range(n)]
    visit[q] = True
    count = 0
    while dq:
        curr, l = dq.popleft()
        if l == 3:
            continue
        for next in trigger[curr]:
            if not visit[next]:
                visit[next] = True
                dq.append([next, l + 1])
                count += 1
    print(visit.count(True) - 1)