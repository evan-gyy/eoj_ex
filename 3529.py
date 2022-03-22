#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n = int(input())
temp = []
for i in range(1, n+1):
    if i == 1:
        print(1)
    else:
        new = []
        for j in range(i):
            if j in [0, i-1]:
                new.append(1)
            else:
                new.append(temp[j-1] + temp[j])
        temp = new
        print(' '.join(map(str, new)))