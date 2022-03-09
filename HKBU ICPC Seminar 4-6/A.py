#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n = int(input())
for i in range(n):
    m = int(input())
    rl = []
    for j in range(m):
        rl.append(int(input()))
    rem = set()
    count = 0
    while len(rem) != m:
        rem = set()
        count += 1
        for k in rl:
            rem.add(k % count)
    print(count)