#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n, head = map(int, input().split())
if head == -1 or n == 0:
    print(0, -1)
    exit()
ll = []
for i in range(n):
    ll.append(input().split())
ll.sort(key=lambda x: int(x[1]))
for i in range(len(ll)):
    if i == len(ll) - 1:
        ll[i][2] = '-1'
        break
    ll[i][2] = ll[i+1][0]
print(n, ll[0][0])
for i in ll:
    print(' '.join(i))