#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
import math
def func(x, y, z):
    return math.sqrt(x**2 + y**2 + z**2) < 100
count = 0
for i in range(int(input())):
    x, y, z = map(int, input().split())
    if func(x, y, z):
        count += 1
print(count)