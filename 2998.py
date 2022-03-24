#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
import math
for i in range(int(input())):
    print(f'case #{i}:')
    n = int(input())
    for j in range(2, int(math.sqrt(n))+1):
        if n % j == 0:
            print(max(j, n//j))
            break