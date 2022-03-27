#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
from functools import lru_cache

@lru_cache(maxsize=1024)
def count(a, n, m, x):
    if x == 1:
        return a
    if x == 2:
        return a
    return count(a, n, m, x-1) + count(a, n, m, x-2)

def main():
    a, n, m, x = map(int, input().split())
