#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
for t in range(int(input())):
    n, m = map(int, input().split())
    ls = []
    for _ in range(m):
        ls.append([int(i) for i in input().split()])
    ls.sort(key=lambda x: (-x[2], x[0], x[1]))
    print(f'case #{t}:')
    for i in ls:
        print('({},{},{})'.format(i[0], i[1], i[2]))
