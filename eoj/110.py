#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n, k = map(int, input().split())
l1 = [i for i in range(0, (n-1)*k + 1, k)]
l2 = list(map(int, input().split()))
flat = [l2[i] - l1[i] for i in range(n)]
flat.sort()
if n % 2 != 0:
    target = flat[n // 2]
else:
    target = (flat[n // 2] + flat[n // 2 + 1]) // 2
if target < 0:
    target = 0
d = 0
for i in flat:
    d += abs(i - target)
print(d)