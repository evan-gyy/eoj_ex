#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
for i in range(int(input())):
    size = int(input())
    s = list(input())
    t = ''
    while s:
        l = 0
        r = len(s) - 1
        while s[l] == s[r] and r > l >=0:
            l += 1
            r -= 1
        if s[l] < s[r]:
            t += s.pop(0)
        else:
            t += s.pop()
    print(f'case #{i}:\n{t}')