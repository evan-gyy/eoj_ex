#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n = int(input())
books = []
for i in range(n):
    b = []
    b.append(input())
    b.append(input())
    b.append(input())
    b.append(input().split())
    b.append(input())
    b.append(input())
    books.append(b)
for i in range(int(input())):
    q = input()
    j = int(q.split(': ')[0])
    k = q.split(': ')[1]
    print(q)
    res = []
    for b in books:
        if j == 3:
            if k in b[3]:
                res.append(b[0])
        else:
            if b[j] == k:
                res.append(b[0])
    if res:
        res.sort(key=lambda x: int(x))
        for r in res:
            print(r)
    else:
        print('Not Found')
