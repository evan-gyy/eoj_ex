#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
from collections import deque
for _ in range(int(input())):
    input()
    weights = list(map(int, input().split()))
    input()
    queries = list(map(int, input().split()))
    res = set(weights)
    dq = deque([])
    visited = []
    for i in weights:
        visit = {i}
        visited.append(visit)
        remain = set(weights) - visit
        dq.append([visit, remain, visit])
    while dq:
        curr = dq.popleft()
        if not curr[1]:
            continue
        for next in curr[1]:
            now = curr[0] | {next}
            if now not in visited:
                visited.append(now)
                temp = set()
                for i in curr[2]:
                    temp.add(abs(i + next))
                    temp.add(abs(i - next))
                res = res.union(temp)
                dq.append([now, curr[1] - {next}, temp])
    ans = ''
    for q in queries:
        ans += '1' if q in res else '0'
    print(ans)