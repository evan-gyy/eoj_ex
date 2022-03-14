#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
h1, h2, n = input().split()
if h1 == '-1' or h2 == '-1':
    print(-1)
    exit()
dic = {}
for i in range(int(n)):
    a, d, next = input().split()
    dic[a] = next
p, q = h1, h2
flag1, flag2 = 0, 0
while p != q and not (p == '-1' and flag1 or q == '-1' and flag2):
    if p == '-1':
        flag1 = 1
        p = h2
    else:
        p = dic[p]
    if q == '-1':
        flag2 = 1
        q = h1
    else:
        q = dic[q]
print(p)
