#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
inl = [1 if is_prime(j) else 0 for j in range(1, 10001)]
for i in range(int(input())):
    c = int(input())
    l1 = inl[:c]
    l2 = [l1[k] for k in range(len(l1)-1, -1, -1)]
    res = 0
    for j in range(c):
        if l1[j] and l2[j]:
            res += 1
    print(res)