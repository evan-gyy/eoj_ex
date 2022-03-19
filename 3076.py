#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
from functools import lru_cache
@lru_cache(maxsize=1024)
def fib(n):
    if n == 0:
        return 0
    if n in [1, 2]:
        return 1
    return fib(n-1) + fib(n-2)
for i in range(int(input())):
    print(f'case #{i}:')
    print(fib(int(input())))