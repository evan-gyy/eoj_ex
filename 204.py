#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
from queue import PriorityQueue
pq = PriorityQueue()
n = int(input())
for i in range(n):
    s = input()
    if not s.startswith('https'):
        pq.put(s)
for i in range(pq.qsize()):
    print(pq.get())