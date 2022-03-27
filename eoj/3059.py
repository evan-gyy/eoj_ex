#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
import math
for i in range(int(input())):
    print(f'case #{i}:')
    l = []
    for j in range(int(input())):
        x, y = map(float, input().split())
        p = math.sqrt(x**2 + y**2)
        t = math.atan(y/x) if x != 0 else math.pi / 2
        if x < 0:
            t = math.pi + t
        if x > 0 and y < 0:
            t = math.pi * 2 + t
        if x == 0:
            if y > 0:
                t = math.pi / 2
            elif y < 0:
                t = math.pi / 2 * 3
            else:
                t = 0.0
        l.append((round(p, 4), round(t, 4)))
    l.sort(key=lambda x: (x[1], -x[0]))
    for item in l:
        print('({:.4f},{:.4f})'.format(item[0], item[1]))