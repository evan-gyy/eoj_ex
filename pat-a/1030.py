#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
from collections import deque
n, m, s, d = map(int, input().split())
dic = {i: [] for i in range(n)}
for i in range(m):
    c1, c2, dist, cost = map(int, input().split())
    dic[c1].append([c2, dist, cost])
min_dist = 0
min_cost = 0
min_path = []

def bfs(c):
    global min_dist, min_cost, min_path, d
    if c == d:
        min_path = [c, d]
        return
    que = deque([[c, 0, 0, [c]]])
    while que:
        h = que.popleft()
        if h[0] == d:
            dist = h[1]
            cost = h[2]
            path = h[3]
            if (min_dist == 0 and min_cost == 0) or (min_dist > dist) or (min_dist == dist and min_cost > cost):
                min_dist = dist
                min_cost = cost
                min_path = path
            continue
        for next in dic[h[0]]:
            if next[0] not in h[-1]:
                que.append([next[0], h[1] + next[1], h[2] + next[2], h[-1] + [next[0]]])

bfs(s)
print(' '.join(str(i) for i in min_path), min_dist, min_cost)