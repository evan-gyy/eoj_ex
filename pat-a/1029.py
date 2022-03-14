#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
l1 = list(map(int, input().split()[1:]))
l2 = list(map(int, input().split()[1:]))
l = l1 + l2
l.sort()
if len(l) % 2 == 0:
    print(l[len(l) // 2 - 1])
else:
    print(l[(len(l)-1)//2])