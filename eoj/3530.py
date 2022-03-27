#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
from itertools import permutations
input()
l = sorted(list(input().split()), reverse=True)
rl = []
temp = []
for i in l:
    if not temp:
        temp.append(i)
    else:
        if temp[-1][0] == i[0]:
            temp.append(i)
        else:
            if len(temp) == 1:
                r = temp[0]
            else:
                r = 0
                for j in permutations(temp, len(temp)):
                    r = max(int(''.join(j)), r)
            rl.append(r)
            temp = [i]
if temp:
    r = 0
    for j in permutations(temp, len(temp)):
        r = max(int(''.join(j)), r)
    rl.append(r)
print(''.join(str(i) for i in rl))