#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
l = list(map(int, input().split()[1:]))
dic = {}
for i in l:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for k, v in dic.items():
    if v == 1:
        print(k)
        exit()
print('None')