#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
perfect = [i for i in range(1, 26 + 1)]
s = input().lower()
dic = {}
n = 0
for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for k, v in sorted(dic.items(), key=lambda x: x[1], reverse=True):
    dic[k] = perfect.pop()
for i in s:
    n += dic[i]
print(n)
