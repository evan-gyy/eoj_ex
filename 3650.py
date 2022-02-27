# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: gyy
a = input()
b = input()
if a == b:
    print(a)
else:
    s = min(a, b)
    idx = len(s) - 1
    for i in range(idx):
        if s[idx] == 'Z':
            idx -= 1
    l = chr(ord(s[idx]) + 1)
    if idx == len(s) - 1:
        res = s[:idx] + l
    else:
        res = s[:idx] + l + 'A' * (len(s) - 1 - idx)
    print(res)