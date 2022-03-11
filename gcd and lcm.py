#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
def gcd(a, b):
    return gcd(b, a%b) if a % b != 0 else b

def lcm(a, b):
    return a * b // gcd(a, b)

for i in range(int(input())):
    a, b = map(int, input().split())
    print(gcd(a, b), lcm(a, b))