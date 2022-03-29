#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
from collections import deque
while True:
    n = int(input())
    if n == -1:
        break
    count = 0
    dq = deque([['0', 1], ['1', 1]])
    while dq:
        curr = dq.popleft()
        if curr[1] == n and '101' not in curr[0]:
            count += 1
            continue
        if '101' not in curr[0]:
            dq.append([curr[0] + '0', curr[1] + 1])
            dq.append([curr[0] + '1', curr[1] + 1])
    print(count)