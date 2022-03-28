#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
min_n = ''
max_n = ''
for i in range(int(input())):
    n = int(input())
    if min_n == '':
        min_n = n
        max_n = n
    else:
        min_n = min(n, min_n)
        max_n = max(n, max_n)
print(max_n-min_n)