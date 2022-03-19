#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
from functools import lru_cache
a, b, c, d = map(int, input().split())
@lru_cache(maxsize=1024)
def gcd(a, b):
    return b if a % b == 0 else gcd(b, a%b)
def lcm(a, b):
    return a * b // gcd(a, b)
l = lcm(b, d)
x = l // b * a + l // d * c
g = gcd(x, l)
print(f"{a}/{b}+{c}/{d}={x//g}/{l//g}.")