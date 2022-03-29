#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
dic = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}
op = input()
curr = (0, 0)
visited = {curr}
for i in op:
    x = curr[0] + dic[i][0]
    y = curr[1] + dic[i][1]
    curr = (x, y)
    visited.add(curr)
print(visited)