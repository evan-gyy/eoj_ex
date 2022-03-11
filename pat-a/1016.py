#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
import time, datetime
cost = list(map(int, input().split()))
sl = []
info = {}
total = {}
for i in range(int(input())):
    sl.append(input().split())
for i in sl:
    if i[2] == 'on-line':
        for j in sl:
            if j[0] == i[0] and j[2] == 'off-line':
                pass
        if i[0] in info:
            info[i[0]][i[1]] = ''
        else:
            info[i[0]] = {}
