#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n, k = map(int, input().split())
dic = {str(i+1): [] for i in range(k)}
for i in range(n):
    name, *cls = input().split()
    for c in cls[1:]:
        dic[c].append(name)
for k, v in dic.items():
    print(k, len(v))
    if not v:
        continue
    for name in sorted(v):
        print(name)
