#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
from itertools import permutations
l = list(input().split()[1:])
l.sort(key=lambda x: int(x[0]))
rl = []
tmp = 0
tl = []
for i in l:
    if not tmp:
        tmp = i[0]
        tl.append(i)
    else:
        if i[0] == tmp:
            tl.append(i)
        else:
            r = []
            for j in permutations(tl, len(tl)):
                r.append(''.join(j))
            rl.append(min(r))
            tl = [i]
            tmp = i[0]
if tl:
    r = []
    for j in permutations(tl, len(tl)):
        r.append(''.join(j))
    rl.append(min(r))
res = ''.join(rl)
t = res[0]
while t == '0':
    res = res[1:]
    if not res:
        res = 0
        break
    t = res[0]
print(res)