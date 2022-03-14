#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
from queue import PriorityQueue
input()
l = input().split()
dic = {}
for i in l:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
q = PriorityQueue()
for k, v in dic.items():
    q.put((-1 * v, k))
rl = []
temp = 0
flag = 0
while not q.empty():
    ord, curr = q.get()
    if temp:
        if curr == temp:
            if not q.empty():
                to, tc = ord, curr
                ord, curr = q.get()
                q.put((to, tc))
            else:
                flag = 1
                break
    temp = curr
    rl.append(curr)
    ord += 1
    if ord != 0:
        q.put((ord, curr))
if flag:
    print(-1)
else:
    print(' '.join(rl))

