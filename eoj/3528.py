# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: gyy
row, col = input().split()
res = 0
for i in range(int(row)):
    sl = input().split()
    sl = [int(i) for i in sl]
    res += max(sl)
print(res)