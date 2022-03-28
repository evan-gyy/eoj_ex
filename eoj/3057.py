#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
def judge(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
count = 0
i = 2
primes = []
while count < 26:
    if judge(i):
        primes.append(i)
        count += 1
    i += 1
for i in range(int(input())):
    print(f'case #{i}:')
    a, b = map(lambda x: [int(j) for j in x.split(',')], input().split())
    a, b = (a, b) if len(a) < len(b) else (b, a)
    while len(a) < len(b):
        a.insert(0, 0)
    flag = 0
    res = []
    for pos in range(len(a)):
        base = primes[pos]
        n = a[len(a) - pos - 1] + b[len(b) - pos - 1] + flag
        flag = 0
        while n >= base:
            n -= base
            flag += 1
        res.append(str(n))
    if flag > 0:
        res.append(str(flag))
    print(','.join(res[::-1]))