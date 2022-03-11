#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
while True:
    try:
        n = int(input())
        l = list(map(int, input().split()))
        flag = 0
        for i in range(n):
            if l[i] > 1 and l[i] < 5:
                flag = 1
                l[i] = 1
                l.insert(i, 1)
                break
        if flag:
            print(' '.join([str(i) for i in l]))
        else:
            print('Deep Dark Fantasy of ECNU')
    except:
        break