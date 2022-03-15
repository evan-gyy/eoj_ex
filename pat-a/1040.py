#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
from functools import lru_cache
s = input()
rs = ''
for i in s:
    rs = i + rs
if s == rs:
    print(len(s))
    exit(0)
@lru_cache(maxsize=1024)
def func(n, m):
    if n == 0 or m == 0:
        ans = 0
    else:
        if s[n] == rs[m]:
            ans = func(n-1, m-1) + 1
        else:
            ans = max(func(n-1, m), func(n, m-1))
    return ans
maxn = func(len(s)-1, len(rs)-1)
print(maxn)