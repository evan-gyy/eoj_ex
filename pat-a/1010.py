#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
def get_max_radix(s):
    m = max(list(s))
    if m.isdigit():
        if int(m) < 2:
            return 2
        else:
            return int(m) + 1
    else:
        return ord(m) - 87 + 1
a, b, tag, radix = input().split()
tag = int(tag)
radix = int(radix)
if tag == 2:
    t = a
    a = b
    b = t
a = int(a, radix)
flag = 0
for i in range(get_max_radix(b), 36):
    if a == int(b, i):
        print(i)
        flag = 1
        break
if not flag:
    print("Impossible")