#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
import re
class ss:
    def __init__(self, s):
        self.s = s

    def __lt__(self, other):
        a = int(re.findall('\d+', self.s)[0])
        b = int(re.findall('\d+', other.s)[0])
        if a == b:
            return self.s < other.s
        return a < b

s = input().split()
al = []
dl = []
for i in s:
    flag = 0
    for j in i:
        if j.isdigit():
            dl.append(ss(i))
            flag = 1
            break
    if not flag:
        al.append(i)
al.sort()
dl.sort()
dl = [i.s for i in dl]
print(' '.join(al+dl))