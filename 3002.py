# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: gyy
from functools import lru_cache
@lru_cache(maxsize=1024)
def trb(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return trb(n - 1) + trb(n - 2) + trb(n - 3)

def main():
    n = input()
    for i in range(int(n)):
        m = int(input())
        print(f"case #{i}:")
        print(trb(m))

main()

