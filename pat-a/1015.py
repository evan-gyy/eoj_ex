#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
def trans(x, r):
    res = []
    while x:
        m = x % r
        x = x // r
        res.append(m)
    rl = [str(res[i]) for i in range(len(res)-1, -1, -1)]
    return int(''.join(rl))

def rev(x):
    s = str(x)
    r = ''
    for i in range(len(s)):
        r = s[i] + r
    return r

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

while True:
    inp = input()
    if '-' in inp:
        break
    p, r = map(int, inp.split())
    a = trans(p, r)
    b = int(rev(a), r)
    if is_prime(p) and is_prime(b):
        print('Yes')
    else:
        print('No')

