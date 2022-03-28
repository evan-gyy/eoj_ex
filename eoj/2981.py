#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
from queue import PriorityQueue
for t in range(int(input())):
    print(f'case #{t}:')
    pq = PriorityQueue()
    for n in range(int(input())):
        op = input().split()
        if len(op) > 1:
            pq.put(int(op[-1]))
        else:
            p = pq.get()
            print(p)