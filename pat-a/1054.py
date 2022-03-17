#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
m, n = map(int, input().split())
dic = {}
for _ in range(n):
    l = input().split()
    for i in l:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
print(max(dic.items(), key=lambda x: x[1])[0])