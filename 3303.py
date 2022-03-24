#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
for i in range(int(input())):
    a, b = map(int, input().split())
    m = 0
    mn = a
    while a <= b:
        c = bin(a).count('1')
        if c > m:
            m = c
            mn = a
        a += 1
    print(f"Case {i + 1}: {mn}")