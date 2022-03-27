#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
for i in range(int(input())):
    print(f'case #{i}:')
    s = input()[::-1]
    dic = {
        '-': -1,
        '0': 0,
        '1': 1
    }
    sum = 0
    for j in range(len(s)):
        sum += dic[s[j]] * pow(3, j)
    print(sum)