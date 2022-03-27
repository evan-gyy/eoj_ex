#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
def simple(s):
    ret = ''
    rl = []
    for i in s:
        if ret:
            if i != ret[-1]:
                ret += i
                rl.append([i, 1])
            else:
                rl[-1][1] += 1
        else:
            ret += i
            rl.append([i, 1])
    return ret, rl

def path(s1, s2):
    ret = 0
    _, c1 = simple(s1)
    _, c2 = simple(s2)
    for i in range(len(c1)):
        ret += abs(c1[i][1] - c2[i][1])
    return ret

sim = ''
sl = []
for i in range(int(input())):
    a = input()
    if not sim:
        sim, _ = simple(a)
    else:
        if simple(a)[0] != sim:
            print(-1)
            exit()
    sl.append(a)
min_path = -1
for i in range(len(sl)):
    target = sl[i]
    total = 0
    for ss in sl:
        total += path(target, ss)
    if min_path == -1:
        min_path = total
    else:
        min_path = min(total, min_path)
print(min_path)