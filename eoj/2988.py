#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
for i in range(int(input())):
    sl = [[]]
    s = input()
    count = 0
    for ss in s:
        if count == 6:
            sl.append([ord(ss)])
            count = 0
        else:
            sl[-1].append(ord(ss))
        count += 1
    pwd = ''
    for j in range(6):
        temp = 0
        for l in sl:
            temp += l[j] if len(l) > j else 0
        pwd += str(temp)[-1]
    print(f'case #{i}:')
    print(pwd)