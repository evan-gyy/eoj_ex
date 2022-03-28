#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
import math
def judge(x, y):
    return math.gcd(x, y) == 1
for i in range(int(input())):
    m, n = map(int, input().split())
    curr = 0
    while n > 0:
        while True:
            curr += 1
            if judge(m, curr):
                break
        n -= 1
    print(f'case #{i}:')
    print(curr)