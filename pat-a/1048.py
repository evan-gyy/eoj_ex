#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n, m = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort()
left = 0
right = len(coins) - 1
res = 'No Solution'
while left < right:
    v1 = coins[left]
    v2 = coins[right]
    if v1 + v2 == m:
        res = f'{v1} {v2}'
        break
    elif v1 + v2 > m:
        right -= 1
    else:
        left += 1
print(res)