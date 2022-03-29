#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
import math
n = int(input())
ls = [int(i) for i in input().split()]
count = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            a, b, c = ls[i], ls[j], ls[k]
            if math.gcd(a, b) == 1:
                if math.gcd(a, c) == math.gcd(b, c) == 1:
                    count += 1
            else:
                if math.gcd(a, c) != 1 and math.gcd(b, c) != 1:
                    count += 1
print(count)