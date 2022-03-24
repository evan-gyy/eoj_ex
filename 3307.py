#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n, q = map(int, input().split())
l = list(map(int, input().split()))
for _ in range(q):
    a, b = map(int, input().split())
    dic = {}
    for i in l[a-1:b]:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    count = 0
    for k, v in dic.items():
        if v == 2:
            count += 1
    print(count)