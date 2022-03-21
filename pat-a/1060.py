#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n, a, b = map(float, input().split())
def convert(x, n):
    count = 0
    while x > 1:
        x /= 10
        count += 1
    x = str(x)[:2+int(n)]
    while len(x) < 2+int(n):
        x += '0'
    return '{}*10^{}'.format(x, count)
if convert(a, n) == convert(b, n):
    print('YES', convert(a, n))
else:
    print('NO', convert(a, n), convert(b, n))