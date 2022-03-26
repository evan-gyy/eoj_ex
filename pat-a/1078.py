#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
def judge(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
m, n = map(int, input().split())
while not judge(m):
    m += 1
d = []
for i in range(1, m // 2 + 1):
    d.append(i**2)
query = list(map(int, input().split()))
hash = [0 for _ in range(m)]
pl = ['-' for _ in range(n)]
for q in range(len(query)):
    mod = query[q] % m
    if hash[mod] == 0:
        hash[mod] = query[q]
        pl[q] = mod
    else:
        pos = [mod + i for i in d]
        for i in pos:
            if i >= 0 and i < m:
                if hash[i] == 0:
                    hash[i] = query[q]
                    pl[q] = i
                    break
print(' '.join([str(i) for i in pl]))