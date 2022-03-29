#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n, m = map(int, input().split())
ai = [int(i) for i in input().split()]
dic = {}
for i in range(1, n+1):
    dic[i] = 0
for i in range(m):
    p, q = map(int, input().split())
    dic[p] = max(dic[p], q)
price = 0
for i in range(1, n+1):
    price += ai[i-1] * dic[i]
print(price)