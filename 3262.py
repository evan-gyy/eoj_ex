#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
from functools import lru_cache
@lru_cache(maxsize=1024)
def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)
def lcm(a, b):
    return a*b // gcd(a, b)
x, n = map(int, input().split())
for i in range(2, n + 1):
    m = lcm(x, i)
    print(m//x)