#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
def rev(n):
    r = ''
    for i in str(n):
        r = i + r
    return int(r)
n, k = map(int, input().split())
count = 0
while count < k and n != rev(n):
    n += rev(n)
    count += 1
print(n)
print(count)