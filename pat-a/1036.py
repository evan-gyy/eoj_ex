#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n = int(input())
ml = []
fl = []
for i in range(n):
    name, gen, id, grade = input().split()
    if gen == 'M':
        ml.append([name, id, int(grade)])
    elif gen == 'F':
        fl.append([name, id, int(grade)])
f = max(fl, key=lambda x: x[-1]) if fl else 'Absent'
m = min(ml, key=lambda x: x[-1]) if ml else 'Absent'
flag = 0
for i in [f, m]:
    if i == 'Absent':
        flag = 1
        print(i)
    else:
        print(i[0], i[1])
if flag:
    print('NA')
else:
    print(f[2] - m[2])

