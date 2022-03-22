#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n = int(input())
q = []
for i in range(n):
    q.append(int(input()))
m = max(q)
s = {}
count = 0
i = 1
while i <= m:
    i += count
    count += 1
    s[i] = 1
for i in q:
    if i in s:
        print(1)
    else:
        print(0)